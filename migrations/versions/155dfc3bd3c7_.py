"""added actions

Revision ID: 155dfc3bd3c7
Revises: 5abfa41e3c25
Create Date: 2021-08-13 21:38:04.657608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '155dfc3bd3c7'
down_revision = '5abfa41e3c25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('images', sa.Column('action_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'images', 'action', ['action_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'images', type_='foreignkey')
    op.drop_column('images', 'action_id')
    op.drop_table('action')
    # ### end Alembic commands ###