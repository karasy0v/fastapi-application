
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import Cinema 



async def get_cinema(id,
    session: AsyncSession) -> Cinema:
    stmnt = select(Cinema).where(Cinema.id == id)
    result = await session.scalar(stmnt)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found!')
    return result