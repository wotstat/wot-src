from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'barracks'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_BARRACKS = b'STATE_hangar_place_barracks'


BARRACKS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_BARRACKS)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
