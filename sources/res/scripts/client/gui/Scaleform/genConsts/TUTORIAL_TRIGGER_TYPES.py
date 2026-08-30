class TUTORIAL_TRIGGER_TYPES(object):
    CLICK_TYPE = b'click'
    CLICK_OUTSIDE_TYPE = b'clickOutside'
    ESCAPE = b'escape'
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    ENABLED_CHANGE = b'enabled_change'
    VISIBLE_CHANGE = b'visible_change'
    ALL = [CLICK_TYPE, CLICK_OUTSIDE_TYPE, ESCAPE, ENABLED, DISABLED, ENABLED_CHANGE, 
     VISIBLE_CHANGE]
