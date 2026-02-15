"""
Mastery Tree — Knowledge Graph (JSON-file-backed for local dev)

Manages the concept dependency graph and student mastery state.
Replaces Neo4j for local development — same interface, file-backed.
"""
import json
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field

from src.config import CONTENT_DIR, MASTERY_DIR


# ── Schemas ──────────────────────────────────────────────────────────────────

class Concept(BaseModel):
    concept_id: str
    title: str
    bloom_level: str  # remember, understand, apply, analyze, evaluate, create
    difficulty: float = Field(ge=0.0, le=1.0)
    prerequisites: list[str] = []
    description: str = ""
    key_ideas: list[str] = []
    chapter_id: str = ""
    chapter_title: str = ""


class MasteryNode(BaseModel):
    student_id: str
    concept_id: str
    mastery_level: float = Field(default=0.0, ge=0.0, le=1.0)
    bloom_level: str = "remember"
    attempts: int = 0
    last_assessment: Optional[str] = None
    misconceptions_detected: list[str] = []
    transfer_tasks_passed: int = 0
    transfer_tasks_total: int = 0
    time_spent_minutes: float = 0.0


class StudentProfile(BaseModel):
    student_id: str
    name: str
    grade: int = 6
    preferred_language: str = "english"
    enrolled_courses: list[str] = []  # course_ids the student is enrolled in
    mastery_nodes: dict[str, MasteryNode] = {}  # keyed by concept_id (globally unique)
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


# ── Course Info ──────────────────────────────────────────────────────────────

class CourseInfo(BaseModel):
    course_id: str
    title: str
    subject: str
    grade: int
    board: str = "General"
    language: str = "english"
    icon: str = "📖"
    color: str = "#4A90D9"
    description: str = ""
    curriculum_file: str  # relative path under CONTENT_DIR
    status: str = "active"  # active, draft, archived


# ── Course Registry ──────────────────────────────────────────────────────────

REGISTRY_PATH = CONTENT_DIR / "courses.json"


def load_course_registry() -> dict[str, CourseInfo]:
    """Load all registered courses from courses.json."""
    if not REGISTRY_PATH.exists():
        raise FileNotFoundError(f"Course registry not found: {REGISTRY_PATH}")
    with open(REGISTRY_PATH) as f:
        data = json.load(f)
    return {
        c["course_id"]: CourseInfo(**c)
        for c in data.get("courses", [])
    }


def get_course_info(course_id: str) -> CourseInfo:
    """Get metadata for a single course."""
    registry = load_course_registry()
    if course_id not in registry:
        raise ValueError(f"Course '{course_id}' not found. Available: {list(registry.keys())}")
    return registry[course_id]


def list_courses(active_only: bool = True) -> list[CourseInfo]:
    """List all registered courses."""
    registry = load_course_registry()
    courses = list(registry.values())
    if active_only:
        courses = [c for c in courses if c.status == "active"]
    return courses


# ── Mastery Tree Service ─────────────────────────────────────────────────────

class MasteryTree:
    """Manages the concept graph and student mastery state for a single course."""

    def __init__(self, course_id: str):
        self.course_id = course_id
        self.course_info = get_course_info(course_id)
        self.concepts: dict[str, Concept] = {}
        self._load_curriculum()

    def _load_curriculum(self):
        """Load concept graph from curriculum JSON (path from registry)."""
        curriculum_path = CONTENT_DIR / self.course_info.curriculum_file
        if not curriculum_path.exists():
            raise FileNotFoundError(f"Curriculum not found: {curriculum_path}")

        with open(curriculum_path) as f:
            data = json.load(f)

        for chapter in data.get("chapters", []):
            for concept_data in chapter.get("concepts", []):
                concept = Concept(
                    **concept_data,
                    chapter_id=chapter["chapter_id"],
                    chapter_title=chapter["title"],
                )
                self.concepts[concept.concept_id] = concept

    def get_concept(self, concept_id: str) -> Optional[Concept]:
        return self.concepts.get(concept_id)

    def get_all_concepts(self) -> list[Concept]:
        return list(self.concepts.values())

    def get_prerequisites(self, concept_id: str) -> list[Concept]:
        concept = self.concepts.get(concept_id)
        if not concept:
            return []
        return [self.concepts[pid] for pid in concept.prerequisites if pid in self.concepts]

    def get_dependents(self, concept_id: str) -> list[Concept]:
        """Get concepts that depend on this concept."""
        return [c for c in self.concepts.values() if concept_id in c.prerequisites]

    def get_chapters(self) -> list[dict]:
        """Get unique chapters in order."""
        seen = {}
        for c in self.concepts.values():
            if c.chapter_id not in seen:
                seen[c.chapter_id] = {"chapter_id": c.chapter_id, "title": c.chapter_title}
        return list(seen.values())

    def get_concepts_for_chapter(self, chapter_id: str) -> list[Concept]:
        return [c for c in self.concepts.values() if c.chapter_id == chapter_id]

    def topological_order(self) -> list[str]:
        """Return concepts in a valid learning order (topological sort)."""
        visited = set()
        order = []

        def dfs(cid: str):
            if cid in visited:
                return
            visited.add(cid)
            concept = self.concepts.get(cid)
            if concept:
                for pre in concept.prerequisites:
                    dfs(pre)
                order.append(cid)

        for cid in self.concepts:
            dfs(cid)
        return order


