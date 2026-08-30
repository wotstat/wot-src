from __future__ import absolute_import
import logging, typing
from collections import namedtuple
from future.utils import viewvalues, viewitems
import BigWorld, CGF, resource_helper
from constants import ARENA_GUI_TYPE
from gui.shared.system_factory import registerDynObjCache, collectDynObjCache
from gui.shared.utils.graphics import isRendererPipelineDeferred
from items.components.component_constants import ZERO_FLOAT
from shared_utils import first
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from vehicle_systems.stricted_loading import makeCallbackWeak
_CONFIG_PATH = b'scripts/dynamic_objects.xml'
_logger = logging.getLogger(__name__)
_ScenariosEffect = namedtuple(b'_ScenariosEffect', (b'path', b'rate', b'offset', b'scaleRatio'))
_DropPlane = namedtuple(b'_DropPlane', (b'model', b'flyAnimation', b'sound'))
_AirDrop = namedtuple(b'_AirDrop', (b'model', b'dropAnimation'))
_Loot = namedtuple(b'_Loot', (b'prefab', b'prefabPickup'))
_MinesEffects = namedtuple(b'_MinesEffects', (b'plantEffect', b'idleEffect', b'destroyEffect', b'placeMinesEffect', b'blowUpEffectName', b'activationEffect'))
_BerserkerEffects = namedtuple(b'_BerserkerEffects', (b'turretEffect', b'hullEffect', b'transformPath'))
MIN_OVER_TERRAIN_HEIGHT = 0
MIN_UPDATE_INTERVAL = 0
_TerrainCircleSettings = namedtuple(b'_TerrainCircleSettings', (b'modelPath', b'color', b'enableAccurateCollision', b'enableWaterCollision', b'maxUpdateInterval', b'overTerrainHeight', b'cutOffDistance', b'cutOffAngle', b'minHeight', b'maxHeight'))

def _createScenarioEffect(section, path):
    return _ScenariosEffect(section.readString(path, b''), section.readFloat(b'rate', ZERO_FLOAT), section.readVector3(b'offset', (ZERO_FLOAT, ZERO_FLOAT, ZERO_FLOAT)), section.readFloat(b'scaleRatio', ZERO_FLOAT))


def _addPrecacheCandidate(prerequisites, modelName):
    prerequisites.add(modelName)
    return


def _createDropPlane(section, prerequisites):
    modelName = section.readString(b'model')
    _addPrecacheCandidate(prerequisites, modelName)
    flyAnimation = section.readString(b'flyAnimation')
    dropPlane = _DropPlane(modelName, flyAnimation, section.readString(b'sound'))
    return dropPlane


def _createAirDrop(section, prerequisites):
    modelName = section.readString(b'model')
    _addPrecacheCandidate(prerequisites, modelName)
    dropAnimation = section.readString(b'dropAnimation')
    airDrop = _AirDrop(modelName, dropAnimation)
    return airDrop


def _createLoots(dataSection, typeSection):
    loots = {}
    for lootType in typeSection.items():
        typeName = lootType[1][b'name'].asString.strip()
        typeID = lootType[1][b'id'].asInt
        loot = dataSection[typeName]
        prefab = loot.readString(b'prefab')
        prefabPickup = loot.readString(b'prefabPickup')
        loots[typeID] = _Loot(prefab, prefabPickup)

    return loots


def createTerrainCircleSettings(section):
    sectionKeys = (b'ally', b'enemy')
    result = dict.fromkeys(sectionKeys)

    def readFloatOrNone(subSection, key):
        if subSection.has_key(key):
            return subSection.readFloat(key, default=None)
        else:
            return

    for sectionKey in sectionKeys:
        subSection = section[sectionKey]
        if subSection is not None:
            result[sectionKey] = _TerrainCircleSettings(subSection.readString(b'visual'), int(subSection.readString(b'color'), 0), subSection.readBool(b'enableAccurateCollision'), subSection.readBool(b'enableWaterCollision', default=False), max(MIN_UPDATE_INTERVAL, subSection.readFloat(b'maxUpdateInterval')), max(MIN_OVER_TERRAIN_HEIGHT, subSection.readFloat(b'overTerrainHeight')), readFloatOrNone(subSection, b'cutOffDistance'), readFloatOrNone(subSection, b'cutOffAngle'), readFloatOrNone(subSection, b'minHeight'), readFloatOrNone(subSection, b'maxHeight'))

    return result


def _parseEffectSubsection(dataSection, sectionKey):
    if dataSection is not None:
        effectSection = dataSection[sectionKey]
        if effectSection is not None:
            effPathPropName = b'path' if isRendererPipelineDeferred() else b'path_fwd'
            return _createScenarioEffect(effectSection, effPathPropName)
    return


