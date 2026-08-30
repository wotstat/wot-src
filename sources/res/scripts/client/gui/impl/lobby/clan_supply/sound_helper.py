from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    ENTER_EVENT = b'clans_supply_map_carro45t_enter'
    EXIT_EVENT = b'clans_supply_map_carro45t_exit'
    STATE_HP_CLANS_INSIDE = b'STATE_hp_clans_inside'
    STATE_HP_CLANS_INSIDE_SUPPLY = b'STATE_hp_clans_inside_supply'
    STATE_HP_CLANS_INSIDE_MAIN = b'STATE_hp_clans_inside_main'
    STATE_HANGAR_FILTERED = b'STATE_hangar_filtered'
    STATE_HANGAR_FILTERED_ON = b'STATE_hangar_filtered_on'
    STATE_HANGAR_FILTERED_OFF = b'STATE_hangar_filtered_off'
    STATE_HANGAR_PLACE = b'STATE_hangar_place'
    STATE_HANGAR_PLACE_CLANS = b'STATE_hangar_place_clans'


def getMainSoundSpace():
    return CommonSoundSpaceSettings(name=b'clan_supply_main_view', entranceStates={(SOUNDS.STATE_HANGAR_PLACE): (SOUNDS.STATE_HANGAR_PLACE_CLANS), 
       (SOUNDS.STATE_HP_CLANS_INSIDE): (SOUNDS.STATE_HP_CLANS_INSIDE_SUPPLY)}, exitStates={(SOUNDS.STATE_HP_CLANS_INSIDE): (SOUNDS.STATE_HP_CLANS_INSIDE_MAIN)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ENTER_EVENT, exitEvent=SOUNDS.EXIT_EVENT)


def getInfoPageSoundSpace():
    return CommonSoundSpaceSettings(name=b'clan_supply_info_page', entranceStates={(SOUNDS.STATE_HANGAR_FILTERED): (SOUNDS.STATE_HANGAR_FILTERED_ON)}, exitStates={(SOUNDS.STATE_HANGAR_FILTERED): (SOUNDS.STATE_HANGAR_FILTERED_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True)
