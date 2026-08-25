from __future__ import absolute_import
import WWISE
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import StatesGroup, States
SENIORITY_REWARD_SOUND_SPACE = CommonSoundSpaceSettings(name=b'seniority_award', entranceStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')

class LootBoxViewEvents(CONST_CONTAINER):
    ENTRY_VIEW_ENTER = b'gui_lootbox_logistic_center_ambience_on'
    ENTRY_VIEW_EXIT = b'gui_lootbox_logistic_center_ambience_off'
    BENGAL_FIRE_OFF = b'gui_lootbox_logistic_center_bengal_fire_off'


def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)
    return
