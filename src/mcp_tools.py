"""
MCP Server — Content & Mastery Tools (Multi-Course)

Exposes the platform's capabilities as MCP tools that the AI Host can discover and invoke.
All tools are course-aware — course_id is required where applicable.

For local dev, these are called directly. In production, they run as an MCP server over stdio/SSE.
"""
from src.mastery_tree import (
    MasteryTree, StudentStore, Concept,
    list_courses, get_course_info, CourseInfo,
)
from src.gemini_engine import (
    evaluate_answer,
    teach_concept,
    generate_questions,
    analyze_misconceptions,
)


# ── Course Manager (lazy-loading, multi-course) ─────────────────────────────

class CourseManager:
    """Manages loaded mastery trees. Lazy-loads courses on first access."""

    def __init__(self):
        self._trees: dict[str, MasteryTree] = {}
        self._store = StudentStore()

    @property
    def store(self) -> StudentStore:
        return self._store

    def get_tree(self, course_id: str) -> MasteryTree:
        """Get (or load) the mastery tree for a course."""
        if course_id not in self._trees:
            self._trees[course_id] = MasteryTree(course_id)
        return self._trees[course_id]

    def list_loaded(self) -> list[str]:
        return list(self._trees.keys())


_mgr = CourseManager()


# ── Tool: List Available Courses ─────────────────────────────────────────────

def tool_list_courses() -> dict:
    """List all available courses on the platform."""
    courses = list_courses(active_only=True)
    return {
        "courses": [
            {
                "course_id": c.course_id,
                "title": c.title,
                "subject": c.subject,
                "grade": c.grade,
                "board": c.board,
                "language": c.language,
                "icon": c.icon,
                "color": c.color,
                "description": c.description,
                "status": c.status,
            }
            for c in courses
        ]
    }


# ── Tool: Get Course Info ────────────────────────────────────────────────────

def tool_get_course_info(course_id: str) -> dict:
    """Get metadata for a specific course."""
    try:
        info = get_course_info(course_id)
        tree = _mgr.get_tree(course_id)
        return {
            **info.model_dump(),
            "total_concepts": len(tree.get_all_concepts()),
            "total_chapters": len(tree.get_chapters()),
        }
    except ValueError as e:
        return {"error": str(e)}


# ── Tool: Get Curriculum Overview ────────────────────────────────────────────

def tool_get_curriculum(course_id: str) -> dict:
    """Get the full curriculum structure for a course — chapters and concepts."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    chapters = tree.get_chapters()
    result = []
    for ch in chapters:
        concepts = tree.get_concepts_for_chapter(ch["chapter_id"])
        result.append({
            "chapter_id": ch["chapter_id"],
            "title": ch["title"],
            "concepts": [
                {
                    "concept_id": c.concept_id,
                    "title": c.title,
                    "difficulty": c.difficulty,
                    "bloom_level": c.bloom_level,
                    "prerequisites": c.prerequisites,
                }
                for c in concepts
            ],
        })
    return {
        "course_id": course_id,
        "title": tree.course_info.title,
        "chapters": result,
    }


# ── Tool: Get Student Profile ────────────────────────────────────────────────

def tool_get_student_profile(student_id: str, course_id: str) -> dict:
    """Get a student's profile and mastery state for a specific course."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    store = _mgr.store
    student = store.get_or_create_student(student_id)
    mastery_summary = store.get_mastery_summary(student_id, tree)
    next_concepts = store.get_next_concepts(student_id, tree)

    return {
        "student_id": student.student_id,
        "name": student.name,
        "grade": student.grade,
        "course_id": course_id,
        "course_title": tree.course_info.title,
        "mastery_summary": mastery_summary,
        "next_recommended": [
            {"concept_id": c.concept_id, "title": c.title, "difficulty": c.difficulty}
            for c in next_concepts
        ],
        "total_concepts": len(tree.get_all_concepts()),
        "mastered_count": sum(1 for m in mastery_summary if m["status"] == "mastered"),
        "in_progress_count": sum(1 for m in mastery_summary if m["status"] == "in_progress"),
    }


# ── Tool: Teach a Concept ───────────────────────────────────────────────────

