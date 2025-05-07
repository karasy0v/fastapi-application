from typing import Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from app.core.models.access_token import AccessToken
from app.core.models.models import User
from app.core.config import settings
from app.api.dependencies.access_token import get_access_tokens_db

def get_database_strategy(
    access_token_db: Annotated[
        AccessTokenDatabase[AccessToken],
        Depends(get_access_tokens_db),
     ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db, 
        lifetime_seconds=settings.access_token.lifetime_seconds,
)