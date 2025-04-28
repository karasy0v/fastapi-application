"""delete uniqueconstraint from seat table

Revision ID: b85575155636
Revises: f3c7f3e082cd
Create Date: 2025-04-28 17:26:20.848574

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b85575155636"
down_revision: Union[str, None] = "f3c7f3e082cd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint("seat", "seats", type_="unique")


def downgrade() -> None:
    """Downgrade schema."""
    op.create_unique_constraint("seat", "seats", ["row", "column"])
