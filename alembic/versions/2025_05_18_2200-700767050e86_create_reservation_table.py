"""create reservation table

Revision ID: 700767050e86
Revises: 3b91342aaba2
Create Date: 2025-05-18 22:00:32.550203

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "700767050e86"
down_revision: Union[str, None] = "3b91342aaba2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "reservations",
        sa.Column("seat_id", sa.Integer(), nullable=False),
        sa.Column("session_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "reserved_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("expires_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column(
            "is_confirmed",
            sa.Boolean(),
            server_default="false",
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["seat_id"],
            ["seats.id"],
            name=op.f("fk_reservations_seat_id_seats"),
        ),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["sessions.id"],
            name=op.f("fk_reservations_session_id_sessions"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_reservations_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_reservations")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("reservations")
