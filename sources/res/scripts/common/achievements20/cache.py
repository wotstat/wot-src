from __future__ import absolute_import
from functools import partial
from time import time
from enum import Enum
from future.utils import viewitems, viewvalues
from past.builtins import xrange
from typing import TYPE_CHECKING, Union, Set, List, Dict, Optional, Any, Iterable
from account_shared import getCustomizationItem
from bonus_readers import readBonusSection, SUPPORTED_BONUSES
from constants import IS_CLIENT, IS_WEB, MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL
from dossiers2.custom.cache import getCache as getHelperCache
from dossiers2.custom.dependencies import VEHICLE_ACHIEVEMENTS_DEPENDENCIES, CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES, VEHICLE_ACHIEVEMENTS_POP_UPS, CUSTOMIZATION_ACHIEVEMENTS_POP_UPS, _processAchievementDependency
from items import vehicles, ITEM_TYPES, ITEM_TYPE_NAMES, parseIntCompactDescr
from items.components.c11n_constants import CustomizationType
from nations import NAMES, INDICES
from realm_utils import ResMgr as rmgr
from soft_exception import SoftException
from wotdecorators import singleton
if TYPE_CHECKING:
    from items.components.c11n_components import BaseCustomizationItem
    from dossiers2.common.DossierDescr import DossierDescr
    from items.vehicles import VehicleType
    from ResMgr import DataSection
DEPRECATED_BONUSES = {23, 24, 25, 26, 27, 
 28, 29, 30}
ACHIEVEMENTS20_SUPPORTED_BONUSES = SUPPORTED_BONUSES - DEPRECATED_BONUSES
ALLOWED_CUSTOMIZATION_TAGS = frozenset((b'c11n2D', b'c11n3D'))
ITEM_CONDITION_KEYS = frozenset((b'vehicle', b'customizationItem'))
ITEM_FILTER_CONDITION_KEYS = frozenset((b'vehicleFilter', b'customizationItemFilter'))
VEHICLE_FILTER_CONDITION_KEYS = frozenset((b'nations', b'vehClasses', b'levels'))
ALLOWED_ACHIEVEMENT_TYPES = frozenset((b'vehicleAchievements', b'customizationAchievements'))
ALLOWED_CONDITIONS_BY_ACHIEVEMENT_TYPE = {b'vehicleAchievements': {
                          b'vehicle', b'vehicleFilter', b'requiredAchievementIDs'}, 
   b'customizationAchievements': {
                                b'customizationItem', b'customizationItemFilter', b'requiredAchievementIDs'}}

class ProgressiveTypes(Enum):
    PROGRESSIVE = b'progressive'
    NOT_PROGRESSIVE = b'notProgressive'


_VALID_PROGRESSIVE_TYPES = {k.value for k in ProgressiveTypes}

class UIConfigFields(Enum):
    TYPE = b'type'
    BACKGROUND = b'background'
    STRING_KEY = b'stringKey'
    ICON_POSITION = b'iconPosition'
    ORDER = b'order'
    THEME = b'theme'
    ICON_SIZE_MAP = b'iconSizeMap'
    VEHICLE = b'vehicle'


_VALID_UI_CONFIG_KEYS = {k.value for k in UIConfigFields}

class IconPositions(Enum):
    TOP = b'top'
    CENTER = b'center'
    BOTTOM = b'bottom'


_VALID_ICON_POSITIONS = {k.value for k in IconPositions}

class IconSizeMap(Enum):
    DEFAULT = b''
    PERSONAL_MISSIONS = b'personal_missions'


_VALID_ICON_SIZE_MAPS = {k.value for k in IconSizeMap}
ROOT_ACHIEVEMENT_IDS = (
 (b'vehicleAchievements', 1), (b'vehicleAchievements', 2), (b'customizationAchievements', 1))
_CONFIG_FILE = b'scripts/item_defs/advanced_achievements/advanced_achievements.xml'

def getCache():
    return g_cache


def _readConfig():
    section = rmgr.openSection(_CONFIG_FILE)[b'achievements']
    config = {}
    for name, value in section.items():
        if name in config:
            raise SoftException((b'Duplicate achievement section name: {}').format(name))
        try:
            config[name] = __readAchievements(name, value)
        except SoftException as e:
            raise SoftException((b"Error: '{}', achievement type '{}'").format(str(e), name))

    return config


