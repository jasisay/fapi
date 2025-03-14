"""add content column to posts table

Revision ID: 3034f7e9019c
Revises: fb033cf0b5c8
Create Date: 2025-02-27 10:31:53.032864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3034f7e9019c'
down_revision: Union[str, None] = 'fb033cf0b5c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
