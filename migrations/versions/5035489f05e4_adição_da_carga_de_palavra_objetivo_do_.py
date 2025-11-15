"""Adição da carga de palavra objetivo do tipo tecnologia

Revision ID: 5035489f05e4
Revises: cbcd87d54551
Create Date: 2025-11-15 09:21:12.396734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5035489f05e4'
down_revision: Union[str, Sequence[str], None] = 'cbcd87d54551'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (691, 4); --blogger
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (894, 4); --by
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (907, 4); --calculator
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (917, 4); --camera
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1004, 4); --CD
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1166, 4); --clip
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1302, 4); --computer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1345, 4); --connect
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1694, 4); --delete
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1786, 4); --dial
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1807, 4); --digital
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1952, 4); --dot
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1975, 4); --drag
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2104, 4); --electronic
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2123, 4); --email
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2172, 4); --engaged
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2188, 4); --enter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2204, 4); --envelope
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2219, 4); --equipment
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2451, 4); --fax
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3006, 4); --hardware
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3039, 4); --headline
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3486, 4); --invent
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3487, 4); --invention
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3524, 4); --IT
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3593, 4); --keyboard
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3652, 4); --laptop
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3874, 4); --machine
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4022, 4); --message
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4101, 4); --mobile phone
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4178, 4); --mouse
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4186, 4); --MP3 player
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4458, 4); --online
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4468, 4); --operator
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4641, 4); --parcel
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4675, 4); --password
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4701, 4); --PC
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4788, 4); --phone
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4794, 4); --photography
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4943, 4); --postcard
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5052, 4); --printer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5804, 4); --server
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6074, 4); --software
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6609, 4); --text
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6610, 4); --text message
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7067, 4); --upload
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7145, 4); --video
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7186, 4); --volume
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7261, 4); --web
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7262, 4); --web page
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7263, 4); --webcam
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7264, 4); --website
    """)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