def __readUIConfig(section, achievementID):
    uiConfig = {}
    if section.has_key(b'UI'):
        for pName, pValue in section[b'UI'].items():
            if pName not in _VALID_UI_CONFIG_KEYS:
                raise SoftException((b'Wrong UI parameter {} for achievement {}').format(pName, achievementID))
            if pName in uiConfig:
                raise SoftException((b'Duplicated UI parameter {} for achievement {}').format(pName, achievementID))
            if pName == UIConfigFields.ICON_SIZE_MAP.value and pValue.asString not in _VALID_ICON_SIZE_MAPS:
                raise SoftException((b'Invalid iconSizeMap {} parameter {} for achievement {}').format(pValue.asString, pName, achievementID))
            if pName == UIConfigFields.ORDER.value:
                uiConfig[pName] = list(map(int, pValue.asString.split()))
            else:
                uiConfig[pName] = pValue.asString

    return uiConfig


def __readAchievements(achievementsType, achievementsSection):
    if achievementsSection is None:
        return {}
    else:
        requiredAchievementIDs = set()
        availableAchievementIDs = set()
        deprecatedAchievementIDs = set()
        achievements = {}
        for name, value in achievementsSection.items():
            if name != b'achievement':
                raise SoftException((b"Unexpected name '{}'").format(name))
            achievementID = value.readInt(b'id', -1)
            if achievementID < 0:
                raise SoftException((b"Achievement id should be non-negative '{}'").format(value.readString(b'id')))
            if achievementID in achievements:
                raise SoftException((b"Duplicate achievement id '{}'").format(achievementID))
            try:
                conditions = __readConditions(value[b'conditions'])
                if set(conditions) - ALLOWED_CONDITIONS_BY_ACHIEVEMENT_TYPE[achievementsType]:
                    raise SoftException((b'Unexpected conditions for achievement type: {}').format(set(conditions) - ALLOWED_CONDITIONS_BY_ACHIEVEMENT_TYPE[achievementsType]))
                if b'requiredAchievementIDs' in conditions:
                    if achievementID in conditions[b'requiredAchievementIDs']:
                        raise SoftException(b"Own achievement id can't be at required achievements list")
                    requiredAchievementIDs |= conditions[b'requiredAchievementIDs']
                stages = __readStages(value[b'stages'], conditions)
                isDeprecated = value.readBool(b'deprecated', False)
                if isDeprecated:
                    deprecatedAchievementIDs.add(achievementID)
                else:
                    availableAchievementIDs.add(achievementID)
                openByUnlock = value.has_key(b'openByUnlock')
                if openByUnlock and achievementsType != b'vehicleAchievements':
                    raise SoftException((b"Only vehicleAchievements could have openByUnlock achivement '{}'").format(value.readString(b'id')))
                achievementData = {b'id': achievementID, 
                   b'stages': stages, 
                   b'conditions': conditions, 
                   b'type': achievementsType, 
                   b'deprecated': isDeprecated, 
                   b'openByUnlock': openByUnlock}
                if IS_CLIENT or IS_WEB:
                    achievementData[b'UI'] = __readUIConfig(value, achievementID)
            except SoftException as e:
                raise SoftException(str(e) + (b", achievement id: '{}'").format(achievementID))

            achievements[achievementID] = Achievement(achievementData)

        if deprecatedAchievementIDs & requiredAchievementIDs:
            raise SoftException((b'Deprecated achievement can not be required: {}').format(deprecatedAchievementIDs & requiredAchievementIDs))
        if requiredAchievementIDs - availableAchievementIDs:
            raise SoftException((b'Missed some required achievements: {}').format(requiredAchievementIDs - availableAchievementIDs))
        return achievements


