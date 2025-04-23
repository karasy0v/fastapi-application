from fastapi import APIRouter
from app.api.cinema.router import router as cinema_router

router = APIRouter()
router.include_router(
    cinema_router
    )