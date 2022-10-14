"""Add votes auto

Revision ID: accfc3933410
Revises: 5cf140a6ee97
Create Date: 2022-10-14 03:52:18.122736

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'accfc3933410'
down_revision = '5cf140a6ee97'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('post_id', 'user_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
