"""add foregin-key to posts table

Revision ID: 53734b1aa88c
Revises: 2aec4e62b443
Create Date: 2022-05-20 11:43:27.821095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53734b1aa88c'
down_revision = '2aec4e62b443'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
