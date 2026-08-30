from __future__ import absolute_import
from enum import Enum

class HangarSoundStates(Enum):
    PLACE = b'STATE_hangar_place'
    SPACE = b'STATE_hangar_space'
    PLACE_GARAGE = b'STATE_hangar_place_garage'
    ALL_VEHICLES_ON = b'STATE_hangar_space_on'
    ALL_VEHICLES_OFF = b'STATE_hangar_space_off'
