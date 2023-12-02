"""update

Revision ID: ae8295163457
Revises: 52d995353731
Create Date: 2023-12-02 17:47:53.683586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae8295163457'
down_revision: Union[str, None] = '52d995353731'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(), nullable=False))
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=False))
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'hashed_password')
    op.drop_column('user', 'is_verified')
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_admin')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###