class _SimpleEffect(object):
    _SECTION_NAME = None

    def __init__(self, dataSection):
        super(_SimpleEffect, self).__init__()
        self.effectDescr = _parseEffectSubsection(dataSection[self._SECTION_NAME], b'effect')
        return


class _TeamRelatedEffect(object):
    _ENEMY_SUB_NAME = b'enemy'
    _ALLY_SUB_NAME = b'ally'
    _SECTION_NAME = None

    def __init__(self, dataSection):
        super(_TeamRelatedEffect, self).__init__()
        tpSection = dataSection[self._SECTION_NAME]
        self.ally = _parseEffectSubsection(tpSection[self._ALLY_SUB_NAME], b'effect')
        self.enemy = _parseEffectSubsection(tpSection[self._ENEMY_SUB_NAME], b'effect')
        return


class _BattleRoyaleTrapPointEffect(object):
    _SECTION_NAME = b'TrapPoint'

    def __init__(self, dataSection):
        tpSection = dataSection[self._SECTION_NAME]
        self.vehicleEffect = _parseEffectSubsection(tpSection, b'vehicleEffect')
        return


class _BattleRoyaleRepairPointEffect(_TeamRelatedEffect):
    _SECTION_NAME = b'RepairPoint'


class _BattleRoyaleBotDeliveryEffect(_TeamRelatedEffect):
    _SECTION_NAME = b'BotDeliveryEffect'


class _BattleRoyaleBotClingDeliveryEffect(_TeamRelatedEffect):
    _SECTION_NAME = b'BotClingDeliveryEffect'


class _BattleRoyaleBotDeliveryMarkerArea(_TeamRelatedEffect):
    _SECTION_NAME = b'BotDeliveryArea'


class _MinesPlantEffect(_SimpleEffect):
    _SECTION_NAME = b'minesPlantEffect'


class _MinesIdleEffect(_TeamRelatedEffect):
    _SECTION_NAME = b'minesIdleEffect'


class _EpicMinesIdleEffect(_TeamRelatedEffect):
    _SECTION_NAME = b'epicMinesIdleEffect'


class _MinesDestroyEffect(_SimpleEffect):
    _SECTION_NAME = b'minesDestroyEffect'


class _VehicleUpgradeEffect(_SimpleEffect):
    _SECTION_NAME = b'VehicleUpgrade'


class _KamikazeActivatedEffect(_SimpleEffect):
    _SECTION_NAME = b'KamikazeActivated'


class _BerserkerHullEffect(_SimpleEffect):
    _SECTION_NAME = b'berserkerHullEffect'


class _BerserkerTurretEffect(_SimpleEffect):
    _SECTION_NAME = b'berserkerTurretEffect'


class _PrefabsReader(object):
    _SECTION_NAME = None
    prefabs = property((lambda self: self.__prefabs))

    def __init__(self, dataSection):
        super(_PrefabsReader, self).__init__()
        self.__prefabs = dataSection[self._SECTION_NAME].readStrings(b'prefab')
        return


class _VehicleRespawnEffects(_PrefabsReader):
    _SECTION_NAME = b'VehicleRespawn'


class _StPatrickLootEffect(_PrefabsReader):
    _SECTION_NAME = b'StPatrickLootEffect'


class _FireCircleEffects(_PrefabsReader):
    _SECTION_NAME = b'FireCircleEffect'


class DynObjectsBase(object):

    def __init__(self):
        super(DynObjectsBase, self).__init__()
        self._initialized = False
        return

    def init(self, dataSection):
        self._initialized = True
        return

    def clear(self):
        return

    def destroy(self):
        return

    def getInspiringEffect(self):
        return {}

    def getHealPointEffect(self):
        return {}

    def getAimingCircleRestrictionEffect(self, equipment):
        return {}


class _CommonForBattleRoyaleAndEpicBattleDynObjects(DynObjectsBase):

    def __init__(self):
        super(_CommonForBattleRoyaleAndEpicBattleDynObjects, self).__init__()
        self.__inspiringEffect = None
        self.__healPointEffect = None
        return

    def init(self, dataSection):
        if not self._initialized:
            self.__inspiringEffect = createTerrainCircleSettings(dataSection[b'InspireAreaVisual'])
            self.__healPointEffect = createTerrainCircleSettings(dataSection[self._healPointKey])
            super(_CommonForBattleRoyaleAndEpicBattleDynObjects, self).init(dataSection)
        return

    def getInspiringEffect(self):
        return self.__inspiringEffect

    def getHealPointEffect(self):
        return self.__healPointEffect

    @property
    def _healPointKey(self):
        return b'HealPointVisual'

    def clear(self):
        return

    def destroy(self):
        return


