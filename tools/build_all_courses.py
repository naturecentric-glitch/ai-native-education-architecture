#!/usr/bin/env python3
"""
Master Orchestrator — Build & Expand All Courses
==================================================
Two-phase pipeline:
  Phase 1: Generate all seed curricula from template data
  Phase 2: Expand each course with Gemini AI (robust, resumable)

Usage:
  python -m tools.build_all_courses               # Both phases
  python -m tools.build_all_courses --generate     # Phase 1 only
  python -m tools.build_all_courses --expand       # Phase 2 only
  python -m tools.build_all_courses --expand --course math6   # Expand one
  python -m tools.build_all_courses --status       # Show expansion status
"""

import argparse
import asyncio
import json
import sys
import time
import traceback
from pathlib import Path

# Ensure project root is on path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


# ── Phase 1: Generate seed curricula ─────────────────────────────────────────

def phase_generate():
    """Phase 1: Generate all seed curricula."""
    print("\n" + "=" * 60)
    print("  PHASE 1 — Generate Seed Curricula")
    print("=" * 60 + "\n")
    from tools.generate_curricula import generate_all
    generate_all()


# ── Status check ─────────────────────────────────────────────────────────────

def show_status():
    """Show expansion status of all courses."""
    from src.config import CONTENT_DIR

    with open(CONTENT_DIR / "courses.json") as f:
        registry = json.load(f)

    courses = registry["courses"]
    expanded = []
    needs_expansion = []
    errors = []

    for c in courses:
        cid = c["course_id"]
        curr_path = CONTENT_DIR / c["curriculum_file"]
        if not curr_path.exists():
            errors.append((cid, "curriculum file missing"))
            continue
        with open(curr_path) as f:
            curr = json.load(f)
        total = sum(len(ch["concepts"]) for ch in curr["chapters"])
        chapters = len(curr["chapters"])
        max_concepts = max(
            (len(ch["concepts"]) for ch in curr["chapters"]),
            default=0,
        )
        if max_concepts > 4:
            expanded.append((cid, total, chapters))
        else:
            needs_expansion.append((cid, total, chapters))

    print(f"\n📊 Course Expansion Status")
    print(f"{'=' * 60}")
    print(f"  ✅ Expanded:        {len(expanded)}")
    print(f"  ⏳ Needs expansion: {len(needs_expansion)}")
    if errors:
        print(f"  ❌ Errors:          {len(errors)}")
    print(f"  📚 Total courses:   {len(courses)}")

    total_concepts = sum(t for _, t, _ in expanded) + sum(
        t for _, t, _ in needs_expansion
    )
    print(f"  🧠 Total concepts:  {total_concepts}")
    print(f"{'=' * 60}")

    if expanded:
        print(f"\n✅ Expanded ({len(expanded)}):")
        for cid, t, ch in expanded:
            print(f"   {cid}: {t} concepts, {ch} chapters")

    if needs_expansion:
        print(f"\n⏳ Needs expansion ({len(needs_expansion)}):")
        for cid, t, ch in needs_expansion:
            print(f"   {cid}: {t} concepts, {ch} chapters")

    if errors:
        print(f"\n❌ Errors ({len(errors)}):")
        for cid, err in errors:
            print(f"   {cid}: {err}")

    return needs_expansion


# ── Phase 2: Expand with Gemini (robust, per-chapter) ───────────────────────

CHAPTER_TIMEOUT = 120  # seconds per chapter
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds between retries
COURSE_DELAY = 2  # seconds between courses


async def _expand_chapter_with_retry(
    course_id: str,
    chapter_key: str,
    chapter_title: str,
    existing_concepts: list,
    course_info: dict,
) -> list:
    """Expand a single chapter with retries and timeout."""
    from src.gemini_engine import expand_chapter

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            new_concepts = await asyncio.wait_for(
                expand_chapter(
                    course_id=course_id,
                    chapter_key=chapter_key,
                    chapter_title=chapter_title,
                    existing_concepts=existing_concepts,
                    course_info=course_info,
                ),
                timeout=CHAPTER_TIMEOUT,
            )
            return new_concepts
        except asyncio.TimeoutError:
            print(f" ⏱️ timeout({attempt}/{MAX_RETRIES})", end="", flush=True)
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY)
        except json.JSONDecodeError as e:
            print(f" ⚠️ json({attempt}/{MAX_RETRIES})", end="", flush=True)
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY)
        except Exception as e:
            err_type = type(e).__name__
            print(
                f" ❌ {err_type}({attempt}/{MAX_RETRIES})",
                end="",
                flush=True,
            )
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_DELAY * attempt)  # Backoff
            else:
                raise
    return []  # All retries exhausted


