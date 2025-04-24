from fastapi import APIRouter, Depends, Path
from app.api.prefixs import CINEMA, TAG_CINEMA
from app.core.models.db_helper import db_helper as db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends,  Path
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.cinema import get_cinema, create_new_cinema, cinema_delete
from app.api.schemas.cinema import CinemaCreate, CinemaRead

router = APIRouter(prefix=CINEMA, tags=TAG_CINEMA)

@router.get('/{id}',response_model=CinemaRead)
async def get_cinema_by_id(id: int = Path(...),
    db: AsyncSession = Depends(db.session_getter)):
    return await get_cinema(id,db)

@router.post('/create')
async def create_cinema(cinema_data: CinemaCreate, db: AsyncSession = Depends(db.session_getter)):
    return await create_new_cinema(cinema_data,db)

@router.delete('/delete/{id}')
async def delete_cinema(id: int = Path(...), db: AsyncSession = Depends(db.session_getter)):
    return await cinema_delete(id,db)