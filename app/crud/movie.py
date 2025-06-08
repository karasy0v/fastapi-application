from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import Movie
from app.core.models.redis_helper import redis_helper
from fastapi.encoders import jsonable_encoder
import json


async def get_movie_by_id(id: int, session: AsyncSession):
    redis = await redis_helper.get_redis()

    cached_movie = await redis.get(f"movie:{id}")
    if cached_movie:
        print("Закешировано")
        movie_data = json.loads(cached_movie)  # loads: json str -> dict/list
        return movie_data

    movie_query = select(Movie).where(Movie.id == id)
    result = await session.scalar(movie_query)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie  not found!")

    movie_data = jsonable_encoder(result)  # sqlalchemy/pydantic object -> dict
    await redis.setex(f"movie:{id}", 3600, json.dumps(movie_data))  # dumps: dict/list -> Json str

    return result
