from fastapi.security import HTTPBearer
from fastapi_users.authentication import BearerTransport
from app.core.config import settings

http_bearer = HTTPBearer(auto_error=False)
bearer_transport = BearerTransport(
    tokenUrl=settings.api.bearer_token_transport,
)
