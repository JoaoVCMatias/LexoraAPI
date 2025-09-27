"""Inserir informações domínio

Revision ID: 6903e9cae520
Revises: 770382e18466
Create Date: 2025-09-27 18:27:04.809325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6903e9cae520'
down_revision: Union[str, Sequence[str], None] = '770382e18466'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Inserindo idiomas
    idiomas = ['Português', 'Inglês']
    for idioma in idiomas:
        op.execute(f"INSERT INTO idioma (descricao_idioma) VALUES ('{idioma}')")

    # Inserindo sexos
    sexos = [('Masculino', 'M'), ('Feminino', 'F')]
    for descricao, sigla in sexos:
        op.execute(f"INSERT INTO sexo (descricao_sexo, sigla_sexo) VALUES ('{descricao}', '{sigla}')")

    # Inserindo disponibilidade
    disponibilidades = ['Leve (0.5h por semana)', ('Moderado (1h por semana)'), ('Intenso (2h por semana)')] 
    for disponibilidade in disponibilidades:
        op.execute(f"INSERT INTO disponibilidade (descricao_disponibilidade) VALUES ('{disponibilidade}')")

    # Inserindo objetivo
    objetivos = ['Viagem', 'Trabalho', 'Morar fora']
    for objetivo in objetivos:
        op.execute(f"INSERT INTO objetivo (descricao_objetivo) VALUES ('{objetivo}')")

    # Inserindo tipo_questao
    tipo_questoes = ['Escrita', 'Escolha', 'Áudio', 'Vídeo', 'Imagem']
    for tipo_questao in tipo_questoes:
        op.execute(f"INSERT INTO tipo_questao (descricao_tipo_questao) VALUES ('{tipo_questao}')")

    # Inserindo experiencia_idioma
    experiencia_idiomas = ['Básico', 'Intermediário', 'Avançado']
    for experiencia_idioma in experiencia_idiomas:
        op.execute(f"INSERT INTO experiencia_idioma (descricao_experiencia_idioma) VALUES ('{experiencia_idioma}')")

    pass


def downgrade() -> None:
    op.execute("TRUNCATE idioma RESTART IDENTITY CASCADE")
    op.execute("TRUNCATE sexo RESTART IDENTITY CASCADE")
    op.execute("TRUNCATE disponibilidade RESTART IDENTITY CASCADE")
    op.execute("TRUNCATE objetivo RESTART IDENTITY CASCADE")
    op.execute("TRUNCATE tipo_questao RESTART IDENTITY CASCADE")
    op.execute("TRUNCATE experiencia_idioma RESTART IDENTITY CASCADE")

    pass
