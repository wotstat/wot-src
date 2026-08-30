from enum import Enum
FEATURE = b'limited_ui'

class LimitedUILogItem(Enum):
    DISABLE_LIMITED_UI_BUTTON = b'disable_limited_ui_button'


class LimitedUILogScreenParent(Enum):
    SETTINGS_WINDOW = b'settings_window'


class LimitedUILogActions(Enum):
    CLICK = b'click'
