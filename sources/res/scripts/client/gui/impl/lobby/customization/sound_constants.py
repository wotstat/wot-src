from sound_gui_manager import CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'c11n'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_C11N = b'STATE_hangar_place_customization'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'
    STATE_STYLEINFO = b'STATE_infopage_show'
    STATE_STYLEINFO_SHOW = b'STATE_infopage_show_on'
    STATE_STYLEINFO_HIDE = b'STATE_infopage_show_off'
    RTPC_STYLEINFO = b'RTPC_ext_infopage_show'
    ENTER = b'cust_mode_entering'
    EXIT = b'cust_mode_exiting'
    SEASON_SELECT = b'cust_camtype_{}'
    TAB_SWITCH = b'cust_tab_switch'
    EDIT_MODE_SWITCH_ON = b'cust_style_edit_on'
    EDIT_MODE_SWITCH_OFF = b'cust_style_edit_off'
    NEW_PROGRESSIVE_DECAL = b'cust_progress_reward'
    PROGRESSIVE_DECAL_COULD_BE_INSTALLED = b'cust_progress_reward_edit'
    PROGRESSIVE_DECAL_UPGRADE = b'cust_progress_upgrade'
    COINS = b'coins'
    SELECT = b'cust_select'
    CHOOSE = b'cust_tankmodule_choose'
    HOVER = b'cust_tankmodule_mouseover'
    APPLY = b'cust_color_apply'
    CUST_CHOICE_NUMBER = b'cust_choice_number'
    CUST_CHOICE_NUMBER_OVER = b'cust_choise_number_over'
    CUST_CHOICE_BACKSPACE = b'cust_choice_backspace'
    CUST_CHOICE_DELETE = b'cust_choice_delete'
    CUST_CHOICE_NUMBER_DENIED = b'cust_choice_number_denied'
    CUST_CHOICE_ESC = b'cust_choise_esc'
    CUST_CHOICE_ENTER = b'cust_choice_enter'
    CUST_LOCK = b'cust_lock'
    BACK_TO_HANGAR = b'ue_hangar_generic_camera_fly_backward'


C11N_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_C11N)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=SOUNDS.ENTER, exitEvent=SOUNDS.EXIT)
