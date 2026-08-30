import os
from realm_utils import ResMgr
from constants import IS_BOT, IS_WEB, IS_CLIENT, ARENA_TYPE_XML_PATH
from constants import ARENA_BONUS_TYPE_IDS, ARENA_GAMEPLAY_IDS, ARENA_GAMEPLAY_NAMES, TEAMS_IN_ARENA, HAS_DEV_RESOURCES, MinimapLayerType
from constants import IS_CELLAPP, IS_BASEAPP
from constants import CHAT_COMMAND_FLAGS
from constants import FRONTLINE_PROGRESSION
from coordinate_system import AXIS_ALIGNED_DIRECTION
from items.vehicles import CAMOUFLAGE_KINDS
from debug_utils import LOG_CURRENT_EXCEPTION
from items import _xml
from soft_exception import SoftException
from collections import defaultdict
from data_structures import DictObj
from visual_script.misc import ASPECT, VisualScriptTag, readVisualScriptPlanParams, readVisualScriptPlans
from SpaceVisibilityFlags import SpaceVisibilityFlagsFactory, SpaceVisibilityFlags
from Math import Vector2
import typing
if typing.TYPE_CHECKING:
    from typing import Dict, Set
if IS_CLIENT:
    from helpers import i18n
    import WWISE
elif IS_WEB:
    from web_stubs import *
if IS_CELLAPP or IS_BASEAPP:
    from server_constants import ARENA_ESTIMATED_LOAD_DEFAULT
g_cache = {}
g_geometryCache = {}
g_spaceCache = {}
g_geometryNamesToIDs = {}
g_geometryNamesToGameplayNames = {}
g_gameplayNames = set()
g_gameplaysMask = 0

def getVisibilityMask(typeID):
    global g_spaceCache
    gameplayID, geometryID = parseTypeID(typeID)
    return g_spaceCache[geometryID][SpaceVisibilityFlags.FLAGS_CONFIG_SECTION].getMaskForGameplayID(gameplayID)


def getCompositeVisibilityMask(geometryID, gameplayIDs):
    return g_spaceCache[geometryID][SpaceVisibilityFlags.FLAGS_CONFIG_SECTION].getMaskForGameplayIDs(gameplayIDs)


def getGameplaysMask(gameplayNames):
    return sum([1 << ARENA_GAMEPLAY_IDS[name] for name in set(gameplayNames)])


def getGameplayIDsForMask(gameplaysMask):
    return [gameplayID for gameplayID in xrange(len(ARENA_GAMEPLAY_NAMES)) if bool(gameplaysMask & 1 << gameplayID)]


def getGameplayName(gameplayID):
    return ARENA_GAMEPLAY_NAMES[gameplayID]


def getGameplayIDForName(gameplayName):
    return ARENA_GAMEPLAY_IDS[gameplayName]


def parseTypeID(typeID):
    return (
     typeID >> 16, typeID & 65535)


def buildArenaTypeID(gameplayID, geometryID):
    return geometryID | gameplayID << 16


_LIST_XML = ARENA_TYPE_XML_PATH + b'_list_.xml'
_DEFAULT_XML = ARENA_TYPE_XML_PATH + b'_default_.xml'

def init(isFullCache=True):
    global g_cache
    global g_gameplayNames
    global g_gameplaysMask
    global g_geometryNamesToGameplayNames
    global g_geometryNamesToIDs
    rootSection = ResMgr.openSection(_LIST_XML)
    if rootSection is None:
        raise SoftException(b"Can't open '%s'" % _LIST_XML)
    defaultXml = ResMgr.openSection(_DEFAULT_XML)
    if defaultXml is None:
        raise SoftException(b"Can't open '%s'" % _DEFAULT_XML)
    defaultGameplayTypesXml = defaultXml[b'gameplayTypes']
    if defaultGameplayTypesXml is None or not defaultGameplayTypesXml:
        raise SoftException(b"No defaults for 'gameplayTypes'")
    geometriesSet = set()
    for key, value in rootSection.items():
        isDevelopmentArena = value.readBool(b'isDevelopment')
        geometryID = value.readInt(b'id')
        if geometryID in geometriesSet:
            raise SoftException(b'Geometry ID=%d is not unique' % geometryID)
        buildResult = __buildCache(geometryID, value.readString(b'name'), defaultXml, isFullCache, isDevelopmentArena)
        if buildResult:
            geometriesSet.add(geometryID)

    ResMgr.purge(_LIST_XML, True)
    ResMgr.purge(_DEFAULT_XML, True)
    g_gameplaysMask = getGameplaysMask(g_gameplayNames)
    g_geometryNamesToIDs = {arenaType.geometryName: arenaType.geometryID for arenaType in g_cache.itervalues()}
    for arenaType in g_cache.itervalues():
        g_geometryNamesToGameplayNames.setdefault(arenaType.geometryName, set()).add(arenaType.gameplayName)

    return


class _BonusTypeOverridesMixin(object):

    def __init__(self):
        self._bonusType = None
        self.__bonusTypeCfg = {}
        return

    def __getattr__(self, name):
        if self._bonusType is not None:
            return self.__bonusTypeCfg.get(self._bonusType, {}).get(name)
        else:
            return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._bonusType = None
        return

    def useBonusTypeOverrides(self, bonusType=None):
        self._bonusType = bonusType
        return self

    def setBonusTypeCfg(self, cfg):
        if self._bonusType is None:
            return
        else:
            if not cfg:
                return
            self.__bonusTypeCfg[self._bonusType] = cfg
            return


class ArenaType(_BonusTypeOverridesMixin):

    def __init__(self, geometryCfg, gameplayCfg):
        super(ArenaType, self).__init__()
        if isinstance(geometryCfg, GeometryType):
            self.__geometryType = geometryCfg
        else:
            self.__geometryType = GeometryType(geometryCfg)
        self.__gameplayCfg = gameplayCfg
        self.__gameplayCfg[b'id'] = gameplayCfg[b'gameplayID'] << 16 | self.__geometryType.geometryID
        if self.maxPlayersInTeam < self.minPlayersInTeam:
            raise SoftException(b"'maxPlayersInTeam' value < 'minPlayersInTeam' value")
        return

    def __getattr__(self, name):
        value = super(ArenaType, self).__getattr__(name)
        if value is not None:
            return value
        else:
            if name in self.__gameplayCfg:
                return self.__gameplayCfg[name]
            with self.__geometryType.useBonusTypeOverrides(self._bonusType) as geometryTypeForBonus:
                return getattr(geometryTypeForBonus, name, None)
            return