class _StrongholdDynObjects(DynObjectsBase):

    def __init__(self):
        super(_StrongholdDynObjects, self).__init__()
        self.__inspiringEffect = None
        return

    def init(self, dataSection):
        if not self._initialized:
            self.__inspiringEffect = createTerrainCircleSettings(dataSection[b'InspireAreaVisual'])
            super(_StrongholdDynObjects, self).init(dataSection)
        return

    def getInspiringEffect(self):
        return self.__inspiringEffect


class _EpicBattleDynObjects(_CommonForBattleRoyaleAndEpicBattleDynObjects):

    def __init__(self):
        super(_EpicBattleDynObjects, self).__init__()
        self.__minesEffects = None
        return

    def init(self, dataSection):
        if not self._initialized:
            self.__minesEffects = _MinesEffects(plantEffect=_MinesPlantEffect(dataSection), idleEffect=_EpicMinesIdleEffect(dataSection), destroyEffect=_MinesDestroyEffect(dataSection), placeMinesEffect=b'epicMinesDecalEffect', blowUpEffectName=b'epicMinesBlowUpEffect', activationEffect=b'epicMinesActivationDecalEffect')
            super(_EpicBattleDynObjects, self).init(dataSection)
        return

    def getMinesEffect(self):
        return self.__minesEffects


class _BattleRoyaleDynObjects(_CommonForBattleRoyaleAndEpicBattleDynObjects):

    def __init__(self):
        super(_BattleRoyaleDynObjects, self).__init__()
        self.__vehicleUpgradeEffect = None
        self.__kamikazeActivatedEffect = None
        self.__trapPoint = None
        self.__repairPoint = None
        self.__botDeliveryEffect = None
        self.__botClingDeliveryEffect = None
        self.__vehicleRespawnEffects = None
        self.__stPatrickLootEffect = None
        self.__botDeliveryMarker = None
        self.__dropPlane = None
        self.__airDrop = None
        self.__loots = {}
        self.__minesEffects = None
        self.__berserkerEffects = None
        self.__fireCircleEffects = None
        self.__resourcesCache = None
        return

    def init(self, dataSection):
        if not self._initialized:
            self.__vehicleUpgradeEffect = _VehicleUpgradeEffect(dataSection)
            self.__kamikazeActivatedEffect = _KamikazeActivatedEffect(dataSection)
            self.__trapPoint = _BattleRoyaleTrapPointEffect(dataSection)
            self.__repairPoint = _BattleRoyaleRepairPointEffect(dataSection)
            self.__botDeliveryEffect = _BattleRoyaleBotDeliveryEffect(dataSection)
            self.__botClingDeliveryEffect = _BattleRoyaleBotClingDeliveryEffect(dataSection)
            self.__botDeliveryMarker = _BattleRoyaleBotDeliveryMarkerArea(dataSection)
            self.__minesEffects = _MinesEffects(plantEffect=_MinesPlantEffect(dataSection), idleEffect=_MinesIdleEffect(dataSection), destroyEffect=_MinesDestroyEffect(dataSection), placeMinesEffect=b'minesDecalEffect', blowUpEffectName=b'minesBlowUpEffect', activationEffect=None)
            self.__berserkerEffects = _BerserkerEffects(turretEffect=_BerserkerTurretEffect(dataSection), hullEffect=_BerserkerHullEffect(dataSection), transformPath=dataSection.readString(b'berserkerTransformPath'))
            self.__fireCircleEffects = _FireCircleEffects(dataSection)
            self.__vehicleRespawnEffects = _VehicleRespawnEffects(dataSection)
            self.__stPatrickLootEffect = _StPatrickLootEffect(dataSection)
            precacheCandidates = set()
            precacheCandidates.update(self.__fireCircleEffects.prefabs)
            precacheCandidates.update(self.__vehicleRespawnEffects.prefabs)
            precacheCandidates.update(self.__stPatrickLootEffect.prefabs)
            CGF.cachePrefabs(list(precacheCandidates))
            prerequisites = set()
            self.__dropPlane = _createDropPlane(dataSection[b'dropPlane'], prerequisites)
            self.__airDrop = _createAirDrop(dataSection[b'airDrop'], prerequisites)
            self.__loots = _createLoots(dataSection, dataSection[b'lootTypes'])
            BigWorld.loadResourceListBG(list(prerequisites), makeCallbackWeak(self.__onResourcesLoaded))
            super(_BattleRoyaleDynObjects, self).init(dataSection)
        return

    def getVehicleUpgradeEffect(self):
        return self.__vehicleUpgradeEffect

    def getKamikazeActivatedEffect(self):
        return self.__kamikazeActivatedEffect

    def getTrapPointEffect(self):
        return self.__trapPoint

    def getRepairPointEffect(self):
        return self.__repairPoint

    def getBotDeliveryEffect(self):
        return self.__botDeliveryEffect

    def getBotClingDeliveryEffect(self):
        return self.__botClingDeliveryEffect

    def getBotDeliveryMarker(self):
        return self.__botDeliveryMarker

    def getDropPlane(self):
        return self.__dropPlane

    def getAirDrop(self):
        return self.__airDrop

    def getLoots(self):
        return self.__loots

    def getMinesEffect(self):
        return self.__minesEffects

    def getBerserkerEffects(self):
        return self.__berserkerEffects

    def getVehicleRespawnEffect(self):
        paths = self.__vehicleRespawnEffects.prefabs
        if not paths:
            return str()
        return paths[0]

    def getStPatrickLootEffect(self):
        return self.__stPatrickLootEffect

    def clear(self):
        return

    def destroy(self):
        self.__vehicleUpgradeEffect = None
        self.__kamikazeActivatedEffect = None
        self.__trapPoint = None
        self.__repairPoint = None
        self.__resourcesCache = None
        self.__minesEffects = None
        return

    @property
    def _healPointKey(self):
        return b'battleRoyaleHealpoint'

    def __onResourcesLoaded(self, resourceRefs):
        self.__resourcesCache = resourceRefs
        return


