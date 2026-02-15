#!/usr/bin/env python3
"""
Expand Course Curriculum with Gemini AI
========================================

Uses the AI_EXPANSION_MODEL (default: gemini-2.5-pro-preview) to expand
a course's seed curriculum with additional concepts per chapter.

Usage:
    python tools/expand_with_gemini.py <course_id>
    python tools/expand_with_gemini.py science9
    python tools/expand_with_gemini.py --all          # expand ALL courses (slow!)
    python tools/expand_with_gemini.py --list          # list available courses

Each chapter gets 3-6 new concepts added, with proper:
- concept_ids following the naming convention
- bloom_levels (progressive)
- prerequisites (linked to existing concepts)
- descriptions and key_ideas

The original seed concepts are preserved; new ones are appended.
"""

import asyncio
import sys
import json
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import CONTENT_DIR, AI_EXPANSION_MODEL
from src.mastery_tree import list_courses, get_course_info
from src.gemini_engine import expand_full_course


async def expand_one(course_id: str):
    """Expand a single course."""
    info = get_course_info(course_id)
    if not info:
        print(f"❌ Course '{course_id}' not found")
        return

    print(f"\n🧠 Expanding: {info.icon} {info.title} ({course_id})")
    print(f"   Using model: {AI_EXPANSION_MODEL}")

    # Count current concepts
    curr_path = CONTENT_DIR / info.curriculum_file
    with open(curr_path) as f:
        curr = json.load(f)
    before = sum(len(ch["concepts"]) for ch in curr["chapters"])
    print(f"   Current concepts: {before}")
    print(f"   Expanding chapters...\n")

    result = await expand_full_course(course_id)

    if "error" in result:
        print(f"   ❌ Error: {result['error']}")
        return

    for ch in result["chapters"]:
        if "error" in ch:
            print(f"   ⚠️  {ch['chapter']}: ERROR — {ch['error']}")
        else:
            print(f"   ✅ {ch['chapter']}: +{ch['new_concepts']} concepts")

    print(f"\n   📊 Total concepts: {before} → {result['total_concepts_now']} (+{result['new_concepts_added']})")


async def expand_all():
    """Expand all active courses."""
    courses = list_courses(active_only=True)
    print(f"🚀 Expanding all {len(courses)} courses...")

    for c in courses:
        await expand_one(c.course_id)

    print("\n✅ All courses expanded!")


def list_all():
    """List all available courses."""
    courses = list_courses(active_only=True)
    print(f"\n📚 {len(courses)} courses available:\n")
    for c in courses:
        curr_path = CONTENT_DIR / c.curriculum_file
        try:
            with open(curr_path) as f:
                curr = json.load(f)
            n_ch = len(curr["chapters"])
            n_c = sum(len(ch["concepts"]) for ch in curr["chapters"])
        except Exception:
            n_ch = n_c = "?"
        print(f"   {c.icon} {c.course_id:20s} — {c.title:45s} [{n_ch} ch, {n_c} concepts]")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    arg = sys.argv[1]

    if arg == "--list":
        list_all()
    elif arg == "--all":
        asyncio.run(expand_all())
    else:
        asyncio.run(expand_one(arg))


if __name__ == "__main__":
    main()
