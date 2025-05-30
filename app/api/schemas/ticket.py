from pydantic import BaseModel

class BuyTicket(BaseModel):
    session_id : int
    seat_id: int
    user_id: int

class ReadTicket(BaseModel):
    price: int
    seat_id: int
    user_id: int
    