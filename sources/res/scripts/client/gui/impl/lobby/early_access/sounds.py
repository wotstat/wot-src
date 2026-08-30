import WWISE
from enum import Enum
from sound_gui_manager import CommonSoundSpaceSettings
from gui.Scaleform.daapi.view.lobby.vehicle_preview.sound_constants import Sounds as VehiclePreviewSounds

class Sounds(Enum):
    INTRO_NAME = b'early_access_intro'
    OVERLAY_HANGAR_FILTERED = b'STATE_hangar_filtered'
    OVERLAY_HANGAR_FILTERED_ON = b'STATE_hangar_filtered_on'


def setResearchesPreviewSoundState():
    WWISE.WW_setState(VehiclePreviewSounds.STATE_PLACE, VehiclePreviewSounds.STATE_PLACE_RESEARCH_PREVIEW)
    return


EARLY_ACCESS_INTRO_SOUND_SPACE = CommonSoundSpaceSettings(name=Sounds.INTRO_NAME.value, entranceStates={(Sounds.OVERLAY_HANGAR_FILTERED.value): (Sounds.OVERLAY_HANGAR_FILTERED_ON.value)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