async def _expand_one_course(course_id: str) -> dict:
    """Expand a single course — chapter by chapter with retries."""
    from src.mastery_tree import get_course_info
    from src.config import CONTENT_DIR

    info = get_course_info(course_id)
    if not info:
        return {"error": f"Course '{course_id}' not found"}

    course_info_dict = info.model_dump()
    curr_path = CONTENT_DIR / info.curriculum_file

    with open(curr_path) as f:
        curriculum = json.load(f)

    total_new = 0
    chapter_results = []

    for i, chapter in enumerate(curriculum["chapters"], 1):
        # Extract chapter_key
        if chapter["concepts"]:
            parts = chapter["concepts"][0]["concept_id"].split(".")
            chapter_key = parts[1] if len(parts) >= 3 else chapter["chapter_id"]
        else:
            chapter_key = chapter["chapter_id"]

        # Skip if chapter already expanded (>4 concepts)
        if len(chapter["concepts"]) > 4:
            continue

        ch_count = len(curriculum["chapters"])
        print(
            f"      [{i}/{ch_count}] {chapter['title']}...",
            end="",
            flush=True,
        )

        try:
            new_concepts = await _expand_chapter_with_retry(
                course_id=course_id,
                chapter_key=chapter_key,
                chapter_title=chapter["title"],
                existing_concepts=chapter["concepts"],
                course_info=course_info_dict,
            )
            chapter["concepts"].extend(new_concepts)
            total_new += len(new_concepts)
            print(f" +{len(new_concepts)} ✅")
            chapter_results.append({
                "chapter": chapter["title"],
                "new_concepts": len(new_concepts),
            })
        except Exception as e:
            print(f" FAILED ❌")
            chapter_results.append({
                "chapter": chapter["title"],
                "error": str(e)[:100],
            })

        # Small delay between chapters to avoid rate limits
        await asyncio.sleep(1)

    # Save expanded curriculum after every course
    with open(curr_path, "w") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)

    total_concepts = sum(len(ch["concepts"]) for ch in curriculum["chapters"])

    return {
        "course_id": course_id,
        "title": info.title,
        "total_concepts_now": total_concepts,
        "new_concepts_added": total_new,
        "chapters": chapter_results,
    }


def _is_already_expanded(course: dict) -> bool:
    """Check if a course is already fully expanded."""
    from src.config import CONTENT_DIR

    curr_path = CONTENT_DIR / course["curriculum_file"]
    if not curr_path.exists():
        return False
    with open(curr_path) as f:
        curr = json.load(f)
    # Consider expanded if ALL chapters have >4 concepts
    for ch in curr["chapters"]:
        if len(ch["concepts"]) <= 4:
            return False
    return True


def phase_expand(course_id=None):
    """Phase 2: Expand with Gemini — robust, resumable."""
    print("\n" + "=" * 60)
    print("  PHASE 2 — Expand with Gemini AI")
    print("=" * 60 + "\n")

    from src.config import CONTENT_DIR

    if course_id:
        # Expand a single course
        print(f"🔄 Expanding: {course_id}")
        try:
            result = asyncio.run(_expand_one_course(course_id))
            if "error" in result:
                print(f"❌ {result['error']}")
            else:
                print(
                    f"\n   ✅ {result['title']}: "
                    f"+{result['new_concepts_added']} new concepts "
                    f"({result['total_concepts_now']} total)"
                )
        except Exception as e:
            print(f"   ❌ Fatal error: {e}")
            traceback.print_exc()
        return

    # Expand all courses (skip already expanded)
    with open(CONTENT_DIR / "courses.json") as f:
        registry = json.load(f)
    courses = registry["courses"]

    total = len(courses)
    total_new = 0
    expanded_count = 0
    skipped_count = 0
    error_list = []

    for idx, course in enumerate(courses, 1):
        cid = course["course_id"]
        title = course["title"]

        # Skip already expanded courses
        if _is_already_expanded(course):
            skipped_count += 1
            print(f"[{idx}/{total}] ⏭️  {title} ({cid}) — already expanded")
            continue

        print(f"\n[{idx}/{total}] 🔄 {title} ({cid})")

        try:
            result = asyncio.run(_expand_one_course(cid))
            if "error" in result:
                error_list.append((cid, result["error"]))
                print(f"   ❌ {result['error']}")
            else:
                added = result.get("new_concepts_added", 0)
                total_new += added
                expanded_count += 1
                print(
                    f"   ✅ +{added} concepts "
                    f"({result['total_concepts_now']} total)"
                )
        except KeyboardInterrupt:
            print(f"\n\n⚠️  Interrupted at {cid}. Progress saved — rerun to resume.")
            break
        except Exception as e:
            error_list.append((cid, str(e)[:200]))
            print(f"   ❌ Fatal: {e}")

        # Delay between courses
        if idx < total:
            time.sleep(COURSE_DELAY)

    print(f"\n{'=' * 60}")
    print(f"✅ Expansion complete")
    print(f"   Expanded:  {expanded_count} courses")
    print(f"   Skipped:   {skipped_count} (already done)")
    print(f"   New concepts: {total_new}")
    if error_list:
        print(f"   ⚠️  Errors: {len(error_list)}")
        for cid, err in error_list:
            print(f"      - {cid}: {err}")
    print("=" * 60)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Build & Expand All NCERT K-12 Courses"
    )
    parser.add_argument(
        "--generate", action="store_true",
        help="Phase 1 only — generate seed curricula",
    )
    parser.add_argument(
        "--expand", action="store_true",
        help="Phase 2 only — expand with Gemini",
    )
    parser.add_argument(
        "--course", type=str,
        help="Expand a single course by ID (with --expand)",
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Show expansion status",
    )
    args = parser.parse_args()

    if args.status:
        show_status()
        return

    # Default: run both phases
    run_generate = True
    run_expand = True

    if args.generate or args.expand:
        run_generate = args.generate
        run_expand = args.expand

    if run_generate:
        phase_generate()

    if run_expand:
        phase_expand(args.course)

    if run_generate and not run_expand:
        print(
            "\n💡 To expand with Gemini: "
            "python -m tools.build_all_courses --expand"
        )

    print("\n🎓 Done!")


if __name__ == "__main__":
    main()
