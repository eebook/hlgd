"""empty message

Revision ID: 24a6f104d789
Revises: 3b834f0f3c0c
Create Date: 2017-11-20 02:53:14.353790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24a6f104d789'
down_revision = '3b834f0f3c0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('metadata', sa.Column('regex', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('metadata', 'regex')
    # ### end Alembic commands ###
