from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import Movie

async def get_movie_by_id(id: int, session: AsyncSession):
    movie_query = select(Movie).where(Movie.id == id)
    result = await session.scalar(movie_query)

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail= 'Movie is not found!'
        )
    return result