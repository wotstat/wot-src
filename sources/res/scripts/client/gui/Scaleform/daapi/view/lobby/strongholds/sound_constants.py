from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    STRONGHOLD_SOUND_SPACE = b'stronghold'
    STRONGHOLD_ADS_SOUND_SPACE = b'stronghold_ads'
    STATE_HANGAR_PLACE = b'STATE_hangar_place'
    STATE_HANGAR_PLACE_CLANS = b'STATE_hangar_place_clans'
    STATE_HP_CLANS_INSIDE = b'STATE_hp_clans_inside'
    STATE_HP_CLANS_INSIDE_MAIN = b'STATE_hp_clans_inside_main'
    STATE_HP_CLANS_INSIDE_ADS = b'STATE_hp_clans_inside_ads'
    ENTER = b'clans_enter'
    ADS_ENTER = b'ads_enter'
    ADS_EXIT = b'ads_exit'


STRONGHOLD_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.STRONGHOLD_SOUND_SPACE, entranceStates={(SOUNDS.STATE_HANGAR_PLACE): (SOUNDS.STATE_HANGAR_PLACE_CLANS)}, exitStates={}, persistentSounds=(
 SOUNDS.ENTER,), stoppableSounds=(), priorities=(), autoStart=True)
STRONGHOLD_ADS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.STRONGHOLD_ADS_SOUND_SPACE, entranceStates={(SOUNDS.STATE_HP_CLANS_INSIDE): (SOUNDS.STATE_HP_CLANS_INSIDE_ADS)}, exitStates={(SOUNDS.STATE_HP_CLANS_INSIDE): (SOUNDS.STATE_HP_CLANS_INSIDE_MAIN)}, enterEvent=SOUNDS.ADS_ENTER, exitEvent=SOUNDS.ADS_EXIT, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, parentSpace=SOUNDS.STRONGHOLD_SOUND_SPACE)
