"""empty message

Revision ID: f00a4eb56135
Revises: 65b7ba84ec5e
Create Date: 2024-06-08 00:53:07.159288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00a4eb56135'
down_revision = '65b7ba84ec5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('destinations', sa.String(), nullable=True))
    op.add_column('profiles', sa.Column('origins', sa.String(), nullable=True))
    op.drop_column('profiles', 'origin')
    op.drop_column('profiles', 'destination')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('destination', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('profiles', sa.Column('origin', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('profiles', 'origins')
    op.drop_column('profiles', 'destinations')
    # ### end Alembic commands ###
