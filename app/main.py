from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from api.main_router import router as api_router
from core.models.db_helper import db_helper
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
