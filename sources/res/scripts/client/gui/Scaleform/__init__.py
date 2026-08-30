import os
from gui.Scaleform.locale.MENU import MENU
from nations import NAMES
from skeletons.gui.system_messages import ISystemMessages
from skeletons.gui.techtree_events import ITechTreeEventsListener
SCALEFORM_SUPPORT = False
try:
    import _Scaleform
    SCALEFORM_SUPPORT = True
except ImportError:
    raise NotImplementedError(b'Client not support Scaleform')

SCALEFORM_SWF_PATH_V3 = b'gui/flash'
VEHICLE_TYPES_ICONS_DIR_PATH = b'../maps/icons/filters/tanks/'
NATION_FILTER_ICONS_DIR_PATH = b'../maps/icons/filters/nations/'
BUTTON_FILTER_ICONS_DIR_PARH = b'../maps/icons/library/'
LEVEL_FILTER_ICONS_DIR_PARH = b'../maps/icons/filters/levels/'
NATIONS_ICON_FILENAME = b'../maps/icons/nations/%s_%s.%s'
NATION_ICON_PREFIX_131x31 = b'131x31'
DEFAULT_VIDEO_BUFFERING_TIME = 2.0

def getVehicleTypeAssetPath(vehicleType, extension=b'.png'):
    return (b'').join([VEHICLE_TYPES_ICONS_DIR_PATH, vehicleType, extension])


def getButtonsAssetPath(button, extension=b'.png'):
    return (b'').join((BUTTON_FILTER_ICONS_DIR_PARH, button, extension))


def getNationsFilterAssetPath(nationName, extension=b'.png'):
    return (b'').join((NATION_FILTER_ICONS_DIR_PATH, nationName, extension))


def getNationsAssetPath(nation, namePrefix=b'', extension=b'png'):
    return NATIONS_ICON_FILENAME % (NAMES[nation], namePrefix, extension)


def getLevelsAssetPath(level_str, extension=b'.png'):
    return (b'').join([LEVEL_FILTER_ICONS_DIR_PARH, level_str, extension])


def getNecessaryArenaFrameName(arenaSubType, hasBase=None, hasControlPoint=None):
    if arenaSubType.startswith(b'assault'):
        return (b'{0}{1}').format(b'assault', b'1' if hasBase else b'2')
    if arenaSubType.startswith(b'comp7') and not hasControlPoint:
        return (b'{0}{1}').format(b'comp7_', b'1' if hasBase else b'2')
    return arenaSubType


def getPathForFlash(path, base=SCALEFORM_SWF_PATH_V3):
    return os.path.relpath(path, base)


def getScaleformConfig(manager):
    from gui.Scaleform.SystemMessagesInterface import SystemMessagesInterface
    messages = SystemMessagesInterface()
    messages.init()
    manager.addInstance(ISystemMessages, messages, finalizer=b'destroy')
    from gui.techtree.techtree_events import TechTreeEventsListener
    listener = TechTreeEventsListener()
    listener.init()
    manager.addInstance(ITechTreeEventsListener, listener, finalizer=b'fini')
    return
