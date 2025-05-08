from fastapi_users import FastAPIUsers
from app.api.dependencies.user_manager import get_user_manager
from app.core.models.models import User
from app.core.types.user_id import UserIdType
from app.api.dependencies.backend import authentication_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
