"""
Content Cache — File-backed caching for AI-generated lessons & questions.

Strategy:
  • Lessons and questions are stored as JSON files alongside curriculum data.
  • "Base" lessons (mastery=0, no misconceptions) and question sets are cached
    under deterministic keys so the same content is never generated twice.
  • Personalised variants (mastery > 0, or specific misconceptions) get their
    own cache entries — but first-time learners (the vast majority) always
    hit the base cache.
  • Evaluations are NOT cached (every student answer is unique).

Storage layout:
    data/content/{course_id}/
        curriculum.json              # existing
        lessons/
            {concept_id}.json        # base lesson (mastery ≈ 0, no misconceptions)
            {concept_id}_m60.json    # variant for mastery ≈ 60%
            {concept_id}_m60_abc.json # variant with misconceptions hash
        questions/
            {concept_id}_3_medium.json
            {concept_id}_5_hard.json
"""
import hashlib
import json
import logging
from pathlib import Path
from typing import Optional

from src.config import CONTENT_DIR

_log = logging.getLogger(__name__)


# ── Helpers ──────────────────────────────────────────────────────────────────

def _mastery_bucket(mastery: float) -> int:
    """Round mastery to the nearest 10% (0, 10, 20, … 100)."""
    return round(mastery * 10) * 10  # 0.37 → 40


def _misconceptions_hash(misconceptions: list[str] | None) -> str:
    """Short stable hash for a set of misconceptions (order-independent)."""
    if not misconceptions:
        return ""
    joined = "|".join(sorted(misconceptions))
    return hashlib.md5(joined.encode()).hexdigest()[:8]


def _lesson_key(concept_id: str, mastery: float, misconceptions: list[str] | None) -> str:
    """Build a filename-safe cache key for a lesson."""
    bucket = _mastery_bucket(mastery)
    base = concept_id.replace(".", "_")
    parts = [base]
    if bucket > 0:
        parts.append(f"m{bucket}")
    mh = _misconceptions_hash(misconceptions)
    if mh:
        parts.append(mh)
    return "_".join(parts)


def _question_key(concept_id: str, count: int, difficulty: str) -> str:
    """Build a filename-safe cache key for a question set."""
    base = concept_id.replace(".", "_")
    return f"{base}_{count}_{difficulty}"


# ── Cache Operations ─────────────────────────────────────────────────────────

class ContentCache:
    """File-backed cache for AI-generated content."""

    def __init__(self, content_dir: Path | None = None):
        self._root = content_dir or CONTENT_DIR

    # ── Lesson Cache ──────────────────────────────────────────────────────

    def _lesson_path(self, course_id: str, concept_id: str,
                     mastery: float, misconceptions: list[str] | None) -> Path:
        key = _lesson_key(concept_id, mastery, misconceptions)
        return self._root / course_id / "lessons" / f"{key}.json"

    def get_lesson(self, course_id: str, concept_id: str,
                   mastery: float = 0.0,
                   misconceptions: list[str] | None = None) -> dict | None:
        """Return cached lesson or None on miss."""
        path = self._lesson_path(course_id, concept_id, mastery, misconceptions)
        if path.exists():
            try:
                with open(path) as f:
                    _log.debug("Cache HIT lesson: %s", path.name)
                    return json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                _log.warning("Corrupt cache file %s: %s", path, e)
                path.unlink(missing_ok=True)
        return None

    def save_lesson(self, course_id: str, concept_id: str,
                    lesson: dict, mastery: float = 0.0,
                    misconceptions: list[str] | None = None) -> Path:
        """Persist a generated lesson to the cache."""
        path = self._lesson_path(course_id, concept_id, mastery, misconceptions)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(lesson, f, indent=2, ensure_ascii=False)
        _log.debug("Cache SAVE lesson: %s", path.name)
        return path

    # ── Question Cache ────────────────────────────────────────────────────

    def _question_path(self, course_id: str, concept_id: str,
                       count: int, difficulty: str) -> Path:
        key = _question_key(concept_id, count, difficulty)
        return self._root / course_id / "questions" / f"{key}.json"

    def get_questions(self, course_id: str, concept_id: str,
                      count: int = 3, difficulty: str = "medium") -> list[dict] | None:
        """Return cached questions or None on miss."""
        path = self._question_path(course_id, concept_id, count, difficulty)
        if path.exists():
            try:
                with open(path) as f:
                    _log.debug("Cache HIT questions: %s", path.name)
                    return json.load(f)
            except (json.JSONDecodeError, OSError) as e:
                _log.warning("Corrupt cache file %s: %s", path, e)
                path.unlink(missing_ok=True)
        return None

    def save_questions(self, course_id: str, concept_id: str,
                       questions: list[dict], count: int = 3,
                       difficulty: str = "medium") -> Path:
        """Persist generated questions to the cache."""
        path = self._question_path(course_id, concept_id, count, difficulty)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        _log.debug("Cache SAVE questions: %s", path.name)
        return path

    # ── Stats ─────────────────────────────────────────────────────────────

    def stats(self, course_id: str | None = None) -> dict:
        """Return cache statistics for one or all courses."""
        courses = [course_id] if course_id else [
            d.name for d in self._root.iterdir() if d.is_dir()
        ]
        total_lessons = 0
        total_questions = 0
        per_course = {}
        for cid in courses:
            lesson_dir = self._root / cid / "lessons"
            question_dir = self._root / cid / "questions"
            nl = len(list(lesson_dir.glob("*.json"))) if lesson_dir.exists() else 0
            nq = len(list(question_dir.glob("*.json"))) if question_dir.exists() else 0
            total_lessons += nl
            total_questions += nq
            per_course[cid] = {"lessons": nl, "questions": nq}
        return {
            "total_lessons_cached": total_lessons,
            "total_question_sets_cached": total_questions,
            "courses": per_course,
        }

    def invalidate_concept(self, course_id: str, concept_id: str) -> int:
        """Remove all cached content for a concept (e.g. after curriculum update)."""
        base = concept_id.replace(".", "_")
        removed = 0
        for subdir in ["lessons", "questions"]:
            d = self._root / course_id / subdir
            if d.exists():
                for f in d.glob(f"{base}*.json"):
                    f.unlink()
                    removed += 1
        return removed


# ── Module-level singleton ───────────────────────────────────────────────────
cache = ContentCache()
