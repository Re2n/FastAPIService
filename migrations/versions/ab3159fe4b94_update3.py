"""update3

Revision ID: ab3159fe4b94
Revises: 51911d458661
Create Date: 2023-12-09 16:49:02.797095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab3159fe4b94'
down_revision: Union[str, None] = '51911d458661'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rent', sa.Column('transportidentifier', sa.String(), nullable=False))
    op.add_column('rent', sa.Column('ownerusername', sa.String(), nullable=False))
    op.add_column('rent', sa.Column('timeStart', sa.String(), nullable=False))
    op.add_column('rent', sa.Column('timeEnd', sa.String(), nullable=True))
    op.add_column('rent', sa.Column('priceOfUnit', sa.Float(), nullable=False))
    op.add_column('rent', sa.Column('priceType', sa.String(), nullable=False))
    op.add_column('rent', sa.Column('finalPrice', sa.Float(), nullable=True))
    op.drop_column('rent', 'id')
    op.add_column('transport', sa.Column('ownerusername', sa.String(), nullable=False))
    op.add_column('transport', sa.Column('canBeRented', sa.Boolean(), nullable=False))
    op.add_column('transport', sa.Column('transportType', sa.String(), nullable=False))
    op.add_column('transport', sa.Column('model', sa.String(), nullable=False))
    op.add_column('transport', sa.Column('color', sa.String(), nullable=False))
    op.add_column('transport', sa.Column('identifier', sa.String(), nullable=False))
    op.add_column('transport', sa.Column('description', sa.String(), nullable=True))
    op.add_column('transport', sa.Column('latitude', sa.Float(), nullable=False))
    op.add_column('transport', sa.Column('longitude', sa.Float(), nullable=False))
    op.add_column('transport', sa.Column('minutePrice', sa.Float(), nullable=True))
    op.add_column('transport', sa.Column('dayPrice', sa.Float(), nullable=True))
    op.drop_column('transport', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transport', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('transport', 'dayPrice')
    op.drop_column('transport', 'minutePrice')
    op.drop_column('transport', 'longitude')
    op.drop_column('transport', 'latitude')
    op.drop_column('transport', 'description')
    op.drop_column('transport', 'identifier')
    op.drop_column('transport', 'color')
    op.drop_column('transport', 'model')
    op.drop_column('transport', 'transportType')
    op.drop_column('transport', 'canBeRented')
    op.drop_column('transport', 'ownerusername')
    op.add_column('rent', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('rent', 'finalPrice')
    op.drop_column('rent', 'priceType')
    op.drop_column('rent', 'priceOfUnit')
    op.drop_column('rent', 'timeEnd')
    op.drop_column('rent', 'timeStart')
    op.drop_column('rent', 'ownerusername')
    op.drop_column('rent', 'transportidentifier')
    # ### end Alembic commands ###
