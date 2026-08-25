from __future__ import absolute_import
import collections, re, time
from functools import total_ordering
from constants import FairplayViolationType
from items import vehicles, ITEM_TYPES
from fairplay_violation_types import getViolationsByMask, FairplayViolations
from items.components.c11n_constants import CustomizationType
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR
from typing import Union, Tuple
from soft_exception import SoftException

class AmmoIterator(object):

    def __init__(self, ammo):
        self.__ammo = ammo
        self.__idx = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        if self.__idx >= len(self.__ammo):
            raise StopIteration
        idx = self.__idx
        self.__idx += 2
        return (abs(self.__ammo[idx]), self.__ammo[idx + 1])

    next = __next__


class LayoutIterator(object):

    def __init__(self, layout):
        self.__layout = layout
        self.__idx = 0
        return

    def __iter__(self):
        return self

    def __next__(self):
        if self.__idx >= len(self.__layout):
            raise StopIteration
        idx = self.__idx
        self.__idx += 2
        compDescr = self.__layout[idx]
        return (abs(compDescr), self.__layout[idx + 1], compDescr < 0)

    next = __next__


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
        violationNamesByMask = getViolationsByMask(violationsMask)
        for vType in FairplayViolationType.PRIORITY:
            violationsByRule = FairplayViolations.getViolationsByType(vType)
            for violation in violationNamesByMask:
                if violation in violationsByRule:
                    return violation

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


@total_ordering
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

    def __hash__(self):
        return hash(self.asString)

    def __eq__(self, other):
        return self.__compare(other) == 0

    def __lt__(self, other):
        return self.__compare(other) < 0

    def __compare(self, other):
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


_VERSION_REGEXP = re.compile(b'^([a-z]{2,4}_)?(([0-9]+\\.){2,4}[0-9]+)(_[0-9]+)?$')

def parseVersion(version):
    result = _VERSION_REGEXP.search(version)
    if result is None:
        return
    else:
        realmCode, mainVersion, _, patchVersion = result.groups()
        if mainVersion:
            realmCode = realmCode.replace(b'_', b'') if realmCode else b''
            patchVersion = int(patchVersion.replace(b'_', b'')) if patchVersion else 0
            return (
             realmCode, mainVersion, patchVersion)
        return


def isValidClientVersion(clientVersion, serverVersion):
    if clientVersion != serverVersion:
        if clientVersion is None or serverVersion is None:
            return False
        clientParsedVersion = parseVersion(clientVersion)
        serverParsedVersion = parseVersion(serverVersion)
        if clientParsedVersion is None or serverParsedVersion is None:
            return False
        clientRealmCode, clientMainVersion, clientPatchVersion = clientParsedVersion
        serverRealmCode, serverMainVersion, serverPatchVersion = serverParsedVersion
        if clientRealmCode != serverRealmCode:
            return False
        if clientMainVersion != serverMainVersion:
            return False
        if clientPatchVersion < serverPatchVersion:
            return False
    return True


def getClientMainVersion():
    mainVersion = None
    try:
        _, clentVersion = readClientServerVersion()
        parsedVersion = parseVersion(clentVersion)
        _, mainVersion, _ = parsedVersion
    except:
        LOG_ERROR(b'Can not read or parse client-server version')

    return mainVersion


def readClientServerVersion():
    import ResMgr
    fileName = b'scripts/entity_defs/interfaces/AccountVersion.def'
    section = ResMgr.openSection(fileName)
    if section is None:
        raise SoftException(b'Cannot open ' + fileName)
    for attrName, section in section[b'Properties'].items():
        if not attrName.startswith(b'requiredVersion_'):
            continue
        version = section.readString(b'Default')
        if not version:
            raise SoftException(b'Subsection AccountVersion.def/Properties/%s/Default is missing or empty' % attrName)
        section = None
        ResMgr.purge(fileName)
        return (attrName, version)

    raise SoftException(b'Field AccountVersion.def/Properties/requiredVersion_* is not found')
    return
