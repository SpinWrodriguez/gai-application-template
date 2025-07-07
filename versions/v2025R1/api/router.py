from fastapi import APIRouter
from .controllers import generative_ai_controller

router = APIRouter()
router.include_router(generative_ai_controller.router, prefix="/gai")
