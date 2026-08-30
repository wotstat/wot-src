from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'vehicle_hub'
    ABOUT_VEHICLE_ENTER = b'ev_about_vehicle_enter'
    ABOUT_VEHICLE_EXIT = b'ev_about_vehicle_exit'
    STATE_PLACE_ABOUT_VEHICLE = b'STATE_hangar_place_about_vehicle'
    STATE_PLACE = b'STATE_hangar_place'


VH_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_ABOUT_VEHICLE)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ABOUT_VEHICLE_ENTER, exitEvent=SOUNDS.ABOUT_VEHICLE_EXIT)
