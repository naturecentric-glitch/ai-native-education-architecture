"""
Gemini-powered evaluation and teaching engine.

Uses Gemini 3 Pro (via langchain-google-genai) to:
1. Evaluate student answers for deep understanding
2. Generate personalized teaching content
3. Create transfer tasks
4. Detect misconceptions
"""
import json
from typing import Optional

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from src.config import GOOGLE_API_KEY
from src.mastery_tree import Concept, MasteryNode, MasteryTree, StudentStore


# ── Gemini Client ────────────────────────────────────────────────────────────

def get_llm(temperature: float = 0.3):
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=temperature,
    )


# ── Evaluation Engine ────────────────────────────────────────────────────────

EVALUATION_SYSTEM_PROMPT = """You are an expert mathematics evaluator for Class 6 students (age 11-12) following the NCERT curriculum in India.

Your job is to evaluate a student's answer for DEEP UNDERSTANDING across three dimensions:

1. **Conceptual Anchors**: Does the student understand the core principle? Not just keywords.
2. **Logic Traceability**: Is their reasoning process sound? Can you trace each step?
3. **Completeness**: Did they address all parts of the question?

IMPORTANT RULES:
- Be encouraging but honest
- Identify specific misconceptions (not vague feedback)
- Assess mastery on a 0.0 to 1.0 scale
- Provide actionable next steps
- Use simple English appropriate for an 11-year-old
- If the answer is in Hindi or another Indian language, evaluate it fairly

You must respond in valid JSON format only."""


async def evaluate_answer(
    concept: Concept,
    question: str,
    student_answer: str,
    previous_mastery: float = 0.0,
) -> dict:
    """Evaluate a student's answer using Gemini."""
    llm = get_llm(temperature=0.2)

    prompt = f"""Evaluate this Class 6 student's answer.

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
        SystemMessage(content=EVALUATION_SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ])

    # Parse JSON from response
    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


# ── Teaching Engine ──────────────────────────────────────────────────────────

TEACHING_SYSTEM_PROMPT = """You are a warm, patient, and brilliant mathematics tutor for Class 6 students (age 11-12) in India, following the NCERT curriculum.

Your teaching style:
- Start with a relatable real-life example from Indian daily life
- Build concepts step-by-step, never skip steps
- Use visual metaphors and analogies
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
) -> dict:
    """Generate a personalized lesson for a concept."""
    llm = get_llm(temperature=0.5)

    context = f"The student's current mastery is {mastery_level:.0%}."
    if misconceptions:
        context += f" Known misconceptions: {', '.join(misconceptions)}. Address these specifically."
    if mastery_level > 0:
        context += " This is a review/remediation — focus on gaps, don't repeat what they already know."

    prompt = f"""Teach this concept to {student_name}:

**Topic**: {concept.title}
**Chapter**: {concept.chapter_title} (NCERT Class 6 Mathematics)
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
    "fun_fact": "<an interesting math fact related to this topic>"
}}"""

    response = await llm.ainvoke([
        SystemMessage(content=TEACHING_SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return json.loads(text)


# ── Question Generator ───────────────────────────────────────────────────────

QUESTION_SYSTEM_PROMPT = """You are an expert question designer for Class 6 mathematics (NCERT, India). 
Generate questions that test DEEP UNDERSTANDING, not just recall.
Include a mix of: direct application, word problems, and transfer tasks (apply concept to unfamiliar context).
All questions should be age-appropriate (11-12 years).
Respond in valid JSON only."""


async def generate_questions(
    concept: Concept,
    count: int = 3,
    difficulty: str = "medium",
    include_transfer: bool = True,
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
        SystemMessage(content=QUESTION_SYSTEM_PROMPT),
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
) -> list[dict]:
    """Deep analysis of what specific misconception led to the wrong answer."""
    llm = get_llm(temperature=0.2)

    prompt = f"""A Class 6 student gave a wrong answer. Analyze the specific misconception.

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
        SystemMessage(content=EVALUATION_SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ])

    text = response.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    result = json.loads(text)
    return result.get("misconceptions", [])
