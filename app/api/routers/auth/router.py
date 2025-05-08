from fastapi import APIRouter
from app.api.prefixs import PREFIX_AUTH, TAG_AUTH
from app.api.dependencies.backend import authentication_backend
from app.api.dependencies.fastapi_users_router import fastapi_users
from app.api.schemas.user import UserRead, UserCreate

router = APIRouter(prefix=PREFIX_AUTH, tags=TAG_AUTH)

router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
    ),
)

router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)
