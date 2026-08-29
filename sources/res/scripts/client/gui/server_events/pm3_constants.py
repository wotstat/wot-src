from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(object):
    COMMON_SOUND_SPACE = b'personalMissions'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_MISSIONS = b'STATE_hangar_place_personalMissions_lbz'
    AMBIENT = b'pm3_lbz_ambient'
    MUSIC = b'pm3_lbz_music'
    STATE_SCREEN_GROUP = b'STATE_pm_lbz'
    STATE_PLACE_SPLIT_SCREEN = b'STATE_pm_lbz_screen_01'
    STATE_PLACE_OPERATION_SCREEN = b'STATE_pm_lbz_screen_02'
    STATE_PLACE_TASK_SCREEN = b'STATE_pm_lbz_screen_03'
    PROJECTOR = b'pm3_lbz_projector_appear'
    PROJECTOR_SLIDE_IN = b'pm3_lbz_projector_slide_in'
    PROJECTOR_SLIDE_OUT = b'pm3_lbz_projector_slide_out'
    SWITCH_CARD_ANIMATION = b'pm_type_select_animation'
    AWARD_WINDOW = b'pm_standard_greeting'
    WOMAN_AWARD_WINDOW = b'pm_special_greeting_woman'
    TANK_AWARD_WINDOW = b'pm_special_greeting_tank'
    STATE_OVERLAY_HANGAR_GENERAL_GROUP = b'STATE_overlay_hangar_general'
    STATE_OVERLAY_HANGAR_GENERAL_ON = b'STATE_overlay_hangar_general_on'
    STATE_OVERLAY_HANGAR_GENERAL_OFF = b'STATE_overlay_hangar_general_off'
    STATE_OPERATION_REWARD_PREVIEW_SCREEN = b'STATE_hangar_place_personalMissions_lbz_preview'
    EVENT_REWARD_SCREEN_GENERAL = b'gui_reward_screen_general'
    EVENT_SPECIAL_GREETING = b'gui_special_greeting'


_SOUNDS_PRIORITIES = (
 SOUNDS.AWARD_WINDOW, SOUNDS.WOMAN_AWARD_WINDOW, SOUNDS.TANK_AWARD_WINDOW)
PERSONAL_MISSIONS_3_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PLACE_MISSIONS)}, exitStates={}, persistentSounds=(
 SOUNDS.MUSIC, SOUNDS.AMBIENT), stoppableSounds=(), priorities=_SOUNDS_PRIORITIES, autoStart=True, enterEvent=b'', exitEvent=b'')

class VoiceOvers(object):
    SPLIT_SCREEN_VO = b'pm3_cabinet_vo'
    STOP_SPLIT_SCREEN_VO = b'pm3_cabinet_vo_stop'
    OPERATION_SCREEN_VO = b'pm3_operation_vo'
    STOP_OPERATION_VO = b'pm3_operation_vo_stop'
    OPERATION_SCREEN_GROUP = b'SWITCH_ext_pm3_operation'
    SWITCH_OPERATION_01 = b'SWITCH_ext_pm3_operation_01'
    SWITCH_OPERATION_02 = b'SWITCH_ext_pm3_operation_02'
    SWITCH_OPERATION_03 = b'SWITCH_ext_pm3_operation_03'
    REWARD_SCREEN_VO = b'pm3_reward_vo'
    STOP_REWARD_VO = b'pm3_reward_vo_stop'
    REWARD_GROUP = b'SWITCH_ext_pm3_reward'
    REWARD_SWITCH_SIMPLE = b'SWITCH_ext_pm3_reward_simple'
    REWARD_SWITCH_HONOR = b'SWITCH_ext_pm3_reward_honor'


class VIDEO(object):
    GROUP = b'STATE_video_overlay'
    PLAY = b'STATE_video_overlay_on'
    STOP = b'STATE_video_overlay_off'
    STOP_EVENT = b'pm3_lbz_vid_stop'
    PAUSE = b'pm3_lbz_vid_pause'
    RESUME = b'pm3_lbz_vid_resume'
    SOUND_INTRO = b'pm3_lbz_vid_intro'
    SOUND_REWARD_1 = b'pm3_lbz_vid_A161_ARMT'
    SOUND_REWARD_2 = b'pm3_lbz_vid_A173_TF_2_CLARK'
    SOUND_REWARD_3 = b'pm3_lbz_vid_F119_Projet_Murat'
    SOUND_REWARD_4 = b'pm3_lbz_vid_T11_MouseKonig'
