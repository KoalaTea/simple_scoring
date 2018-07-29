"""empty message

Revision ID: 7e08d89e671a
Revises: ebe172c00b2d
Create Date: 2018-07-28 15:28:20.184527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e08d89e671a'
down_revision = 'ebe172c00b2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ssh_creds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('score', sa.Column('success', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('score', 'success')
    op.drop_table('ssh_creds')
    # ### end Alembic commands ###