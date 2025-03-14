"""Add foreign key to posts table

Revision ID: b77ed6af0d47
Revises: c853b6480895
Create Date: 2025-02-28 11:43:48.507044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b77ed6af0d47'
down_revision: Union[str, None] = 'c853b6480895'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table='posts',referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
