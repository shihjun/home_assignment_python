"""empty message

Revision ID: 15383b9deadf
Revises: d4e4e9efed35
Create Date: 2019-09-11 18:01:40.213813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15383b9deadf'
down_revision = 'd4e4e9efed35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('home',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sell', sa.Integer(), nullable=True),
    sa.Column('list', sa.Integer(), nullable=True),
    sa.Column('living', sa.Integer(), nullable=True),
    sa.Column('rooms', sa.Integer(), nullable=True),
    sa.Column('beds', sa.Integer(), nullable=True),
    sa.Column('baths', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('acres', sa.Float(), nullable=True),
    sa.Column('taxes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('home')
    # ### end Alembic commands ###