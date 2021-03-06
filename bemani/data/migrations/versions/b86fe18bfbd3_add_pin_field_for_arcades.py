"""Add pin field for arcades.

Revision ID: b86fe18bfbd3
Revises: 6e2a520d2782
Create Date: 2017-04-14 17:59:18.488816

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = 'b86fe18bfbd3'
down_revision = '6e2a520d2782'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('arcade', sa.Column('pin', sa.String(length=8), nullable=True))
    # ### end Alembic commands ###

    sql = "UPDATE arcade SET pin = '00000000'"
    conn.execute(text(sql), {})


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('arcade', 'pin')
    # ### end Alembic commands ###