class _SpawnPointsConfig(object):

    def __init__(self, size, visualsPath, colors, overTerrainHeight):
        self.__size = size
        self.__visualsPath = visualsPath
        self.__colors = colors
        self.__overTerrainHeight = overTerrainHeight
        return

    @property
    def size(self):
        return self.__size

    @property
    def overTerrainHeight(self):
        return self.__overTerrainHeight

    def getColor(self, isMyOwn, isConfirmed):
        ownageKey = b'own' if isMyOwn else b'ally'
        confirmationKey = b'confirmed' if isConfirmed else b'notConfirmed'
        return self.__colors[ownageKey][confirmationKey]

    def getVisualPath(self, positionNumber):
        positionName = (b'position{}').format(positionNumber)
        return self.__visualsPath.get(positionName)

    @classmethod
    def createFromXML(cls, section):
        return cls(size=section.readVector2(b'areaSize'), visualsPath=cls.__readVisualsPath(section[b'visualsPath']), colors=cls.__readColors(section[b'colors']), overTerrainHeight=section.readFloat(b'overTerrainHeight'))

    @staticmethod
    def __readVisualsPath(section):
        return {key: section.readString(key) for key in section.keys()}

    @staticmethod
    def __readColors(section):
        colors = {}
        renderKey = b'deferred' if isRendererPipelineDeferred() else b'forward'
        for ownageType, colorsConfig in section[renderKey].items():
            colors[ownageType] = {b'confirmed': (int(colorsConfig.readString(b'confirmed'), 16)), b'notConfirmed': (int(colorsConfig.readString(b'notConfirmed'), 16))}

        return colors


class _PointsOfInterestConfig(object):

    def __init__(self, prefabs):
        self.__prefabs = prefabs
        return

    def getPointOfInterestPrefab(self, radius):
        for (minRange, maxRange), path in viewitems(self.__prefabs):
            if minRange <= radius < maxRange:
                return path

        _logger.error(b'Failed to get prefab for PointOfInterest (radius=%d)', radius)
        return first(viewvalues(self.__prefabs))

    def getPrefabs(self):
        return self.__prefabs.values()

    @classmethod
    def createFromXML(cls, section):
        points = {}
        for _, prefab in section.items():
            radiusRange = prefab.readVector2(b'radiusRange')
            path = prefab.readString(b'path')
            points[(radiusRange.x, radiusRange.y)] = path

        return cls(points)


class _FeatureDynObjects(DynObjectsBase):
    _ROOT_SECTION_NAME = b''

    def __init__(self):
        super(_FeatureDynObjects, self).__init__()
        self.__cachedPrefabs = set()
        return

    def init(self, dataSection):
        if self._initialized:
            return
        else:
            section = dataSection[self._ROOT_SECTION_NAME]
            if section is None:
                return
            toCache = self._init(dataSection=section)
            self.__cachedPrefabs.update(toCache)
            CGF.cachePrefabs(list(self.__cachedPrefabs))
            super(_FeatureDynObjects, self).init(dataSection)
            return

    def _init(self, dataSection):
        return set()

    def clear(self):
        if self.__cachedPrefabs:
            CGF.removePrefabsFromCache(list(self.__cachedPrefabs))
            self.__cachedPrefabs.clear()
        return

    def destroy(self):
        self.clear()
        super(_FeatureDynObjects, self).destroy()
        return


