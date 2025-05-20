from datetime import (
    timezone,
    datetime,
    timedelta,
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import Session
from app.core.config import settings


async def validate_time_booking(session_id: int, db: AsyncSession):
    session_query = select(Session).where(Session.id == session_id)

    session_result = await db.scalars(session_query)

    result = session_result.first()

    if (result.start_time - timedelta(hours=settings.reservation_time.hours_before_start)).replace(
        tzinfo=timezone.utc
    ) < datetime.now(timezone.utc):
        return False
    return result.start_time
