from fastapi_users import schemas

from app.core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    pass


class UserCreate(schemas.BaseUserCreate):
    name: str
    surname: str
    phone_number: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
