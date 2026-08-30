from enum import Enum
TIME_LIMIT = 2

class Features(str, Enum):
    ARMOR_INSPECTOR = b'armor_inspector'


class Tabs(str, Enum):
    ARMOR_TAB = b'armor_tab'


class LogItems(str, Enum):
    ARMOR_TOOLTIP = b'armor_tooltip'


class LogActions(str, Enum):
    OPEN = b'open'
    CLOSE = b'close'
    CLICK = b'click'
    TOOLTIP_ACTION = b'watched'
    EXPAND = b'expand'
    COLLAPSE = b'collapse'
