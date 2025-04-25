from pydantic import BaseModel

class Cinema(BaseModel):
    name: str

class AuditoriumRead(BaseModel):
    name: str
    cinema: Cinema