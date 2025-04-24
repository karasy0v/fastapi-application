from pydantic import BaseModel

class CinemaRead(BaseModel):
    name: str

class CinemaCreate(BaseModel):
    name: str

class CinemaUpdate(BaseModel):
    id: int
    name: str