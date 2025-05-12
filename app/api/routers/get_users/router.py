from fastapi import FastAPI
from fastapi import APIRouter
from app.api.schemas.user import UserRead, UserUpdate
from app.api.dependencies.fastapi_users_router import fastapi_users
from app.api.prefixs import PREFIX_USER, TAG_USER

router = APIRouter(
    prefix=PREFIX_USER,
    tags=TAG_USER,
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