def __stageAllValueGetterByVehicleFilter(filterData):
    vehicleCache = getHelperCache()
    vehiclesByFilter = vehicleCache[b'vehiclesInTrees']
    if b'nations' in filterData and filterData[b'nations'] != set(viewvalues(INDICES)):
        nationVehicles = set()
        for nationID in filterData[b'nations']:
            nationVehicles |= vehicleCache[b'vehiclesInTreesByNation'][nationID]

        vehiclesByFilter &= nationVehicles
    if b'vehClasses' in filterData and filterData[b'vehClasses'] != vehicles.VEHICLE_CLASS_TAGS:
        classVehicles = set()
        for vehClass in filterData[b'vehClasses']:
            classVehicles |= vehicleCache[b'vehiclesByClass'][vehClass]

        vehiclesByFilter &= classVehicles
    if b'levels' in filterData and filterData[b'levels'] != set(xrange(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1)):
        levelVehicles = set()
        for level in filterData[b'levels']:
            levelVehicles |= vehicleCache[b'vehiclesByLevel'].get(level, set())

        vehiclesByFilter &= levelVehicles
    return len(vehiclesByFilter)


def __stageAllValueGetterByCustomizationItemFilter(filterData):
    customizationItemTypesCache = vehicles.g_cache.customization20().itemTypes
    allValue = 0
    if b'custTypes' in filterData:
        for custType in filterData[b'custTypes']:
            allValue += len(customizationItemTypesCache[custType])

    return allValue


__stageAllValueGetterByCondition = {b'vehicleFilter': __stageAllValueGetterByVehicleFilter, 
   b'customizationItemFilter': __stageAllValueGetterByCustomizationItemFilter}

def __readStages(stagesSection, conditions):
    if stagesSection is None:
        return []
    else:
        stages = []
        for name, value in stagesSection.items():
            if name != b'stage':
                raise SoftException(b'')
            stageValue = value.readString(b'value')
            if not stageValue:
                raise SoftException((b"Missed stage '{}' value").format(len(stages)))
            if stageValue == b'all':
                stageValue = 0
                for conditionName, conditionData in viewitems(conditions):
                    if conditionName not in __stageAllValueGetterByCondition:
                        raise SoftException((b"Unexpected condition '{}' for 'all' value, stage index: {}").format(conditionName, len(stages)))
                    stageValue += __stageAllValueGetterByCondition[conditionName](conditionData)

            else:
                stageValue = int(stageValue)
            if stageValue < 1:
                raise SoftException((b'Stage value should be greater than 0: {}, stage index: {}').format(stageValue, len(stages)))
            points = value.readInt(b'points', 0)
            rewards = readBonusSection(ACHIEVEMENTS20_SUPPORTED_BONUSES, value[b'rewards'])
            if stages and stages[-1][b'value'] >= stageValue:
                raise SoftException((b'Stages should be increased sequence by stage value: {}, stage index: {}').format(stageValue, len(stages)))
            stages.append({b'id': (len(stages) + 1), 
               b'value': stageValue, 
               b'points': points, 
               b'rewards': rewards})

        return stages


def __readVehicleFilterConditions(filterSection):
    if filterSection is None:
        return {}
    else:
        unexpectedFilterKeys = set(filterSection.keys()) - VEHICLE_FILTER_CONDITION_KEYS
        if unexpectedFilterKeys:
            raise SoftException((b'Unexpected filter keys: {}').format(unexpectedFilterKeys))
        if filterSection.has_key(b'nations'):
            nations = set(filterSection.readString(b'nations').split())
            invalidNations = nations - set(NAMES)
            if invalidNations:
                raise SoftException((b'Invalid nations: {}').format(invalidNations))
            nationsIDs = {INDICES[nation] for nation in nations}
        else:
            nationsIDs = set(viewvalues(INDICES))
        if filterSection.has_key(b'vehClasses'):
            vehClasses = set(filterSection.readString(b'vehClasses').split())
            invalidVehClasses = vehClasses - vehicles.VEHICLE_CLASS_TAGS
            if invalidVehClasses:
                raise SoftException((b'Invalid vehicle types: {}').format(invalidVehClasses))
        else:
            vehClasses = vehicles.VEHICLE_CLASS_TAGS
        if filterSection.has_key(b'levels'):
            levels = set(int(level) for level in filterSection.readString(b'levels').split())
            if any(level < MIN_VEHICLE_LEVEL or level > MAX_VEHICLE_LEVEL for level in levels):
                raise SoftException(b'Invalid levels')
        else:
            levels = set(xrange(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1))
        return {b'nations': nationsIDs, 
           b'vehClasses': vehClasses, 
           b'levels': levels}


