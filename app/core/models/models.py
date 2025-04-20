from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.core.models.base import Base


class User(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    surname: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(10), nullable=False)
