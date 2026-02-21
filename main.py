from fastapi import FastAPI
from app.models.models import User
from pydantic import BaseModel  

app = FastAPI()

class CalculateRequest(BaseModel):
    num1: float  
    num2: float

@app.post("/calculate")
async def calculate(request: CalculateRequest):
    result = request.num1 + request.num2
    return {"result": result}