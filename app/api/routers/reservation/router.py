from fastapi import (
    APIRouter,
    Depends,
    Path,
)
from app.api.prefixs import (
    PREFIX_RESERVATION,
    TAG_RESERVATION,
)
from app.crud.confirm_reservation import confirm_reservations
from app.api.schemas.reservation import ReservationCreate
from app.core.models.db_helper import db_helper as db
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.models import User
from app.crud.reservation import create_reservation
from app.api.dependencies.get_current_user import current_user
from app.core.config import settings

router = APIRouter(
    prefix=PREFIX_RESERVATION,
    tags=TAG_RESERVATION,
)


@router.post(settings.reservation_prefix.reservation_prefix)
async def add_reservation(
    reservation_data: ReservationCreate,
    db: AsyncSession = Depends(db.session_getter),
    user: User = Depends(current_user),
):
    return await create_reservation(reservation_data, db, user)


@router.post(settings.reservation_prefix.confirm_reservation_prefix)
async def confirm_reservation(
    id: int = Path(...),
    db: AsyncSession = Depends(db.session_getter),
    user: User = Depends(current_user),
):
    return await confirm_reservations(id, db, user)
