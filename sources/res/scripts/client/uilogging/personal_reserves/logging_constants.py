from enum import Enum
from typing import TYPE_CHECKING
from gui.impl.gen import R
if TYPE_CHECKING:
    from typing import Union
    DIALOG_LOGGING_ITEM_TYPES = Union[PersonalReservesLogDialogs, PersonalReservesLogButtons, str]
FEATURE = b'personal_reserves_20'
MIN_VIEW_TIME = 2.0
ACTIVATION_LAYOUT_ID = R.views.lobby.personal_reserves.ReservesActivationView()

class PersonalReservesLogActions(Enum):
    OPEN = b'open'
    CLOSE = b'close'
    CLICK = b'click'
    VIEWED = b'viewed'


class PersonalReservesLogKeys(Enum):
    HANGAR = b'hangar'
    LOBBY_HEADER = b'lobby_header_bar'
    ACTIVATION_WINDOW = b'reserves_activation_window'
    BATTLE = b'battle'
    INTRO_WINDOW = b'reserves_intro_window'
    RESERVES_CONVERSION_WINDOW = b'reserves_conversion_window'
    WIDGET = b'reserves_entry_point_widget'
    RESERVES_DEPOT_TAB = b'reserves_depot_tab'
    FULL_STATS_TAB = b'full_stats_tab'
    DEPOT = b'depo_storage_page'
    ACTIVATION_IN_BATTLE_TAB = b'in_battle_activation_tab'


class PersonalReservesLogNotifications(Enum):
    EXPIRE = b'reserve_expire_notification'


class PersonalReservesLogTooltips(Enum):
    RESERVES_WIDGET_TOOLTIP = b'reserves_widget_tooltip'


class PersonalReservesLogClicks(Enum):
    WIDGET_CLICKED = b'widget_clicked'


class PersonalReservesLogButtons(Enum):
    BUY_AND_ACTIVATE = b'buy_and_activate_button'
    BUY_GOLD = b'buy_gold_button'
    CANCEL = b'cancel_button'
    EXIT = b'exit_button'
    AFFIRMATIVE = b'affirmative_button'
    TO_RESERVES = b'to_reserves_button'
    GOTO_ACTIVATION = b'goto_activation_button'
    TAB_SELECT_BUTTON = b'tab_select_button'
    SHORTCUT_BUTTON = b'shortcut_button'


class PersonalReservesLogDialogs(Enum):
    BUY_AND_ACTIVATE = b'buy_and_activate_dialog'
    BUY_GOLD = b'buy_gold_dialog'
    BUY_AND_UPGRADE = b'buy_and_upgrade_dialog'


BATTLE_DURATION_KEY = b'battle_duration'
ARENA_PERIOD_KEY = b'arena_period'
SECONDS_SINCE_BATTLE_STARTED_KEY = b'seconds_since_battle_started'
ARENA_PERIOD_TO_KEY = {0: b'idle', 
   1: b'waiting', 
   2: b'prebattle', 
   3: b'battle', 
   4: b'afterbattle'}
