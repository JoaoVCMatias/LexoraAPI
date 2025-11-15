"""Adição da carga de palavra objetivo do tipo trabalho

Revision ID: cbcd87d54551
Revises: b25359748ae7
Create Date: 2025-11-15 09:15:00.553306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbcd87d54551'
down_revision: Union[str, Sequence[str], None] = 'b25359748ae7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (77, 2); --actress
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (157, 2); --agent
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (322, 2); --application
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (323, 2); --apply
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (341, 2); --architect
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (357, 2); --army
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (374, 2); --artist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (414, 2); --athlete
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (477, 2); --babysitter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (519, 2); --banker
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (747, 2); --boss
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (878, 2); --businessman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (879, 2); --businesswoman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (929, 2); --candidate
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (936, 2); --canteen
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (944, 2); --captain
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (960, 2); --career
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1078, 2); --chef
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1081, 2); --chemist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1147, 2); --cleaner
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1212, 2); --colleague
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1260, 2); --company
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1302, 2); --computer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1327, 2); --conference
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1420, 2); --cook
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1516, 2); --crew
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1579, 2); --customs
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1604, 2); --dancer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1718, 2); --dentist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1721, 2); --department
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1749, 2); --desk
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1769, 2); --detective
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1792, 2); --diary
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1823, 2); --diploma
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1829, 2); --director
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1912, 2); --diver
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1998, 2); --driver
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2043, 2); --earn
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2123, 2); --email
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2142, 2); --employ
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2143, 2); --employee
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2144, 2); --employer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2145, 2); --employment
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2347, 2); --explorer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2390, 2); --factory
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2425, 2); --farm
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2426, 2); --farmer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2614, 2); --football
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2615, 2); --footballer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2711, 2); --full
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2835, 2); --goalkeeper
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2940, 2); --guest
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2942, 2); --guide
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2965, 2); --hairdresser
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3174, 2); --housewife
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3175, 2); --housework
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3431, 2); --instructor
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3550, 2); --job
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3561, 2); --journalist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3609, 2); --king
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3631, 2); --laboratory
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3683, 2); --lawyer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3714, 2); --lecturer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3744, 2); --letter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3754, 2); --librarian
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3910, 2); --manager
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3980, 2); --mechanic
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3995, 2); --meeting
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4022, 2); --message
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4210, 2); --musician
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4367, 2); --novelist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4413, 2); --occupation
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4420, 2); --of
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4430, 2); --office
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4431, 2); --officer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4519, 2); --out
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4591, 2); --owner
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4612, 2); --painter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4793, 2); --photographer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4820, 2); --pilot
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4851, 2); --player
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4880, 2); --poet
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4894, 2); --policeman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4895, 2); --policewoman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4904, 2); --politician
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4945, 2); --postman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5016, 2); --president
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5079, 2); --profession
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5082, 2); --professor
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5088, 2); --programmer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5152, 2); --publisher
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5183, 2); --qualification
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5194, 2); --queen
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5302, 2); --receptionist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5436, 2); --reporter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5494, 2); --retire
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5496, 2); --retirement
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5638, 2); --sailor
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5641, 2); --salary
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5643, 2); --salesman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5646, 2); --saleswoman
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5710, 2); --scientist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5752, 2); --secretary
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5757, 2); --security
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5884, 2); --shopper
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5949, 2); --singer
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6078, 2); --soldier
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6206, 2); --staff
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6339, 2); --student
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6544, 2); --taxi
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6547, 2); --teacher
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6587, 2); --tennis
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6973, 2); --unemployed
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6996, 2); --uniform
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7196, 2); --wage
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7202, 2); --waiter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7203, 2); --waitress
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7387, 2); --work
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7390, 2); --worker
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
