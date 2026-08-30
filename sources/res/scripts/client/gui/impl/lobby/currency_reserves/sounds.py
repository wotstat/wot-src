from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    STATE = b'STATE_overlay_hangar_general'
    ENTER = b'STATE_overlay_hangar_general_on'
    EXIT = b'STATE_overlay_hangar_general_off'


RESERVES_AWARD_SOUND_SPACE = CommonSoundSpaceSettings(name=b'reserves_award_view', entranceStates={(SOUNDS.STATE): (SOUNDS.ENTER)}, exitStates={(SOUNDS.STATE): (SOUNDS.EXIT)}, enterEvent=b'', persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