class GeometryType(_BonusTypeOverridesMixin):

    def __init__(self, cfg):
        super(GeometryType, self).__init__()
        self.__cfg = cfg
        return

    def __getattr__(self, name):
        value = super(GeometryType, self).__getattr__(name)
        if value is not None:
            return value
        else:
            return self.__cfg.get(name)


class _DroneSettingHolder(object):

    def __init__(self):
        super(_DroneSettingHolder, self).__init__()
        self.__defaultValue = None
        self.__specificValues = {}
        return

    def setValue(self, arenaTypeLabel, value):
        self.__specificValues[arenaTypeLabel] = value
        return self

    def getValue(self, arenaTypeLabel):
        value = self.__specificValues.get(arenaTypeLabel)
        if value is not None:
            return value
        else:
            return self.__defaultValue

    def setDefault(self, value):
        self.__defaultValue = value
        return self

    def getDefault(self):
        return self.__defaultValue

    def getSpecificItemsCount(self):
        return len(self.__specificValues)

    def __getitem__(self, key):
        return self.getValue(key)


def __buildCache(geometryID, geometryName, defaultXml, isFullCache, isDevelopmentArena=False):
    global g_geometryCache
    sectionName = ARENA_TYPE_XML_PATH + geometryName + b'.xml'
    section = ResMgr.openSection(sectionName)
    if section is None:
        if isDevelopmentArena:
            return False
        raise SoftException(b"Can't open '%s'" % sectionName)
    geometryCfg = __readGeometryCfg(geometryID, geometryName, section, defaultXml)
    geometryType = __addBonusTypeOverrides(GeometryType(geometryCfg), section, defaultXml)
    g_geometryCache[geometryID] = geometryType
    if isFullCache:
        spaceName = os.path.basename(geometryCfg[b'geometry'])
        spaceData = __readSpaceCfg(spaceName)
        g_spaceCache[geometryID] = spaceData
    for gameplayCfg in __readGameplayCfgs(geometryName, section, defaultXml, geometryCfg):
        arenaType = ArenaType(geometryType, gameplayCfg)
        g_cache[arenaType.id] = arenaType
        g_gameplayNames.add(arenaType.gameplayName)

    ResMgr.purge(sectionName, True)
    return True


def __addBonusTypeOverrides(overridable, section, defaultXml):
    for bonusTypeID, bonusType in ARENA_BONUS_TYPE_IDS.iteritems():
        with overridable.useBonusTypeOverrides(bonusTypeID) as overriden:
            bonusTypeCfg = __readBonusTypeCfgs(overridable.geometryName, section, defaultXml, bonusType)
            overriden.setBonusTypeCfg(bonusTypeCfg)

    return overridable


def __readBonusTypeCfgs(geometryName, section, defaultXml, bonusType):
    arenaOverrides = __getBonusTypeOverrides(section, bonusType)
    defaultOverrides = __getBonusTypeOverrides(defaultXml, bonusType)
    arenaOverrides = arenaOverrides or defaultOverrides
    defaultOverrides = defaultOverrides or arenaOverrides
    if not arenaOverrides:
        return None
    else:
        try:
            cfg = {}
            if (IS_CELLAPP or IS_BASEAPP) and __hasKey(b'estimatedLoad', arenaOverrides, defaultOverrides):
                cfg[b'estimatedLoad'] = _readFloat(b'estimatedLoad', arenaOverrides, defaultOverrides)
            if __hasKey(b'maxPlayersInTeam', arenaOverrides, defaultOverrides):
                cfg[b'maxPlayersInTeam'] = __readMaxPlayersInTeam(arenaOverrides, defaultOverrides)
            if __hasKey(b'runDelay', arenaOverrides, defaultOverrides):
                cfg[b'runDelay'] = _readInt(b'runDelay', arenaOverrides, defaultOverrides)
            if __hasKey(b'runDelayDev', arenaOverrides, defaultOverrides):
                cfg[b'runDelayDev'] = _readInt(b'runDelayDev', arenaOverrides, defaultOverrides)
        except Exception as e:
            LOG_CURRENT_EXCEPTION()
            raise SoftException(b"wrong %s bonusTypeOverrides section '%s' : %s" % (geometryName, bonusType, e))

        return cfg


def __getBonusTypeOverrides(Xml, bonusType):
    Overrides = Xml[b'bonusTypeOverrides']
    if Overrides:
        return Overrides[bonusType]
    else:
        return
        return


def __readGeometryCfg(geometryID, geometryName, section, defaultXml):
    try:
        cfg = {}
        cfg[b'geometryID'] = geometryID
        cfg[b'geometryName'] = geometryName
        cfg[b'geometry'] = _readString(b'geometry', section, defaultXml)
        cfg[b'boundingBox'] = _readBoundingBox(section)
        cfg[b'spaceBoundingBox'] = __calcSpaceBoundingBox(cfg[b'boundingBox'])
        cfg[b'weatherPresets'] = __readWeatherPresets(section)
        cfg[b'vehicleCamouflageKind'] = __readVehicleCamouflageKind(section)
        cfg[b'isDevelopment'] = __readBool(b'isDevelopment', section, defaultXml, False)
        if IS_CELLAPP or IS_BASEAPP:
            cfg[b'estimatedLoad'] = _readFloat(b'estimatedLoad', section, defaultXml, ARENA_ESTIMATED_LOAD_DEFAULT)
        if IS_CLIENT or IS_WEB:
            cfg[b'name'] = i18n.makeString(_readString(b'name', section, defaultXml))
        if IS_CLIENT:
            cfg[b'umbraEnabled'] = _readInt(b'umbraEnabled', section, defaultXml)
            cfg[b'defaultReverbPreset'] = _readString(b'defaultReverbPreset', section, defaultXml).strip()
            cfg[b'batchingEnabled'] = _readInt(b'batchingEnabled', section, defaultXml)
            cfg[b'waterTexScale'] = section.readFloat(b'water/texScale', 0.5)
            cfg[b'waterFreqX'] = section.readFloat(b'water/freqX', 1.0)
            cfg[b'waterFreqZ'] = section.readFloat(b'water/freqZ', 1.0)
            cfg[b'defaultGroundEffect'] = __readDefaultGroundEffect(section, defaultXml)
        cfg.update(__readCommonCfg(section, defaultXml, True, {}))
    except Exception as e:
        LOG_CURRENT_EXCEPTION()
        raise SoftException(b"Wrong arena type XML '%s' : %s" % (geometryName, str(e)))

    return cfg


