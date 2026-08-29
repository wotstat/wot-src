import collections
from items import vehicles, ITEM_TYPES
from constants import FAIRPLAY_VIOLATIONS_NAMES, FAIRPLAY_VIOLATIONS_MASKS
from items.components.c11n_constants import CustomizationType
from debug_utils import *
from typing import Union, Tuple

class AmmoIterator(object):

    def __init__(self, ammo):
        self.__ammo = ammo
        self.__idx = 0
        return

    def __iter__(self):
        return self

    def next(self):
        if self.__idx >= len(self.__ammo):
            raise StopIteration
        idx = self.__idx
        self.__idx += 2
        return (abs(self.__ammo[idx]), self.__ammo[idx + 1])


class LayoutIterator(object):

    def __init__(self, layout):
        self.__layout = layout
        self.__idx = 0
        return

    def __iter__(self):
        return self

    def next(self):
        if self.__idx >= len(self.__layout):
            raise StopIteration
        idx = self.__idx
        self.__idx += 2
        compDescr = self.__layout[idx]
        return (abs(compDescr), self.__layout[idx + 1], compDescr < 0)


def getAmmoDiff(ammo1, ammo2):
    diff = collections.defaultdict(int)
    for compDescr, count in AmmoIterator(ammo1):
        if compDescr != 0:
            diff[abs(compDescr)] += count

    for compDescr, count in AmmoIterator(ammo2):
        if compDescr != 0:
            diff[abs(compDescr)] -= count

    return diff


def getEquipmentsDiff(eqs1, eqs2):
    diff = collections.defaultdict(int)
    for eqCompDescr in eqs1:
        if eqCompDescr != 0:
            diff[abs(eqCompDescr)] += 1

    for eqCompDescr in eqs2:
        if eqCompDescr != 0:
            diff[abs(eqCompDescr)] -= 1

    return diff


def currentWeekPlayDaysCount(curTime, newDayStart, newWeekStart):
    curTime -= newDayStart
    wday = time.gmtime(curTime).tm_wday + 1
    curWeekPlayDaysCnt = wday - newWeekStart
    if newWeekStart >= 0:
        if curWeekPlayDaysCnt == 0:
            curWeekPlayDaysCnt = 7
        elif curWeekPlayDaysCnt < 0:
            curWeekPlayDaysCnt += 7
    elif curWeekPlayDaysCnt == 8:
        curWeekPlayDaysCnt = 1
    elif curWeekPlayDaysCnt > 8:
        curWeekPlayDaysCnt -= 7
    return curWeekPlayDaysCnt


def getFairPlayViolationName(violationsMask):
    if violationsMask == 0:
        return
    else:
        for name in FAIRPLAY_VIOLATIONS_NAMES:
            if violationsMask & FAIRPLAY_VIOLATIONS_MASKS[name] != 0:
                return name

        return


def getCustomizationItem(custType, custID):
    custTypeID = getattr(CustomizationType, str(custType).upper(), None)
    if not custTypeID:
        return (None, (b'Invalid customization type = {0}').format(custType))
    else:
        c11nItems = vehicles.g_cache.customization20().itemTypes.get(custTypeID, None)
        if not c11nItems:
            return (None, (b'Unknown customization typeID = {0}. custType = {1}').format(custTypeID, custType))
        c11nItem = c11nItems.get(custID)
        if not c11nItem:
            return (None,
             (b'Invalid customization item id = {0}. typeID = {1}, custType = {2}').format(custID, custTypeID, custType))
        return (
         c11nItem, b'')


def validateCustomizationItem(custData):
    custID = custData.get(b'id', None)
    splitted = custData.get(b'custType', b'').split(b':')
    custType = splitted[0]
    isProgression = len(splitted) == 2 and splitted[1] == b'progression'
    value = custData.get(b'value', None)
    vehTypeCompDescr = custData.get(b'vehTypeCompDescr', None)
    if custID is None:
        return (False, b'Cust id is not specified')
    else:
        if not custType:
            return (False, b'Cust type is not specified')
        if not isinstance(value, int) or value == 0 and not isProgression:
            return (False, b'Invalid value')
        c11nItem, errStr = getCustomizationItem(custType, custID)
        if not c11nItem:
            return (False, errStr)
        if custType == CustomizationType.STYLE and b'serialNumberSequence' in custData and not c11nItem.isWithSerialNumber:
            return (False, b'Only styles with serial numbers can have serialNumberSequence')
        if vehTypeCompDescr is not None:
            itemTypeID, vehNationID, vehInnationID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
            if itemTypeID != ITEM_TYPES.vehicle:
                return (False, b'Invalid type compact descriptor')
            try:
                vehTypeDescr = vehicles.g_cache.vehicle(vehNationID, vehInnationID)
            except:
                LOG_CURRENT_EXCEPTION()
                return (False, b'Invalid type compact descriptor')

            if not c11nItem.matchVehicleType(vehTypeDescr):
                return (False,
                 (b'Customization item {} and vehTypeCompDescr {} mismatch').format(c11nItem.id, vehTypeCompDescr))
        return (
         True, c11nItem)


class NotificationItem(object):

    def __init__(self, item):
        self.item = item
        cont = []
        cont.append(item[b'type'])
        text = item[b'text']
        for k in sorted(text.keys()):
            cont.append(k)
            cont.append(text[k])

        cont.append(item[b'data'])
        for s in sorted(item[b'requiredTokens']):
            cont.append(s)

        self.asString = (b'').join(cont)
        return

    def __cmp__(self, other):
        if other is None:
            return 1
        else:
            left = self.asString
            right = other.asString
            if left == right:
                return 0
            if left < right:
                return -1
            return 1

    def __hash__(self):
        return hash(self.asString)
