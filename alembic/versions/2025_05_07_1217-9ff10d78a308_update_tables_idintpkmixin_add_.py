"""update tables IdIntPkMixin, add BaseUserTable in User

Revision ID: 9ff10d78a308
Revises: addf0067fe6a
Create Date: 2025-05-07 12:17:32.782688

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9ff10d78a308"
down_revision: Union[str, None] = "addf0067fe6a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "users", sa.Column("email", sa.String(length=320), nullable=False)
    )
    op.add_column(
        "users",
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
    )
    op.add_column(
        "users", sa.Column("is_active", sa.Boolean(), nullable=False)
    )
    op.add_column(
        "users", sa.Column("is_superuser", sa.Boolean(), nullable=False)
    )
    op.add_column(
        "users", sa.Column("is_verified", sa.Boolean(), nullable=False)
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_column("users", "is_verified")
    op.drop_column("users", "is_superuser")
    op.drop_column("users", "is_active")
    op.drop_column("users", "hashed_password")
    op.drop_column("users", "email")
