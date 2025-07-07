from fastapi import APIRouter, Body
from ..services.generative_ai_service import get_ai_response

router = APIRouter()

@router.post("/generate")
async def generate(prompt: str = Body(..., embed=True)):
    response = await get_ai_response(prompt)
    return {"response": response}
