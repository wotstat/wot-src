class MECHANIC_WIDGET_HOTKEY_CONST(object):
    NORMAL = b'normal'
    WARNING = b'warning'
    ALERT = b'alert'
    INACTIVE = b'inactive'
    INVALID_KEY = b'invalidKey'
    HOT_KEY_STATES = [NORMAL, WARNING, ALERT, INACTIVE, INVALID_KEY]
    COMMAND_ACTIVATE = b'activate'
    ALTERNATIVE_ACTIVATE = b'altActivate'
    PREPARING = b'preparing'
    CANCELLED = b'cancelled'
    SWITCH = b'switch'
    COMMANDS = [COMMAND_ACTIVATE, ALTERNATIVE_ACTIVATE, PREPARING, CANCELLED, SWITCH]
