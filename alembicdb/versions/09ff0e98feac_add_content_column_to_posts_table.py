"""add content column to posts table

Revision ID: 09ff0e98feac
Revises: 03f968f5c850
Create Date: 2022-05-20 10:14:33.754881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09ff0e98feac'
down_revision = '03f968f5c850'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