class _KillCamEffectDynObjects(_FeatureDynObjects):
    CONFIG_NAME = b'KillCamEffectDynObjects'
    _ROOT_SECTION_NAME = b'killCameraVisualEffects'

    def __init__(self):
        super(_KillCamEffectDynObjects, self).__init__()
        self.emptyGO = None
        self.cone = None
        self.impactPoint = None
        self.spacedArmorLinePoint = None
        self.explosionSphere = None
        self.spacedArmorImpactPoint = None
        self.trajectoryRed = None
        self.trajectoryGradient = None
        return

    def _init(self, dataSection):
        self.emptyGO = dataSection[b'emptyGO'][b'path'].asString
        self.cone = dataSection[b'cone'][b'path'].asString
        self.impactPoint = dataSection[b'impactPoint'][b'path'].asString
        self.spacedArmorLinePoint = dataSection[b'spacedArmorLinePoint'][b'path'].asString
        self.explosionSphere = dataSection[b'explosionSphere'][b'path'].asString
        self.spacedArmorImpactPoint = dataSection[b'spacedArmorImpactPoint'][b'path'].asString
        self.trajectoryRed = dataSection[b'trajectoryRed'][b'path'].asString
        self.trajectoryGradient = dataSection[b'trajectoryGradient'][b'path'].asString
        return {
         self.emptyGO, self.cone, self.impactPoint, self.spacedArmorLinePoint, self.explosionSphere,
         self.spacedArmorImpactPoint, self.trajectoryRed, self.trajectoryGradient}


registerDynObjCache(ARENA_GUI_TYPE.SORTIE_2, _StrongholdDynObjects)
registerDynObjCache(ARENA_GUI_TYPE.FORT_BATTLE_2, _StrongholdDynObjects)
registerDynObjCache(ARENA_GUI_TYPE.BATTLE_ROYALE, _BattleRoyaleDynObjects)
registerDynObjCache(ARENA_GUI_TYPE.EPIC_BATTLE, _EpicBattleDynObjects)
registerDynObjCache(ARENA_GUI_TYPE.EPIC_TRAINING, _EpicBattleDynObjects)
registerDynObjCache(ARENA_GUI_TYPE.EVENT_BATTLES, _EpicBattleDynObjects)
_COMMON_FEATURES_CONF_STORAGES = (
 _KillCamEffectDynObjects,)

class BattleDynamicObjectsCache(IBattleDynamicObjectsCache):

    def __init__(self):
        super(BattleDynamicObjectsCache, self).__init__()
        self.__gameModeConfigStorage = {}
        self.__featuresConfigStorage = {}
        return

    def getConfig(self, arenaType):
        return self.__gameModeConfigStorage.get(arenaType)

    def getFeaturesConfig(self, feature):
        return self.__featuresConfigStorage.get(feature)

    def load(self, arenaType):
        _logger.info(b'Trying to load resources for arenaType = %s', arenaType)
        _, section = resource_helper.getRoot(_CONFIG_PATH)
        if arenaType in self.__gameModeConfigStorage:
            self.__gameModeConfigStorage[arenaType].init(section)
        else:
            cache = collectDynObjCache(arenaType)
            if cache:
                confStorage = cache()
                self.__gameModeConfigStorage[arenaType] = confStorage
                confStorage.init(section)
                resource_helper.purgeResource(_CONFIG_PATH)
        for featureStorageCls in _COMMON_FEATURES_CONF_STORAGES:
            fstorage = featureStorageCls()
            self.__featuresConfigStorage[fstorage.CONFIG_NAME] = fstorage
            fstorage.init(dataSection=section)

        return

    def unload(self, arenaType):
        for cV in viewvalues(self.__gameModeConfigStorage):
            cV.clear()

        return

    def destroy(self):
        if self.__gameModeConfigStorage is not None:
            for cV in viewvalues(self.__gameModeConfigStorage):
                cV.destroy()

            self.__gameModeConfigStorage = None
        if self.__featuresConfigStorage is not None:
            for cV in viewvalues(self.__featuresConfigStorage):
                cV.destroy()

            self.__featuresConfigStorage = None
        return
