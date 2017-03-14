"""empty message

Revision ID: 590bc47d9a68
Revises: 297cf0fb75bf
Create Date: 2017-03-08 06:08:12.148678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '590bc47d9a68'
down_revision = '297cf0fb75bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('user_profile', sa.Column('gender', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'gender')
    op.drop_column('user_profile', 'age')
    # ### end Alembic commands ###