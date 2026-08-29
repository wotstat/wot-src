from enum import Enum
FEATURE = b'lootbox'
DEFAULT_TIME_LIMIT = 1.0

class Actions(Enum):
    OPEN = b'open'
    CLICK = b'click'
    TOOLTIP_WATCHED = b'tooltip_watched'
    ANIMATION_SWITCH = b'animation_switch'
    PROBABILITY_OPEN_CLICK = b'probability_open_click'
    PROBABILITY_VIEWED = b'probability_viewed'
    STATISTIC_OPEN_CLICK = b'statistic_open_click'
    STATISTIC_ESC_HOTKEY = b'statistic_esc_hotkey'
    STORAGE_ESC_HOTKEY = b'storage_esc_hotkey'


class Items(Enum):
    CAROUSEL_ENTRY_POINT = b'carousel_entry_point'
    ANIMATION_SWITCH_BUTTON = b'animation_switch_button'
    PROBABILITY_BTN = b'probability_btn'
    STATISTIC_BTN = b'statistic_btn'
    STATISTIC_NO_BOX_BTN = b'statistic_no_box_btn'
    STATISTIC_FULL_STATS_BTN = b'statistic_full_stats_btn'
    UNKNOWN_STATS_BTN = b'unknown_stats_btn'
    RIGHT_CORNER_BUY_BTN = b'right_corner_buy_btn'
    CURRENT_LOOTBOX_BUY_BTN = b'current_lootbox_buy_btn'
    NO_LOOTBOX_BUY_BTN = b'no_lootbox_buy_btn'
    UNKNOWN_BUY_BTN = b'unknown_buy_btn'
    CLOSE_CROSS_BTN = b'close_cross_btn'
    CLOSE_ESC_HOTKEY = b'close_esc_hotkey'
    CURRENT_LB_TAB = b'current_lootbox_tab'
    ALL_LB_TAB = b'all_boxes_tab'


class Views(Enum):
    HANGAR = b'hangar'
    STORAGE = b'storage'
    PROBABILITY = b'probability'
    REWARDS = b'rewards'
    REWARD_VIDEO = b'reward_video'
    WELCOME = b'welcome'
    STATISTICS_SHORT_STATS = b'statistics_short_stats'


BUY_BUTTONS_MAP = {0: (Items.UNKNOWN_BUY_BTN), 
   1: (Items.RIGHT_CORNER_BUY_BTN), 
   2: (Items.CURRENT_LOOTBOX_BUY_BTN), 
   3: (Items.NO_LOOTBOX_BUY_BTN)}
STATISTIC_BUTTONS_MAP = {0: (Items.STATISTIC_BTN), 
   1: (Items.STATISTIC_NO_BOX_BTN), 
   2: (Items.STATISTIC_FULL_STATS_BTN), 
   3: (Items.UNKNOWN_STATS_BTN)}
TABS_STATE_MAP = {0: (Items.CURRENT_LB_TAB), 
   1: (Items.ALL_LB_TAB)}
