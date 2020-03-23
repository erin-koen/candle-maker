"""candle table

Revision ID: 0b5cc44f4a90
Revises: 
Create Date: 2020-03-23 07:46:18.013126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b5cc44f4a90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('candle_end_date', sa.DateTime(), nullable=True),
    sa.Column('candle_high', sa.Float(), nullable=True),
    sa.Column('candle_low', sa.Float(), nullable=True),
    sa.Column('candle_open', sa.Float(), nullable=True),
    sa.Column('candle_close', sa.Float(), nullable=True),
    sa.Column('candle_volume', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('candle')
    # ### end Alembic commands ###