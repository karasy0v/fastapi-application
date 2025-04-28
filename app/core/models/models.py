from typing import List
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from app.core.models.annotations import (
    int_not_nullable_an,
    str_not_nullable_and_uniq,
    str_not_nullable_an,
    bool_not_nullable_and_default_false,
    phone_number_an,
    datetime_now_not_nullable_an,
)
from sqlalchemy import (
    ForeignKey,
)
from app.core.models.base import Base


class User(Base):
    __tablename__ = "users"

    name: Mapped[str_not_nullable_an]
    surname: Mapped[str_not_nullable_an]
    phone_number: Mapped[phone_number_an]


class Cinema(Base):
    __tablename__ = "cinemas"

    name: Mapped[str_not_nullable_and_uniq]

    auditoriums: Mapped[List["Auditorium"]] = relationship(back_populates='cinema')


class Auditorium(Base):
    __tablename__ = "auditoriums"

    cinema_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("cinemas.id"))
    name: Mapped[str_not_nullable_an]

    cinema: Mapped["Cinema"] = relationship(back_populates="auditoriums")
    seats: Mapped[list["Seat"]] = relationship(back_populates="auditorium")


class Seat(Base):
    __tablename__ = "seats"

    auditorium_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("auditoriums.id"))
    row: Mapped[int_not_nullable_an]
    column: Mapped[int_not_nullable_an]
    busy: Mapped[bool_not_nullable_and_default_false]

    auditorium: Mapped['Auditorium'] = relationship(back_populates='seats')

    


class Movie(Base):
    __tablename__ = "movies"

    name: Mapped[str_not_nullable_and_uniq]
    duration: Mapped[int_not_nullable_an]

    sessions: Mapped[list["Session"]] = relationship(back_populates='movie')

class Session(Base):
    __tablename__ = "sessions"

    auditorium_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("auditoriums.id"))
    movie_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("movies.id"))
    start_time: Mapped[datetime_now_not_nullable_an]
    end_time: Mapped[datetime_now_not_nullable_an]

    movie: Mapped["Movie"] = relationship(back_populates='sessions')


class Ticket(Base):
    __tablename__ = "tickets"

    price: Mapped[int_not_nullable_an]
    session_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("sessions.id"))
    seat_id: Mapped[int_not_nullable_an] = mapped_column(ForeignKey("seats.id"))
