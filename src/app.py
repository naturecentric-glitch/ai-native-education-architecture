"""
AI Host — FastAPI Application

Central server that exposes the education platform via REST endpoints.
In production, this would use LangGraph for multi-step agent orchestration.
For local dev, it calls MCP tools directly.
"""
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.config import APP_HOST, APP_PORT
from src.mcp_tools import (
    tool_get_curriculum,
    tool_get_student_profile,
    tool_teach_concept,
    tool_generate_questions,
    tool_evaluate_answer,
    tool_get_next_concepts,
    tool_get_concept,
)


# ── App Setup ────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 AI-Native Education Platform starting...")
    print("📚 Class 6 Mathematics — NCERT Curriculum loaded")
    yield
    print("👋 Shutting down...")

app = FastAPI(
    title="AI-Native Education Platform",
    description="Class 6 Mathematics — Mastery-based learning with Gemini AI",
    version="0.1.0",
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


# ── API Endpoints ────────────────────────────────────────────────────────────

@app.get("/api/curriculum")
async def get_curriculum():
    """Get the full curriculum — chapters and concepts."""
    return tool_get_curriculum()


@app.get("/api/concept/{concept_id}")
async def get_concept(concept_id: str):
    """Get details for a specific concept."""
    result = tool_get_concept(concept_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.get("/api/student/{student_id}")
async def get_student(student_id: str):
    """Get student profile and mastery state."""
    return tool_get_student_profile(student_id)


@app.get("/api/student/{student_id}/next")
async def get_next(student_id: str, limit: int = 3):
    """Get next recommended concepts for a student."""
    return tool_get_next_concepts(student_id, limit)


@app.post("/api/teach")
async def teach(req: TeachRequest):
    """Generate a personalized lesson for a concept."""
    result = await tool_teach_concept(req.student_id, req.concept_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.post("/api/questions")
async def questions(req: QuestionRequest):
    """Generate practice questions for a concept."""
    result = await tool_generate_questions(req.concept_id, req.count, req.difficulty)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@app.post("/api/evaluate")
async def evaluate(req: EvaluateRequest):
    """Evaluate a student's answer and update mastery."""
    result = await tool_evaluate_answer(req.student_id, req.concept_id, req.question, req.answer)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


# ── Serve Frontend ───────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the main student interface."""
    with open("frontend/index.html") as f:
        return HTMLResponse(content=f.read())


# ── Run ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host=APP_HOST, port=int(APP_PORT), reload=True)
