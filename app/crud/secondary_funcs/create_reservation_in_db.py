from datetime import (
    timedelta,
    timezone,
    datetime,
)
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.core.models.models import Reservation


async def create_reservation_in_db(seat_id, session_id, user_id, session_time, db: AsyncSession):
    new_reservation = Reservation(
        seat_id=seat_id,
        session_id=session_id,
        user_id=user_id,
        reserved_at=datetime.now(timezone.utc),
        expires_at=(session_time - timedelta(hours=settings.reservation_time.hours_expires_at)).replace(
            tzinfo=timezone.utc
        ),
        is_confirmed=False,
    )
    db.add(new_reservation)
    await db.commit()

    return new_reservation
