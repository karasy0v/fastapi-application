from datetime import datetime
from pydantic import BaseModel


class ReservationCreate(BaseModel):
    row: int
    column: int
    session_id: int
