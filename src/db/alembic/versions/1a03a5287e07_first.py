"""first

Revision ID: 1a03a5287e07
Revises: 
Create Date: 2022-09-22 11:55:49.074109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a03a5287e07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('parent_id', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###