def __readGameplayCfgs(geometryName, section, defaultXml, geometryCfg):
    try:
        if section[b'gameplayTypes'] is None:
            gameplayName = b'ctf'
            gameplayID = getGameplayIDForName(gameplayName)
            return [
             {b'gameplayID': gameplayID, 
                b'gameplayName': gameplayName}]
        if not section[b'gameplayTypes']:
            raise SoftException(b"no 'gameplayTypes' section")
        cfgs = []
        defaultGameplayTypesXml = defaultXml[b'gameplayTypes']
        for name, subsection in section[b'gameplayTypes'].items():
            defaultSubsection = defaultGameplayTypesXml[name]
            if defaultSubsection is None:
                raise SoftException(b"no defaults for '%s'" % name)
            gameplayCfg = __readGameplayCfg(name, subsection, defaultSubsection, geometryCfg)
            if IS_CLIENT:
                wwmusicDroneSetup = b'wwmusicDroneSetup'
                gameplayCfg[wwmusicDroneSetup] = __readWWmusicDroneSection(wwmusicDroneSetup, section, defaultXml, name)
            cfgs.append(gameplayCfg)

    except Exception as e:
        LOG_CURRENT_EXCEPTION()
        raise SoftException(b"Wrong arena type XML '%s' : %s" % (geometryName, e))

    return cfgs


def __readGameplayCfg(gameplayName, section, defaultXml, geometryCfg):
    try:
        cfg = {}
        cfg[b'gameplayID'] = getGameplayIDForName(gameplayName)
        cfg[b'gameplayName'] = gameplayName
        for setting in (b'battleEndWarningAppearTime', b'battleEndWarningDuration', b'battleEndingSoonTime', b'battleEndWarningExtraAppearTime'):
            cfg[setting] = 0
            if not gameplayName.startswith(b'fallout') and __hasKey(setting, section, defaultXml):
                cfg[setting] = _readInt(setting, section, defaultXml)

        if gameplayName == b'nations':
            raise SoftException(b'national battles are disabled')
        notificationsRemapping = __readNotificationsRemappingSection(section, defaultXml)
        if notificationsRemapping is not None:
            cfg[b'notificationsRemapping'] = notificationsRemapping
        cfg.update(__readCommonCfg(section, defaultXml, False, geometryCfg))
    except Exception as e:
        LOG_CURRENT_EXCEPTION()
        raise SoftException(b"wrong gameplay section '%s' : %s" % (gameplayName, e))

    return cfg


