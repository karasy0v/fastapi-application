from fastapi import Depends, HTTPException
from app.api.exceptions import (
    SeatNotFoundError,
    TicketAlreadyBooked,
    TimeForBookingIsOver,
)
from app.core.models.models import (
    User,
)
from app.api.dependencies.get_current_user import current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.secondary_funcs.create_reservation_in_db import create_reservation_in_db
from app.crud.secondary_funcs.validate_seats_exists import validate_seats
from app.crud.secondary_funcs.validate_reservation_already_exist import validate_reservation
from app.crud.secondary_funcs.validate_time_booking import validate_time_booking
from app.api.schemas.reservation import ReservationCreate
from app.core.models.redis_helper import redis_helper


async def create_reservation(
    reservation_data: ReservationCreate,
    db: AsyncSession,
    user: User = Depends(current_user),
):
    redis = await redis_helper.get_redis()

    lock_key = f"seat_lock:{reservation_data.session_id}:{reservation_data.row}:{reservation_data.column}"

    if await redis.set(lock_key, 1, ex=300, nx=True):
        try:
            if await redis.sismember(
                f"reserved_seat:{reservation_data.session_id}",
                f"{reservation_data.row}:{reservation_data.column}",
            ):
                raise HTTPException(status_code=409, detail="Seat already reserved (cached)")

            seat_id = await validate_seats(
                reservation_data.row, reservation_data.column, reservation_data.session_id, db
            )
            if not seat_id:
                raise SeatNotFoundError(reservation_data.row, reservation_data.column)

            if await validate_reservation(seat_id, reservation_data.session_id, db):
                raise TicketAlreadyBooked(reservation_data.row, reservation_data.column)

            session_time = await validate_time_booking(reservation_data.session_id, db)
            if not session_time:
                raise TimeForBookingIsOver()

            reservation = await create_reservation_in_db(
                seat_id, reservation_data.session_id, user.id, session_time, db
            )
            await redis.sadd(
                f"reserved_seat:{reservation_data.session_id}",
                f"{reservation_data.row}:{reservation_data.column}",
            )

            return reservation
        finally:
            await redis.delete(lock_key)
    else:
        raise HTTPException(status_code=409, detail="Seat is being reserved by another user.")
