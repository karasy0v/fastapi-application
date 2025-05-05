from fastapi import APIRouter, Depends
from app.api.prefixs import TAG_TICKET, PREFIX_TICKET
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.ticket import BuyTicket, ReadTicket
from app.core.models.db_helper import db_helper as db
from app.crud.ticket import get_tickets, buy_tickets
router = APIRouter(prefix=PREFIX_TICKET, tags= TAG_TICKET)

@router.get('/')
async def get_ticket(user_id: int, db: AsyncSession = Depends(db.session_getter)):
    return await get_tickets(user_id, db)

@router.post('/buy', response_model = ReadTicket)
async def buy_ticket(ticket_data: BuyTicket, db: AsyncSession = Depends(db.session_getter)):
    return await buy_tickets(ticket_data, db)