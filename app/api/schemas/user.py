from fastapi_users import schemas

from app.api.schemas.get_user import UserBase
from app.core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType], UserBase):
    pass


class UserCreate(schemas.BaseUserCreate, UserBase):
    pass


class UserUpdate(schemas.BaseUserUpdate, UserBase):
    pass
