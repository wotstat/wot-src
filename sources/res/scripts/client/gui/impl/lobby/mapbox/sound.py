from enum import Enum
from sound_gui_manager import CommonSoundSpaceSettings
import WWISE

class Sounds(Enum):
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'


class MapBoxSounds(Enum):
    REWARD_SCREEN = b'bp_reward_screen'


def getMapboxViewSoundSpace(enterEvent=b'', exitEvent=b''):
    return CommonSoundSpaceSettings(name=b'mapbox_view', entranceStates={(Sounds.OVERLAY_HANGAR_GENERAL.value): (Sounds.OVERLAY_HANGAR_GENERAL_ON.value)}, exitStates={(Sounds.OVERLAY_HANGAR_GENERAL.value): (Sounds.OVERLAY_HANGAR_GENERAL_OFF.value)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=enterEvent, exitEvent=exitEvent)


def playSound(eventName):
    WWISE.WW_eventGlobal(eventName)
    return
