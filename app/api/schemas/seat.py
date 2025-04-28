from pydantic import BaseModel

class SeatRead(BaseModel):
    busy: bool
    row: int
    column: int
    auditorium_id: int