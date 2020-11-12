"""add users table

Revision ID: 954707c38061
Revises:
Create Date: 2020-11-11 00:03:57.949379

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '954707c38061'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )


def downgrade():
    op.drop_table('users')
