from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from io import BytesIO
import json
import traceback

from resume_parser import extract_resume_text
from question_generator import generate_questions
from feedback_engine import evaluate_answer

app = FastAPI()


# ---------------- HOME ----------------
@app.get("/")
def home():
    return {"message": "AI Interview Assistant Running"}


# ---------------- UPLOAD RESUME ----------------
@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):

    try:
        contents = await file.read()
        file_stream = BytesIO(contents)

        resume_text = extract_resume_text(file_stream)

        if not resume_text or not resume_text.strip():
            return {"error": "No text extracted from resume"}

        raw_questions = generate_questions(resume_text)

        # ---------------- SAFE NORMALIZATION ----------------
        questions = []

        if isinstance(raw_questions, list):
            questions = raw_questions

        elif isinstance(raw_questions, str):

            cleaned = raw_questions.replace("```json", "").replace("```", "").strip()

            try:
                parsed = json.loads(cleaned)

                if isinstance(parsed, list):
                    questions = parsed

                else:
                    questions = [str(parsed)]

            except:
                # fallback split (safe)
                questions = [q.strip() for q in cleaned.split("\n") if q.strip()]

        # FINAL CLEANING
        questions = [str(q).strip() for q in questions if str(q).strip()]

        return {
            "questions": questions[:5]   # force exactly 5 max
        }

    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}


# ---------------- REQUEST MODEL ----------------
class AnswerRequest(BaseModel):
    question: str
    answer: str


# ---------------- EVALUATE ANSWER ----------------
@app.post("/evaluate-answer/")
def evaluate(data: AnswerRequest):

    try:
        feedback = evaluate_answer(data.question, data.answer)

        # clean markdown
        if isinstance(feedback, str):
            cleaned = feedback.replace("```json", "").replace("```", "").strip()

            try:
                parsed = json.loads(cleaned)

                # ensure proper structure
                return {
                    "score": parsed.get("score", 0),
                    "feedback": parsed.get("feedback", "No feedback")
                }

            except:
                # fallback parsing from text
                return {
                    "score": extract_score(cleaned),
                    "feedback": cleaned
                }

        return {
            "score": 0,
            "feedback": "Invalid response from model"
        }

    except Exception as e:
        return {
            "score": 0,
            "feedback": str(e)
        }


# ---------------- HELPER ----------------
import re

def extract_score(text):
    match = re.search(r'(\d+)\s*/\s*10', text)
    if match:
        return int(match.group(1))
    return 0