"""Initiated post, user, comment database

Revision ID: 575ad24a05d1
Revises: 
Create Date: 2024-03-17 16:54:49.422015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '575ad24a05d1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # sa.
    # op.add_column("Post", 
    #               sa.Column('Tag'))
    pass


def downgrade() -> None:
    pass
