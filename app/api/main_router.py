from fastapi import APIRouter
from app.api.cinema.router import router as cinema_router
from app.api.auditorium.router import router as auditorium_router

router = APIRouter()

routers = [cinema_router,
    auditorium_router]

for rout in routers:
    router.include_router(rout)