from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'tasks'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_TASKS = b'STATE_hangar_place_tasks'
    ENTER = b'tasks_bp_s12_enter'
    EXIT = b'tasks_bp_s12_exit'


TASKS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_TASKS)}, exitStates={}, enterEvent=SOUNDS.ENTER, exitEvent=SOUNDS.EXIT, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
