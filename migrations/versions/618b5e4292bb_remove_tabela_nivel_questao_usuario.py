"""Remove tabela nivel_questao_usuario

Revision ID: 618b5e4292bb
Revises: d0d6f28ff06b
Create Date: 2025-10-09 20:25:04.578078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '618b5e4292bb'
down_revision: Union[str, Sequence[str], None] = 'd0d6f28ff06b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('nivel_questao_usuario')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