def __readCommonCfg(section, defaultXml, raiseIfMissing, geometryCfg):
    cfg = {}
    if raiseIfMissing or __hasKey(b'explicitRequestOnly', section, defaultXml):
        cfg[b'explicitRequestOnly'] = __readBool(b'explicitRequestOnly', section, defaultXml)
    if raiseIfMissing or __hasKey(b'minPlayersInTeam', section, defaultXml):
        cfg[b'minPlayersInTeam'] = __readMinPlayersInTeam(section, defaultXml)
    if raiseIfMissing or __hasKey(b'maxPlayersInTeam', section, defaultXml):
        cfg[b'maxPlayersInTeam'] = __readMaxPlayersInTeam(section, defaultXml)
    if raiseIfMissing or __hasKey(b'maxTeamsInArena', section, defaultXml):
        cfg[b'maxTeamsInArena'] = __readTeamsCount(b'maxTeamsInArena', section, defaultXml)
    if raiseIfMissing or __hasKey(b'minTeamsInArena', section, defaultXml):
        cfg[b'minTeamsInArena'] = __readTeamsCount(b'minTeamsInArena', section, defaultXml)
    if raiseIfMissing or __hasKey(b'runDelay', section, defaultXml):
        cfg[b'runDelay'] = _readInt(b'runDelay', section, defaultXml)
    if raiseIfMissing or __hasKey(b'runDelayDev', section, defaultXml):
        cfg[b'runDelayDev'] = _readInt(b'runDelayDev', section, defaultXml)
    if raiseIfMissing or __hasKey(b'roundLength', section, defaultXml):
        cfg[b'roundLength'] = _readInt(b'roundLength', section, defaultXml)
    if raiseIfMissing or __hasKey(b'winnerIfTimeout', section, defaultXml):
        cfg[b'winnerIfTimeout'] = _readInt(b'winnerIfTimeout', section, defaultXml)
    if raiseIfMissing or __hasKey(b'winnerIfExtermination', section, defaultXml):
        cfg[b'winnerIfExtermination'] = _readInt(b'winnerIfExtermination', section, defaultXml)
    if raiseIfMissing or __hasKey(b'artilleryPreparationChance', section, defaultXml):
        cfg[b'artilleryPreparationChance'] = _readFloat(b'artilleryPreparationChance', section, defaultXml)
    if raiseIfMissing or section.has_key(b'mapActivities'):
        cfg[b'mapActivitiesTimeframes'] = __readMapActivitiesTimeframes(section)
    if raiseIfMissing or section.has_key(b'boundingBox'):
        cfg[b'boundingBox'] = _readBoundingBox(section)
    maxTeamsInArena = cfg.get(b'maxTeamsInArena', geometryCfg.get(b'maxTeamsInArena', None))
    cfg.update(__readWinPoints(section))
    cfg.update(__readGameplayPoints(section, geometryCfg))
    cfg[b'teamBasePositions'] = __readTeamBasePositions(section, maxTeamsInArena)
    cfg[b'teamSpawnPoints'] = __readTeamSpawnPoints(section, maxTeamsInArena)
    cfg[b'squadTeamNumbers'], cfg[b'soloTeamNumbers'] = __readTeamNumbers(section, maxTeamsInArena)
    cfg[VisualScriptTag] = _readVisualScript(section)
    if raiseIfMissing or __hasKey(b'numPlayerGroups', section, defaultXml):
        cfg[b'numPlayerGroups'] = _readInt(b'numPlayerGroups', section, defaultXml, 0)
    if raiseIfMissing or __hasKey(b'playerGroupLimit', section, defaultXml):
        cfg[b'playerGroupLimit'] = _readInt(b'playerGroupLimit', section, defaultXml, 0)
    if raiseIfMissing or __hasKey(b'respawnType', section, defaultXml):
        cfg[b'respawnType'] = _readString(b'respawnType', section, defaultXml, b'')
    if raiseIfMissing or __hasKey(b'unlockUnusedVehiclesOnLeave', section, defaultXml):
        cfg[b'unlockUnusedVehiclesOnLeave'] = __readBool(b'unlockUnusedVehiclesOnLeave', section, defaultXml, False)
    if raiseIfMissing or __hasKey(b'numDestructiblesToDestroyForWin', section, defaultXml):
        cfg[b'numDestructiblesToDestroyForWin'] = _readInt(b'numDestructiblesToDestroyForWin', section, defaultXml, 0)
    if raiseIfMissing or __hasKey(b'addGameTimePerDestructible', section, defaultXml):
        cfg[b'addGameTimePerDestructible'] = _readFloat(b'addGameTimePerDestructible', section, defaultXml, 0.0)
    if __hasKey(b'sectorSettings', section, defaultXml):
        cfg[b'sectorSettings'] = SectorSettings(b'sectorSettings', section, defaultXml)
    if __hasKey(b'epicSectorSettings', section, defaultXml):
        cfg[b'epicSectorSettings'] = EpicSectorSettings(b'epicSectorSettings', section, defaultXml)
    if __hasKey(b'epicSectorGrid', section, defaultXml):
        cfg[b'epicSectorGrid'] = EpicSectorGrid(b'epicSectorGrid', section, defaultXml)
    if __hasKey(b'frontLinesAlgorithm', section, defaultXml):
        cfg[b'frontLinesAlgorithm'] = FrontLinesAlgorithmSettings(section, defaultXml)
    if __hasKey(b'frontLinesGeometry', section, defaultXml):
        cfg[b'frontLinesGeometry'] = FrontLinesGeometrySettings(section, defaultXml)
    if __hasKey(b'recoveryMechanic', section, defaultXml):
        cfg[b'recoveryMechanic'] = RecoveryMechanicSettings(section, defaultXml)
    if __hasKey(b'overtimeMechanic', section, defaultXml):
        cfg[b'overtimeMechanic'] = OvertimeMechanicSettings(section, defaultXml)
    if raiseIfMissing or __hasKey(b'capturePointsLimit', section, defaultXml):
        cfg[b'capturePointsLimit'] = _readInt(b'capturePointsLimit', section, defaultXml, -1)
    if raiseIfMissing or __hasKey(b'defencePointsLimit', section, defaultXml):
        cfg[b'defencePointsLimit'] = _readInt(b'defencePointsLimit', section, defaultXml, -1)
    if raiseIfMissing or __hasKey(b'ironShieldDefenderTeam', section, defaultXml):
        cfg[b'ironShieldDefenderTeam'] = _readInt(b'ironShieldDefenderTeam', section, defaultXml, 0)
    if raiseIfMissing or __hasKey(b'defenderBonusTeam', section, defaultXml):
        cfg[b'defenderBonusTeam'] = _readInt(b'defenderBonusTeam', section, defaultXml, 0)
    if raiseIfMissing or __hasKey(b'defenderBonusInterval', section, defaultXml):
        cfg[b'defenderBonusInterval'] = _readInt(b'defenderBonusInterval', section, defaultXml, 0)
    if raiseIfMissing or __hasKey(b'enabledChatCommandFlags', section, defaultXml):
        cfg[b'enabledChatCommandFlags'] = __readChatCommandFlags(b'enabledChatCommandFlags', section, defaultXml)
    if __hasKey(b'recon', section, defaultXml):
        cfg[b'recon'] = ReconSettings(section[b'recon'])
    if raiseIfMissing or __hasKey(b'resetLocalTeamKillerAtRespawn', section, defaultXml):
        cfg[b'resetLocalTeamKillerAtRespawn'] = __readBool(b'resetLocalTeamKillerAtRespawn', section, defaultXml)
    if raiseIfMissing or __hasKey(b'stopVehiclesAtArenaFreeze', section, defaultXml):
        cfg[b'stopVehiclesAtArenaFreeze'] = __readBool(b'stopVehiclesAtArenaFreeze', section, defaultXml, False)
    if raiseIfMissing or __hasKey(b'leaveDisconnectedTimeout', section, defaultXml):
        cfg[b'leaveDisconnectedTimeout'] = _readInt(b'leaveDisconnectedTimeout', section, defaultXml, -1)
    if IS_CLIENT or IS_WEB:
        if raiseIfMissing or __hasKey(b'description', section, defaultXml):
            cfg[b'description'] = i18n.makeString(_readString(b'description', section, defaultXml))
        if raiseIfMissing or __hasKey(b'minimap', section, defaultXml):
            cfg[b'minimap'] = _readString(b'minimap', section, defaultXml)
        if section.has_key(b'minimapLayers'):
            result = {}
            for item in section[b'minimapLayers'].values():
                layerId = item.readString(b'layerId')
                path = item.readString(b'path')
                layerType = item.readString(b'layerType')
                result[layerId] = (
                 path, layerType)

            cfg[b'minimapLayers'] = result
        if __hasKey(b'overviewmap', section, defaultXml):
            cfg[b'overviewmap'] = _readString(b'overviewmap', section, defaultXml)
        if raiseIfMissing or __hasKey(b'wwambientSound', section, defaultXml):
            cfg[b'ambientSound'] = _readString(b'wwambientSound', section, defaultXml)
        musicSetup = None
        if raiseIfMissing or __hasKey(b'wwmusicSetup', section, defaultXml):
            musicSetup = __readWWmusicSection(section, defaultXml)
        if musicSetup is not None:
            cfg[b'wwmusicSetup'] = musicSetup
        if raiseIfMissing or __hasKey(b'wwbattleCountdownTimerSound', section, defaultXml):
            cfg[b'battleCountdownTimerSound'] = _readString(b'wwbattleCountdownTimerSound', section, defaultXml)
        if raiseIfMissing or section.has_key(b'mapActivities'):
            cfg[b'mapActivitiesSection'] = section[b'mapActivities']
        if section.has_key(b'soundRemapping'):
            cfg[b'soundRemapping'] = section[b'soundRemapping']
    if IS_CLIENT or IS_BOT:
        cfg[b'controlPoints'] = __readControlPoints(section)
        cfg[b'teamLowLevelSpawnPoints'] = __readTeamSpawnPoints(section, maxTeamsInArena, nodeNameTemplate=b'team%d_low', required=False)
        cfg[b'botPoints'] = __readBotPoints(section)
        cfg[b'pointsOfInterest'] = __readPointsOfInterest(section)
        if raiseIfMissing or __hasKey(b'soundNotificationsPlan', section, defaultXml):
            cfg[b'soundNotificationsPlan'] = _readString(b'soundNotificationsPlan', section, defaultXml)
        if raiseIfMissing or __hasKey(b'soundNotificationsContext', section, defaultXml):
            cfg[b'soundNotificationsContext'] = _readString(b'soundNotificationsContext', section, defaultXml)
    return cfg


