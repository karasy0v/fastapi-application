from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.core.models.models import Seat

async def get_seats(auditorium_id: int, row: int, col: int, session: AsyncSession):
    seat_query = select(Seat).where(Seat.auditorium_id == auditorium_id, Seat.row == row, Seat.column == col)
    seat = await session.scalar(seat_query)
    
    if not seat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Seat not found')
    return seat