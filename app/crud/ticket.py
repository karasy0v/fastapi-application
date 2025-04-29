from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.ticket import BuyTicket
from app.core.models.models import Session, User, Ticket, Seat

async def get_tickets(user_id: int, db: AsyncSession):
    stmt = select(User).options(joinedload(User.tickets)).where(User.id == user_id)
    result = await db.scalar(stmt)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return result

async def buy_tickets(ticket_data: BuyTicket, db: AsyncSession): # user_id: int,  seat_id: int,
    stmt = select(Ticket).where(Ticket.seat_id == ticket_data.seat_id, Ticket.session_id == ticket_data.session_id)
    result = await db.scalar(stmt)


    if result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This ticket already exists!')
    seat_query = select(Seat).where(Seat.id == ticket_data.seat_id)
    seat = await db.scalar(seat_query)

    new_ticket = Ticket(
        session_id = ticket_data.session_id,
        seat_id = ticket_data.seat_id,
        user_id = ticket_data.user_id,
        price = seat.price,
    )

    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket