from __future__ import absolute_import
from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'shop'
    VEHICLE_PREVIEW_SOUND_SPACE = b'shopVehiclePreview'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_SHOP = b'STATE_hangar_place_shop'
    STATE_PLACE_VEHICLE_PREVIEW = b'STATE_hangar_place_shop_preview'
    ENTER = b'shop_enter'
    EXIT = b'shop_exit'


SHOP_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_SHOP)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ENTER, exitEvent=SOUNDS.EXIT)
SHOP_PREVIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.VEHICLE_PREVIEW_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_VEHICLE_PREVIEW)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'', parentSpace=SOUNDS.COMMON_SOUND_SPACE)
