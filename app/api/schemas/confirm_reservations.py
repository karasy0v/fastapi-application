from pydantic import BaseModel


class ConfirmReservation(BaseModel):
    reservation_id: int
