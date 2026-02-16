"""
Pre-generate content cache — Warm lessons & questions for all concepts.

Usage:
    python -m tools.pregenerate_content                        # all courses
    python -m tools.pregenerate_content --course math6         # one course
    python -m tools.pregenerate_content --course math6 --questions-only
    python -m tools.pregenerate_content --course math6 --lessons-only
    python -m tools.pregenerate_content --status               # cache stats
    python -m tools.pregenerate_content --status --course math6

Generates and saves:
  • Base lesson (mastery=0, no misconceptions) for each concept
  • Medium-difficulty question set (3 questions) for each concept

Skips concepts that already have cached content.
Uses the fallback model automatically if primary quota is exhausted.
"""
import argparse
import asyncio
import json
import logging
import sys
import time
from pathlib import Path

# Allow running as `python -m tools.pregenerate_content`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import CONTENT_DIR
from src.content_cache import ContentCache
from src.mastery_tree import MasteryTree, list_courses, get_course_info
from src.gemini_engine import teach_concept, generate_questions

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
_log = logging.getLogger(__name__)

cache = ContentCache()


async def pregenerate_lesson(course_id: str, concept, course_info_dict: dict) -> bool:
    """Generate and cache a base lesson for a concept. Returns True if generated."""
    cached = cache.get_lesson(course_id, concept.concept_id, 0.0, None)
    if cached:
        return False  # already cached

    try:
        lesson = await teach_concept(
            concept, "Student", 0.0, None, course_info=course_info_dict,
        )
        cache.save_lesson(course_id, concept.concept_id, lesson, 0.0, None)
        return True
    except Exception as e:
        _log.error("  ✗ Lesson %s failed: %s", concept.concept_id, e)
        return False


async def pregenerate_questions(course_id: str, concept, course_info_dict: dict,
                                 count: int = 3, difficulty: str = "medium") -> bool:
    """Generate and cache questions for a concept. Returns True if generated."""
    cached = cache.get_questions(course_id, concept.concept_id, count, difficulty)
    if cached:
        return False  # already cached

    try:
        qs = await generate_questions(
            concept, count, difficulty, course_info=course_info_dict,
        )
        cache.save_questions(course_id, concept.concept_id, qs, count, difficulty)
        return True
    except Exception as e:
        _log.error("  ✗ Questions %s failed: %s", concept.concept_id, e)
        return False


async def pregenerate_course(course_id: str, lessons: bool = True, questions: bool = True):
    """Pre-generate all content for a single course."""
    info = get_course_info(course_id)
    tree = MasteryTree(course_id)
    concepts = tree.get_all_concepts()
    course_info_dict = info.model_dump()

    _log.info("📘 %s — %d concepts", info.title, len(concepts))

    lesson_gen = 0
    lesson_skip = 0
    q_gen = 0
    q_skip = 0
    errors = 0
    t0 = time.time()

    for i, concept in enumerate(concepts, 1):
        label = f"  [{i}/{len(concepts)}] {concept.title}"

        if lessons:
            ok = await pregenerate_lesson(course_id, concept, course_info_dict)
            if ok:
                lesson_gen += 1
                _log.info("%s — lesson ✓ (generated)", label)
            else:
                # check if it was a skip or an error (get_lesson returns None on miss)
                if cache.get_lesson(course_id, concept.concept_id, 0.0, None):
                    lesson_skip += 1
                else:
                    errors += 1

        if questions:
            ok = await pregenerate_questions(course_id, concept, course_info_dict)
            if ok:
                q_gen += 1
                _log.info("%s — questions ✓ (generated)", label)
            else:
                if cache.get_questions(course_id, concept.concept_id, 3, "medium"):
                    q_skip += 1
                else:
                    errors += 1

        # Rate limiting: short pause between AI calls to avoid quota spikes
        if (lesson_gen + q_gen) > 0 and (lesson_gen + q_gen) % 5 == 0:
            await asyncio.sleep(1.0)

    elapsed = time.time() - t0
    _log.info(
        "  ✅ %s done in %.0fs — lessons: %d new, %d cached | questions: %d new, %d cached | errors: %d",
        course_id, elapsed, lesson_gen, lesson_skip, q_gen, q_skip, errors,
    )
    return {
        "course_id": course_id,
        "lessons_generated": lesson_gen,
        "lessons_cached": lesson_skip,
        "questions_generated": q_gen,
        "questions_cached": q_skip,
        "errors": errors,
        "elapsed_seconds": round(elapsed, 1),
    }


async def pregenerate_all(course_filter: str | None = None,
                           lessons: bool = True, questions: bool = True):
    """Pre-generate content for all (or one) course."""
    courses = list_courses(active_only=True)
    if course_filter:
        courses = [c for c in courses if c.course_id == course_filter]
        if not courses:
            _log.error("Course '%s' not found", course_filter)
            return

    _log.info("🚀 Pre-generating content for %d course(s)...", len(courses))
    results = []
    for c in courses:
        r = await pregenerate_course(c.course_id, lessons=lessons, questions=questions)
        results.append(r)

    total_lessons = sum(r["lessons_generated"] for r in results)
    total_questions = sum(r["questions_generated"] for r in results)
    _log.info(
        "\n🎉 Done! Generated %d lessons + %d question sets across %d course(s)",
        total_lessons, total_questions, len(results),
    )


def show_status(course_filter: str | None = None):
    """Print cache statistics."""
    stats = cache.stats(course_filter)
    print(f"\n📊 Content Cache Stats")
    print(f"   Total lessons cached:  {stats['total_lessons_cached']}")
    print(f"   Total question sets:   {stats['total_question_sets_cached']}")
    if stats["courses"]:
        print(f"\n   Per course:")
        for cid, s in sorted(stats["courses"].items()):
            if s["lessons"] or s["questions"]:
                print(f"     {cid:30s}  lessons={s['lessons']:4d}  questions={s['questions']:4d}")
    else:
        print("   (no cached content yet)")


def main():
    parser = argparse.ArgumentParser(description="Pre-generate AI content cache")
    parser.add_argument("--course", type=str, help="Only process this course")
    parser.add_argument("--lessons-only", action="store_true", help="Only generate lessons")
    parser.add_argument("--questions-only", action="store_true", help="Only generate questions")
    parser.add_argument("--status", action="store_true", help="Show cache stats and exit")
    args = parser.parse_args()

    if args.status:
        show_status(args.course)
        return

    do_lessons = not args.questions_only
    do_questions = not args.lessons_only

    asyncio.run(pregenerate_all(
        course_filter=args.course,
        lessons=do_lessons,
        questions=do_questions,
    ))


if __name__ == "__main__":
    main()
