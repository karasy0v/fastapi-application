from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.dependencies.exception_handlers import register_exception_handlers
from app.core.models.redis_helper import redis_helper
from app.api.main_router import router as api_router
from app.core.models.db_helper import db_helper
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_helper.init()
    yield
    await db_helper.dispose()
    await redis_helper.close()


app = FastAPI(
    default_response_class=JSONResponse,
    lifespan=lifespan,
)


app.include_router(
    api_router,
    prefix=settings.api.prefix,
)

register_exception_handlers(app)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.run.host, port=settings.run.port, reload=True)
