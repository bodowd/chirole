"""empty message

Revision ID: 7950ab520817
Revises: 35dc636a1717
Create Date: 2020-05-04 22:02:33.089141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7950ab520817'
down_revision = '35dc636a1717'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('link_to_application_site', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'link_to_application_site')
    # ### end Alembic commands ###