def __readWWmusicSection(section, defaultXml):
    wwmusic = None
    if __hasKey(b'wwmusicSetup', section, defaultXml):
        wwmusic = {}
        dataSection = section if section.has_key(b'wwmusicSetup') else defaultXml
        for name, value in _xml.getChildren(defaultXml, dataSection, b'wwmusicSetup'):
            wwmusic[name] = value.asString

    return wwmusic


def __readNotificationsRemappingSection(section, defaultXml):
    notificationsRemapping = None
    if __hasKey(b'notificationsRemapping', section, defaultXml):
        notificationsRemapping = {}
        dataSection = section if section.has_key(b'notificationsRemapping') else defaultXml
        for _, event in _xml.getChildren(defaultXml, dataSection, b'notificationsRemapping'):
            notificationsRemapping[event[b'name'].asString] = event[b'mod'].asString if event.has_key(b'mod') else None

    return notificationsRemapping


def __readWWmusicDroneSection(wwmusicDroneSetup, section, defaultXml, gameplayName):
    if section.has_key(wwmusicDroneSetup):
        dataSection = section
    else:
        dataSection = defaultXml
    outcome = defaultdict(_DroneSettingHolder)
    droneChildren = sorted(_xml.getChildren(defaultXml, dataSection, wwmusicDroneSetup), key=(lambda item: len(item[1].items())))
    valueTag = b'value'
    for settingName, settingChildren in droneChildren:
        if settingChildren.has_key(valueTag):
            settingValue = settingChildren.readInt(valueTag)
            if settingChildren.has_key(b'arena_type_label'):
                if settingChildren.has_key(b'gameplay_name'):
                    if gameplayName == settingChildren.readString(b'gameplay_name'):
                        outcome[settingName].setValue(settingChildren.readString(b'arena_type_label'), settingValue)
                else:
                    outcome[settingName].setValue(settingChildren.readString(b'arena_type_label'), settingValue)
            elif settingChildren.has_key(b'gameplay_name'):
                if gameplayName == settingChildren.readString(b'gameplay_name'):
                    outcome[settingName].setDefault(settingValue)
            else:
                outcome[settingName].setDefault(settingValue)
        else:
            raise SoftException((b'"{}" section missed the key "{}"!').format(settingName, valueTag))

    return outcome


def __readSpaceCfg(geometryName):
    cfg = {}
    cfg[SpaceVisibilityFlags.FLAGS_CONFIG_SECTION] = SpaceVisibilityFlagsFactory.create(geometryName)
    return cfg


def __hasKey(key, xml, defaultXml):
    return xml.has_key(key) or defaultXml.has_key(key)


def _readString(key, xml, defaultXml, defaultValue=None):
    if xml.has_key(key):
        return xml.readString(key)
    else:
        if defaultXml.has_key(key):
            return defaultXml.readString(key)
        if defaultValue is not None:
            return defaultValue
        raise SoftException(b"missing key '%s'" % key)
        return


def __readStrings(key, xml, defaultXml, defaultValue=None):
    if xml.has_key(key):
        return xml.readStrings(key)
    else:
        if defaultXml.has_key(key):
            return defaultXml.readStrings(key)
        if defaultValue is not None:
            return defaultValue
        raise SoftException(b"missing key '%s'" % key)
        return


def _readInt(key, xml, defaultXml, defaultValue=None):
    if xml.has_key(key):
        return xml.readInt(key)
    else:
        if defaultXml.has_key(key):
            return defaultXml.readInt(key)
        if defaultValue is not None:
            return defaultValue
        raise SoftException(b"missing key '%s'" % key)
        return


def _readFloat(key, xml, defaultXml, defaultValue=None):
    if xml.has_key(key):
        return xml.readFloat(key)
    else:
        if defaultXml.has_key(key):
            return defaultXml.readFloat(key)
        if defaultValue is not None:
            return defaultValue
        raise SoftException(b"missing key '%s'" % key)
        return


def __readBool(key, xml, defaultXml, defaultValue=None):
    if xml.has_key(key):
        return xml.readBool(key)
    else:
        if defaultXml.has_key(key):
            return defaultXml.readBool(key)
        if defaultValue is not None:
            return defaultValue
        raise SoftException(b"missing key '%s'" % key)
        return


def _readFloatArray(key, tag, xml, defaultXml, defaultValue=None):
    if xml.has_key(key):
        return xml[key].readFloats(tag)
    else:
        if defaultXml.has_key(key):
            return defaultXml[key].readFloats(tag)
        if defaultValue is not None:
            return defaultValue
        raise SoftException(b"missing key '%s'" % key)
        return


def _readVisualScriptAspect(section, aspect, commonParams):
    plans = []
    if section.has_key(aspect):
        plans = readVisualScriptPlans(section[aspect], commonParams)
    return plans


def _readVisualScript(section):
    if section.has_key(VisualScriptTag):
        vseSection = section[VisualScriptTag]
        commonParams = {}
        if vseSection.has_key(b'common'):
            commonParams = readVisualScriptPlanParams(vseSection[b'common'])
        return {(ASPECT.CLIENT): (_readVisualScriptAspect(vseSection, ASPECT.CLIENT.lower(), commonParams)), (ASPECT.SERVER): (_readVisualScriptAspect(vseSection, ASPECT.SERVER.lower(), commonParams))}
    return {(ASPECT.CLIENT): [], (ASPECT.SERVER): []}


