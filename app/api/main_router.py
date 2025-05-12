from fastapi import APIRouter
from app.api.routers.cinema.router import router as cinema_router
from app.api.routers.auditorium.router import router as auditorium_router
from app.api.routers.movies.router import router as movie_router
from app.api.routers.session.router import router as session_router
from app.api.routers.seat.router import router as seat_router
from app.api.routers.buy_ticket.router import router as buy_ticket_router
from app.api.routers.auth.router import router as auth_router
from app.api.routers.get_users.router import router as users_router

router = APIRouter()

routers = [
    cinema_router,
    auditorium_router,
    movie_router,
    session_router,
    seat_router,
    buy_ticket_router,
    auth_router,
    users_router,
]

for rout in routers:
    router.include_router(rout)
