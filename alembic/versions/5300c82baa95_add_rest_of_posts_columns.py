"""Add rest of posts columns

Revision ID: 5300c82baa95
Revises: b77ed6af0d47
Create Date: 2025-03-07 11:08:31.715708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5300c82baa95'
down_revision: Union[str, None] = 'b77ed6af0d47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),)
    op.add_column('posts',sa.Column('Likes',sa.Integer()),)
    op.add_column('posts',sa.Column('DisLikes',sa.Integer()),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    op.drop_column('posts','Likes')
    op.drop_column('posts','DisLikes')
    pass
