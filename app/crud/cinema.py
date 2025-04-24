
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas.cinema import CinemaCreate, CinemaUpdate
from app.core.models.models import Cinema 



async def get_cinema(id,
    session: AsyncSession) -> Cinema:
    stmnt = select(Cinema).where(Cinema.id == id)
    result = await session.scalar(stmnt)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cinema not found!')
    return result

async def create_new_cinema(cinema_data: CinemaCreate, session: AsyncSession)  -> Cinema:
    query_check = select(Cinema).where(Cinema.name == cinema_data.name)
    result = await session.scalar(query_check)    
    if result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Cinema with name {cinema_data.name} is already exists!')
    
    new_cinema = Cinema(
        name=cinema_data.name
    )
    session.add(new_cinema)
    await session.commit()
    return{'detail' : 'successfull!'}


async def cinema_delete(id: int, session: AsyncSession):
    query_check = select(Cinema).where(Cinema.id == id)
    result = await session.scalar(query_check)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'You are trying to delete a cinema, but it doesn`t exist!')
    
    await session.delete(result)
    await session.commit()
    return {'detail': 'successfully deleted!'}

async def cinema_update(cinema_data: CinemaUpdate, session: AsyncSession):
    query_check = select(Cinema).where(Cinema.id == cinema_data.id)
    result = await session.scalar(query_check)
    
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = 'Cinema not found!')
    
    result.name = cinema_data.name
    await session.commit()
    return {'datail': 'successfull updated!'}


