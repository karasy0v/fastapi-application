from pydantic import BaseModel
from datetime import datetime

class SessionRead(BaseModel):
    start_time: datetime  
    end_time: datetime
    auditorium_id: int
    movie_id: int

class SessionCreate(BaseModel):
    auditorium_id: int
    movie_id: int
    start_time: datetime

