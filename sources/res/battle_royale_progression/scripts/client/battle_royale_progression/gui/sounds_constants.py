from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    GENERAL_STATE = b'STATE_overlay_hangar_general'
    GENERAL_STATE_ON = b'STATE_overlay_hangar_general_on'
    GENERAL_STATE_OFF = b'STATE_overlay_hangar_general_off'


GENERAL_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.GENERAL_STATE, entranceStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_ON)}, exitStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
