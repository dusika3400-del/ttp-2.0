from fastapi import FastAPI
from app.models.models import Feedback
from pydantic import BaseModel  

app = FastAPI()

feedback_db = []

@app.post('/feedback')
async def add_feedback(feedback: Feedback):
    feedback_db.append({"name": feedback.name, "message": feedback.message})
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}