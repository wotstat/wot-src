from gui.impl.gen import R
from helpers.time_utils import ONE_DAY, ONE_HOUR
from shared_utils import CONST_CONTAINER
ZERO_TIME = 0.0
TIME_FORMAT_DAYS = b'days'
TIME_FORMAT_HOURS = b'hours'
TIME_FORMAT_TO_TIME_UNIT = {TIME_FORMAT_DAYS: ONE_DAY, 
   TIME_FORMAT_HOURS: ONE_HOUR}
R_BUYING_PANEL = R.strings.marathon.vehiclePreview.buyingPanel
R_TITLE_TOOLTIP = R.strings.marathon.vehiclePreview.title.tooltip
BUYING_BUTTON_ICON_ALIGN = b'right'
TOKEN_COUNT_INDEX = 1
MISSION_TAB_FORMAT = b'MISSIONS_TAB_{}'
AWARD_TOKENS_FORMAT = b'{}{}'

class MarathonState(CONST_CONTAINER):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 3
    SUSPENDED = 4
    DISABLED = 5
    UNKNOWN = 6
    ENABLED_STATE = (NOT_STARTED, IN_PROGRESS, FINISHED)
    DISABLED_STATE = (SUSPENDED, DISABLED, UNKNOWN)


class MarathonWarning(CONST_CONTAINER):
    WRONG_VEH_TYPE = b'veh_type'
    WRONG_BATTLE_TYPE = b'battle_type'
    NONE = b''


class MarathonFlagTooltip(CONST_CONTAINER):
    from gui.marathon.marathon_header_tooltips import BaseTooltip, ProgressHeaderTooltip, CountdownHeaderTooltip, SimpleTextHeaderTooltip
    BASE = BaseTooltip
    COUNTDOWN = CountdownHeaderTooltip
    PROGRESS = ProgressHeaderTooltip
    TEXT = SimpleTextHeaderTooltip
