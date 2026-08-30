from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'crew'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_BARRAKS = b'STATE_hangar_place_barracks'
    STATE_PLACE_HANGAR = b'STATE_hangar_place_garage'
    OVERLAY_SOUND_SPACE = b'crew_overlay'
    OVERLAY_HANGAR_GENERAL = b'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'
    CREW_TANK_CLICK = b'crew_tank_click'
    CREW_LEARN_CLICK = b'crew_crewbook_learn'
    CREW_TIPS_NOTIFICATION = b'crew_notification_tips'
    CREW_TIPS_ERROR = b'crew_notification_error_tips'
    CREW_BOOKS_ENTRANCE = b'crew_page_whoosh'
    CREW_RESET_PERK_SELECTION = b'crew_reset_perks_no_card_selection'
    CREW_RESET_PERK_NO_LOSS = b'crew_reset_perks'
    CREW_RESET_PERK_XP_LOSS = b'crew_reset_perks_percent_down'
    CREW_RESET_PERK_HUGE_LOSS = b'crew_reset_perks_break'
    CREW_PERK_UPGRADE = b'crew_perks_upgrade'
    CREW_CHANGE_ROLE = b'crew_change_qualification'
    CONVERSION_AWARD = b'gui_reward_screen_general'
    MENTORING_LICENSE_AWARD = b'gui_reward_screen_general'


CREW_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_BARRAKS)}, exitStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_HANGAR)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'hangar_crew_enter', exitEvent=b'hangar_crew_exit')
CREW_SOUND_OVERLAY_SPACE = CommonSoundSpaceSettings(name=SOUNDS.OVERLAY_SOUND_SPACE, entranceStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_ON)}, exitStates={(SOUNDS.OVERLAY_HANGAR_GENERAL): (SOUNDS.OVERLAY_HANGAR_GENERAL_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'', parentSpace=SOUNDS.COMMON_SOUND_SPACE)
