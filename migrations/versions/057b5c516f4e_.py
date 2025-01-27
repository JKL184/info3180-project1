"""empty message

Revision ID: 057b5c516f4e
Revises: 
Create Date: 2021-03-21 22:32:55.505173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '057b5c516f4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('desc', sa.String(length=300), nullable=True),
    sa.Column('room', sa.String(length=80), nullable=True),
    sa.Column('bathroom', sa.String(length=80), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('proptype', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    op.drop_table('properties')
    # ### end Alembic commands ###