async def tool_teach_concept(student_id: str, course_id: str, concept_id: str) -> dict:
    """Generate a personalized lesson for a concept within a course."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    concept = tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found in course {course_id}"}

    store = _mgr.store
    student = store.get_or_create_student(student_id)
    node = student.mastery_nodes.get(concept_id)
    mastery = node.mastery_level if node else 0.0
    misconceptions = node.misconceptions_detected if node else []

    course_info_dict = tree.course_info.model_dump() if tree.course_info else None
    lesson = await teach_concept(concept, student.name, mastery, misconceptions, course_info=course_info_dict)
    return {
        "course_id": course_id,
        "concept_id": concept_id,
        "concept_title": concept.title,
        "chapter": concept.chapter_title,
        "lesson": lesson,
        "current_mastery": mastery,
    }


# ── Tool: Generate Practice Questions ────────────────────────────────────────

async def tool_generate_questions(
    course_id: str,
    concept_id: str,
    count: int = 3,
    difficulty: str = "medium",
) -> dict:
    """Generate practice questions for a concept within a course."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    concept = tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found in course {course_id}"}

    course_info_dict = tree.course_info.model_dump() if tree.course_info else None
    questions = await generate_questions(concept, count, difficulty, course_info=course_info_dict)
    return {
        "course_id": course_id,
        "concept_id": concept_id,
        "concept_title": concept.title,
        "questions": questions,
    }


# ── Tool: Evaluate Student Answer ────────────────────────────────────────────

async def tool_evaluate_answer(
    student_id: str,
    course_id: str,
    concept_id: str,
    question: str,
    answer: str,
) -> dict:
    """Evaluate a student's answer and update mastery."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    concept = tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found in course {course_id}"}

    store = _mgr.store
    student = store.get_or_create_student(student_id)
    node = student.mastery_nodes.get(concept_id)
    previous_mastery = node.mastery_level if node else 0.0

    course_info_dict = tree.course_info.model_dump() if tree.course_info else None
    evaluation = await evaluate_answer(concept, question, answer, previous_mastery, course_info=course_info_dict)

    mastery_score = evaluation.get("mastery_score", 0.0)
    misconceptions = evaluation.get("misconceptions", [])

    updated_node = store.update_mastery(
        student_id=student_id,
        concept_id=concept_id,
        mastery_level=mastery_score,
        misconceptions=misconceptions,
        time_spent=2.0,
    )

    return {
        "course_id": course_id,
        "concept_id": concept_id,
        "evaluation": evaluation,
        "previous_mastery": previous_mastery,
        "new_mastery": updated_node.mastery_level,
        "total_attempts": updated_node.attempts,
    }


# ── Tool: Get Next Recommended Concepts ──────────────────────────────────────

def tool_get_next_concepts(student_id: str, course_id: str, limit: int = 3) -> dict:
    """Get the next concepts recommended for the student in a course."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    next_concepts = _mgr.store.get_next_concepts(student_id, tree, limit)
    return {
        "student_id": student_id,
        "course_id": course_id,
        "recommended": [
            {
                "concept_id": c.concept_id,
                "title": c.title,
                "chapter": c.chapter_title,
                "difficulty": c.difficulty,
                "bloom_level": c.bloom_level,
                "description": c.description,
            }
            for c in next_concepts
        ],
    }


# ── Tool: Get Concept Details ────────────────────────────────────────────────

def tool_get_concept(course_id: str, concept_id: str) -> dict:
    """Get detailed information about a specific concept within a course."""
    try:
        tree = _mgr.get_tree(course_id)
    except ValueError as e:
        return {"error": str(e)}

    concept = tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found in course {course_id}"}

    prerequisites = tree.get_prerequisites(concept_id)
    dependents = tree.get_dependents(concept_id)

    return {
        "course_id": course_id,
        "concept_id": concept.concept_id,
        "title": concept.title,
        "chapter": concept.chapter_title,
        "description": concept.description,
        "key_ideas": concept.key_ideas,
        "difficulty": concept.difficulty,
        "bloom_level": concept.bloom_level,
        "prerequisites": [{"id": p.concept_id, "title": p.title} for p in prerequisites],
        "unlocks": [{"id": d.concept_id, "title": d.title} for d in dependents],
    }
