"""delete price from Ticket table

Revision ID: 207a450e2c5d
Revises: 6355a0b2e035
Create Date: 2025-04-29 13:54:10.287936

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "207a450e2c5d"
down_revision: Union[str, None] = "6355a0b2e035"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("tickets", "price")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "tickets",
        sa.Column("price", sa.INTEGER(), autoincrement=False, nullable=False),
    )
