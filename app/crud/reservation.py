from fastapi import Depends
from datetime import (
    timedelta,
    timezone,
    datetime,
)
from app.api.exceptions import (
    SeatNotFoundError,
    TicketAlreadyBooked,
    TimeForBookingIsOver,
)
from app.core.models.models import (
    Reservation,
    User,
)
from app.api.dependencies.get_current_user import current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.secondary_funcs.validate_seats_exists import validate_seats
from app.crud.secondary_funcs.validate_reservation_already_exist import validate_reservation
from app.crud.secondary_funcs.validate_time_booking import validate_time_booking
from app.api.schemas.reservation import ReservationCreate
from app.core.config import settings


async def create_reservation(
    reservation_data: ReservationCreate,
    db: AsyncSession,
    user: User = Depends(current_user),
):

    seat_id = await validate_seats(reservation_data.row, reservation_data.column, reservation_data.session_id, db)

    if not seat_id:
        raise SeatNotFoundError(reservation_data.row, reservation_data.column)

    if await validate_reservation(seat_id, reservation_data.session_id, db):
        raise TicketAlreadyBooked(reservation_data.row, reservation_data.column)

    session_time = await validate_time_booking(reservation_data.session_id, db)
    if not session_time:
        raise TimeForBookingIsOver()

    new_reservation = Reservation(
        seat_id=seat_id,
        session_id=reservation_data.session_id,
        user_id=user.id,
        reserved_at=datetime.now(timezone.utc),
        expires_at=(session_time - timedelta(hours=settings.reservation_time.hours_expires_at)).replace(
            tzinfo=timezone.utc
        ),
        is_confirmed=False,
    )

    db.add(new_reservation)
    await db.commit()
    await db.refresh(new_reservation)

    return new_reservation
