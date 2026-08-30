from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from shared_utils import CONST_CONTAINER

class ICONS_SIZES(CONST_CONTAINER):
    X550 = b'550x550'
    X320 = b'320x320'
    X220 = b'220x220'
    X110 = b'110x110'
    X80 = b'80x80'
    X48 = b'48x48'
    X32 = b'32x32'
    X24 = b'24x24'


class BADGES_ICONS(CONST_CONTAINER):
    X320 = ICONS_SIZES.X320
    X220 = ICONS_SIZES.X220
    X110 = ICONS_SIZES.X110
    X80 = ICONS_SIZES.X80
    X48 = ICONS_SIZES.X48
    X32 = ICONS_SIZES.X32
    X24 = ICONS_SIZES.X24


class BADGES_STRIPS_ICONS(CONST_CONTAINER):
    X100 = b'100x40'
    X68 = b'68x28'
    X64 = b'64x24'


class BADGES_HIGHLIGHTS(CONST_CONTAINER):
    RED = b'red'
    VIOLET = b'violet'
    GREEN = b'green'
    GOLD = b'gold'


def getBadgeIconPath(size, badgeID):
    return RES_ICONS.getBadgeIcon(size, badgeID)


def getAwardBadgeIconPath(size, badgeID):
    return RES_ICONS.getAwardBadgeIcon(size, badgeID)


def getBadgeHighlightIconPath(value):
    return RES_ICONS.getBadgeHighlightIcon(value)


def getPersonalMissionVehicleAwardImage(size, vehicleName):
    return RES_ICONS.getPersonalMissionVehicleAwardImage(size, vehicleName)