def __readCustomizationItemConditions(customizationItemSection):
    custType, custID = customizationItemSection.asString.split(b':')
    item, error = getCustomizationItem(custType, int(custID))
    if error:
        raise SoftException((b'Invalid customization item, error - {}').format(error))
    return item.compactDescr


def __readCustomizationItemFilter(filterSection):
    if filterSection is None:
        return {}
    else:
        unexpectedFilterKeys = set(filterSection.keys()) - {b'custTypes', b'tags', b'progressiveTypes'}
        if unexpectedFilterKeys:
            raise SoftException((b'Unexpected filter keys: {}').format(unexpectedFilterKeys))
        if filterSection.has_key(b'custTypes'):
            custTypes = set(filterSection.readString(b'custTypes').split())
            custTypeIDs = {getattr(CustomizationType, custType.upper()) for custType in custTypes}
        else:
            custTypeIDs = CustomizationType.RANGE
        if filterSection.has_key(b'tags'):
            tags = set(filterSection.readString(b'tags').split())
        else:
            tags = set()
        unexpectedCustamizationTags = tags - ALLOWED_CUSTOMIZATION_TAGS
        if unexpectedCustamizationTags:
            raise SoftException((b'Unexpected customization tags: {}').format(unexpectedCustamizationTags))
        if filterSection.has_key(b'progressiveTypes'):
            progressiveTypes = set(filterSection.readString(b'progressiveTypes').split())
            unexpectedProgressiveTypes = progressiveTypes - _VALID_PROGRESSIVE_TYPES
            if unexpectedProgressiveTypes:
                raise SoftException((b'Unexpected progressive types keys: {}').format(unexpectedProgressiveTypes))
            progressive = progressiveTypes
        else:
            progressive = _VALID_PROGRESSIVE_TYPES
        return {b'custTypes': custTypeIDs, 
           b'tags': tags, 
           b'progressiveTypes': progressive}


__conditionReaders = {b'vehicle': (lambda vehicleSection: vehicles.g_cache.vehicle(*vehicles.g_list.getIDsByName(vehicleSection.asString)).compactDescr), 
   b'customizationItem': __readCustomizationItemConditions, 
   b'vehicleFilter': __readVehicleFilterConditions, 
   b'customizationItemFilter': __readCustomizationItemFilter, 
   b'requiredAchievementIDs': (lambda achievementsSection: set(map(int, achievementsSection.asString.split())))}

def __readConditions(conditionsSections):
    if conditionsSections is None:
        return {}
    else:
        conditions = {}
        for name, value in conditionsSections.items():
            if name in conditions:
                raise SoftException((b'Duplicate condition type: {}').format(name))
            if name not in __conditionReaders:
                raise SoftException((b'Unexpected condition: {}').format(name))
            if len(conditions) > 0:
                raise SoftException(b'Should be only 1 condition type')
            conditions[name] = __conditionReaders[name](value)

        return conditions


