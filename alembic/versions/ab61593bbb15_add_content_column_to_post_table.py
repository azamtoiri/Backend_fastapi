"""add content column to post table

Revision ID: ab61593bbb15
Revises: b8d2cf82528b
Create Date: 2022-10-14 03:25:40.971630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab61593bbb15'
down_revision = 'b8d2cf82528b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_column('posts', 'content')
