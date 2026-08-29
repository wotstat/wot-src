class LAYER_NAMES(object):
    UNDEFINED = b''
    ROOT = b'root'
    MARKER = b'marker'
    VIEWS = b'view'
    SUBVIEW = b'subView'
    TOP_SUB_VIEW = b'topSubView'
    WINDOWS = b'window'
    FULLSCREEN_WINDOWS = b'fullscreenWindow'
    IME = b'ime'
    SYSTEM_MESSAGES = b'systemMessages'
    DIALOGS = b'topWindow'
    SERVICE_LAYOUT = b'serviceLayout'
    HIDDEN_SERVICE_LAYOUT = b'hiddenServiceLayout'
    OVERLAY = b'overlay'
    TOOL_TIPS = b'toolTips'
    WAITING = b'waiting'
    CURSOR = b'cursor'
    LAYER_ORDER = [UNDEFINED, ROOT, HIDDEN_SERVICE_LAYOUT, MARKER, VIEWS, SUBVIEW, TOP_SUB_VIEW, 
     WINDOWS, FULLSCREEN_WINDOWS, SYSTEM_MESSAGES, DIALOGS, OVERLAY, IME, 
     SERVICE_LAYOUT, TOOL_TIPS, CURSOR, WAITING]
    FOCUS_ORDER = [WAITING, OVERLAY, DIALOGS, FULLSCREEN_WINDOWS, WINDOWS, TOP_SUB_VIEW, SUBVIEW, 
     VIEWS, MARKER]
