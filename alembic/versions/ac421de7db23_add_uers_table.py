"""add uers table

Revision ID: ac421de7db23
Revises: 3034f7e9019c
Create Date: 2025-02-27 10:53:29.565443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac421de7db23'
down_revision: Union[str, None] = '3034f7e9019c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