# ── Student Mastery Store ────────────────────────────────────────────────────

class StudentStore:
    """File-backed student state management."""

    def __init__(self):
        self.store_dir = MASTERY_DIR
        self.store_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, student_id: str) -> Path:
        return self.store_dir / f"{student_id}.json"

    def create_student(self, student_id: str, name: str, grade: int = 6) -> StudentProfile:
        profile = StudentProfile(student_id=student_id, name=name, grade=grade)
        self._save(profile)
        return profile

    def get_student(self, student_id: str) -> Optional[StudentProfile]:
        path = self._path(student_id)
        if not path.exists():
            return None
        with open(path) as f:
            return StudentProfile(**json.load(f))

    def get_or_create_student(self, student_id: str, name: str = "Student") -> StudentProfile:
        student = self.get_student(student_id)
        if not student:
            student = self.create_student(student_id, name)
        return student

    def update_mastery(
        self,
        student_id: str,
        concept_id: str,
        mastery_level: float,
        misconceptions: list[str] | None = None,
        time_spent: float = 0.0,
    ) -> MasteryNode:
        student = self.get_or_create_student(student_id)

        if concept_id in student.mastery_nodes:
            node = student.mastery_nodes[concept_id]
        else:
            node = MasteryNode(student_id=student_id, concept_id=concept_id)

        node.mastery_level = max(node.mastery_level, mastery_level)  # mastery only goes up
        node.attempts += 1
        node.last_assessment = datetime.now(timezone.utc).isoformat()
        node.time_spent_minutes += time_spent
        if misconceptions:
            node.misconceptions_detected = list(
                set(node.misconceptions_detected + misconceptions)
            )

        student.mastery_nodes[concept_id] = node
        self._save(student)
        return node

    def get_mastery_summary(self, student_id: str, tree: MasteryTree) -> list[dict]:
        """Get mastery status for all concepts."""
        student = self.get_or_create_student(student_id)
        summary = []
        for concept in tree.get_all_concepts():
            node = student.mastery_nodes.get(concept.concept_id)
            prereqs_met = all(
                student.mastery_nodes.get(p, MasteryNode(student_id=student_id, concept_id=p)).mastery_level >= 0.6
                for p in concept.prerequisites
            )
            summary.append({
                "concept_id": concept.concept_id,
                "title": concept.title,
                "chapter": concept.chapter_title,
                "difficulty": concept.difficulty,
                "mastery_level": node.mastery_level if node else 0.0,
                "attempts": node.attempts if node else 0,
                "status": _status(node, prereqs_met),
                "misconceptions": node.misconceptions_detected if node else [],
            })
        return summary

    def get_next_concepts(self, student_id: str, tree: MasteryTree, limit: int = 3) -> list[Concept]:
        """Get the next concepts the student should study."""
        student = self.get_or_create_student(student_id)
        candidates = []

        for cid in tree.topological_order():
            node = student.mastery_nodes.get(cid)
            if node and node.mastery_level >= 0.7:
                continue  # already mastered

            concept = tree.get_concept(cid)
            if not concept:
                continue

            # Check prerequisites
            prereqs_met = all(
                student.mastery_nodes.get(p, MasteryNode(student_id=student_id, concept_id=p)).mastery_level >= 0.6
                for p in concept.prerequisites
            )
            if prereqs_met:
                candidates.append(concept)

        return candidates[:limit]

    def _save(self, student: StudentProfile):
        with open(self._path(student.student_id), "w") as f:
            json.dump(student.model_dump(), f, indent=2, default=str)

    def list_students(self) -> list[str]:
        return [p.stem for p in self.store_dir.glob("*.json")]


def _status(node: Optional[MasteryNode], prereqs_met: bool) -> str:
    if node is None or node.mastery_level == 0:
        return "locked" if not prereqs_met else "available"
    if node.mastery_level >= 0.7:
        return "mastered"
    return "in_progress"
