"""create unique constraint in Seat table and add column price in Ticket

Revision ID: fe67587ed7c0
Revises: 207a450e2c5d
Create Date: 2025-04-29 16:40:44.362685

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "fe67587ed7c0"
down_revision: Union[str, None] = "207a450e2c5d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_unique_constraint(
        op.f("uq_seats_auditorium_id_row_column"),
        "seats",
        ["auditorium_id", "row", "column"],
    )
    op.add_column("tickets", sa.Column("price", sa.Integer(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("tickets", "price")
    op.drop_constraint(
        op.f("uq_seats_auditorium_id_row_column"), "seats", type_="unique"
    )
