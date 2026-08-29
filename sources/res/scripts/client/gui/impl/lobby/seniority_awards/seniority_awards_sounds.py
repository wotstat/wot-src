import WWISE
from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import StatesGroup, States
SENIORITY_REWARD_SOUND_SPACE = CommonSoundSpaceSettings(name=b'seniority_award', entranceStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(StatesGroup.OVERLAY_HANGAR_GENERAL): (States.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')

def playSound(eventName):
    if eventName:
        WWISE.WW_eventGlobal(eventName)
    return
