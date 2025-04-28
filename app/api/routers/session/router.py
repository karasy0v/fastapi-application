from fastapi import APIRouter, Depends, Path
from app.api.schemas.session import SessionCreate
from app.core.models.db_helper import db_helper as db
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.prefixs import PREFIX_SESSION, TAG_SESSION
from app.crud.session import get_session_by_id, create_new_session

router = APIRouter(prefix=PREFIX_SESSION, tags = TAG_SESSION)

@router.get('/{id}')
async def get_session(id: int = Path(...), db: AsyncSession = Depends(db.session_getter)):
    return await get_session_by_id(id,db)

@router.post('/create')
async def create_session(session_data: SessionCreate, db: AsyncSession = Depends(db.session_getter)):
    return await create_new_session(session_data, db)