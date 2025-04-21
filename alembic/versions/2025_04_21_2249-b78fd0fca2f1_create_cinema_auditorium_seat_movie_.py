"""create cinema, auditorium, seat, movie, session and ticket tables

Revision ID: b78fd0fca2f1
Revises: 90c6e40bbf6f
Create Date: 2025-04-21 22:49:20.911309

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b78fd0fca2f1"
down_revision: Union[str, None] = "90c6e40bbf6f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "cinemas",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_cinemas")),
        sa.UniqueConstraint("name", name=op.f("uq_cinemas_name")),
    )
    op.create_table(
        "movies",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_movies")),
        sa.UniqueConstraint("name", name=op.f("uq_movies_name")),
    )
    op.create_table(
        "auditoriums",
        sa.Column("cinema_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["cinema_id"],
            ["cinemas.id"],
            name=op.f("fk_auditoriums_cinema_id_cinemas"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_auditoriums")),
    )
    op.create_table(
        "seats",
        sa.Column("auditorium_id", sa.Integer(), nullable=False),
        sa.Column("row", sa.Integer(), nullable=False),
        sa.Column("column", sa.Integer(), nullable=False),
        sa.Column(
            "busy", sa.Boolean(), server_default="false", nullable=False
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["auditorium_id"],
            ["auditoriums.id"],
            name=op.f("fk_seats_auditorium_id_auditoriums"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_seats")),
        sa.UniqueConstraint("row", "column", name="seat"),
    )
    op.create_table(
        "sessions",
        sa.Column("auditorium_id", sa.Integer(), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column(
            "start_time",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["auditorium_id"],
            ["auditoriums.id"],
            name=op.f("fk_sessions_auditorium_id_auditoriums"),
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movies.id"],
            name=op.f("fk_sessions_movie_id_movies"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_sessions")),
    )
    op.create_table(
        "tickets",
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("session_id", sa.Integer(), nullable=False),
        sa.Column("seat_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["seat_id"], ["seats.id"], name=op.f("fk_tickets_seat_id_seats")
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["sessions.id"],
            name=op.f("fk_tickets_session_id_sessions"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_tickets")),
    )
    op.drop_constraint("uq_users_name", "users", type_="unique")
    op.drop_constraint("uq_users_surname", "users", type_="unique")


def downgrade() -> None:
    """Downgrade schema."""
    op.create_unique_constraint("uq_users_surname", "users", ["surname"])
    op.create_unique_constraint("uq_users_name", "users", ["name"])
    op.drop_table("tickets")
    op.drop_table("sessions")
    op.drop_table("seats")
    op.drop_table("auditoriums")
    op.drop_table("movies")
    op.drop_table("cinemas")
