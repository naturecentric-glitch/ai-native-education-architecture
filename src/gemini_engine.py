"""
Gemini-powered evaluation and teaching engine — SUBJECT-AGNOSTIC.

Uses Gemini (via langchain-google-genai) to:
1. Evaluate student answers for deep understanding (any subject)
2. Generate personalized teaching content
3. Create transfer tasks
4. Detect misconceptions
5. Expand course curricula with AI

The engine reads subject/grade/board context from course metadata,
so prompts adapt automatically to any course.
"""
import json
from typing import Optional

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from src.config import GOOGLE_API_KEY, AI_MODEL, AI_EXPANSION_MODEL
from src.mastery_tree import Concept, MasteryNode, MasteryTree, StudentStore


# ── Gemini Client ────────────────────────────────────────────────────────────

def get_llm(temperature: float = 0.3, model: str | None = None):
    return ChatGoogleGenerativeAI(
        model=model or AI_MODEL,
        google_api_key=GOOGLE_API_KEY,
        temperature=temperature,
    )


def _subject_context(course_info: dict | None) -> str:
    """Build dynamic subject context string from course metadata."""
    if not course_info:
        return "a general education course"
    subject = course_info.get("subject", "general")
    title = course_info.get("title", "")
    grade = course_info.get("grade", 0)
    board = course_info.get("board", "")
    age_range = {6: "11-12", 7: "12-13", 8: "13-14", 9: "14-15", 10: "15-16",
                 11: "16-17", 12: "17-18"}.get(grade, "11-18")
    parts = []
    if title:
        parts.append(title)
    if board:
        parts.append(f"({board} curriculum)")
    if grade:
        parts.append(f"for Class {grade} students (age {age_range})")
    return " ".join(parts) if parts else subject


# ── Evaluation Engine ────────────────────────────────────────────────────────

def _evaluation_prompt(course_info: dict | None) -> str:
    ctx = _subject_context(course_info)
    return f"""You are an expert evaluator for {ctx}.

Your job is to evaluate a student's answer for DEEP UNDERSTANDING across three dimensions:

1. **Conceptual Anchors**: Does the student understand the core principle? Not just keywords.
2. **Logic Traceability**: Is their reasoning process sound? Can you trace each step?
3. **Completeness**: Did they address all parts of the question?

IMPORTANT RULES:
- Be encouraging but honest
- Identify specific misconceptions (not vague feedback)
- Assess mastery on a 0.0 to 1.0 scale
- Provide actionable next steps
- Use simple, clear English appropriate for the student's age
- If the answer is in Hindi or another Indian language, evaluate it fairly

You must respond in valid JSON format only."""


