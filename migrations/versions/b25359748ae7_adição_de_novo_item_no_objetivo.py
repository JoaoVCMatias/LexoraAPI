"""Adição de novo item no Objetivo

Revision ID: b25359748ae7
Revises: d7f7348ab424
Create Date: 2025-10-18 21:35:40.250880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b25359748ae7'
down_revision: Union[str, Sequence[str], None] = 'd7f7348ab424'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""INSERT INTO objetivo(descricao_objetivo) 
     VALUES ('Tecnologia');
    """)
    pass


def downgrade() -> None:
    op.execute("""DELETE FROM objetivo WHERE descricao_objetivo = 'Tecnologia';""")
    pass
