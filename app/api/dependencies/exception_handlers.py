from fastapi import (
    FastAPI,
    Request,
)
from fastapi.responses import JSONResponse

from app.api.exceptions import (
    SeatNotFoundError,
    TicketAlreadyBooked,
    TimeForBookingIsOver,
    ReservationNotFoundError,
    ReservationUnavailable,
    TimeToReservationalExpired,
)


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(SeatNotFoundError)
    async def seat_not_found_handler(request: Request, exc: SeatNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(TicketAlreadyBooked)
    async def reservation_error_handler(request: Request, exc: TicketAlreadyBooked):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )

    @app.exception_handler(TimeForBookingIsOver)
    async def time_booking_over_error_handler(request: Request, exc: TimeForBookingIsOver):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )

    @app.exception_handler(ReservationNotFoundError)
    async def reservation_not_found_error(request: Request, exc: ReservationNotFoundError):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(ReservationUnavailable)
    async def reservation_not_found_error(request: Request, exc: ReservationUnavailable):
        return JSONResponse(
            status_code=403,
            content={"detail": str(exc)},
        )

    @app.exception_handler(TimeToReservationalExpired)
    async def reservation_not_found_error(request: Request, exc: TimeToReservationalExpired):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)},
        )
