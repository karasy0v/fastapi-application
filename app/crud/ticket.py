from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.ticket import BuyTicket
from app.core.models.models import Session, User, Ticket, Seat

async def get_tickets(user_id: int, db: AsyncSession):
    stmt = select(User).options(joinedload(User.tickets)).where(User.id == user_id)
    result = await db.scalar(stmt)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return result

async def buy_tickets(ticket_data: BuyTicket, db: AsyncSession):
    stmt = select(Ticket).where(Ticket.seat_id == ticket_data.seat_id, Ticket.session_id == ticket_data.session_id)
    ticket_result = await db.scalars(stmt)

    result = ticket_result.first()


    if result:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='This ticket already exists!')
    
    session_query = select(Session).where(
        Session.id == ticket_data.session_id, 
    )
    session = await db.scalar(session_query)


    if session.start_time < datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Time over!")
    
    
    seat_query = select(Seat).join(Session, Session.auditorium_id == Seat.auditorium_id).where(Seat.id == ticket_data.seat_id, Session.id == ticket_data.session_id)
    seat = await db.scalar(seat_query)
  
    if not seat:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Bad data!')

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
    '''
    create trigger in postgresql

    
    CREATE OR REPLACE FUNCTION update_end_time()
    RETURNS TRIGGER AS $$
    BEGIN
        IF TG_OP = 'INSERT' OR 
        (TG_OP = 'UPDATE' AND (
            OLD.start_time IS DISTINCT FROM NEW.start_time OR
            OLD.movie_id IS DISTINCT FROM NEW.movie_id
        )) THEN
            
            NEW.end_time := NEW.start_time + (
                SELECT (duration * INTERVAL '1 minute') 
                FROM movies 
                WHERE movies.id = NEW.movie_id
            );
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

    CREATE OR REPLACE TRIGGER update_end_time_in_session
    BEFORE INSERT OR UPDATE ON sessions
    FOR EACH ROW
    EXECUTE FUNCTION update_end_time();
    '''
