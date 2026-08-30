from __future__ import absolute_import
from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    SPACE = b'open_bundle_space'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_BUNDLE = b'STATE_hangar_place_open_bundle'
    BUNDLE_ENTER = b'openbundle_enter'
    BUNDLE_EXIT = b'openbundle_exit'


OPEN_BUNDLE_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_BUNDLE)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.BUNDLE_ENTER, exitEvent=SOUNDS.BUNDLE_EXIT)
