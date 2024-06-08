"""empty message

Revision ID: b6c29c692770
Revises: 8c90d5d5a4d4
Create Date: 2024-06-07 15:15:01.366612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6c29c692770'
down_revision = '8c90d5d5a4d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_profiles_destination', table_name='profiles')
    op.drop_index('ix_profiles_origin', table_name='profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_profiles_origin', 'profiles', ['origin'], unique=False)
    op.create_index('ix_profiles_destination', 'profiles', ['destination'], unique=False)
    # ### end Alembic commands ###
