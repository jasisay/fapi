"""Create post table

Revision ID: fb033cf0b5c8
Revises: 
Create Date: 2025-02-23 12:54:43.064791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb033cf0b5c8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False,primary_key=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
