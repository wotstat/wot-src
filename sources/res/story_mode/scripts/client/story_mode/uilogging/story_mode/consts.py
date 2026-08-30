from enum import Enum

class Features(str, Enum):
    ONBOARDING = b'onboarding'
    STORY_MODE = b'story_mode'


class LogWindows(str, Enum):
    HELP = b'help_window'
    QUEUE = b'queue_window'
    INTRO_VIDEO = b'intro_video'
    OUTRO_VIDEO = b'outro_video'
    PRE_BATTLE = b'pre_battle_window'
    POST_BATTLE = b'post_battle_window'
    EPILOGUE = b'epilogue_window'
    CONGRATULATIONS = b'congratulations_window'
    MODE_SELECTOR_CARD = b'mode_selector_card'
    MISSION_SELECTION = b'mission_selection_window'
    ESCAPE_MENU = b'escape_menu'
    SETTINGS_MENU = b'settings_menu'
    INFO_PAGE = b'info_page'
    ENTRY_POINT = b'newbie_banner'
    ENTRY_POINT_TOOLTIP = b'newbie_banner_tooltip'
    ENTRY_POINT_EVENT = b'event_banner'
    ENTRY_POINT_TOOLTIP_EVENT = b'event_banner_tooltip'
    NEWBIE_ADVERTISING = b'newbie_advertising_view'
    EVENT_WELCOME = b'event_welcome_view'
    COMPLETED_TASKS_WARNING = b'completed_tasks_warning_window'


class LogButtons(str, Enum):
    SKIP = b'skip_button'
    CONTINUE = b'continue_button'
    OK = b'ok_button'
    APPLY = b'apply_button'
    CLOSE = b'close_button'
    QUIT = b'quit_button'
    BATTLE = b'battle_button'
    RESTART_BATTLE = b'restart_battle_button'
    INFO = b'info_button'
    SELECT = b'select_button'
    GARAGE = b'garage_button'
    SETTINGS = b'settings_button'
    HELP = b'help_button'
    TAB = b'tab'
    SUBMIT = b'submit_button'
    ABOUT = b'about_button'
    TAB_SECTION = b'tab_section'


class LogActions(str, Enum):
    OPEN = b'open'
    CLOSE = b'close'
    CLICK = b'click'
    AUTO_SELECT = b'auto_select'
    SHOW = b'show'
    PLAY = b'play'
    WATCHED = b'watched'
    GAME_LOADING_CLOSE = b'game_loading_close'


class LogBattleResultStats(str, Enum):
    WIN = b'win'
    LOST = b'lost'


TOOLTIP_MIN_VIEW_TIME = 2.0
