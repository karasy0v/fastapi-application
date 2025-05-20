from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import Reservation


async def validate_reservation(seat_id: int, session_id: int, db: AsyncSession):
    reservation_query = select(Reservation).where(Reservation.seat_id == seat_id, Reservation.session_id == session_id)
    reservation = await db.scalar(reservation_query)

    if reservation:
        return True
    return False
