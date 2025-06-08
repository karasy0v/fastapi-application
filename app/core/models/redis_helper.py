from redis.asyncio import Redis, ConnectionPool
from app.core.config import settings


class RedisHelper:
    def __init__(self):
        self._pool: ConnectionPool | None = None
        self._redis: Redis | None = None

    async def init(self):
        self._pool = ConnectionPool(
            host=settings.redis.host,
            port=settings.redis.port,
            db=settings.redis.db,
            password=settings.redis.password,
            encoding=settings.redis.encoding,
            decode_responses=settings.redis.decode_response,
        )
        self._redis = Redis(connection_pool=self._pool)

    async def get_redis(self):
        if self._redis is None:
            await self.init()
        return self._redis

    async def close(self):
        if self._redis is not None:
            await self._redis.close()
        if self._pool is not None:
            await self._pool.disconnect()


redis_helper = RedisHelper()
