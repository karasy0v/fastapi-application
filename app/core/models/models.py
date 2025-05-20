from sqlalchemy import ForeignKey, UniqueConstraint
from enum import Enum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models.annotations import (
    int_not_nullable_an,
    str_not_nullable_and_uniq,
    str_not_nullable_an,
    phone_number_an,
    datetime_now_not_nullable_an,
    datetime_not_nullable,
    bool_not_nullable_and_default_false,
)
from sqlalchemy import ForeignKey
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from app.core.models.base import Base
from app.core.types.user_id import UserIdType
from .mixins.id_int_pk import IdIntPkMixin


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    __tablename__ = "users"

    name: Mapped[str_not_nullable_an]
    surname: Mapped[str_not_nullable_an]
    phone_number: Mapped[phone_number_an]

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, cls)

    tickets: Mapped[list["Ticket"]] = relationship(back_populates="user")


class Cinema(IdIntPkMixin, Base):
    __tablename__ = "cinemas"

    name: Mapped[str_not_nullable_and_uniq]

    auditoriums: Mapped[list["Auditorium"]] = relationship(back_populates="cinema")


class Auditorium(IdIntPkMixin, Base):
    __tablename__ = "auditoriums"

    cinema_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("cinemas.id"))
    name: Mapped[str_not_nullable_an]

    cinema: Mapped["Cinema"] = relationship(back_populates="auditoriums")
    seats: Mapped[list["Seat"]] = relationship(back_populates="auditorium")


class Seat(IdIntPkMixin, Base):
    __tablename__ = "seats"

    auditorium_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("auditoriums.id"))
    row: Mapped[int_not_nullable_an]
    column: Mapped[int_not_nullable_an]
    price: Mapped[int_not_nullable_an]

    __table_args__ = (UniqueConstraint("auditorium_id", "row", "column"),)

    auditorium: Mapped["Auditorium"] = relationship(back_populates="seats")


class Movie(IdIntPkMixin, Base):
    __tablename__ = "movies"

    name: Mapped[str_not_nullable_and_uniq]
    duration: Mapped[int_not_nullable_an]

    sessions: Mapped[list["Session"]] = relationship(back_populates="movie")


class Session(IdIntPkMixin, Base):
    __tablename__ = "sessions"

    auditorium_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("auditoriums.id"))
    movie_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("movies.id"))
    start_time: Mapped[datetime_now_not_nullable_an]
    end_time: Mapped[datetime_not_nullable]

    movie: Mapped["Movie"] = relationship(back_populates="sessions")
    tickets: Mapped[list["Ticket"]] = relationship(back_populates="session")


class Ticket(IdIntPkMixin, Base):
    __tablename__ = "tickets"

    price: Mapped[int_not_nullable_an]
    session_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("sessions.id"))
    seat_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("seats.id"))
    user_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="tickets")
    session: Mapped["Session"] = relationship(back_populates="tickets")


class Reservation(IdIntPkMixin, Base):
    __tablename__ = "reservations"

    seat_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("seats.id"))
    session_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("sessions.id"))
    user_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("users.id"))
    reserved_at: Mapped[datetime_now_not_nullable_an]
    expires_at: Mapped[datetime_not_nullable]
    is_confirmed: Mapped[bool_not_nullable_and_default_false]
