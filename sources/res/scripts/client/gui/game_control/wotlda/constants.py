from __future__ import absolute_import
import enum
from future.utils import listvalues

class SupportedWotldaLoadoutType(enum.Enum):
    EASY_TANK_EQUIP = b'easy_tank_equip'
    RANDOM = b'random'
    ONSLAUGHT = b'comp7'
    CREW = b'crew'


class SupportedWTRRange(enum.Enum):
    GOLD = b'gold'
    LEGEND = b'legend'

    @staticmethod
    def allRanges():
        return listvalues(SupportedWTRRange.__members__)


EQUIPMENT_ARCHETYPE_1 = b'equipment_archetype_id_1'
EQUIPMENT_ARCHETYPE_2 = b'equipment_archetype_id_2'
EQUIPMENT_ARCHETYPE_3 = b'equipment_archetype_id_3'
LOADOUT_USAGE_PERCENTAGE = b'usage_percentage'
LAST_UPDATE_TIMESTAMP = b'updated_at'
ExpectedArchetypes = {
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32, 
 33}

class OptDeviceAssistType(enum.Enum):
    NODATA = 0
    NORMAL = 1
    LINKED = 2
    COMBINED = 3