def _readBoundingBox(section):
    bottomLeft = section.readVector2(b'boundingBox/bottomLeft')
    upperRight = section.readVector2(b'boundingBox/upperRight')
    if bottomLeft[0] >= upperRight[0] or bottomLeft[1] >= upperRight[1]:
        raise SoftException(b"wrong 'boundingBox' values")
    return (
     bottomLeft, upperRight)


def __calcSpaceBoundingBox(arenaBoundingBox):
    ARENA_EXTENT = 100
    return (arenaBoundingBox[0] - Vector2(ARENA_EXTENT, ARENA_EXTENT),
     arenaBoundingBox[1] + Vector2(ARENA_EXTENT, ARENA_EXTENT))


def __readChatCommandFlags(name, section, defaultXml):
    if section.has_key(name):
        flagsAsWhitespaceSeparatedString = section.readString(name)
    else:
        flagsAsWhitespaceSeparatedString = defaultXml.readString(name)
    flagsAsListOfStrings = flagsAsWhitespaceSeparatedString.split()
    flagsAsListOfValues = [CHAT_COMMAND_FLAGS.FLAG_BY_NAME[flagStr] for flagStr in flagsAsListOfStrings]
    flagsMask = 0
    for flag in flagsAsListOfValues:
        flagsMask |= flag

    return flagsMask


class ReconSettings(object):

    def __init__(self, section):
        self.flyDirections = self._readXmlReconFlyDirections(section[b'flyDirections'])
        return

    def _readXmlReconFlyDirections(self, section):
        flyDirections = {}
        for name, value in section.items():
            if name == b'flyDirection':
                team = value.readInt(b'team')
                direction = value.readVector3(b'direction')
                flyDirections[team] = direction

        return flyDirections


class FrontLinesGeometrySettings(object):

    def __init__(self, section, defaultXml):
        dcfg = self._readXmlFronts(defaultXml[b'frontLinesGeometry'])
        cfg = self._readXmlFronts(section[b'frontLinesGeometry'])
        dcfg.update(cfg)
        self.fronts = dcfg
        return

    def _readXmlFronts(self, section):
        fronts = {}
        if section is not None:
            for name, value in section.items():
                if name == b'front':
                    playerGroup = value.readInt(b'playerGroup')
                    settings = dict(direction=value.readVector2(b'direction'), bounds=_readBoundingBox(value))
                    fronts[playerGroup] = DictObj(settings)

        return fronts


class FrontLinesAlgorithmSettings(object):

    def __init__(self, section, defaultXml):
        dcfg = self._readXmlSettings(defaultXml[b'frontLinesAlgorithm'])
        cfg = self._readXmlSettings(section[b'frontLinesAlgorithm'])
        dcfg.update(cfg)
        self.__dict__ = dcfg
        return

    def _readFloats(self, section, *names):
        return {name: section.readFloat(name) for name in names}

    def _readInts(self, section, *names):
        return {name: section.readInt(name) for name in names}

    def _readXmlSettings(self, section):
        settings = {}
        if section is not None:
            settings.update(self._readFloats(section, b'columnWidth', b'frontDropPerColumn', b'outlierFraction', b'outlierVerticalDistance', b'intrusionVerticalTolerance', b'intrusionCheckExtendBounds'))
            settings.update(self._readInts(section, b'defenderTeam', b'frontEdgeExtendColumns'))
        return settings


class RecoveryMechanicSettings(object):

    def __init__(self, section, defaultXml):
        dcfg = self._readXmlSettings(defaultXml[b'recoveryMechanic'])
        cfg = self._readXmlSettings(section[b'recoveryMechanic'])
        dcfg.update(cfg)
        self.__dict__ = dcfg
        return

    def _readInts(self, section, *names):
        return {name: section.readInt(name) for name in names}

    def _readXmlSettings(self, section):
        settings = {}
        if section is not None:
            settings.update(self._readInts(section, b'recoveryCounter', b'recoveryBlockingCounter'))
        return settings


class OvertimeMechanicSettings(object):

    def __init__(self, section, defaultXml):
        dcfg = self._readXmlSettings(defaultXml[b'overtimeMechanic'])
        cfg = self._readXmlSettings(section[b'overtimeMechanic'])
        dcfg.update(cfg)
        self.__dict__ = dcfg
        return

    def _readInts(self, section, *names):
        return {name: section.readInt(name) for name in names}

    def _readXmlSettings(self, section):
        settings = {}
        if section is not None:
            settings.update(self._readInts(section, b'overtimeLimit'))
        return settings


class SectorProtectionZoneSettings(object):

    def __init__(self, key, section, defaultXml):
        self.numberOfTurrets = _readInt(key + b'/numberOfTurrets', section, defaultXml, 2)
        self.maxStayTime = _readFloat(key + b'/maxStayTime', section, defaultXml, 5.0)
        self.minShootingTime = _readFloat(key + b'/minShootingTime', section, defaultXml, 15.0)
        self.minShootingInterval = _readFloat(key + b'/minShootingInterval', section, defaultXml, 1.0)
        self.shotShellNation = _readString(key + b'/shotShellNation', section, defaultXml, b'germany')
        self.shotShellName = _readString(key + b'/shotShellName', section, defaultXml, b'sector_artillery_shell')
        self.shotPiercingPower = _readFloat(key + b'/shotPiercingPower', section, defaultXml, 45.0)
        self.shotRadius = _readFloat(key + b'/shotRadius', section, defaultXml, 5.0)
        self.shotDuration = _readFloat(key + b'/shotDuration', section, defaultXml, 1.0)
        self.minTurretShootInterval = _readFloat(key + b'/minTurretShootInterval', section, defaultXml, 2.0)
        return


