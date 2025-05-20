from fastapi import Depends
from datetime import (
    timezone,
    datetime,
)
from app.api.dependencies.get_current_user import current_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.exceptions import (
    ReservationNotFoundError,
    ReservationUnavailable,
    TimeToReservationalExpired,
)

from app.core.models.models import (
    Reservation,
    User,
    Ticket,
    Seat,
)


async def confirm_reservations(
    reservation_id: int,
    db: AsyncSession,
    user: User = Depends(current_user),
):
    reservation = await db.get(Reservation, reservation_id)

    print(reservation)

    if not reservation:
        raise ReservationNotFoundError()

    if reservation.user_id != user.id:
        raise ReservationUnavailable()

    if reservation.expires_at < datetime.now(timezone.utc):
        raise TimeToReservationalExpired()

    if reservation.is_confirmed:
        TimeToReservationalExpired()

    seat_price = await db.get(Seat, reservation.seat_id)

    new_ticket = Ticket(
        session_id=reservation.session_id,
        seat_id=reservation.seat_id,
        user_id=reservation.user_id,
        price=seat_price.price,
    )

    db.add(new_ticket)
    await db.delete(reservation)
    await db.commit()
    await db.refresh(new_ticket)

    return new_ticket
