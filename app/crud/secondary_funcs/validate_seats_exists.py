from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import (
    Seat,
    Session,
)


async def validate_seats(row: int, col: int, session_id: int, db: AsyncSession):
    seat_query = (
        select(Seat)
        .join(Session, Seat.auditorium_id == Session.auditorium_id)
        .where(Seat.row == row, Seat.column == col, Session.id == session_id)
    )
    seat = await db.scalar(seat_query)

    if seat:
        return seat.id
    return False
