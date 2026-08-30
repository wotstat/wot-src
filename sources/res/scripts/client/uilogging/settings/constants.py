from enum import Enum
FEATURE = b'settings'
GROUP = b'settings'

class SettingsLogActions(Enum):
    SETTINGS_INITED = b'settings_inited'
    SETTINGS_CHANGED = b'settings_changed'
