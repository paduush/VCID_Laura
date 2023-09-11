"""empty message

Revision ID: b04b0c67c649
Revises: 959877d464ae
Create Date: 2023-09-04 17:43:06.831662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b04b0c67c649'
down_revision = '959877d464ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('atoken', sa.String(length=32), nullable=True))
        batch_op.add_column(sa.Column('runout', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_atoken'), ['atoken'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_atoken'))
        batch_op.drop_column('runout')
        batch_op.drop_column('atoken')

    # ### end Alembic commands ###