@singleton
class g_cache(object):

    def __init__(self):
        self.__data = {}
        self.__totalVehicleAchievement = None
        return

    def init(self):
        self.__data = data = _readConfig()
        achievementsByConditions = data.setdefault(b'achievementsByConditions', {})
        for achievementType, achievementsByType in viewitems(data):
            (VEHICLE_ACHIEVEMENTS_POP_UPS if achievementType == b'vehicleAchievements' else CUSTOMIZATION_ACHIEVEMENTS_POP_UPS).extend(achievementsByType)
            dependencies = VEHICLE_ACHIEVEMENTS_DEPENDENCIES if achievementType == b'vehicleAchievements' else CUSTOMIZATION_ACHIEVEMENTS_DEPENDENCIES
            for achievementID, achievement in viewitems(achievementsByType):
                rewards = achievement.getAllBonuses()
                if rewards and b'dogTagComponents' in rewards:
                    self.__totalVehicleAchievement = (
                     achievementType, achievementID)
                for conditionKey, conditionData in viewitems(achievement.conditions):
                    if conditionKey in ITEM_CONDITION_KEYS:
                        achievementsByConditions.setdefault(conditionKey, {}).setdefault(conditionData, set()).add(achievement)
                    elif conditionKey in ITEM_FILTER_CONDITION_KEYS:
                        itemFilter = achievementsByConditions.setdefault(conditionKey, {})
                        for filterName, filterValues in viewitems(conditionData):
                            filterData = itemFilter.setdefault(filterName, {})
                            for filterValue in filterValues:
                                filterData.setdefault(filterValue, set()).add(achievement)

                    elif conditionKey == b'requiredAchievementIDs':
                        requiredAchievements = [data[achievementType][requiredAchievementID] for requiredAchievementID in conditionData if not data[achievementType][requiredAchievementID].deprecated]
                        for requiredAchievement in requiredAchievements:
                            dependencies.setdefault(requiredAchievement.id, []).append(partial(_processAchievementDependency, achievement, requiredAchievements))

                    else:
                        raise SoftException((b'Unexpected condition key: {}, achievement type: {}, achievement id: {}').format(conditionKey, achievementType, achievementID))

        return

    def _getAchievementsByItem(self, itemTypeName, item):
        return self.__data.get(b'achievementsByConditions', {}).get(itemTypeName, {}).get(item.compactDescr, ())

    def _getAchievementsByVehicleFilter(self, itemTypeName, vehicleType):
        achievementsByConditions = self.__data.get(b'achievementsByConditions', {})
        achievementsByVehicleFilter = achievementsByConditions.get(b'vehicleFilter', None)
        if achievementsByVehicleFilter and vehicleType.compactDescr in getHelperCache().get(b'vehiclesByClass', {}).get(vehicleType.classTag, ()):
            achievements = achievementsByVehicleFilter.get(b'nations', {}).get(vehicleType.id[0], set()) & achievementsByVehicleFilter.get(b'vehClasses', {}).get(vehicleType.classTag, set()) & achievementsByVehicleFilter.get(b'levels', {}).get(vehicleType.level, set())
        else:
            achievements = ()
        return achievements

    def _getAchievementsByCustomizationItemFilter(self, itemTypeName, item):
        achievementsByConditions = self.__data.get(b'achievementsByConditions', {})
        achievementsByCustItemFilter = achievementsByConditions.get(b'customizationItemFilter', None)
        achievements = set()
        if achievementsByCustItemFilter:
            achievements.update(achievementsByCustItemFilter.get(b'custTypes', {}).get(item.itemType, set()))
            progressiveAchievements = achievementsByCustItemFilter.get(b'progressiveTypes', None)
            if progressiveAchievements:
                if item.isProgressive():
                    progressiveType = ProgressiveTypes.PROGRESSIVE.value
                else:
                    progressiveType = ProgressiveTypes.NOT_PROGRESSIVE.value
                achievements &= progressiveAchievements.get(progressiveType, set())
            for tag in item.tags:
                achievmenetsByTag = achievementsByCustItemFilter.get(b'tags', {}).get(tag, None)
                if achievmenetsByTag:
                    achievements &= achievmenetsByTag

        return tuple(achievements)

    _achievementsGettersByItemType = {(ITEM_TYPES.vehicle): (
                            _getAchievementsByItem,
                            _getAchievementsByVehicleFilter), 
       (ITEM_TYPES.customizationItem): (
                                      _getAchievementsByItem,
                                      _getAchievementsByCustomizationItemFilter)}

    def getAchievementsByItem(self, item, receivedItems):
        achievements = []
        itemCompactDescr = item.compactDescr
        itemTypeID, _, __ = parseIntCompactDescr(itemCompactDescr)
        vehicleCache = getHelperCache()
        if not (itemTypeID == ITEM_TYPES.customizationItem and item.isProgressive()):
            if itemTypeID not in self._achievementsGettersByItemType or itemCompactDescr in receivedItems:
                return achievements
        itemTypeName = ITEM_TYPE_NAMES[itemTypeID]
        for getter in self._achievementsGettersByItemType.get(itemTypeID, ()):
            achievements.extend(getter(self, itemTypeName, item))

        if itemTypeID == ITEM_TYPES.vehicle and itemCompactDescr not in vehicleCache[b'vehiclesInTrees']:
            achievements = [item for item in achievements if not item.isAchievedByUnlock()]
        return achievements

    def getAchievementByID(self, achievementType, achievementID):
        return self.__data.get(achievementType, {}).get(achievementID, None)

    def getTotalVehicleAchievement(self):
        return self.__totalVehicleAchievement