class SectorSettings(object):

    def __init__(self, key, section, defaultXml):
        self.transitionTime = _readFloat(key + b'/transitionTime', section, defaultXml, 60.0)
        self.maxStayTime = _readFloat(key + b'/maxStayTime', section, defaultXml, 30.0)
        self.destructionDuration = _readFloat(key + b'/destructionDuration', section, defaultXml, 5.0)
        self.closedZoneFireDelay = _readFloat(key + b'/closedZoneFireDelay', section, defaultXml, 4.0)
        self.numBombs = _readInt(key + b'/numBombs', section, defaultXml, 10)
        self.bombingHeight = _readFloat(key + b'/bombingHeight', section, defaultXml, 70.0)
        self.bombingWidth = _readFloat(key + b'/bombingWidth', section, defaultXml, 50.0)
        self.maxRandomBombsPerTarget = _readInt(key + b'/maxRandomBombsPerTarget', section, defaultXml, 3)
        self.bombShellNation = _readString(key + b'/bombShellNation', section, defaultXml, b'germany')
        self.bombShellName = _readString(key + b'/bombShellName', section, defaultXml, b'sector_bomber_shell')
        self.protectionZone = SectorProtectionZoneSettings(b'sectorSettings/protectionZone', section, defaultXml)
        return


class EpicSectorSettings(object):

    def __init__(self, key, section, defaultXml):
        addGameTimeString = _readString(key + b'/addGameTimePerCapture', section, defaultXml, b'')
        self.addGameTimePerCapture = [float(s) for s in addGameTimeString.split()]
        self.addGameTimeAllCaptured = _readFloat(key + b'/addGameTimeAllCaptured', section, defaultXml, 0.0)
        self.frontLineInit = _readFloat(key + b'/frontLineInit', section, defaultXml, 400.0)
        self.transitionFrontLineBoundBackward = _readFloat(key + b'/transitionFrontLineBoundBackward', section, defaultXml, 300.0)
        self.transitionFrontLineBoundForward = _readFloat(key + b'/transitionFrontLineBoundForward', section, defaultXml, 250.0)
        defenderMotivationFactorsString = _readString(key + b'/defenderMotivationFactors', section, defaultXml, b'')
        self.defenderMotivationFactors = [float(s) for s in defenderMotivationFactorsString.split()]
        self.overtimeMaxFrontlineOffset = _readFloat(key + b'/overtimeMaxFrontlineOffset', section, defaultXml, -600.0)
        return


class EpicSectorGrid(object):

    def __init__(self, key, section, defaultXml):
        mainDirectionName = section.readString(key + b'/mainDirection', b'-Z')
        self.mainDirection = AXIS_ALIGNED_DIRECTION.FROM_NAME[mainDirectionName]
        self.bordersZ = sorted(_readFloatArray(key + b'/bordersZ', b'border', section, defaultXml))
        self.bordersX = sorted(_readFloatArray(key + b'/bordersX', b'border', section, defaultXml))
        self.owningTeam = section.readInt(key + b'/owningTeam', 1)
        self.__validate()
        return

    def __validate(self):
        if self.mainDirection != FRONTLINE_PROGRESSION.DIRECTION:
            raise SoftException((b'Unsupported axis aligned direction. Expected: {}, in fact: {}.').format(FRONTLINE_PROGRESSION.DIRECTION, self.mainDirection))
        if len(self.bordersZ) != FRONTLINE_PROGRESSION.BORDERS_Z:
            raise SoftException((b'Unsupported borders size (Z order). Expected: {}, in fact: {}.').format(FRONTLINE_PROGRESSION.BORDERS_Z, self.bordersZ))
        if len(self.bordersX) != FRONTLINE_PROGRESSION.BORDERS_X:
            raise SoftException((b'Unsupported borders size (X order). Expected: {}, in fact: {}.').format(FRONTLINE_PROGRESSION.BORDERS_X, self.bordersX))
        return


def __readWeatherPresets(section):
    weatherXML = section[b'weather']
    if weatherXML is None or not weatherXML:
        return [{b'rnd_range': (0, 1)}]
    else:
        presets = []
        possibilitySum = 0
        for presetXML in weatherXML.values():
            preset = {}
            for key, valueXML in presetXML.items():
                preset[key] = valueXML.asString

            presets.append(preset)
            possibilitySum += presetXML.readFloat(b'possibility', 1.0)

        factor = 1 / possibilitySum
        prev_upper_limit = 0
        for preset in presets:
            possibility = float(preset.pop(b'possibility', 1.0))
            rnd_range = (prev_upper_limit, prev_upper_limit + possibility * factor)
            preset[b'rnd_range'] = rnd_range
            prev_upper_limit = rnd_range[1]

        return presets


def __readVehicleCamouflageKind(section):
    kindName = section.readString(b'vehicleCamouflageKind')
    kind = CAMOUFLAGE_KINDS.get(kindName)
    if kind is None:
        raise SoftException(b"missing or wrong section 'vehicleCamouflageKind'")
    return kind


def __readMinPlayersInTeam(section, defaultXml):
    minPlayersInTeam = _readInt(b'minPlayersInTeam', section, defaultXml)
    if minPlayersInTeam < 0:
        raise SoftException(b"wrong 'minPlayersInTeam' value")
    return minPlayersInTeam


def __readMaxPlayersInTeam(section, defaultXml):
    maxPlayersInTeam = _readInt(b'maxPlayersInTeam', section, defaultXml)
    if maxPlayersInTeam < 0:
        raise SoftException(b"wrong 'maxPlayersInTeam' value")
    return maxPlayersInTeam


def __readTeamsCount(key, section, defaultXml):
    value = _readInt(key, section, defaultXml)
    if not TEAMS_IN_ARENA.MIN_TEAMS <= value <= TEAMS_IN_ARENA.MAX_TEAMS:
        raise SoftException(b'Invalid teams in arena')
    return value


def __readTeamNumbers(section, maxTeamsInArena):
    if not (section.has_key(b'squadTeamNumbers') or section.has_key(b'soloTeamNumbers')):
        if maxTeamsInArena > 2:
            raise SoftException(b'For multiteam mode squadTeamNumbers and (or) soloTeamNumbers must be set')
        return (set(), set())
    squadTeamNumbers = set([int(v) for v in section.readString(b'squadTeamNumbers', b'').split()])
    soloTeamNumbers = set([int(v) for v in section.readString(b'soloTeamNumbers', b'').split()])
    if len(squadTeamNumbers) + len(soloTeamNumbers) != maxTeamsInArena:
        raise SoftException(b'Number of squad (%d) and solo (%d) teams must be equal to maxTeamsInArena (%d)' % (
         len(squadTeamNumbers), len(soloTeamNumbers), maxTeamsInArena))
    if len(squadTeamNumbers & soloTeamNumbers) > 0:
        raise SoftException(b'Squad and solo team numbers contains identical team numbers (%s)' % str(squadTeamNumbers & soloTeamNumbers))
    allTeamNumbers = squadTeamNumbers | soloTeamNumbers
    if min(allTeamNumbers) < 1 or max(allTeamNumbers) > TEAMS_IN_ARENA.MAX_TEAMS:
        raise SoftException(b'Invalid team number. Must be between 1 and %d.' % TEAMS_IN_ARENA.MAX_TEAMS)
    return (squadTeamNumbers, soloTeamNumbers)


