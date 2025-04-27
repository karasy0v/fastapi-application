from fastapi import APIRouter, Depends, Path
from app.api.prefixs import TAG_MOVIE, PREFIX_MOVIE
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.movies import MovieRead
from app.core.models.db_helper import db_helper as db
from app.crud.movie import get_movie_by_id

router = APIRouter(prefix=PREFIX_MOVIE, tags=TAG_MOVIE)

@router.get('/{id}',response_model=MovieRead)
async def get_movie(id: int = Path(...), db: AsyncSession = Depends(db.session_getter)):
    return await get_movie_by_id(id, db)
