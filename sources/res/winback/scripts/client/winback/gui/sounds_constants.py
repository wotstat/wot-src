from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    GENERAL_STATE = b'STATE_overlay_hangar_general'
    GENERAL_STATE_ON = b'STATE_overlay_hangar_general_on'
    GENERAL_STATE_OFF = b'STATE_overlay_hangar_general_off'


class WinbackSounds(CONST_CONTAINER):
    REWARD_SCREEN = b'gui_reward_screen_general'


GENERAL_SOUND_SPACE = CommonSoundSpaceSettings(name=b'winback_general', entranceStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_ON)}, exitStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
REWARD_SOUND_SPACE = CommonSoundSpaceSettings(name=b'winback_reward', entranceStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_ON)}, exitStates={(SOUNDS.GENERAL_STATE): (SOUNDS.GENERAL_STATE_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=WinbackSounds.REWARD_SCREEN, exitEvent=b'')
