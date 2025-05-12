from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    phone_number: str
