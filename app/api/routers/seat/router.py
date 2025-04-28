from fastapi import APIRouter, Depends
from app.api.schemas.seat import SeatRead
from app.core.models.db_helper import db_helper as db
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.prefixs import PREFIX_SEAT, TAG_SEAT
from app.crud.seat import get_seats

router = APIRouter(prefix=PREFIX_SEAT, tags = TAG_SEAT)


@router.get('/',response_model=SeatRead)
async def get_seat(auditorium_id: int,row: int, column: int, db: AsyncSession = Depends(db.session_getter)):
    return await get_seats(auditorium_id, row,column,db)