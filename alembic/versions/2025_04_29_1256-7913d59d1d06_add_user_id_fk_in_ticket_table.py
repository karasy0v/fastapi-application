"""add user_id fk in Ticket table

Revision ID: 7913d59d1d06
Revises: b85575155636
Create Date: 2025-04-29 12:56:10.334187

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "7913d59d1d06"
down_revision: Union[str, None] = "b85575155636"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "tickets", sa.Column("user_id", sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        op.f("fk_tickets_user_id_users"),
        "tickets",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        op.f("fk_tickets_user_id_users"), "tickets", type_="foreignkey"
    )
    op.drop_column("tickets", "user_id")
