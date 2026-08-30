from shared_utils import CONST_CONTAINER
import WWISE
from sound_gui_manager import CommonSoundSpaceSettings

def playSound(eventName):
    WWISE.WW_eventGlobal(eventName)
    return


class Sounds(CONST_CONTAINER):
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_PP = b'STATE_hangar_place_post_progression'
    COMMON_SOUND_SPACE = b'post_progression_space'
    ENTER = b'ev_pp_enter'
    ENTER_ELITE_VIEW = b'ev_pp_elite_status_acquired'
    MODIFICATION_DESTROY = b'ev_pp_modification_destroy'
    MODIFICATION_MOUNT = b'ev_pp_modification_mount'
    SETUP_SWITCH = b'ev_pp_setup_switch'
    GAMEPLAY_SETUP_SWITCH = b'ev_pp_gameplay_setup_switch'


PP_VIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.COMMON_SOUND_SPACE, entranceStates={(Sounds.STATE_PLACE): (Sounds.STATE_PLACE_PP)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=Sounds.ENTER, exitEvent=b'')
