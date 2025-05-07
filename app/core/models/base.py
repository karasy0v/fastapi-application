from sqlalchemy import Integer, MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from app.core.config import settings


class Base(DeclarativeBase):

    metadata = MetaData(naming_convention=settings.db.naming_convention)
   
    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
