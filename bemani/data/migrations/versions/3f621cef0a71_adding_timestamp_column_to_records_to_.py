"""Adding timestamp column to records to implement king-of-the-hill scoring.

Revision ID: 3f621cef0a71
Revises: f270dd360519
Create Date: 2017-03-21 20:29:38.813890

"""
import calendar
from datetime import datetime
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision = '3f621cef0a71'
down_revision = 'f270dd360519'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('score', sa.Column('timestamp', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_score_points'), 'score', ['points'], unique=False)
    op.create_index(op.f('ix_score_timestamp'), 'score', ['timestamp'], unique=False)
    # ### end Alembic commands ###

    # Set a default timestamp for all existing scores
    now = datetime.utcnow()
    timestamp = calendar.timegm(now.utctimetuple())
    sql = "UPDATE score SET timestamp = :timestamp WHERE timestamp IS null"
    conn.execute(text(sql), {'timestamp': timestamp})


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_score_timestamp'), table_name='score')
    op.drop_index(op.f('ix_score_points'), table_name='score')
    op.drop_column('score', 'timestamp')
    # ### end Alembic commands ###
