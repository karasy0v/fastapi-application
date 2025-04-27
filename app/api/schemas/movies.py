from pydantic import BaseModel

class MovieRead(BaseModel):
    name: str
    duration: int