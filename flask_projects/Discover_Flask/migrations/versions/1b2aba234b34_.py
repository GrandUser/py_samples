"""empty message

Revision ID: 1b2aba234b34
Revises: None
Create Date: 2016-08-31 06:51:46.969435

"""

# revision identifiers, used by Alembic.
revision = '1b2aba234b34'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.alter_column('posts', 'description',
               existing_type=sa.CHAR(length=1000),
               nullable=False)
    op.alter_column('posts', 'title',
               existing_type=sa.CHAR(length=300),
               nullable=False)
    op.create_foreign_key(None, 'posts', 'users', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.alter_column('posts', 'title',
               existing_type=sa.CHAR(length=300),
               nullable=True)
    op.alter_column('posts', 'description',
               existing_type=sa.CHAR(length=1000),
               nullable=True)
    op.drop_column('posts', 'author_id')
    op.drop_table('users')
    ### end Alembic commands ###
