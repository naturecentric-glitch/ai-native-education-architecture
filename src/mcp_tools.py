"""
MCP Server — Content & Mastery Tools

Exposes the platform's capabilities as MCP tools that the AI Host can discover and invoke.
For local dev, these are called directly. In production, they run as an MCP server over stdio/SSE.
"""
from src.mastery_tree import MasteryTree, StudentStore, Concept
from src.gemini_engine import (
    evaluate_answer,
    teach_concept,
    generate_questions,
    analyze_misconceptions,
)


# ── Singletons ───────────────────────────────────────────────────────────────

_tree = MasteryTree("math6")
_store = StudentStore()


# ── Tool: Get Curriculum Overview ────────────────────────────────────────────

def tool_get_curriculum() -> dict:
    """Get the full curriculum structure — chapters and concepts."""
    chapters = _tree.get_chapters()
    result = []
    for ch in chapters:
        concepts = _tree.get_concepts_for_chapter(ch["chapter_id"])
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
    return {"subject": "Class 6 Mathematics", "chapters": result}


# ── Tool: Get Student Profile ────────────────────────────────────────────────

def tool_get_student_profile(student_id: str) -> dict:
    """Get a student's full profile including mastery state."""
    student = _store.get_or_create_student(student_id)
    mastery_summary = _store.get_mastery_summary(student_id, _tree)
    next_concepts = _store.get_next_concepts(student_id, _tree)

    return {
        "student_id": student.student_id,
        "name": student.name,
        "grade": student.grade,
        "mastery_summary": mastery_summary,
        "next_recommended": [
            {"concept_id": c.concept_id, "title": c.title, "difficulty": c.difficulty}
            for c in next_concepts
        ],
        "total_concepts": len(_tree.get_all_concepts()),
        "mastered_count": sum(1 for m in mastery_summary if m["status"] == "mastered"),
        "in_progress_count": sum(1 for m in mastery_summary if m["status"] == "in_progress"),
    }


# ── Tool: Teach a Concept ───────────────────────────────────────────────────

async def tool_teach_concept(student_id: str, concept_id: str) -> dict:
    """Generate a personalized lesson for a concept."""
    concept = _tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found"}

    student = _store.get_or_create_student(student_id)
    node = student.mastery_nodes.get(concept_id)
    mastery = node.mastery_level if node else 0.0
    misconceptions = node.misconceptions_detected if node else []

    lesson = await teach_concept(concept, student.name, mastery, misconceptions)
    return {
        "concept_id": concept_id,
        "concept_title": concept.title,
        "chapter": concept.chapter_title,
        "lesson": lesson,
        "current_mastery": mastery,
    }


# ── Tool: Generate Practice Questions ────────────────────────────────────────

async def tool_generate_questions(
    concept_id: str,
    count: int = 3,
    difficulty: str = "medium",
) -> dict:
    """Generate practice questions for a concept."""
    concept = _tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found"}

    questions = await generate_questions(concept, count, difficulty)
    return {
        "concept_id": concept_id,
        "concept_title": concept.title,
        "questions": questions,
    }


# ── Tool: Evaluate Student Answer ────────────────────────────────────────────

async def tool_evaluate_answer(
    student_id: str,
    concept_id: str,
    question: str,
    answer: str,
) -> dict:
    """Evaluate a student's answer and update mastery."""
    concept = _tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found"}

    student = _store.get_or_create_student(student_id)
    node = student.mastery_nodes.get(concept_id)
    previous_mastery = node.mastery_level if node else 0.0

    evaluation = await evaluate_answer(concept, question, answer, previous_mastery)

    # Update mastery in store
    mastery_score = evaluation.get("mastery_score", 0.0)
    misconceptions = evaluation.get("misconceptions", [])

    updated_node = _store.update_mastery(
        student_id=student_id,
        concept_id=concept_id,
        mastery_level=mastery_score,
        misconceptions=misconceptions,
        time_spent=2.0,  # estimated per question
    )

    return {
        "concept_id": concept_id,
        "evaluation": evaluation,
        "previous_mastery": previous_mastery,
        "new_mastery": updated_node.mastery_level,
        "total_attempts": updated_node.attempts,
    }


# ── Tool: Get Next Recommended Concepts ──────────────────────────────────────

def tool_get_next_concepts(student_id: str, limit: int = 3) -> dict:
    """Get the next concepts recommended for the student."""
    next_concepts = _store.get_next_concepts(student_id, _tree, limit)
    return {
        "student_id": student_id,
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

def tool_get_concept(concept_id: str) -> dict:
    """Get detailed information about a specific concept."""
    concept = _tree.get_concept(concept_id)
    if not concept:
        return {"error": f"Concept {concept_id} not found"}

    prerequisites = _tree.get_prerequisites(concept_id)
    dependents = _tree.get_dependents(concept_id)

    return {
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
