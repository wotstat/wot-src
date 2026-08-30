from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    SPACE = b'resource_well_space'
    COMMON_ENTER = b'resources_well_enter'
    COMMON_EXIT = b'resources_well_exit'
    PREVIEW_SPACE = b'resource_well_preview_space'
    PREVIEW_ENTER = b'resources_well_preview_enter'
    PREVIEW_EXIT = b'resources_well_preview_exit'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'


RESOURCE_WELL_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.SPACE, entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.COMMON_ENTER, exitEvent=SOUNDS.COMMON_EXIT)
