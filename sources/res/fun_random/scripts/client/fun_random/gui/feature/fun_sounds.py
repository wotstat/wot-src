from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class FunSounds(CONST_CONTAINER):
    HANGAR_PLACE_STATE = b'STATE_hangar_place'
    HANGAR_PLACE_TASKS = b'STATE_hangar_place_tasks'
    PROGRESSION_SPACE_NAME = b'fun_progression_view'
    PROGRESSION_ENTER_EVENT = b'ev_fep_tasks_enter'
    PROGRESSION_EXIT_EVENT = b'ev_fep_tasks_exit'


FUN_PROGRESSION_SOUND_SPACE = CommonSoundSpaceSettings(name=FunSounds.PROGRESSION_SPACE_NAME, entranceStates={(FunSounds.HANGAR_PLACE_STATE): (FunSounds.HANGAR_PLACE_TASKS)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=FunSounds.PROGRESSION_ENTER_EVENT, exitEvent=FunSounds.PROGRESSION_EXIT_EVENT)
