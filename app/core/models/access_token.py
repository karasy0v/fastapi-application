
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import(  
    Mapped, 
    mapped_column,
)

from app.core.types.user_id import UserIdType
from app.core.models.base import Base


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):  
    user_id: Mapped[UserIdType] = mapped_column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False)

    @classmethod
    def get_access_token_db(cls, session: AsyncSession):
        return SQLAlchemyAccessTokenDatabase(session, cls)
