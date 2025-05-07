from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends
from app.core.models.access_token import AccessToken
from app.core.models.db_helper import db_helper

async def get_access_tokens_db(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
        ],
):  
    yield AccessToken.get_db(session=session)