def __readMapActivitiesTimeframes(section):
    mapActivitiesXML = section[b'mapActivities']
    if not mapActivitiesXML:
        return []
    timeframes = []
    for activityXML in mapActivitiesXML.values():
        startTimes = activityXML.readVector2(b'startTime')
        if (startTimes[0] >= 0) != (startTimes[1] >= 0):
            raise SoftException(b"wrong subsection 'mapActivities/startTime'. All values of startTime must have same sign")
        possibility = activityXML.readFloat(b'possibility', 1.0)
        timeframes.append((startTimes[0], startTimes[1], possibility))

    return timeframes


def __readDefaultGroundEffect(section, defaultXml):
    defaultGroundEff = _readString(b'defaultGroundEffect', section, defaultXml).strip()
    if defaultGroundEff == b'':
        return None
    else:
        if defaultGroundEff.find(b'|') != -1:
            defaultGroundEff = defaultGroundEff.split(b'|')
            for i in xrange(0, len(defaultGroundEff)):
                defaultGroundEff[i] = defaultGroundEff[i].strip()

        return defaultGroundEff


def __readControlPoints(section):
    res = []
    for name, value in section.items():
        if name == b'controlPoint':
            res.append(value.readVector2(b''))

    if res:
        return res
    else:
        return


def __readBotPoints(section):
    res = {}
    for name, value in section.items():
        if name == b'botPoint':
            index = value[b'index'].readInt(b'')
            pos = value[b'position'].readVector3(b'')
            res[index] = pos

    if res:
        return res
    else:
        return


def __readPointsOfInterest(section):
    res = []
    pointsSection = section[b'pointsOfInterestUDO']
    if pointsSection is not None:
        for name, value in pointsSection.items():
            if name == b'point':
                pointType = value.readInt(b'type')
                pointPosition = value.readVector2(b'position')
                res.append({b'type': pointType, b'position': pointPosition})

    return res


def __readTeamBasePositions(section, maxTeamsInArena):
    section = section[b'teamBasePositions']
    teamBases = tuple([{} for _ in xrange(maxTeamsInArena)])
    if section is None:
        return teamBases
    else:
        for idx, teamBase in enumerate(teamBases):
            teamIdx = idx + 1
            s = section[b'team%s' % teamIdx]
            if s is None:
                continue
            for name, value in s.items():
                try:
                    id = int(name[8:])
                except:
                    raise SoftException(b"wrong subsection 'teamBasePositions/team%s/%s'" % (teamIdx, s.name))

                teamBase[id] = value.readVector2(b'')

        return teamBases


def __readTeamSpawnPoints(section, maxTeamsInArena, nodeNameTemplate=b'team%d', required=True):
    section = section[b'teamSpawnPoints']
    allTeamSpawnPoints = tuple([[] for _ in xrange(maxTeamsInArena)])
    if section is None:
        return allTeamSpawnPoints
    else:
        for idx, teamSpawnPoint in enumerate(allTeamSpawnPoints):
            teamIdx = idx + 1
            s = section[nodeNameTemplate % teamIdx]
            if s is None:
                if required:
                    raise SoftException(b"missing 'teamSpawnPoints/%s'" % (nodeNameTemplate % teamIdx))
            else:
                for value in s.values():
                    teamSpawnPoint.append(value.readVector2(b''))

        return allTeamSpawnPoints


def __readGameplayPoints(section, geometryCfg):
    sps = []
    aps = []
    rps = {}
    rsps = []
    swps = []
    repairPointIDByGUID = geometryCfg.setdefault(b'repairPointIDByGUID', {})
    for name, value in section.items():
        if name == b'flagSpawnPoint':
            sps.append({b'position': (value.readVector3(b'position')), 
               b'team': (value.readInt(b'team')), 
               b'winPoints': (value.readFloat(b'winPoints'))})
        elif name == b'flagAbsorptionPoint':
            aps.append({b'position': (value.readVector3(b'position')), 
               b'team': (value.readInt(b'team')), 
               b'guid': (value.readString(b'guid'))})
        elif name == b'repairPoint':
            guid = value.readString(b'guid')
            point = {b'position': (value.readVector3(b'position')), 
               b'team': (value.readInt(b'team')), 
               b'radius': (value.readFloat(b'radius')), 
               b'cooldown': (value.readFloat(b'cooldown')), 
               b'repairTime': (value.readFloat(b'repairTime')), 
               b'repairFlags': (value.readInt(b'repairFlags')), 
               b'guid': guid}
            baseID = repairPointIDByGUID.get(guid, len(repairPointIDByGUID))
            rps[baseID] = point
            repairPointIDByGUID[guid] = baseID
        elif name == b'resourcePoint':
            rsps.append({b'position': (value.readVector3(b'position')), 
               b'radius': (value.readFloat(b'radius')), 
               b'startDelay': (value.readFloat(b'startDelay')), 
               b'cooldown': (value.readFloat(b'cooldown')), 
               b'damageLockTime': (value.readFloat(b'damageLockTime')), 
               b'amount': (value.readInt(b'amount')), 
               b'absorptionSpeed': (value.readFloat(b'absorptionSpeed')), 
               b'reuseCount': (value.readInt(b'reuseCount')), 
               b'team': (value.readInt(b'team')), 
               b'guid': (value.readString(b'guid'))})
        elif name == b'sectorWayPoint':
            swps.append({b'position': (value.readVector3(b'position')), 
               b'team': (value.readInt(b'team'))})

    cfg = {b'flagSpawnPoints': sps, 
       b'flagAbsorptionPoints': aps, 
       b'repairPoints': rps, 
       b'resourcePoints': rsps, 
       b'sectorWayPoints': swps}
    return cfg


def __readWinPoints(section):
    return {b'winPointsSettings': (section.readString(b'winPoints', b'DEFAULT'))}


def readVisualScriptSection(section):
    return _readVisualScript(section)
