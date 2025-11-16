"""Alteração da coluna data resposta da QuestaoUsuario

Revision ID: 573471b019bd
Revises: 2129ee6e87a9
Create Date: 2025-11-16 10:33:57.625975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '573471b019bd'
down_revision: Union[str, Sequence[str], None] = '2129ee6e87a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'questao_usuario',
        'data_resposta',
        existing_type=sa.VARCHAR(length=3),
        type_=sa.TIMESTAMP(timezone=False),
        existing_nullable=True,
        postgresql_using="data_resposta::timestamp without time zone"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'questao_usuario',
        'data_resposta',
        existing_type=sa.TIMESTAMP(timezone=False),
        type_=sa.VARCHAR(length=3),
        existing_nullable=True
    )
