from bootcamp.BootcampConstants import HINT_TYPE
__all__ = (b'ACTIONS_HINTS_TO_LOG_ONCE', b'ACTION_SEQUENCES', b'BC_AWARDS_MAP', b'BATTLE_HINTS_TO_LOG_ON_ANIMATION_FINISH', b'BATTLE_HINTS_TO_LOG_ON_COMPLETE', b'BATTLE_HINTS_TO_LOG_ON_HIDE', b'BC_LOG_ACTIONS', b'BC_LOG_KEYS', b'CHECK', b'HANGAR_MENU_ITEMS', b'HANGAR_HINTS_TO_LOG_ON_COMPLETE', b'LIMITS', b'SNIPER_MODE', b'SNIPER_MODE_SEQUENCE')

class BC_LOG_ACTIONS:
    SKIP_VIDEO = b'skip_video'
    MOUSE_CLICK = b'mouse_click'
    MOUSE_MOVE = b'mouse_move'
    CLOSE = b'close'
    CONTINUE_BUTTON_PRESSED = b'continue_button_pressed'
    RESEARCH_BUTTON_PRESSED = b'research_button_pressed'
    BATTLE_BUTTON_PRESSED = b'battle_button_pressed'
    BUY_ITEM = b'buy_item'
    UNLOCK_ITEM = b'unlock_item'
    INFO_PAGE_ICON_CLICKED = b'info_page_icon_clicked'
    CLOSED = b'closed'
    OPENED = b'opened'
    CLICK = b'click'
    CONFIRM = b'confirm'
    SHOW = b'show'
    SELECT = b'select'
    LEAVE = b'leave'
    BUTTON_BACK_TO_HANGAR = b'button_back_to_hangar'
    BUTTON_VIEW_IN_HANGAR = b'button_view_in_hangar'
    VIDEO_FINISHED = b'video_finished'


class SNIPER_MODE:
    ON = b'sniper_mode_on'
    OFF = b'sniper_mode_off'


def getCommonAwards():
    return {b'blocked': b'blocked', 
       b'damage': b'damage', 
       b'destroyed': b'destroyed', 
       b'detected': b'detected', 
       b'assisted': b'assisted', 
       b'0': b'rewards_block', 
       b'1': b'medal_block', 
       b'2': b'medal_block', 
       b'3': b'medal_block', 
       b'': b'XP/credits block'}


def getCustomAwards():
    return {4: {b'0': b'rewards_block', 
           b'1': b'rewards_block', 
           b'2': b'medal_block', 
           b'3': b'medal_block'}, 
       5: {b'0': b'medal_block', 
           b'1': b'medal_block', 
           b'2': b'medal_block'}}


def createAwardsMap():
    awardsMap = {}
    customAwardsLessonsIDs = [
     4, 5]
    for lessonID in range(6):
        awardsMap[lessonID] = getCommonAwards()

    for lessonID in customAwardsLessonsIDs:
        awardsMap[lessonID].update(getCustomAwards()[lessonID])

    return awardsMap


BATTLE_HINTS_TO_LOG_ON_COMPLETE = {(HINT_TYPE.HINT_MOVE_TURRET): b'move_turret', 
   (HINT_TYPE.HINT_MOVE): b'move', 
   (HINT_TYPE.HINT_SHOOT): b'shoot'}
BATTLE_HINTS_TO_LOG_ON_HIDE = {(HINT_TYPE.HINT_AIM): b'aim', 
   (HINT_TYPE.HINT_MESSAGE_AVOID): b'avoid_enemy', 
   (HINT_TYPE.HINT_B3_FALL_BACK): b'fall_back', 
   (HINT_TYPE.HINT_B3_FOLIAGE2): b'flank', 
   (HINT_TYPE.HINT_REPAIR_TRACK): b'repair_track', 
   (HINT_TYPE.HINT_HEAL_CREW): b'heal_crew', 
   (HINT_TYPE.HINT_USE_EXTINGUISHER): b'use_extinguisher', 
   (HINT_TYPE.HINT_WEAK_POINTS): b'weak_points', 
   (HINT_TYPE.HINT_B3_YOU_ARE_DETECTED): b'you_are_detected', 
   (HINT_TYPE.HINT_B3_FLANK): b'go_flank', 
   (HINT_TYPE.HINT_B3_FOLIAGE): b'foliage', 
   (HINT_TYPE.HINT_B3_DO_CAPTURE): b'do_capture', 
   (HINT_TYPE.HINT_B3_CAPTURE_IN_PROGRESS): b'capture_in_progress', 
   (HINT_TYPE.HINT_B3_CAPTURE_RESET): b'capture_reset', 
   (HINT_TYPE.HINT_B3_CAPTURE_TOGETHER): b'capture_together'}
BATTLE_HINTS_TO_LOG_ON_ANIMATION_FINISH = {(HINT_TYPE.HINT_SNIPER_ON_DISTANCE): (SNIPER_MODE.ON), 
   (HINT_TYPE.HINT_SNIPER): (SNIPER_MODE.ON)}
SNIPER_MODE_SEQUENCE = [
 SNIPER_MODE.ON, SNIPER_MODE.OFF]
ACTION_SEQUENCES = {(SNIPER_MODE.ON): SNIPER_MODE_SEQUENCE}
HANGAR_HINTS_TO_LOG_ON_COMPLETE = {22: (BC_LOG_ACTIONS.MOUSE_MOVE)}
ACTIONS_HINTS_TO_LOG_ONCE = [
 BATTLE_HINTS_TO_LOG_ON_HIDE[HINT_TYPE.HINT_WEAK_POINTS]]
HANGAR_MENU_ITEMS = {b'hangar': b'hangar', 
   b'techtree': b'techtree'}
BC_AWARDS_MAP = createAwardsMap()

class BC_LOG_KEYS:
    BC_NATION_SELECT = b'bc_nation_select'
    BC_BATTLE_HINTS = b'bc_battle_hints'
    BC_INTRO_VIDEO = b'bc_intro_video'
    BC_OUTRO_VIDEO = b'bc_outro_video'
    BC_INTERLUDE_VIDEO = b'bc_interlude_video'
    BC_RESULT_SCREEN = b'bc_result_screen'
    BC_HANGAR_HINTS = b'bc_hangar_hints'
    BC_RESEARCH_VEHICLES = b'bc_research_vehicles'
    BC_HANGAR_MENU = b'bc_hangar_menu'
    BC_CURRENT_PROGRESS_WIDGET = b'bc_current_progress_widget'
    BC_PROGRESS_WIDGET = b'bc_progress_widget'
    BC_EXIT_VIEW = b'bc_exit_view'
    BC_DEVICE_SETUP_SUB_VIEW = b'bc_device_setup_sub_view'
    BC_CONSUMABLE_SETUP_SUB_VIEW = b'bc_consumable_setup_sub_view'
    BC_QUESTS_VIEW = b'bc_quests_view'
    MS_WINDOW = b'ms_window'


class CHECK:
    GREATER_THAN = b'gt'
    EQUAL = b'eq'


class LIMITS:
    INVALID_MIN_LENGTH = 0
    INTRO_VIDEO_MAX_LENGTH = 50
    OUTRO_VIDEO_MAX_LENGTH = 85
    INTERLUDE_VIDEO_MAX_LENGTH = 38
    RESEARCH_MAX_LESSON = 3
