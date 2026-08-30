from __future__ import absolute_import
from enum import Enum
DT_PDATA_KEY = b'dogTags'

class Settings(Enum):
    SHOW_VICTIMS_DT = b'showVictimsDogTag'
    SHOW_DT_TO_KILLER = b'showDogTagToKiller'

    def __lt__(self, other):
        return self.value < other.value


SETTINGS_POSITIONS = {(Settings.SHOW_VICTIMS_DT): 1, 
   (Settings.SHOW_DT_TO_KILLER): 2}
