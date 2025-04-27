from fastapi import APIRouter
from app.api.routers.cinema.router import router as cinema_router
from app.api.routers.auditorium.router import router as auditorium_router
from app.api.routers.movies.router import router as movie_router

router = APIRouter()

routers = [cinema_router,
    auditorium_router,
    movie_router]

for rout in routers:
    router.include_router(rout)