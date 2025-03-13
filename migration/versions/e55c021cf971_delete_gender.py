"""Delete gender 

Revision ID: e55c021cf971
Revises: 42859ade802a
Create Date: 2025-03-13 22:46:47.736571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e55c021cf971'
down_revision: Union[str, None] = '42859ade802a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
