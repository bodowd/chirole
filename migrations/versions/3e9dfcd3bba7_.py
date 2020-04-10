"""empty message

Revision ID: 3e9dfcd3bba7
Revises: d8f50de077e4
Create Date: 2020-04-05 20:46:49.597153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e9dfcd3bba7'
down_revision = 'd8f50de077e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'job_location',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'job_location',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###