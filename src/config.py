"""
AI-Native Education Platform — Configuration
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONTENT_DIR = DATA_DIR / "content"
MASTERY_DIR = DATA_DIR / "mastery"
STUDENT_DIR = DATA_DIR / "students"

# Ensure directories exist
for d in [CONTENT_DIR, MASTERY_DIR, STUDENT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Google Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# App
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
APP_ENV = os.getenv("APP_ENV", "development")
