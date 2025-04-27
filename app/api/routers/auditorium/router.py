from fastapi import APIRouter, Depends, Path
from app.api.prefixs import PREFIX_AUDITORIUM, TAG_AUDITORIUM
from app.api.schemas.auditorium import AuditoriumRead
from app.core.models.db_helper import db_helper as db
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.auditorium import get_auditorium_by_id


router = APIRouter(prefix=PREFIX_AUDITORIUM, tags=TAG_AUDITORIUM)


@router.get('/{id}', response_model=AuditoriumRead) 
async def get_audirotium(id: int = Path(...), db: AsyncSession = Depends(db.session_getter)):
    return await get_auditorium_by_id(id, db)
