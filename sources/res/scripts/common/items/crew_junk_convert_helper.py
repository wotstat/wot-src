from __future__ import absolute_import
import typing
from collections import defaultdict
from future.utils import viewitems
from items import tankmen, vehicles
if typing.TYPE_CHECKING:
    from typing import Dict, List, Tuple
    from items.tankmen import TankmanDescr
XP_TRASH_LIMIT = 210060
VALID_GROUP = (b'men1', b'women1')
NATIONS_CREW_BOOKS = {0: {b'guideCD': 5406, b'crewBookCD': 10526, b'brochureCD': 286}, 1: {b'guideCD': 5662, b'crewBookCD': 10782, b'brochureCD': 542}, 2: {b'guideCD': 5918, b'crewBookCD': 11038, b'brochureCD': 798}, 3: {b'guideCD': 7198, b'crewBookCD': 12318, b'brochureCD': 2078}, 4: {b'guideCD': 6174, b'crewBookCD': 11294, b'brochureCD': 1054}, 5: {b'guideCD': 6430, b'crewBookCD': 11550, b'brochureCD': 1310}, 6: {b'guideCD': 6686, b'crewBookCD': 11806, b'brochureCD': 1566}, 7: {b'guideCD': 6942, b'crewBookCD': 12062, b'brochureCD': 1822}, 8: {b'guideCD': 7710, b'crewBookCD': 12830, b'brochureCD': 2590}, 9: {b'guideCD': 7454, b'crewBookCD': 12574, b'brochureCD': 2334}, 10: {b'guideCD': 7966, b'crewBookCD': 13086, b'brochureCD': 2846}}
CREW_BOOK_XP = 250001
GUIDE_XP = 100001
BROCHURE_XP = 20001

def findJunkTankmen(tankmenCompDescrs, tankmenVehicles=None):
    removeTankmenList = {}
    for key, compDescr in viewitems(tankmenCompDescrs):
        if tankmenVehicles is not None and key in tankmenVehicles:
            continue
        tankmanDescr = tankmen.TankmanDescr(compDescr)
        if isTrashTankman(tankmanDescr):
            removeTankmenList[key] = tankmanDescr

    return removeTankmenList


def calculateXpFromTankmen(tankmenCompDescrs):
    savingXPByNation = defaultdict(int)
    cashVehicleNativeType = {}
    for tankmanDescr in tankmenCompDescrs:
        _savingTrashTankmanXP(tankmanDescr, cashVehicleNativeType, savingXPByNation)

    return savingXPByNation


def getNationBooksFromXp(xpByNation):
    crewBooks = {}
    for nationID, xp in viewitems(xpByNation):
        if not xp:
            continue
        crewBookCD = NATIONS_CREW_BOOKS[nationID][b'crewBookCD']
        guideCD = NATIONS_CREW_BOOKS[nationID][b'guideCD']
        brochureCD = NATIONS_CREW_BOOKS[nationID][b'brochureCD']
        itemCount = xp // CREW_BOOK_XP
        xp %= CREW_BOOK_XP
        if itemCount > 0:
            crewBooks[crewBookCD] = crewBooks.get(crewBookCD, 0) + itemCount
        itemCount = xp // GUIDE_XP
        xp %= GUIDE_XP
        if itemCount > 0:
            crewBooks[guideCD] = crewBooks.get(guideCD, 0) + itemCount
        itemCount = xp // BROCHURE_XP + 1
        crewBooks[brochureCD] = crewBooks.get(brochureCD, 0) + itemCount

    return crewBooks


def _savingTrashTankmanXP(tankmanDescr, cashVehicleNativeType, savingXPByNation):
    nationID = tankmanDescr.nationID
    typeID = (nationID, tankmanDescr.vehicleTypeID)
    if typeID in cashVehicleNativeType:
        vehType = cashVehicleNativeType[typeID]
    else:
        vehicleNativeDescr = vehicles.VehicleDescr(typeID=typeID)
        vehType = vehicles.getVehicleType(vehicleNativeDescr.type.compactDescr)
        cashVehicleNativeType[typeID] = vehType
    xp = tankmanDescr.totalXP()
    if xp > 0:
        savingXPByNation[nationID] += xp // len(vehType.crewRoles)
    return


def isTrashTankman(tankman):
    if checkXPLimit(tankman):
        return False
    if checkUnique(tankman):
        return False
    if not checkFreeSkills(tankman):
        return False
    return True


def checkXPLimit(tankman):
    tankmanXP = tankman.totalXP()
    return tankmanXP >= XP_TRASH_LIMIT


def checkFreeSkills(tankman):
    if tankman.freeSkillsNumber > 0:
        return False
    return True


def checkUnique(tankman):
    nationConfig = tankmen.getNationConfig(tankman.nationID)
    group = nationConfig.getGroups(tankman.isPremium)[tankman.gid]
    return group.name not in VALID_GROUP
