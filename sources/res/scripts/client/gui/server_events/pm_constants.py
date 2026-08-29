from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER
from personal_missions import PM_BRANCH

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'personalMissions'
    FIRST_RUN_AWARD_APPEARANCE = b'pm_appearance_of_reward'
    AMBIENT = b'pm_ambient'
    MUSIC = b'pm_music'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'
    STATE_PLACE_MISSIONS = b'STATE_hangar_place_personalMissions'
    RTCP_MISSIONS_NUMBER = b'RTPC_ext_mission_number'
    RTCP_MISSIONS_ZOOM = b'RTPC_ext_mission_zoom'
    RTCP_DEBRIS_CONTROL = b'RTPC_ext_mission_debris_control'
    OPERATION_NAV_CLICK = b'tank_selection'
    OPERATION_NAV_CLICK_ANIMATION = b'pm_tank_select_animation'
    CHAIN_NAV_CLICK = b'pm_type_select_animation'
    REGION_CLICK = b'tabb'
    FREE_AWARD_LIST_SPENT = b'pm_reward_list_spend'
    AWARD_WINDOW = b'pm_standard_greeting'
    AWARD_LIST_AWARD_WINDOW = b'pm_special_greeting'
    WOMAN_AWARD_WINDOW = b'pm_special_greeting_woman'
    TANK_AWARD_WINDOW = b'pm_special_greeting_tank'
    RTCP_OVERLAY = b'RTPC_ext_greeting_overlay'
    ONE_AWARD_LIST_RECEIVED = b'pm_greeting_order_form'
    ONE_AWARD_LIST_RECEIVED_CONFIRM = b'pm_greeting_order_form_confirm'
    FOUR_AWARD_LISTS_RECEIVED = b'pm_conversion_order_form'
    RTCP_MISSION_BRANCH = {(PM_BRANCH.REGULAR): b'RTPC_ext_mission_zoom_green', 
       (PM_BRANCH.PERSONAL_MISSION_2): b'RTPC_ext_mission_zoom_blue'}
    BRANCH_DEFAULT = 0
    BRANCH_SELECTED = 100
    MIN_MISSIONS_ZOOM = 0
    MAX_MISSIONS_ZOOM = 100


_SOUNDS_PRIORITIES = (
 SOUNDS.AWARD_WINDOW, SOUNDS.WOMAN_AWARD_WINDOW, SOUNDS.TANK_AWARD_WINDOW)
PERSONAL_MISSIONS_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_MISSIONS)}, exitStates={}, persistentSounds=(
 SOUNDS.MUSIC, SOUNDS.AMBIENT), stoppableSounds=(), priorities=_SOUNDS_PRIORITIES, autoStart=True, enterEvent=b'', exitEvent=b'')
PERSONAL_MISSIONS_SILENT_SOUND_SPACE = CommonSoundSpaceSettings(SOUNDS.COMMON_SOUND_SPACE, {}, {}, (), (), _SOUNDS_PRIORITIES, False, b'', b'')

class PM_TUTOR_FIELDS(CONST_CONTAINER):
    GREETING_SCREEN_SHOWN = b'pm_greeting_screen_shown'
    FIRST_ENTRY_AWARDS_SHOWN = b'pm_first_entry_awards_shown'
    INITIAL_FAL_COUNT = b'pm_initial_free_award_lists_count'
    ONE_FAL_SHOWN = b'pm_first_free_award_list_shown'
    MULTIPLE_FAL_SHOWN = b'pm_four_free_award_lists_shown'
    PM2_ONE_FAL_SHOWN = b'pm2_first_free_award_list_shown'
    PM2_MULTIPLE_FAL_SHOWN = b'pm2_four_free_award_lists_shown'
