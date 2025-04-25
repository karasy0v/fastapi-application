from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import Auditorium

async def get_auditorium_by_id(id: int, session: AsyncSession):
    query_check = select(Auditorium).where(Auditorium.id == id).options(joinedload(Auditorium.cinema))
    result = await session.scalar(query_check)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Auditorium is nor found!')
    return result

