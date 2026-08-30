import nations
from items import vehicles, ITEM_TYPES
from items.badges_common import BadgesCommon
from account_shared import AmmoIterator
from constants import PREBATTLE_ACCOUNT_STATE, VEHICLE_CLASSES, ARENA_GUI_TYPE, PREBATTLE_ROLE, IGR_TYPE, IS_DEVELOPMENT
from debug_utils import LOG_DEBUG

def decodeRoster(roster):
    return (
     roster & 15, not roster & 240)


def encodeRoster(team, assigned):
    return team | (not assigned) << 4


def isVehicleValid(vehDescr, vehAmmo, limits):
    if vehDescr.type.compactDescr in limits[b'forbiddenVehicles']:
        return (
         False, b'limits/tags')
    minLevel, maxLevel = limits[b'level']
    classLevelLimits = limits[b'classLevel']
    for classTag in VEHICLE_CLASSES:
        if classTag not in vehDescr.type.tags:
            continue
        if classTag in classLevelLimits:
            classMinLevel, classMaxLevel = classLevelLimits[classTag]
            if not classMinLevel <= vehDescr.level <= classMaxLevel:
                return (False, b'limits/classLevel')
        elif not minLevel <= vehDescr.level <= maxLevel:
            return (False, b'limits/level')

    classesLimits = limits[b'classes']
    if classesLimits is not None:
        for classTag in VEHICLE_CLASSES:
            if classTag in vehDescr.type.tags and classTag not in classesLimits:
                return (False, b'limits/classes')

    nationLimits = limits[b'nations']
    if nationLimits is not None and nations.NAMES[vehDescr.type.id[0]] not in nationLimits:
        return (False, b'limits/nations')
    else:
        vehTypeCompDescr = vehDescr.type.compactDescr
        vehicleLimits = limits[b'vehicles']
        if vehicleLimits is not None and vehTypeCompDescr not in vehicleLimits:
            return (False, b'limits/vehicles')
        componentLimits = limits[b'components'].get(vehTypeCompDescr, None)
        if componentLimits is not None:
            isValid, components = componentLimits
            for compDescr in _collectCurrentReplaceableVehicleComponents(vehDescr):
                if isValid and compDescr not in components:
                    return (False, b'limits/components')
                if not isValid and compDescr in components:
                    return (False, b'limits/components')

        ammoLimits = limits[b'ammo']
        if ammoLimits is not None:
            isValid, ammoSet = ammoLimits
            for compDescr, count in AmmoIterator(vehAmmo):
                if compDescr == 0 or count == 0:
                    continue
                if isValid and compDescr not in ammoSet:
                    return (False, b'limits/ammo')
                if not isValid and compDescr in ammoSet:
                    return (False, b'limits/ammo')

        shellsLimits = limits[b'shells']
        if shellsLimits:
            for compDescr, count in AmmoIterator(vehAmmo):
                if compDescr == 0 or count == 0:
                    continue
                itemTypeIdx = vehicles.parseIntCompactDescr(compDescr)[0]
                if itemTypeIdx != ITEM_TYPES.shell:
                    continue
                if count > shellsLimits.get(compDescr, 65535):
                    return (False, b'limits/shells')

        tagsLimits = limits[b'tags']
        if tagsLimits is not None:
            isValid, tagSet = tagsLimits
            for tag in tagSet:
                if isValid and tag not in vehDescr.type.tags:
                    return (False, b'limits/tags')
                if not isValid and tag in vehDescr.type.tags:
                    return (False, b'limits/tags')

        return (
         True, None)


def isObserver(vehCompDescr):
    return bool(vehCompDescr) and b'observer' in vehicles.getVehicleType(vehCompDescr).tags


def isTeamValid(accountsInfo, limits):
    minLevel, maxLevel = limits[b'level']
    tagsLimits = limits[b'tags']
    count = 0
    totalLevel = 0
    observerCount = 0
    vehs = {}
    for accInfo in accountsInfo.itervalues():
        if not accInfo[b'state'] & PREBATTLE_ACCOUNT_STATE.READY:
            continue
        if b'vehTypeCompDescr' not in accInfo or b'vehLevel' not in accInfo:
            vehDescr = vehicles.VehicleDescr(compactDescr=accInfo[b'vehCompDescr'])
            vehLevel = vehDescr.level
            vehTypeCompDescr = vehDescr.type.compactDescr
        else:
            vehLevel = accInfo[b'vehLevel']
            vehTypeCompDescr = accInfo[b'vehTypeCompDescr']
        if not minLevel <= vehLevel <= maxLevel:
            return (False, b'limits/level')
        vehTags = vehicles.getVehicleType(vehTypeCompDescr).tags
        if tagsLimits is not None:
            isValid, tagSet = tagsLimits
            for tag in tagSet:
                if isValid and tag not in vehTags:
                    return (False, b'limits/tags')
                if not isValid and tag in vehTags:
                    return (False, b'limits/tags')

        count += 1
        observerCount += int(b'observer' in vehTags)
        totalLevel += vehLevel
        vehs[vehTypeCompDescr] = vehs.get(vehTypeCompDescr, 0) + 1

    if count < limits[b'minCount']:
        return (False, b'limit/minCount')
    else:
        if observerCount > 0 and count == observerCount:
            if not IS_DEVELOPMENT:
                return (False, b'limit/observerVehicles')
            LOG_DEBUG(b'Ignoring limit for observers in development mode.')
        minTotalLevel, maxTotalLevel = limits[b'totalLevel']
        if not minTotalLevel <= totalLevel <= maxTotalLevel:
            return (False, b'limit/totalLevel')
        vehicleLimits = limits[b'vehicles']
        if vehicleLimits is not None:
            for vehTypeCompDescr, (minCount, maxCount) in vehicleLimits.iteritems():
                count = vehs.get(vehTypeCompDescr, 0)
                if not minCount <= count <= maxCount:
                    return (False, b'limits/vehicles')

        return (
         True, b'')


