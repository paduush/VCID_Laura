"""empty message

Revision ID: f079a2319cf5
Revises: 3e08f004fb06
Create Date: 2023-09-01 10:08:51.638519

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f079a2319cf5'
down_revision = '3e08f004fb06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_index('ix_recipe_ingred20')
        batch_op.drop_index('ix_recipe_isprivat')
        batch_op.drop_index('ix_recipe_steps9')
        batch_op.drop_column('ingred20')
        batch_op.drop_column('steps9')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('steps9', mysql.VARCHAR(length=256), nullable=True))
        batch_op.add_column(sa.Column('ingred20', mysql.VARCHAR(length=32), nullable=True))
        batch_op.create_index('ix_recipe_steps9', ['steps9'], unique=False)
        batch_op.create_index('ix_recipe_isprivat', ['isprivat'], unique=False)
        batch_op.create_index('ix_recipe_ingred20', ['ingred20'], unique=False)

    # ### end Alembic commands ###
