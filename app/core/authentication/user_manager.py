import logging
from typing import Optional, Union
from app.api.schemas.user import UserCreate
from app.core.types.user_id import UserIdType
from fastapi import Request
from fastapi_users import BaseUserManager, IntegerIDMixin, InvalidPasswordException
from app.core.config import settings
from app.core.models.models import User


log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = settings.authentication.reset_password_token_secret
    verification_token_secret = settings.authentication.verification_token_secret

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)

    async def validate_password(self, password: str, user: Union[UserCreate, User]) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(reason="Password should be at least 8 characters")

        if user.email in password:
            raise InvalidPasswordException(reason="Password should not contain e-mail")
