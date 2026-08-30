from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class ModeSelectorSound(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'mode_selector'
    STATE_PLACE = b'STATE_mode_selector'
    STATE_MODE_SELECTOR_ON = b'STATE_mode_selector_on'
    STATE_MODE_SELECTOR_OFF = b'STATE_mode_selector_off'
    ENTER_EVENT = b'ev_mode_selector_enter'
    EXIT_EVENT = b'ev_mode_selector_exit'


MODE_SELECTOR_SOUND_SPACE = CommonSoundSpaceSettings(name=ModeSelectorSound.COMMON_SOUND_SPACE, entranceStates={(ModeSelectorSound.STATE_PLACE): (ModeSelectorSound.STATE_MODE_SELECTOR_ON)}, exitStates={(ModeSelectorSound.STATE_PLACE): (ModeSelectorSound.STATE_MODE_SELECTOR_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=ModeSelectorSound.ENTER_EVENT, exitEvent=ModeSelectorSound.EXIT_EVENT)
