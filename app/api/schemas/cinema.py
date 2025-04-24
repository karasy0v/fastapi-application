from pydantic import BaseModel

class CinemaRead(BaseModel):
    name: str

class CinemaCreate(BaseModel):
    name: str
