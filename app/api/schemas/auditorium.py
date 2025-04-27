from pydantic import BaseModel

class Cinema(BaseModel):
    id: int
    name: str

class AuditoriumRead(BaseModel):
    name: str
    cinema: Cinema

