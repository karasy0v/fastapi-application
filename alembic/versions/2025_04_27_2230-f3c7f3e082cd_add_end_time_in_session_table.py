"""add end_time in session table

Revision ID: f3c7f3e082cd
Revises: b78fd0fca2f1
Create Date: 2025-04-27 22:30:37.424919

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "f3c7f3e082cd"
down_revision: Union[str, None] = "b78fd0fca2f1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "sessions",
        sa.Column(
            "end_time",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("sessions", "end_time")
