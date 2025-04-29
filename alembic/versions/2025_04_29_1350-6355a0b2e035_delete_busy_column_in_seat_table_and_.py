"""delete busy column in Seat table and add price, delete column price in Ticket table

Revision ID: 6355a0b2e035
Revises: 7913d59d1d06
Create Date: 2025-04-29 13:50:21.543936

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6355a0b2e035"
down_revision: Union[str, None] = "7913d59d1d06"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("seats", sa.Column("price", sa.Integer(), nullable=False))
    op.drop_column("seats", "busy")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "seats",
        sa.Column(
            "busy",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_column("seats", "price")
