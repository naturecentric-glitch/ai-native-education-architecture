#!/usr/bin/env python3
"""
Generate all Class 10 Math content: curriculum, lessons, questions, placement test.

Usage:  python -m tools.math10_content
"""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = BASE / "data" / "content" / "math10"


def main():
    from .curriculum import CURRICULUM
    from . import (
        ch01_real_numbers, ch02_polynomials, ch03_linear_equations,
        ch04_quadratic_equations, ch05_ap, ch06_triangles,
        ch07_coordinate_geometry, ch08_trigonometry, ch09_trig_applications,
        ch10_circles, ch11_constructions, ch12_areas_circles,
        ch13_surface_area_volume, ch14_statistics, ch15_probability,
    )

    chapters = [
        ch01_real_numbers, ch02_polynomials, ch03_linear_equations,
        ch04_quadratic_equations, ch05_ap, ch06_triangles,
        ch07_coordinate_geometry, ch08_trigonometry, ch09_trig_applications,
        ch10_circles, ch11_constructions, ch12_areas_circles,
        ch13_surface_area_volume, ch14_statistics, ch15_probability,
    ]

    # ── Merge all content ────────────────────────────────────────────────
    all_lessons = {}
    all_questions = {}
    for mod in chapters:
        all_lessons.update(mod.LESSONS)
        all_questions.update(mod.QUESTIONS)

    # ── Write curriculum.json ────────────────────────────────────────────
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONTENT_DIR / "curriculum.json", "w") as f:
        json.dump(CURRICULUM, f, indent=2, ensure_ascii=False)

    total_concepts = sum(len(ch["concepts"]) for ch in CURRICULUM["chapters"])
    print(f"📘 Curriculum: {len(CURRICULUM['chapters'])} chapters, {total_concepts} concepts")

    # ── Write lesson files ───────────────────────────────────────────────
    lesson_dir = CONTENT_DIR / "lessons"
    lesson_dir.mkdir(parents=True, exist_ok=True)
    # Clear old lessons
    for old in lesson_dir.glob("*.json"):
        old.unlink()
    for cid, lesson in all_lessons.items():
        key = cid.replace(".", "_")
        with open(lesson_dir / f"{key}.json", "w") as f:
            json.dump(lesson, f, indent=2, ensure_ascii=False)
    print(f"✅ Lessons: {len(all_lessons)} written")

    # ── Write question files (as _3_medium.json to match default cache key) ──
    question_dir = CONTENT_DIR / "questions"
    question_dir.mkdir(parents=True, exist_ok=True)
    # Clear old questions
    for old in question_dir.glob("*.json"):
        old.unlink()
    for cid, qs in all_questions.items():
        key = cid.replace(".", "_")
        with open(question_dir / f"{key}_3_medium.json", "w") as f:
            json.dump(qs, f, indent=2, ensure_ascii=False)
    print(f"✅ Questions: {len(all_questions)} sets ({sum(len(qs) for qs in all_questions.values())} total)")

    # ── Write placement test ─────────────────────────────────────────────
    placement = []
    for ch in CURRICULUM["chapters"]:
        # Pick the last (hardest) concept of each chapter for diagnostic
        last_concept = ch["concepts"][-1]
        cid = last_concept["concept_id"]
        if cid in all_questions:
            # Pick the hardest question (last one)
            hard_q = all_questions[cid][-1]
            placement.append({
                "chapter_id": ch["chapter_id"],
                "chapter_title": ch["title"],
                "concept_id": cid,
                "concept_title": last_concept["title"],
                "question": hard_q,
                "concepts_unlocked": [c["concept_id"] for c in ch["concepts"]],
            })
    with open(CONTENT_DIR / "placement.json", "w") as f:
        json.dump(placement, f, indent=2, ensure_ascii=False)
    print(f"🎯 Placement test: {len(placement)} diagnostic questions")

    # ── Validation ───────────────────────────────────────────────────────
    missing_lessons = set()
    missing_questions = set()
    for ch in CURRICULUM["chapters"]:
        for c in ch["concepts"]:
            cid = c["concept_id"]
            if cid not in all_lessons:
                missing_lessons.add(cid)
            if cid not in all_questions:
                missing_questions.add(cid)

    if missing_lessons:
        print(f"\n⚠️  Missing lessons: {missing_lessons}")
    if missing_questions:
        print(f"⚠️  Missing questions: {missing_questions}")
    if not missing_lessons and not missing_questions:
        print(f"\n🎉 All {total_concepts} concepts have lessons and questions!")


if __name__ == "__main__":
    main()
