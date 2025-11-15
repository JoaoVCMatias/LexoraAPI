"""Adição da carga de palavra objetivo do tipo viagem

Revision ID: 2129ee6e87a9
Revises: 5035489f05e4
Create Date: 2025-11-15 09:25:45.203392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2129ee6e87a9'
down_revision: Union[str, Sequence[str], None] = '5035489f05e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (43, 1); --accommodation
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (171, 1); --air
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (176, 1); --airline
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (178, 1); --airport
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (233, 1); --ambulance
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (270, 1); --announcement
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (364, 1); --arrival
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (365, 1); --arrive
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (413, 1); --at
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (483, 1); --backpack
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (484, 1); --backpacker
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (485, 1); --backpacking
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (495, 1); --bag
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (496, 1); --baggage
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (639, 1); --bicycle
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (643, 1); --bike
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (710, 1); --boat
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (741, 1); --border
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (809, 1); --bridge
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (825, 1); --brochure
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (873, 1); --bus
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (877, 1); --business
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (894, 1); --by
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (896, 1); --cab
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (898, 1); --cabin
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (926, 1); --canal
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (941, 1); --capital
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (948, 1); --car
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (978, 1); --case
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (991, 1); --catch
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1043, 1); --change
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (8319, 1); --charter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1127, 1); --city
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1335, 1); --confirm
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1474, 1); --country
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1532, 1); --crossing
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1534, 1); --crossroads
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1567, 1); --currency
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1579, 1); --customs
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1590, 1); --cycle
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1592, 1); --cyclist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1705, 1); --deliver
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1720, 1); --depart
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1723, 1); --departure
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1759, 1); --destination
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1827, 1); --direction
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1931, 1); --document
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1937, 1); --dollar
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (1998, 1); --driver
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2014, 1); --due
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2026, 1); --duty-free
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2129, 1); --embassy
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2246, 1); --euro
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2386, 1); --facilities
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2423, 1); --fare
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2475, 1); --ferry
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2573, 1); --flight
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2592, 1); --fly
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2613, 1); --foot
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2626, 1); --foreign
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2709, 1); --fuel
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2750, 1); --garage
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2757, 1); --gas
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2759, 1); --gate
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2940, 1); --guest
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2942, 1); --guide
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (2943, 1); --guidebook
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3068, 1); --helicopter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3125, 1); --holiday
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3167, 1); --hotel
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3263, 1); --immigration
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3373, 1); --information
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3546, 1); --jet
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3562, 1); --journey
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3839, 1); --lorry
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3863, 1); --luggage
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3874, 1); --machine
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3921, 1); --map
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (3980, 1); --mechanic
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4075, 1); --mirror
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4084, 1); --miss
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4167, 1); --motorbike
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4170, 1); --motorway
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4242, 1); --nationality
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4437, 1); --oil
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4468, 1); --operator
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4519, 1); --out
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4569, 1); --overnight
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4648, 1); --parking
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4667, 1); --pass
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4669, 1); --passenger
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4674, 1); --passport
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4682, 1); --path
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4775, 1); --petrol
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4820, 1); --pilot
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (4849, 1); --platform
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5232, 1); --rail
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5233, 1); --railroad
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5234, 1); --railway
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5301, 1); --reception
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5423, 1); --repair
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5455, 1); --reservation
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5456, 1); --reserve
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5500, 1); --return
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5534, 1); --ride
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5556, 1); --road
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5590, 1); --roundabout
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5591, 1); --route
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5636, 1); --sail
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5713, 1); --scooter
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5731, 1); --sea
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5805, 1); --service
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5917, 1); --sightseeing
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (5926, 1); --signpost
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6126, 1); --space
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6236, 1); --station
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6282, 1); --stop
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6371, 1); --subway
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6394, 1); --suitcase
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6544, 1); --taxi
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6717, 1); --tire
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6767, 1); --tourist
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6786, 1); --traffic
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6801, 1); --tram
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6815, 1); --translate
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6816, 1); --translation
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6893, 1); --tunnel
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (6951, 1); --underground
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7101, 1); --vacation
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7123, 1); --vehicle
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7169, 1); --visa
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7173, 1); --visit
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7174, 1); --visitor
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7246, 1); --way
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7299, 1); --wheel
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7347, 1); --window
INSERT INTO public.palavra_objetivo  (id_palavra, id_objetivo) VALUES (7348, 1); --windscreen
    """)


def downgrade() -> None:
    """Downgrade schema."""
    pass