class Achievement(object):

    def __init__(self, achievementData):
        self.__data = achievementData
        return

    def __getattr__(self, item):
        if item in self.__data:
            return self.__data[item]
        raise AttributeError
        return

    def __getitem__(self, item):
        try:
            return self.__data[item]
        except KeyError:
            raise KeyError

        return

    def __contains__(self, item):
        return item in self.__data

    def getActiveStage(self, currentValue, currentStage):
        stages = self.__data.get(b'stages', None)
        lastStage = len(stages)
        if not stages or currentStage > lastStage:
            return
        if currentValue >= stages[-1][b'value']:
            return stages[-1]
        else:
            for stageIndex in xrange(currentStage - 1 if currentStage else 0, lastStage):
                if currentValue < stages[stageIndex][b'value']:
                    return stages[stageIndex]

            return

    def isAchievedByUnlock(self):
        return self.__data.get(b'openByUnlock', False)

    def isAchievementCompleted(self, currentValue):
        stages = self.__data.get(b'stages', None)
        return stages and currentValue >= stages[-1][b'value']

    @staticmethod
    def isAnyStageCompleted(currentStage):
        return currentStage > 0

    def getCurrentDataFromDossier(self, dossierDescr):
        achievementType = self.__data.get(b'type', None)
        achievementID = self.__data.get(b'id', None)
        if achievementType not in dossierDescr or achievementID not in dossierDescr[achievementType]:
            return (0, 0, 0)
        return dossierDescr[achievementType][achievementID]

    def updateValueInDossier(self, dossierDescr, currentValue=None, currentStage=None, currentTimestamp=None):
        data = self.__data
        if currentValue is None or currentStage is None or currentTimestamp is None:
            currentValue, currentStage, currentTimestamp = self.getCurrentDataFromDossier(dossierDescr)
        activeStage = self.getActiveStage(currentValue, currentStage)
        if not activeStage:
            return
        else:
            if currentStage < activeStage[b'id'] and currentValue + 1 >= activeStage[b'value']:
                currentStage = activeStage[b'id']
                currentTimestamp = int(time())
            dossierDescr[data[b'type']][data[b'id']] = (currentValue + 1, currentStage, currentTimestamp)
            return

    def initializeValueInDossier(self, dossierDescr, currentValue=None, currentStage=None):
        data = self.__data
        currentValue = currentValue or 0
        currentStage = currentStage or 0
        currentTimestamp = int(time())
        activeStage = self.getActiveStage(currentValue, currentStage)
        if activeStage:
            currentStage = activeStage[b'id']
            if currentValue < activeStage[b'value']:
                currentStage -= 1
        dossierDescr[data[b'type']][data[b'id']] = (
         currentValue, currentStage, currentTimestamp)
        return (currentValue, currentStage, currentTimestamp)

    def getStageBonusByValue(self, currentStage):
        stages = self.__data.get(b'stages', None)
        if not stages or currentStage > len(stages):
            return {}
        return stages[currentStage - 1].get(b'rewards', {})

    def getStagePointsByValue(self, currentStage):
        stages = self.__data.get(b'stages', None)
        if not stages or currentStage > len(stages):
            return 0
        return stages[currentStage - 1][b'points']

    def getAllBonuses(self):
        result = {}
        stages = self.__data.get(b'stages', None)
        if not stages:
            return result
        else:
            for stage in stages:
                rewards = stage.get(b'rewards')
                if rewards:
                    for rewardName, rewardValue in viewitems(rewards):
                        result.setdefault(rewardName, []).append(rewardValue)

            return result

    def getStageValue(self, stage):
        stages = self.__data.get(b'stages')
        if stages is None or stage > len(stages) or stage <= 0:
            return 0
        return stages[stage - 1][b'value']

    def getID(self):
        return self.__data.get(b'id')


def init():
    g_cache.init()
    return