async def evaluate_answer(
    concept: Concept,
    question: str,
    student_answer: str,
    previous_mastery: float = 0.0,
    course_info: dict | None = None,
) -> dict:
    """Evaluate a student's answer using Gemini."""
    llm = get_llm(temperature=0.2)
    ctx = _subject_context(course_info)

    prompt = f"""Evaluate this student's answer for {ctx}.

**Topic**: {concept.title}
**Chapter**: {concept.chapter_title}
**Key Ideas to Look For**: {json.dumps(concept.key_ideas)}
**Question**: {question}
**Student's Answer**: {student_answer}
**Previous Mastery Level**: {previous_mastery}

Respond with this exact JSON structure:
{{
    "mastery_score": <float 0.0 to 1.0>,
    "conceptual_understanding": <float 0.0 to 1.0>,
    "logic_traceability": <float 0.0 to 1.0>,
    "completeness": <float 0.0 to 1.0>,
    "misconceptions": [<list of specific misconceptions detected, empty if none>],
    "feedback": "<encouraging, specific feedback for the student>",
    "correct_approach": "<brief explanation of the right way to think about this>",
    "next_step": "<what the student should focus on next>"
}}"""

    response = await llm.ainvoke([
        SystemMessage(content=_evaluation_prompt(course_info)),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


# ── Teaching Engine ──────────────────────────────────────────────────────────

def _teaching_prompt(course_info: dict | None) -> str:
    ctx = _subject_context(course_info)
    subject = (course_info or {}).get("subject", "the subject")
    return f"""You are a warm, patient, and brilliant tutor for {ctx}.

Your teaching style:
- Start with a relatable real-life example from Indian daily life
- Build concepts step-by-step, never skip steps
- Use visual metaphors and analogies relevant to {subject}
- Ask guiding questions to make the student think
- Celebrate small wins
- Use simple English (the student may not be a native English speaker)
- Include a "Try This!" practice problem at the end
- Keep it concise but thorough (300-500 words)"""


async def teach_concept(
    concept: Concept,
    student_name: str = "Student",
    mastery_level: float = 0.0,
    misconceptions: list[str] | None = None,
    course_info: dict | None = None,
) -> dict:
    """Generate a personalized lesson for a concept."""
    llm = get_llm(temperature=0.5)
    ctx = _subject_context(course_info)

    context = f"The student's current mastery is {mastery_level:.0%}."
    if misconceptions:
        context += f" Known misconceptions: {', '.join(misconceptions)}. Address these specifically."
    if mastery_level > 0:
        context += " This is a review/remediation — focus on gaps, don't repeat what they already know."

    prompt = f"""Teach this concept to {student_name}:

**Topic**: {concept.title}
**Chapter**: {concept.chapter_title} ({ctx})
**Description**: {concept.description}
**Key Ideas to Cover**: {json.dumps(concept.key_ideas)}
**Bloom's Level**: {concept.bloom_level}
**{context}**

Structure your response as JSON:
{{
    "title": "<engaging lesson title>",
    "hook": "<real-life hook/story to grab attention — Indian context>",
    "explanation": "<main teaching content with step-by-step explanation>",
    "worked_example": "<a fully worked example with each step explained>",
    "try_this": {{
        "question": "<a practice problem for the student>",
        "hint": "<a gentle hint>",
        "answer": "<the correct answer with explanation>"
    }},
    "fun_fact": "<an interesting fact related to this topic>"
}}"""

    response = await llm.ainvoke([
        SystemMessage(content=_teaching_prompt(course_info)),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


# ── Question Generator ───────────────────────────────────────────────────────

def _question_prompt(course_info: dict | None) -> str:
    ctx = _subject_context(course_info)
    return f"""You are an expert question designer for {ctx}.
Generate questions that test DEEP UNDERSTANDING, not just recall.
Include a mix of: direct application, word problems, and transfer tasks (apply concept to unfamiliar context).
All questions should be age-appropriate for the target students.
Respond in valid JSON only."""


async def generate_questions(
    concept: Concept,
    count: int = 3,
    difficulty: str = "medium",
    include_transfer: bool = True,
    course_info: dict | None = None,
) -> list[dict]:
    """Generate practice questions for a concept."""
    llm = get_llm(temperature=0.6)

    prompt = f"""Generate {count} questions for this topic:

**Topic**: {concept.title}
**Chapter**: {concept.chapter_title}
**Key Ideas**: {json.dumps(concept.key_ideas)}
**Difficulty**: {difficulty} (easy/medium/hard)
**Include Transfer Task**: {include_transfer}

A "transfer task" requires applying the concept to a completely new, real-world context the student hasn't seen before.

Respond with JSON:
{{
    "questions": [
        {{
            "id": 1,
            "type": "<direct|word_problem|transfer_task>",
            "question": "<the question>",
            "hint": "<optional hint>",
            "expected_answer": "<correct answer with explanation>",
            "concepts_tested": ["<concept ids tested>"],
            "difficulty": <float 0.0 to 1.0>
        }}
    ]
}}"""

    response = await llm.ainvoke([
        SystemMessage(content=_question_prompt(course_info)),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    result = json.loads(text)
    return result.get("questions", [])


# ── Misconception Analyzer ───────────────────────────────────────────────────

async def analyze_misconceptions(
    concept: Concept,
    student_answer: str,
    correct_answer: str,
    course_info: dict | None = None,
) -> list[dict]:
    """Deep analysis of what specific misconception led to the wrong answer."""
    llm = get_llm(temperature=0.2)
    ctx = _subject_context(course_info)

    prompt = f"""A student studying {ctx} gave a wrong answer. Analyze the specific misconception.

**Topic**: {concept.title}
**Key Ideas**: {json.dumps(concept.key_ideas)}
**Correct Answer**: {correct_answer}
**Student's Answer**: {student_answer}

Respond with JSON:
{{
    "misconceptions": [
        {{
            "misconception": "<specific misconception name>",
            "description": "<what the student likely thought>",
            "evidence": "<what in their answer shows this>",
            "remediation": "<specific activity to fix this>"
        }}
    ]
}}"""

    response = await llm.ainvoke([
        SystemMessage(content=_evaluation_prompt(course_info)),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    result = json.loads(text)
    return result.get("misconceptions", [])


# ── Curriculum Expansion Engine ──────────────────────────────────────────────

EXPANSION_SYSTEM_PROMPT = """You are a curriculum design expert. Given a course's existing chapter structure and seed concepts, 
you generate additional concepts that fill out the chapter comprehensively.

Rules:
- Each new concept must have a unique concept_id following the pattern: {course_id}.{chapter_key}.{snake_case_suffix}
- Assign appropriate bloom_level (remember/understand/apply/analyze/evaluate/create)
- Set difficulty 0.0-1.0 (progressive within the chapter)
- Define prerequisites referencing existing concept_ids where appropriate
- Write clear, concise descriptions
- Include 3-5 key_ideas per concept
- Generate 3-6 new concepts per chapter (depending on chapter depth)
- Do NOT duplicate existing concepts
- Respond in valid JSON only"""


async def expand_chapter(
    course_id: str,
    chapter_key: str,
    chapter_title: str,
    existing_concepts: list[dict],
    course_info: dict | None = None,
) -> list[dict]:
    """Use Gemini to expand a chapter with additional concepts."""
    llm = get_llm(temperature=0.6, model=AI_EXPANSION_MODEL)
    ctx = _subject_context(course_info)

    existing_summary = json.dumps([
        {"concept_id": c["concept_id"], "title": c["title"], "bloom_level": c["bloom_level"]}
        for c in existing_concepts
    ], indent=2)

    prompt = f"""Expand this chapter with additional concepts for {ctx}:

**Course ID**: {course_id}
**Chapter Key** (for concept_id prefix): {chapter_key}
**Chapter Title**: {chapter_title}
**Existing Concepts**:
{existing_summary}

Generate 3-6 NEW concepts that complement the existing ones. Cover areas not yet addressed.
Use concept_id format: {course_id}.{chapter_key}.<new_suffix>

Respond with JSON:
{{
    "new_concepts": [
        {{
            "concept_id": "{course_id}.{chapter_key}.<suffix>",
            "title": "<concept title>",
            "bloom_level": "<bloom level>",
            "difficulty": <float>,
            "prerequisites": ["<existing concept_ids where relevant>"],
            "description": "<clear description>",
            "key_ideas": ["<idea1>", "<idea2>", "<idea3>"]
        }}
    ]
}}"""

    response = await llm.ainvoke([
        SystemMessage(content=EXPANSION_SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    result = json.loads(text)
    return result.get("new_concepts", [])


async def expand_full_course(course_id: str) -> dict:
    """Expand an entire course curriculum using Gemini."""
    from src.mastery_tree import get_course_info
    from src.config import CONTENT_DIR

    info = get_course_info(course_id)
    if not info:
        return {"error": f"Course '{course_id}' not found"}

    course_info_dict = info.model_dump()

    # Load current curriculum
    curr_path = CONTENT_DIR / info.curriculum_file
    with open(curr_path) as f:
        curriculum = json.load(f)

    total_new = 0
    expanded_chapters = []

    for chapter in curriculum["chapters"]:
        # Extract chapter_key from first concept's concept_id
        if chapter["concepts"]:
            parts = chapter["concepts"][0]["concept_id"].split(".")
            chapter_key = parts[1] if len(parts) >= 3 else chapter["chapter_id"]
        else:
            chapter_key = chapter["chapter_id"]

        try:
            new_concepts = await expand_chapter(
                course_id=course_id,
                chapter_key=chapter_key,
                chapter_title=chapter["title"],
                existing_concepts=chapter["concepts"],
                course_info=course_info_dict,
            )
            chapter["concepts"].extend(new_concepts)
            total_new += len(new_concepts)
            expanded_chapters.append({
                "chapter": chapter["title"],
                "new_concepts": len(new_concepts),
            })
        except Exception as e:
            expanded_chapters.append({
                "chapter": chapter["title"],
                "error": str(e),
            })

    # Save expanded curriculum
    with open(curr_path, "w") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)

    total_concepts = sum(len(ch["concepts"]) for ch in curriculum["chapters"])

    return {
        "course_id": course_id,
        "title": info.title,
        "total_concepts_now": total_concepts,
        "new_concepts_added": total_new,
        "chapters": expanded_chapters,
    }
