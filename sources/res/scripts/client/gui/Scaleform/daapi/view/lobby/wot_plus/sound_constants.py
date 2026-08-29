from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    INFO_PAGE_NAME = b'wot_plus_info_page'
    VEHICLE_RENTAL_PAGE_NAME = b'vehicle_rental_page'
    INTRO_PAGE_NAME = b'wot_plus_intro_page'
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'


WOT_PLUS_INFO_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.INFO_PAGE_NAME, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
VEHICLE_RENTAL_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.VEHICLE_RENTAL_PAGE_NAME, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
WOT_PLUS_INTRO_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.INTRO_PAGE_NAME, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
