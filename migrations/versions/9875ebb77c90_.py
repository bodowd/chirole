"""empty message

Revision ID: 9875ebb77c90
Revises: 1b92db4fb0ce
Create Date: 2020-04-18 16:40:46.261600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9875ebb77c90'
down_revision = '1b92db4fb0ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('paid', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'paid')
    # ### end Alembic commands ###