class PrebattleSettings(object):

    def __init__(self, settings):
        self.__settings = settings
        return

    def __getitem__(self, key):
        if key in self.__settings:
            return self.__settings[key]
        return SETTING_DEFAULTS[key]

    def __setitem__(self, key, value):
        self.__settings[key] = value
        return

    def getTeamLimits(self, team):
        return TeamLimits(self.__settings, team)


class TeamLimits(object):

    def __init__(self, settings, team):
        self.__limits = settings[b'limits']
        self.__team = team
        return

    def __getitem__(self, key):
        if key in self.__limits.get(self.__team, {}):
            return self.__limits[self.__team][key]
        if key in self.__limits.get(0, {}):
            return self.__limits[0][key]
        return LIMIT_DEFAULTS[key]


SETTING_DEFAULTS = {b'ver': 1, 
   b'arenaGuiType': (ARENA_GUI_TYPE.UNKNOWN), 
   b'roles': {}, b'clanRoles': {}, b'teamRoles': {1: (PREBATTLE_ROLE.SEE_1), 2: (PREBATTLE_ROLE.SEE_2)}, b'hideNames': False, 
   b'hideVehicles': False, 
   b'hideOpponentCount': False, 
   b'concealFinalRoster': False, 
   b'initialRosters': ({}, {}), b'defaultRoster': 1, 
   b'accountsToInvite': [], b'clansToInvite': [], b'creator': b'', 
   b'creatorBadges': (BadgesCommon.selectedBadgesEmpty()), 
   b'creatorClanDBID': 0, 
   b'creatorClanAbbrev': b'', 
   b'creatorIGRType': (IGR_TYPE.NONE), 
   b'creatorDBID': 0, 
   b'creatorAttrs': 0, 
   b'isOpened': False, 
   b'battlesLimit': 0, 
   b'winsLimit': 0, 
   b'winnerIfDraw': 0, 
   b'switchBattleTeams': False, 
   b'lifeTime': 0, 
   b'destroyIfCreatorOut': True, 
   b'startTime': 0, 
   b'startIfReady': True, 
   b'timeBetweenBattles': 0, 
   b'arenaTypeID': None, 
   b'roundLength': None, 
   b'comment': b'', 
   b'chatChannels': 1, 
   b'arenaVoipChannels': 0, 
   b'notifyWeb': False, 
   b'extraData': {}, b'gameplaysMask': 0, 
   b'vehicleLockMode': 0, 
   b'clanRentedVehicleLockMode': 0, 
   b'vehicleLockTimeFactors': {}, b'observeBothTeams': True, 
   b'numGroupsPerTeam': 0, 
   b'playerGroupLimit': 0, 
   b'tournamentArenasTypeIDs': [], b'clanRankRoles': {1: {}, 2: {}}}
LIMIT_DEFAULTS = {b'maxCountTotal': 256, 
   b'minCount': 1, 
   b'maxCount': (0, 65535), 
   b'totalLevel': (0, 65535), 
   b'level': (0, 65535), 
   b'classLevel': {}, b'classes': None, 
   b'vehicles': None, 
   b'components': {}, b'ammo': None, 
   b'shells': {}, b'tags': None, 
   b'nations': None, 
   b'forbiddenVehicles': (set())}

def _collectCurrentReplaceableVehicleComponents(vehicleDescr):
    res = []
    vehicleType = vehicleDescr.type
    if len(vehicleType.chassis) > 1:
        res.append(vehicleDescr.chassis.compactDescr)
    if len(vehicleType.engines) > 1:
        res.append(vehicleDescr.engine.compactDescr)
    if len(vehicleType.radios) > 1:
        res.append(vehicleDescr.radio.compactDescr)
    for posIdx, (turretDescr, gunDescr) in enumerate(vehicleDescr.turrets):
        if len(vehicleType.turrets[posIdx]) > 1:
            res.append(turretDescr.compactDescr)
        if len(turretDescr.guns) > 1:
            res.append(gunDescr.compactDescr)

    return res


def getClanWarsExtraEquipments(clansEquipments, joinedAccountsDBIDs, prebattleID):
    cache = vehicles.g_cache
    equipmentIDs = cache.equipmentIDs()
    equipments = cache.equipments()
    extraEquipments = {}
    for team, info in clansEquipments.iteritems():
        accountDBIDs = filter((lambda dbID: dbID in joinedAccountsDBIDs), info[b'top_leaders'])
        if accountDBIDs:
            extraEquipments[accountDBIDs[0]] = {b'prebattleID': prebattleID, b'clanDBID': 0, 
               b'rev': 0, 
               b'equipments': [equipments[equipmentIDs[equipmentName]].compactDescr for equipmentName in info[b'equipments']]}

    return extraEquipments
