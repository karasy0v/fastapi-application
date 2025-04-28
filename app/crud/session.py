from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.session import SessionCreate, SessionRead
from app.core.models.models import Movie, Session
from datetime import timedelta
from app.core.config import settings


async def get_session_by_id(id: int, session: AsyncSession):
    session_query = select(Session).where(Session.id == id)
    result = await session.scalar(session_query)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Session is not found!')
    return SessionRead(
        start_time=result.start_time.strftime(settings.dt.value),
        end_time = result.end_time.strftime(settings.dt.value),
        auditorium_id=result.auditorium_id,
        movie_id=result.movie_id,
    )


async def create_new_session(session_data: SessionCreate, session: AsyncSession):
    movie_query = select(Movie).where(Movie.id == session_data.movie_id)
    movie = await session.scalar(movie_query)

    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Movie not found!') 
    
    new_session = Session(
        auditorium_id = session_data.auditorium_id,
        movie_id = session_data.movie_id,
        start_time = session_data.start_time.replace(tzinfo=None), 
        end_time = (session_data.start_time + timedelta(minutes=movie.duration)).replace(tzinfo=None),
    )

    session.add(new_session)
    await session.commit()
    await session.refresh(new_session)

    return new_session