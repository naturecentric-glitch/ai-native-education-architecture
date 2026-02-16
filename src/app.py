"""
AI Host — FastAPI Application (Multi-Course)

Central server that exposes the education platform via REST endpoints.
All routes are course-aware. /api/courses lists available courses,
and all other routes are scoped under /api/courses/{course_id}/...

In production, this would use LangGraph for multi-step agent orchestration.
For local dev, it calls MCP tools directly.
"""
import logging
import traceback
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

logger = logging.getLogger(__name__)

from src.config import APP_HOST, APP_PORT
from src.mcp_tools import (
    tool_list_courses,
    tool_get_course_info,
    tool_get_curriculum,
    tool_get_student_profile,
    tool_teach_concept,
    tool_generate_questions,
    tool_evaluate_answer,
    tool_get_next_concepts,
    tool_get_concept,
    tool_get_placement_test,
    tool_skip_chapter,
    tool_get_prerequisites_help,
)
from src.gemini_engine import expand_full_course
from src.content_cache import cache as content_cache


# ── App Setup ────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.mastery_tree import list_courses
    courses = list_courses()
    print("🚀 AI-Native Education Platform starting...")
    print(f"📚 {len(courses)} course(s) registered:")
    for c in courses:
        print(f"   {c.icon} {c.title} ({c.course_id})")
    yield
    print("👋 Shutting down...")

app = FastAPI(
    title="AI-Native Education Platform",
    description="Multi-course, mastery-based learning platform with Gemini AI",
    version="0.2.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Request Schemas ──────────────────────────────────────────────────────────

class TeachRequest(BaseModel):
    student_id: str = "student-001"
    concept_id: str

class QuestionRequest(BaseModel):
    concept_id: str
    count: int = 3
    difficulty: str = "medium"

class EvaluateRequest(BaseModel):
    student_id: str = "student-001"
    concept_id: str
    question: str
    answer: str

class SkipChapterRequest(BaseModel):
    student_id: str = "student-001"
    chapter_id: str
    passed: bool


# ── Course Discovery ─────────────────────────────────────────────────────────

@app.get("/api/courses")
async def get_courses():
    """List all available courses on the platform."""
    return tool_list_courses()


@app.get("/api/courses/{course_id}")
async def get_course(course_id: str):
    """Get metadata and stats for a specific course."""
    result = tool_get_course_info(course_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# ── Course-Scoped Endpoints ──────────────────────────────────────────────────

@app.get("/api/courses/{course_id}/curriculum")
async def get_curriculum(course_id: str):
    """Get the full curriculum for a course — chapters and concepts."""
    result = tool_get_curriculum(course_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/courses/{course_id}/concepts/{concept_id}")
async def get_concept(course_id: str, concept_id: str):
    """Get details for a specific concept within a course."""
    result = tool_get_concept(course_id, concept_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/courses/{course_id}/students/{student_id}")
async def get_student(course_id: str, student_id: str):
    """Get student profile and mastery state for a course."""
    result = tool_get_student_profile(student_id, course_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/courses/{course_id}/students/{student_id}/next")
async def get_next(course_id: str, student_id: str, limit: int = 3):
    """Get next recommended concepts for a student in a course."""
    result = tool_get_next_concepts(student_id, course_id, limit)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.post("/api/courses/{course_id}/teach")
async def teach(course_id: str, req: TeachRequest):
    """Generate a personalized lesson for a concept."""
    try:
        result = await tool_teach_concept(req.student_id, course_id, req.concept_id)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error("teach %s/%s failed: %s", course_id, req.concept_id, e)
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"AI generation failed: {type(e).__name__}: {e}")


@app.post("/api/courses/{course_id}/questions")
async def questions(course_id: str, req: QuestionRequest):
    """Generate practice questions for a concept."""
    try:
        result = await tool_generate_questions(course_id, req.concept_id, req.count, req.difficulty)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error("questions %s/%s failed: %s", course_id, req.concept_id, e)
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"AI generation failed: {type(e).__name__}: {e}")


@app.post("/api/courses/{course_id}/evaluate")
async def evaluate(course_id: str, req: EvaluateRequest):
    """Evaluate a student's answer and update mastery."""
    try:
        result = await tool_evaluate_answer(req.student_id, course_id, req.concept_id, req.question, req.answer)
        if "error" in result:
            raise HTTPException(status_code=404, detail=result["error"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error("evaluate %s/%s failed: %s", course_id, req.concept_id, e)
        logger.debug(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"AI evaluation failed: {type(e).__name__}: {e}")


# ── Admin / Expansion Endpoints ──────────────────────────────────────────────

# ── Placement & Skip Endpoints ───────────────────────────────────────────────

@app.get("/api/courses/{course_id}/placement")
async def get_placement_test(course_id: str):
    """Get the placement/diagnostic test for a course.
    One hard question per chapter — answer correctly to skip ahead."""
    result = tool_get_placement_test(course_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.post("/api/courses/{course_id}/skip")
async def skip_chapter(course_id: str, req: SkipChapterRequest):
    """Mark a chapter as mastered (placement skip) or leave it untouched."""
    result = tool_skip_chapter(req.student_id, course_id, req.chapter_id, req.passed)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/courses/{course_id}/concepts/{concept_id}/prerequisites")
async def get_prerequisites_help(course_id: str, concept_id: str, student_id: str = "student-001"):
    """Check which prerequisites a student is missing and get a study plan."""
    result = tool_get_prerequisites_help(student_id, course_id, concept_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# ── Admin / Expansion Endpoints ──────────────────────────────────────────────

@app.post("/api/admin/courses/{course_id}/expand")
async def expand_course(course_id: str):
    """Use Gemini to expand a course curriculum with additional AI-generated concepts.
    This uses the AI_EXPANSION_MODEL (default: gemini-2.5-pro-preview) to intelligently
    add 3-6 new concepts per chapter, filling in gaps in the seed curriculum."""
    result = await expand_full_course(course_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/admin/cache/stats")
async def cache_stats(course_id: str | None = None):
    """Get content cache statistics."""
    return content_cache.stats(course_id)


# ── Serve Frontend ───────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the course catalog (landing page)."""
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())


@app.get("/course/{course_id}", response_class=HTMLResponse)
async def course_page(course_id: str):
    """Serve the course learning interface."""
    with open("frontend/course.html") as f:
        html = f.read().replace("{{COURSE_ID}}", course_id)
        return HTMLResponse(content=html)


# ── Run ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host=APP_HOST, port=int(APP_PORT), reload=True)
