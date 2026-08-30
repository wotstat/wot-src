import logging, operator, typing, weakref
from abc import ABCMeta, abstractmethod, abstractproperty
from collections import namedtuple
import constants
from constants import ATTACK_REASON, ATTACK_REASONS
from debug_utils import LOG_WARNING
from gui import GUI_NATIONS_ORDER_INDICES
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events import formatters, events_constants
from gui.server_events.formatters import getUniqueBonusTypes
from gui.shared.system_factory import collectModeNameKwargsByBonusType
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared.utils.requesters.ItemsRequester import RESEARCH_CRITERIA
from helpers import i18n, dependency, getLocalizedData
from items import vehicles
from shared_utils import CONST_CONTAINER
from skeletons.gui.game_control import IIGRController, IWotPlusController, IWinbackController, IWhiteTigerController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Any, Dict, Optional, List, Callable, Tuple
    from gui.shared.utils.requesters.ItemsRequester import RequestCriteria
_logger = logging.getLogger(__name__)
_AVAILABLE_GUI_TYPES_LABELS = {(constants.ARENA_BONUS_TYPE.REGULAR): (constants.ARENA_GUI_TYPE.RANDOM), 
   (constants.ARENA_BONUS_TYPE.TRAINING): (constants.ARENA_GUI_TYPE.TRAINING), 
   (constants.ARENA_BONUS_TYPE.TOURNAMENT_REGULAR): (constants.ARENA_GUI_TYPE.TRAINING), 
   (constants.ARENA_BONUS_TYPE.TOURNAMENT_COMP7): (constants.ARENA_GUI_TYPE.COMP7)}
_AVAILABLE_BONUS_TYPES_LABELS = {(constants.ARENA_BONUS_TYPE.CYBERSPORT): b'team7x7'}
_RELATIONS = formatters.RELATIONS
_RELATIONS_SCHEME = formatters.RELATIONS_SCHEME
_ET = constants.EVENT_TYPE
_TOKEN_REQUIREMENT_QUESTS = set(_ET.LIKE_BATTLE_QUESTS + _ET.LIKE_TOKEN_QUESTS)

def _getArenaBonusType(preBattleCond):
    if preBattleCond is not None:
        bonusTypeNode = preBattleCond.getConditions().find(b'bonusTypes')
        if bonusTypeNode is not None:
            return getUniqueBonusTypes(bonusTypeNode.getValue())
    return {constants.ARENA_BONUS_TYPE.UNKNOWN}


def _getArenaBonusTypeForUnit(preBattleCond):
    if preBattleCond is not None:
        squadNode = preBattleCond.getConditions().find(b'isSquad')
        if squadNode is not None and squadNode.getValue():
            return b'squad'
        bonusTypeNode = preBattleCond.getConditions().find(b'bonusTypes')
        if bonusTypeNode is not None:
            bonusTypes = list(bonusTypeNode.getValue())
            if len(bonusTypes) == 1 and bonusTypes[0] in _AVAILABLE_BONUS_TYPES_LABELS:
                return _AVAILABLE_BONUS_TYPES_LABELS[bonusTypes[0]]
    return b'formation'


class GROUP_TYPE(CONST_CONTAINER):
    OR = b'or'
    AND = b'and'


_SORT_ORDER = (b'igrType', b'premiumPlusAccount', b'premiumAccount', b'inClan', b'GR', b'accountDossier', b'vehiclesUnlocked', b'vehiclesOwned', b'token', b'hasReceivedMultipliedXP', b'vehicleDossier', b'vehicleDescr', b'customization', b'bonusTypes', b'isSquad', b'mapCamouflageKind', b'geometryNames', b'win', b'isAlive', b'achievements', b'results', b'unitResults', b'vehicleKills', b'vehicleDamage', b'vehicleStun', b'clanKills', b'multiStunEvent', b'firstBloodcumulative', b'cumulativeExt', b'cumulativeSum', b'vehicleKillsCumulative', b'vehicleDamageCumulative', b'vehicleStunCumulative')
_SORT_ORDER_INDICES = dict((name, idx) for idx, name in enumerate(_SORT_ORDER))

def _handleRelation(relation, source, toCompare):
    if relation == _RELATIONS.EQ:
        return source == toCompare
    if relation == _RELATIONS.GT:
        return source > toCompare
    if relation == _RELATIONS.GTQ:
        return source >= toCompare
    if relation == _RELATIONS.LS:
        return source < toCompare
    if relation == _RELATIONS.LSQ:
        return source <= toCompare
    if relation == _RELATIONS.NEQ:
        return source != toCompare
    LOG_WARNING(b'Unknown kind of values relation', relation, source, toCompare)
    return False


def _findRelation(condDataKeys):
    res = set(_RELATIONS.ALL()) & set(condDataKeys)
    if res:
        return res.pop()
    else:
        return


def _getNodeValue(node, key, default=None):
    if key in node:
        dNode = dict(node[key])
        if b'value' in dNode:
            return dNode[b'value']
    return default


def _getRelationValueFromConditionData(conditionData):
    relation = _findRelation(conditionData.keys())
    relationValue = _getNodeValue(conditionData, relation)
    return relationValue


def _getCustomTitleValueFromConditionData(conditionData):
    generalValue = conditionData.get(b'value')
    if generalValue:
        if isinstance(generalValue, tuple):
            return generalValue[1]
        return generalValue
    generalValue = _getNodeValue(conditionData, b'max')
    if generalValue:
        return generalValue
    generalValue = _getNodeValue(conditionData, b'count')
    if generalValue:
        return generalValue
    generalValue = _getRelationValueFromConditionData(conditionData)
    return generalValue


def getCustomDescriptionValueFromConditionData(conditionData):
    return _getCustomTitleValueFromConditionData(conditionData)


def iterKeyPath(key):
    splitData = key.split(b':')
    if len(splitData) == 2:
        poName, pathInPo = key.split(b':')
        if len(poName) > 1:
            yield poName[1:]
            for v in pathInPo.split(b'/'):
                yield v

    return


def _getDescriptionString(data, keyName, valueFunc):
    descrData = data.get(keyName)
    if descrData:
        if b'key' in descrData:
            textResource = R.strings.recursiveDyn(iterKeyPath(descrData[b'key']))
            if textResource.exists():
                value = valueFunc(data)
                if isinstance(value, (int, float)):
                    pluralCount = int(value)
                    value = backport.getNiceNumberFormat(value)
                    return backport.ntext(textResource(), pluralCount, value=value)
                return backport.text(textResource())
            return descrData[b'key']
        return getLocalizedData(data, keyName)
    else:
        return


_VehicleData = namedtuple(b'_VehicleData', b'isAvailable, discountValue, discountType')

def _prepareVehData(vehIntCDsList, predicate=None):
    predicate = predicate or (lambda *args: True)
    items = dependency.instance(IItemsCache).items
    result = []
    for vehIntCD in vehIntCDsList:
        vehicle = items.getItemByCD(vehIntCD)
        result.append((
         vehicle,
         _VehicleData(isAvailable=not vehicle.isInInventory or predicate(vehicle), discountValue=None, discountType=None)))

    return result


class _Typeable(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def classType(self):
        return


class _Negatable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def negate(self):
        return


class _Updatable(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, other, groupType):
        return


class _AvailabilityCheckable(object):
    __metaclass__ = ABCMeta

    def isAvailable(self, *args, **kwargs):
        return self._isAvailable(*args, **kwargs)

    def _isAvailable(self, *args, **kwargs):
        return True


class _Condition(_Typeable):

    def __init__(self, name, data, uniqueName):
        super(_Condition, self).__init__()
        self._name = name
        self._data = data
        self._uniqueName = uniqueName
        return

    @property
    def classType(self):
        return b'Condition'

    def getName(self):
        return self._name

    def getData(self):
        return self._data

    def getUniqueName(self):
        return self._uniqueName

    def clearItemsCache(self):
        return

    def getValue(self):
        raise SoftException(b'This method should not be reached in this context')
        return

    def getCustomTitle(self):
        return _getDescriptionString(self._data, b'title', _getCustomTitleValueFromConditionData)

    def getCustomDescription(self):
        return _getDescriptionString(self._data, b'description', getCustomDescriptionValueFromConditionData)

    def isHidden(self):
        return self._data.get(b'hideInGui', False)

    @property
    def progressID(self):
        return self._data.get(b'progressID')

    def getProgressID(self):
        data = self._data.get(b'value', {})
        if not data or not len(data) > 1:
            return None
        return data[0]


class _ConditionsGroup(_AvailabilityCheckable, _Negatable, _Typeable):

    def __init__(self, groupType, isNegative=False):
        super(_ConditionsGroup, self).__init__()
        self.items = []
        self.type = groupType
        self.isNegative = isNegative
        return

    def __repr__(self):
        return b'%s<count=%d>' % (self.__class__.__name__, len(self.items))

    @property
    def classType(self):
        return b'ConditionsGroup'

    def getName(self):
        return self.type

    def isAvailable(self, *args, **kwargs):
        res = self._isAvailable(*args, **kwargs)
        if self.isNegative:
            res = not res
        return res

    def add(self, condition):
        if isinstance(condition, (list, tuple)):
            for cond in condition:
                self._addNewCondition(cond)

        else:
            self._addNewCondition(condition)
        return

    def remove(self, condition):
        self.items.remove(condition)
        return

    def find(self, condName):
        for cond in self.items:
            if cond.getName() == condName:
                return cond

        return

    def findAll(self, condName):
        result = []
        for cond in self.items:
            if cond.getName() == condName:
                result.append(cond)

        return result

    def negate(self):
        self.isNegative = not self.isNegative
        return

    def isEmpty(self):
        return not self.items

    def getSortedItems(self):
        return sorted(self.items, cmp=self._sortItems, key=operator.methodcaller(b'getName'))

    def isHidden(self):
        return False

    @classmethod
    def _sortItems(cls, a, b):
        if a not in _SORT_ORDER:
            return 1
        if b not in _SORT_ORDER:
            return -1
        return _SORT_ORDER_INDICES[a] - _SORT_ORDER_INDICES[b]

    def _addNewCondition(self, cond):
        if isinstance(cond, _Updatable):
            otherCond = self.find(cond.getName())
            if otherCond is None:
                self.items = [c for c in self.items if not cond.update(c, self.type)]
            elif otherCond.update(cond, self.type):
                cond = None
        if cond is not None:
            self.items.append(cond)
        return


class _Requirement(_Condition, _AvailabilityCheckable, _Negatable):
    itemsCache = dependency.descriptor(IItemsCache)

    def __repr__(self):
        return b'%s<>' % self.__class__.__name__


class _VehicleRequirement(_Requirement):

    def _isAvailable(self, vehicle):
        return True


class _VehsListParser(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        self.__vehIntCDs = None
        return

    def isAnyVehicleAcceptable(self):
        return self._isAnyVehicleAcceptable(self._data)

    def getFilterCriteria(self, data):
        types, nations, levels, classes, roles = self._parseFilters(data)
        defaultCriteria = self._getDefaultCriteria()
        if types:
            criteria = REQ_CRITERIA.VEHICLE.SPECIFIC_BY_CD(types)
        else:
            criteria = REQ_CRITERIA.EMPTY
            if nations:
                criteria |= REQ_CRITERIA.NATIONS(nations)
            if levels:
                criteria |= REQ_CRITERIA.VEHICLE.LEVELS(levels)
            if classes:
                criteria |= REQ_CRITERIA.VEHICLE.CLASSES(classes)
            if roles:
                criteria |= REQ_CRITERIA.VEHICLE.ROLES(roles)
        return self._postProcessCriteria(defaultCriteria, criteria)

    def _clearItemsCache(self):
        self.__vehIntCDs = None
        return

    def _postProcessCriteria(self, defaultCriteria, criteria):
        return defaultCriteria | criteria

    def _isAnyVehicleAcceptable(self, data):
        return not set(data) & {1, 2, 3, 4, 5}

    def _getDefaultCriteria(self):
        return REQ_CRITERIA.DISCLOSABLE

    def _getVehIntCDs(self, data):
        if self.__vehIntCDs is None:
            self.__vehIntCDs = self.itemsCache.items.getVehicles(self.getFilterCriteria(data)).keys()
        return self.__vehIntCDs

    def _parseFilters(self, data):
        types, nations, levels, classes, roles = (None, None, None, None, None)
        if b'types' in data:
            types = _getNodeValue(data, b'types')
        if b'nations' in data:
            nations = _getNodeValue(data, b'nations')
            nations = sorted(nations, key=GUI_NATIONS_ORDER_INDICES.get)
        if b'levels' in data:
            levels = _getNodeValue(data, b'levels')
        if b'classes' in data:
            acceptedClasses = _getNodeValue(data, b'classes')
            classes = [name for name, index in constants.VEHICLE_CLASS_INDICES.items() if index in acceptedClasses]
        if b'roles' in data:
            acceptedRoles = _getNodeValue(data, b'roles')
            roles = [constants.ROLE_TYPE_TO_LABEL[roleID] for roleID in acceptedRoles]
        return (types, nations, levels, classes, roles)


class _VehsListCondition(_Condition, _VehsListParser):

    def __init__(self, name, data, path):
        super(_VehsListCondition, self).__init__(name, dict(data), path)
        self._relation = _findRelation(self._data.keys())
        self._relationValue = _getNodeValue(self._data, self._relation)
        self._isNegative = False
        return

    @property
    def relationValue(self):
        return self._relationValue

    @property
    def relation(self):
        return self._relation

    @property
    def data(self):
        return self._data

    def isNegative(self):
        return self._isNegative

    def getVehiclesList(self):
        return self._getVehIntCDs(self._data)

    def negate(self):
        if self._relation is not None:
            self._relation = _RELATIONS.getOppositeRelation(self._relation)
        else:
            self._isNegative = not self._isNegative
        return

    def clearItemsCache(self):
        self._clearItemsCache()
        return

    def getVehiclesData(self):
        return []

    def parseFilters(self):
        return self._parseFilters(self._data)

    def getFireStarted(self):
        return _getNodeValue(self._data, b'fireStarted', default=False)

    def getAttackReasonIdx(self):
        return _getNodeValue(self._data, b'attackReason', default=ATTACK_REASON.getIndex(ATTACK_REASON.SHOT))

    def getAttackReason(self):
        return ATTACK_REASONS[self.getAttackReasonIdx()]

    def getLabelKey(self):
        raise SoftException(b'This method should not be reached in this context')
        return


class _VehsListRequirement(_VehsListCondition, _AvailabilityCheckable, _Negatable):

    def __init__(self, name, data, path):
        super(_VehsListRequirement, self).__init__(name, data, path)
        if self._relation is None:
            self._relation = _RELATIONS.GTQ
            self._relationValue = 1
        return

    def __repr__(self):
        return b'%s<%s=%r>' % (self.__class__.__name__, self._relation, self._relationValue)

    def _isAvailable(self):
        vehIntCDsList = self._getVehIntCDs(self._data)
        if self._relation is not None:
            return _handleRelation(self._relation, len(filter(self._checkVehicle, vehIntCDsList)), self._relationValue)
        else:
            return True

    def _checkVehicle(self, vehIntCD):
        return True


class AndGroup(_ConditionsGroup):

    def __init__(self, isNegative=False):
        super(AndGroup, self).__init__(GROUP_TYPE.AND, isNegative)
        return

    def _isAvailable(self, *args, **kwargs):
        res = True
        for cond in self.items:
            res = cond.isAvailable(*args, **kwargs)
            if not res:
                return res

        return res


class OrGroup(_ConditionsGroup):

    def __init__(self, isNegative=False):
        super(OrGroup, self).__init__(GROUP_TYPE.OR, isNegative)
        return

    def _isAvailable(self, *args, **kwargs):
        for cond in self.items:
            if cond.isAvailable(*args, **kwargs):
                return True

        return False


class IGR(_Requirement, _Updatable):
    igrCtrl = dependency.descriptor(IIGRController)

    def __init__(self, path, data):
        super(IGR, self).__init__(b'igrType', dict(data), path)
        self._igrTypes = {self._data.get(b'value')}
        return

    def getIgrTypes(self):
        return self._igrTypes

    def negate(self):
        igrTypes = constants.IGR_TYPE
        self._igrTypes ^= {igrTypes.BASE, igrTypes.PREMIUM}
        return

    def update(self, other, groupType):
        if groupType == GROUP_TYPE.OR:
            if other.getName() == b'igrType':
                self._igrTypes |= other._igrTypes
                return True
        return False

    def _isAvailable(self):
        return self.igrCtrl.getRoomType() in self._igrTypes


class GlobalRating(_Requirement):

    def __init__(self, path, data):
        super(GlobalRating, self).__init__(b'GR', dict(data), path)
        self._relation = _findRelation(self._data.keys())
        self._relationValue = float(_getNodeValue(self._data, self._relation))
        return

    @property
    def relation(self):
        return self._relation

    @property
    def relationValue(self):
        return self._relationValue

    def negate(self):
        self._relation = _RELATIONS.getOppositeRelation(self._relation)
        return

    def _isAvailable(self):
        if self._relationValue is None:
            return False
        else:
            return _handleRelation(self._relation, self.itemsCache.items.stats.globalRating, self._relationValue)


class PremiumAccount(_Requirement):

    def __init__(self, path, data):
        super(PremiumAccount, self).__init__(b'premiumAccount', dict(data), path)
        self._needValue = self._data.get(b'value')
        return

    def isPremiumNeeded(self):
        return self._needValue

    def negate(self):
        self._needValue = not self._needValue
        return

    def _isAvailable(self):
        if self._needValue is not None:
            return self.itemsCache.items.stats.isPremium == self._needValue
        else:
            return True


class PremiumPlusAccount(_Requirement):

    def __init__(self, path, data):
        super(PremiumPlusAccount, self).__init__(b'premiumPlusAccount', dict(data), path)
        self._needValue = self._data.get(b'value')
        return

    def isPremiumNeeded(self):
        return self._needValue

    def negate(self):
        self._needValue = not self._needValue
        return

    def _isAvailable(self):
        if self._needValue is not None:
            return self.itemsCache.items.stats.isActivePremium(constants.PREMIUM_TYPE.PLUS) == self._needValue
        else:
            return True


class WotPlus(_Requirement):
    wotPlusController = dependency.descriptor(IWotPlusController)

    def __init__(self, path, data):
        super(WotPlus, self).__init__(b'wotPlus', dict(data), path)
        self._needValue = self._data.get(b'value')
        return

    def isWotPlusNeeded(self):
        return self._needValue

    def negate(self):
        self._needValue = not self._needValue
        return

    def _isAvailable(self):
        return self.wotPlusController.isEnabled() == self._needValue


class VersusAIProgression(_Requirement):

    def __init__(self, path, data):
        super(VersusAIProgression, self).__init__(b'versusAIProgression', dict(data), path)
        self._value = self._data.get(b'value')
        self._isNegate = False
        return

    def negate(self):
        self._isNegate = not self._isNegate
        return

    def _isAvailable(self):
        winbackController = dependency.getInstanceIfHas(IWinbackController)
        if winbackController and winbackController.isEnabled() and winbackController.isProgressionEnabled():
            isMatched = winbackController.progressionName == self._value
            if self._isNegate:
                return not isMatched
            return isMatched
        return False


class InClan(_Requirement):

    def __init__(self, path, data):
        super(InClan, self).__init__(b'inClan', dict(data), path)
        self._ids = self._data.get(b'value') or None
        self._isNegative = False
        return

    def getClanIds(self):
        return self._ids

    def isNegative(self):
        return self._isNegative

    def negate(self):
        self._isNegative = not self._isNegative
        return

    def _isAvailable(self):
        clanDBID = self.itemsCache.items.stats.clanDBID
        if self._ids is not None:
            if not self._isNegative:
                return clanDBID in self._ids
            return clanDBID not in self._ids
        else:
            return bool(clanDBID) != self._isNegative


class Token(_Requirement):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, path, data):
        super(Token, self).__init__(b'token', dict(data), path)
        self._id = _getNodeValue(self._data, b'id')
        self._consumable = b'consume' in self._data
        self._relation = _findRelation(self._data.keys())
        self._relationValue = int(_getNodeValue(self._data, self._relation, 0))
        self._complex = formatters.parseComplexToken(self._id)
        return

    def isConsumable(self):
        return self._consumable

    def getID(self):
        return self._id

    def isDisplayable(self):
        return self._complex.isDisplayable

    def isDailyQuest(self):
        return self.getID().startswith(events_constants.DAILY_QUEST_TOKEN_PREFIX)

    def getUserName(self):
        userName = self.eventsCache.prefetcher.getTokenInfo(self._complex.styleID)
        return userName

    def isOnSale(self):
        return self.eventsCache.prefetcher.isTokenOnSale(self._complex.webID)

    def getImage(self, size):
        return self.eventsCache.prefetcher.getTokenImage(self._complex.styleID, size)

    def getStyleID(self):
        return self._complex.styleID

    def getWebID(self):
        return self._complex.webID

    def negate(self):
        self._relation = _RELATIONS.getOppositeRelation(self._relation)
        return

    def getNeededCount(self):
        if self._relation == _RELATIONS.GT:
            return self._relationValue + 1
        return self._relationValue

    def getReceivedCount(self):
        return self.eventsCache.questsProgress.getTokenCount(self.getID())

    def _isAvailable(self):
        return _handleRelation(self._relation, self.eventsCache.questsProgress.getTokenCount(self._id), self._relationValue)


class QuestCondition(_Requirement):
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, path, data):
        super(QuestCondition, self).__init__(b'quest', dict(data), path)
        self._id = _getNodeValue(self._data, b'id')
        self._relation = _findRelation(self._data.keys())
        self._relationValue = int(_getNodeValue(self._data, self._relation, 0))
        return

    def getID(self):
        return self._id

    def negate(self):
        self._relation = _RELATIONS.getOppositeRelation(self._relation)
        return

    def isQuestCompleted(self):
        quest = self.eventsCache.getQuestByID(self._id)
        return quest and quest.isCompleted()

    def _isAvailable(self):
        return True


class TokenQuestToken(Token):

    def _isAvailable(self):
        return True


class VehiclesUnlocked(_VehsListRequirement):

    def __init__(self, path, data):
        super(VehiclesUnlocked, self).__init__(b'vehiclesUnlocked', dict(data), path)
        return

    def _checkVehicle(self, vehicleIntCD):
        vehicle = self.itemsCache.items.getItemByCD(vehicleIntCD)
        return vehicle.isUnlocked and not vehicle.isInitiallyUnlocked

    def _getDefaultCriteria(self):
        return RESEARCH_CRITERIA.VEHICLE_TO_UNLOCK


class VehiclesOwned(_VehsListRequirement):

    def __init__(self, path, data):
        super(VehiclesOwned, self).__init__(b'vehiclesOwned', dict(data), path)
        return

    def _checkVehicle(self, vehicleIntCD):
        vehicle = self.itemsCache.items.getItemByCD(vehicleIntCD)
        return vehicle.isInInventory


class PremiumVehicle(_VehicleRequirement):

    def __init__(self, path, data):
        super(PremiumVehicle, self).__init__(b'premiumVehicle', dict(data), path)
        self._needValue = self._data.get(b'value')
        return

    def __repr__(self):
        return b'PremiumVehicle<value=%r>' % self._needValue

    def negate(self):
        self._needValue = not self._needValue
        return

    def getFilterCriteria(self, data):
        criteria = REQ_CRITERIA.DISCLOSABLE
        if self._needValue:
            return criteria | REQ_CRITERIA.VEHICLE.PREMIUM
        return criteria | ~REQ_CRITERIA.VEHICLE.PREMIUM

    def _isAvailable(self, vehicle):
        return vehicle.isPremium == self._needValue


class XPMultipliedVehicle(_VehicleRequirement):

    def __init__(self, path, data):
        super(XPMultipliedVehicle, self).__init__(b'hasReceivedMultipliedXP', dict(data), path)
        self._needValue = self._data.get(b'value')
        return

    def __repr__(self):
        return b'XPMultipliedVehicle<value=%r>' % self._needValue

    def negate(self):
        self._needValue = not self._needValue
        return

    def isAvailableReason(self, vehicle):
        isOk = self._isAvailable(vehicle)
        if self._needValue:
            reason = b'xpMultReceived'
        else:
            reason = b'xpMultReceived/not'
        return (isOk, reason)

    def getValue(self):
        return self._needValue

    def _isAvailable(self, vehicle):
        return (vehicle.dailyXPFactor == -1) == self._needValue


class WtTicketRequired(_VehicleRequirement):
    __wtController = dependency.descriptor(IWhiteTigerController)

    def __init__(self, path, data):
        super(WtTicketRequired, self).__init__(b'wtTicketRequired', dict(data), path)
        self._needValue = True
        return

    def __repr__(self):
        return b'%s<value=%r>' % (self.__class__.__name__, self._needValue)

    def negate(self):
        self._needValue = not self._needValue
        return

    def isAvailableReason(self, vehicle):
        return (
         self._isAvailable(vehicle), b'ticketsShortage')

    def getValue(self):
        return self._needValue


class InstalledItemCondition(_VehicleRequirement):

    def __init__(self, path, itemType, data, customData):
        super(InstalledItemCondition, self).__init__(b'installedItem', dict(data), path)
        self._itemType = itemType
        self._itemsIds = self._data.get(b'value', set())
        self._isInstalled = True
        self._data.update(customData)
        return

    def isNegative(self):
        return not self._isInstalled

    def getItemType(self):
        return self._itemType

    def getItemsList(self):
        return [self.itemsCache.items.getItemByCD(intCD) for intCD in self._itemsIds]

    def negate(self):
        self._isInstalled = not self._isInstalled
        return

    def _isAvailable(self, vehicle):
        for item in self.getItemsList():
            if item.isInstalled(vehicle) == self._isInstalled:
                return True

        return False


class InstalledModulesOnVehicle(_VehicleRequirement):
    MODULES_KEYS = (b'guns', b'engines', b'chassis', b'turrets', b'radios', b'optionalDevice')

    def __init__(self, path, data):
        super(InstalledModulesOnVehicle, self).__init__(b'installedModules', dict(data), path)
        self._modulesConditions = []
        customData = {b'title': (self._data.get(b'title')), 
           b'description': (self._data.get(b'description'))}
        for key, value in self._data.iteritems():
            if key in self.MODULES_KEYS:
                path = b'%s.%s' % (path, key)
                self._modulesConditions.append(InstalledItemCondition(path, key, value, customData))

        return

    def __repr__(self):
        return b'InstalledModulesOnVehicle<value=%r>' % self.getModulesConditions()

    def negate(self):
        for c in self._modulesConditions:
            c.negate()

        return

    def getModulesConditions(self):
        return self._modulesConditions

    def _isAvailable(self, vehicle):
        for c in self._modulesConditions:
            if not c.isAvailable(vehicle):
                return False

        return True


class VehicleDescr(_VehicleRequirement, _VehsListParser, _Updatable):

    def __init__(self, path, data):
        super(VehicleDescr, self).__init__(b'vehicleDescr', dict(data), path)
        self._otherCriteria = REQ_CRITERIA.EMPTY
        self._isNegative = False
        return

    def clearItemsCache(self):
        self._clearItemsCache()
        return

    def negate(self):
        self._isNegative = not self._isNegative
        return

    def update(self, other, groupType):
        if groupType != GROUP_TYPE.AND:
            return False
        if other.getName() in (b'vehicleDescr', b'premiumVehicle'):
            self._otherCriteria |= other.getFilterCriteria(other._data)
            return True
        return False

    def getVehiclesList(self):
        return self._getVehIntCDs(self._data)

    def _postProcessCriteria(self, defaultCriteria, criteria):
        if self._isNegative:
            criteria = ~criteria
        return defaultCriteria | criteria | self._otherCriteria

    def _isAvailable(self, vehicle):
        return vehicle.intCD in self._getVehIntCDs(self._data)

    def parseFilters(self):
        return self._parseFilters(self._data)


class EarlyAccessVehicleDescr(VehicleDescr):

    def __init__(self, data):
        super(EarlyAccessVehicleDescr, self).__init__(b'', data)
        return

    def _getDefaultCriteria(self):
        return REQ_CRITERIA.EMPTY


class _DossierValue(_Requirement):

    def __init__(self, name, data, path):
        super(_DossierValue, self).__init__(name, dict(data), path)
        self._recordName = _getNodeValue(self._data, b'record', b'').split(b':')
        self._average = b'average' in self._data
        self._relation = _findRelation(self._data.keys())
        self._relationValue = float(_getNodeValue(self._data, self._relation, 0.0))
        return

    @property
    def relation(self):
        return self._relation

    @property
    def relationValue(self):
        return self._relationValue

    @property
    def average(self):
        return self._average

    @property
    def recordName(self):
        return self._recordName

    def negate(self):
        self._relation = _RELATIONS.getOppositeRelation(self._relation)
        return

    def _checkDossier(self, dossier):
        block, record = self._recordName
        dossierDescr = dossier.getDossierDescr()
        dossierValue = dossierDescr[block][record]
        if self._average:
            battlesCount = dossierDescr[block][b'battlesCount']
            dossierValue /= float(battlesCount or 1)
        return _handleRelation(self._relation, dossierValue, self._relationValue)


class AccountDossierValue(_DossierValue):

    def __init__(self, path, data):
        super(AccountDossierValue, self).__init__(b'accountDossier', dict(data), path)
        return

    def _isAvailable(self):
        return self._checkDossier(self.itemsCache.items.getAccountDossier())


class BattleBonusType(_Condition, _Negatable):

    def __init__(self, path, data):
        super(BattleBonusType, self).__init__(b'bonusTypes', dict(data), path)
        self._types = self._data.get(b'value')
        return

    def __repr__(self):
        return b'BattleBonusType<types=%r>' % self._types

    def negate(self):
        newTypes = []
        for bt in constants.ARENA_BONUS_TYPE.RANGE:
            if bt not in self._types:
                newTypes.append(bt)

        self._types = newTypes
        return

    def getValue(self):
        return self._types


class BattleSquad(_Condition, _Negatable):

    def __init__(self, path, data):
        super(BattleSquad, self).__init__(b'isSquad', dict(data), path)
        self._isSquad = self._data.get(b'value')
        return

    def __repr__(self):
        return b'BattleSquad<isSquad=%r>' % self._isSquad

    def negate(self):
        self._isSquad = not self._isSquad
        return

    def getValue(self):
        return self._isSquad


class BattleClanMembership(_Condition, _Negatable):

    def __init__(self, path, data, preBattleCondProxy=None):
        super(BattleClanMembership, self).__init__(b'clanMembership', dict(data), path)
        self._value = self._data.get(b'value')
        self.__proxy = weakref.proxy(preBattleCondProxy)
        return

    def __repr__(self):
        return b'BattleClanMembership<relation=%r; bonusType=%s>' % (
         self._value, _getArenaBonusTypeForUnit(self.__proxy))

    def negate(self):
        return

    def getValue(self):
        return self._value

    def getArenaBonusType(self):
        return _getArenaBonusTypeForUnit(self.__proxy)


class BattleCamouflage(_Condition, _Negatable):

    def __init__(self, path, data):
        super(BattleCamouflage, self).__init__(b'camouflageKind', dict(data), path)
        self._camos = self._data.get(b'value')
        return

    def __repr__(self):
        return b'BattleCamouflage<camos=%r>' % self._camos

    def getValue(self):
        return self._camos

    def negate(self):
        newCamos = []
        for _, camoID in vehicles.CAMOUFLAGE_KINDS.iteritems():
            if camoID not in self._camos:
                newCamos.append(camoID)

        self._camos = newCamos
        return


class BattleMap(_Condition, _Negatable):

    def __init__(self, path, data):
        super(BattleMap, self).__init__(b'geometryNames', dict(data), path)
        self._maps = self._data.get(b'value')
        self._isNegative = False
        return

    def __repr__(self):
        return b'BattleMap<maps=%r>' % self._maps

    def negate(self):
        self._isNegative = not self._isNegative
        return

    def isNegative(self):
        return self._isNegative

    def getMaps(self):
        return self._maps


class Win(_Condition, _Negatable):

    def __init__(self, path, data):
        super(Win, self).__init__(b'win', dict(data), path)
        self._isWin = True
        return

    def __repr__(self):
        return b'Win<value=%r>' % self._isWin

    def negate(self):
        self._isWin = not self._isWin
        return

    def getValue(self):
        return self._isWin


class Survive(_Condition, _Negatable):

    def __init__(self, path, data):
        super(Survive, self).__init__(b'isAlive', dict(data), path)
        self._isAlive = True
        return

    def __repr__(self):
        return b'Survive<value=%r>' % self._isAlive

    def negate(self):
        self._isAlive = not self._isAlive
        return

    def getValue(self):
        return self._isAlive


class CorrespondedCamouflage(_Requirement):

    def __init__(self, path, data):
        super(CorrespondedCamouflage, self).__init__(b'correspondedCamouflage', dict(data), path)
        self._isInstalled = True
        return

    def __repr__(self):
        return b'CorrespondedCamouflage<value=%r>' % self._isInstalled

    def negate(self):
        self._isInstalled = not self._isInstalled
        return

    def getValue(self):
        return self._isInstalled


class Achievements(_Condition, _Negatable, _Updatable):

    def __init__(self, path, data):
        super(Achievements, self).__init__(b'achievements', dict(data), path)
        self._achieves = set(self._data.get(b'value'))
        self._isNegative = False
        return

    def __repr__(self):
        return b'Achievements<idx=%r>' % self._achieves

    def negate(self):
        self._isNegative = not self._isNegative
        return

    def update(self, other, groupType):
        if groupType == GROUP_TYPE.OR and other.getName() == b'achievements':
            self._achieves |= other._achieves
            return True
        return False

    def isNegative(self):
        return self._isNegative

    def getValue(self):
        return self._achieves


class ClanKills(_Condition, _Negatable):

    def __init__(self, path, data):
        super(ClanKills, self).__init__(b'clanKills', dict(data), path)
        self._camos2ids = {}
        self._isNegative = False
        for camoName, ids in data:
            self._camos2ids[camoName] = ids

        return

    def __repr__(self):
        return b'ClanKills<camos=%r>' % str(self._camos2ids)

    def negate(self):
        self._isNegative = not self._isNegative
        return

    def isNegative(self):
        return self._isNegative

    def getCamos2ids(self):
        return self._camos2ids


class Customization(_Requirement):

    def __init__(self, path, data):
        super(Customization, self).__init__(b'customization', dict(data), path)
        self._styleId = self._data.get(b'styleId')
        self._isInstalled = True
        return

    def __repr__(self):
        return b'Customization<styleId=%d; isInstalled=%r>' % (self._styleId, self._isInstalled)

    def negate(self):
        self._isInstalled = not self._isInstalled
        return

    def getValue(self):
        return self._isInstalled


class Cumulativable(_Condition):
    __metaclass__ = ABCMeta

    def getProgressPerGroup(self, curProgData=None, prevProgData=None):
        return self._parseProgress(curProgData, prevProgData)

    def getUserString(self):
        return b''

    @abstractmethod
    def getTotalValue(self):
        return

    @abstractmethod
    def getBonusData(self):
        return

    @abstractmethod
    def getKey(self):
        return

    def _parseProgress(self, curProgData, prevProgData):
        result = {}
        bonus = self.getBonusData()
        curProgData = bonus.getProgress() if curProgData is None else curProgData
        prevProgData = {} if prevProgData is None else prevProgData
        if bonus is None:
            return result
        else:
            key = self.getKey()
            groupBy = bonus.getGroupByValue()
            total = self.getTotalValue()
            if groupBy is None:
                curProg = curProgData.get(None, {})
                prevProg = prevProgData.get(None, {})
                diff = self.__getProgDiff(curProg, prevProg)
                result[None] = (
                 min(curProg.get(key, 0), total), total, diff, self.__isProgressCompleted(curProg))
            else:
                for gByKey, progress in curProgData.iteritems():
                    diff = self.__getProgDiff(progress, prevProgData.get(gByKey, {}))
                    result[gByKey] = (min(progress.get(key, 0), total), total, diff, self.__isProgressCompleted(progress))

            return result

    def __getProgDiff(self, curProg, prevProg):
        key = self.getKey()
        total = self.getTotalValue()
        current = min(curProg.get(key, 0), total)
        curBonusCount = curProg.get(b'bonusCount', 0)
        prevBonusCount = prevProg.get(b'bonusCount', 0) if prevProg else 0
        if curBonusCount > prevBonusCount:
            if self.__isProgressCompleted(curProg):
                return total - min(prevProg.get(key, 0), total)
            return current
        return current - min(prevProg.get(key, 0), total)

    def __isProgressCompleted(self, progress):
        bonusLimit = self.getBonusData().getBonusLimit()
        if bonusLimit is not None:
            return progress.get(b'bonusCount', 0) >= bonusLimit
        else:
            return False


class BattlesCount(Cumulativable):

    def __init__(self, path, data, bonusCond, preBattleCond=None):
        super(BattlesCount, self).__init__(b'battles', dict(data), path)
        self._bonus = weakref.proxy(bonusCond)
        self._bonusTypes = _getArenaBonusType(preBattleCond)
        return

    def __repr__(self):
        return b'BattlesCount<key=%s; total=%d>' % (self.getKey(), self.getTotalValue())

    def getUserString(self):
        result = []
        for bType in self._bonusTypes:
            kwargs = collectModeNameKwargsByBonusType(bType) or {}
            result.append(unicode(i18n.makeString(QUESTS.getDetailsDossier(bType, self.getKey()), **kwargs)))

        if not result:
            _logger.warning(b'There are no matching condition strings for selected arenaBonusTypes')
            return u''
        return (u', ').join(result)

    def getTotalValue(self):
        return _getNodeValue(self._data, b'count', 0)

    def hasUpperLimit(self):
        return _getNodeValue(self._data, b'upperLimit', False)

    def getBonusData(self):
        return self._bonus

    def getKey(self):
        return b'battlesCount'


class BattleResults(_Condition, _Negatable, _Updatable):
    TOP_RANGE_HIGHEST = 1
    TOP_RANGE_LOWEST = 15

    def __init__(self, path, data, localeKey=b'single'):
        super(BattleResults, self).__init__(b'results', dict(data), path)
        self._keyName = _getNodeValue(self._data, b'key')
        self._max = (
         self.TOP_RANGE_HIGHEST, int(_getNodeValue(self._data, b'max', self.TOP_RANGE_LOWEST)))
        self._isTotal = b'total' in self._data
        self._isAvg = b'average' in self._data
        self._relation = _findRelation(self._data.keys())
        self._relationValue = _getNodeValue(self._data, self._relation)
        self._localeKey = localeKey
        self._isNegative = False
        aggregatedData = self._data.get(b'plus', [])
        keys = []
        for keyData in aggregatedData:
            keyNode = dict([keyData])
            key = _getNodeValue(keyNode, b'key')
            if key:
                keys.append(key)

        self._aggregatedKeys = tuple(sorted(keys))
        return

    def __repr__(self):
        return b'BattleResults<key=%s; %s=%r; max=%r; total=%r; avg=%r>' % (
         self._keyName, self._relation, self._relationValue, self._max,
         self._isTotal, self._isAvg)

    def getAggregatedKeys(self):
        return self._aggregatedKeys

    @property
    def relationValue(self):
        return self._relationValue

    @property
    def localeKey(self):
        return self._localeKey

    @property
    def keyName(self):
        return self._keyName

    @property
    def relation(self):
        return self._relation

    def isNegative(self):
        return self._isNegative

    def isAvg(self):
        return self._isAvg

    def isTotal(self):
        return self._isTotal

    def getMaxRange(self):
        return self._max

    def getTopRange(self):
        if not self._isNegative:
            return self._max
        return (
         min(self._max[1] + 1, self.TOP_RANGE_LOWEST), self.TOP_RANGE_LOWEST)

    def update(self, other, groupType):
        if groupType == GROUP_TYPE.AND:
            if other.getName() == b'results' and self.keyName == other.keyName and self.relation == other.relation:
                topRange, otherTopRange = self.getTopRange(), other.getTopRange()
                self._max = (
                 max(topRange[0], otherTopRange[0]),
                 min(topRange[1], otherTopRange[1]))
                return True
        return False

    def negate(self):
        self._relation = _RELATIONS.getOppositeRelation(self._relation)
        self._isNegative = not self._isNegative
        return


class CritCondition(_Condition, _Negatable):

    def __init__(self, path, critType, data):
        super(CritCondition, self).__init__(b'crit', dict(data), path)
        self._critType = critType
        self._relation = _findRelation(self._data.keys())
        self._relationValue = _getNodeValue(self._data, self._relation)
        self._critName = _getNodeValue(self._data, b'critName')
        self._isNegative = False
        return

    def isNegative(self):
        return self._isNegative

    def getCritType(self):
        return self._critType

    def getCritName(self):
        return self._critName

    @property
    def relation(self):
        return self._relation

    @property
    def relationValue(self):
        return self._relationValue

    def negate(self):
        self._relation = _RELATIONS.getOppositeRelation(self._relation)
        self._isNegative = not self._isNegative
        return


class CritsGroup(_Condition, _Negatable):

    def __init__(self, path, data):
        super(CritsGroup, self).__init__(b'crits', dict(data), path)
        self._isNegative = False
        self._results = []
        for critsType, critsList in self.getData().iteritems():
            for _, critsData in critsList:
                self._results.append(CritCondition(b'%s.%s' % (path, critsType), critsType, critsData))

        return

    def __repr__(self):
        return b'Crits<critsCount=%d>' % len(self._results)

    def isNegative(self):
        return self._isNegative

    def negate(self):
        self._isNegative = not self._isNegative
        for result in self._results:
            result.negate()

        return

    def getCrits(self):
        return self._results


class UnitResults(_Condition, _Negatable):

    def __init__(self, path, data, preBattleCond=None):
        super(UnitResults, self).__init__(b'unitResults', dict(data), path)
        self._isAllAlive = _getNodeValue(self._data, b'allAlive')
        self._unitKey = _getArenaBonusTypeForUnit(preBattleCond)
        self._results = []
        self._unitVehKills = None
        self._unitVehDamage = None
        for idx, (keyName, value) in enumerate(data):
            resultData, isNegative = None, False
            if keyName == b'not' and value:
                (_, resultData), isNegative = value[0], not isNegative
            elif keyName == b'results':
                resultData = value
                if resultData is not None:
                    results = BattleResults(b'%s.battleResults%d' % (path, idx), resultData, localeKey=self._unitKey)
                    if isNegative:
                        results.negate()
                    self._results.append(results)
            elif keyName == b'unitVehicleDamage':
                if value is not None:
                    self._unitVehDamage = VehicleDamage(b'%s.unitVehicleDamage%d' % (path, idx), value)
                    if isNegative:
                        self._unitVehDamage.negate()
            elif keyName == b'unitVehicleKills':
                if value is not None:
                    self._unitVehKills = VehicleKills(b'%s.unitVehicleKills%d' % (path, idx), value)
                    if isNegative:
                        self._unitVehKills.negate()

        return

    def __repr__(self):
        return b'UnitResults<resultsCount=%d>' % len(self._results)

    def negate(self):
        self._isAllAlive = not self._isAllAlive
        for result in self._results:
            result.negate()

        return

    def getResults(self):
        return self._results

    def getUnitVehKills(self):
        return self._unitVehKills

    def getUnitVehDamage(self):
        return self._unitVehDamage

    def getUnitKey(self):
        return self._unitKey

    def isAllAlive(self):
        return self._isAllAlive


class CumulativeResult(Cumulativable):

    def __init__(self, path, data, bonusCond, isUnit=False, preBattleCond=None):
        super(CumulativeResult, self).__init__(b'cumulative', dict(data), path)
        self._bonus = weakref.proxy(bonusCond)
        self._key, self._total = self._data.get(b'value', (None, 0))
        self._isUnit = isUnit
        self._unitName = _getArenaBonusTypeForUnit(preBattleCond)
        return

    def __repr__(self):
        return b'CumulativeResult<key=%s; total=%d>' % (self.getKey(), self.getTotalValue())

    def getUserString(self):
        return self.__getLabelString()

    @property
    def keyName(self):
        return self._key

    def getTotalValue(self):
        return self._total

    def getBonusData(self):
        return self._bonus

    def getKey(self):
        if self._isUnit:
            return b'unit_%s' % self._key
        return self._key

    def __getLabelString(self):
        param = backport.text(R.strings.quests.details.conditions.cumulative.dyn(self._key)())
        if self._isUnit:
            label = b'#quests:details/conditions/cumulative/%s' % self._unitName
        else:
            label = b'#quests:details/conditions/cumulative/single'
        return i18n.makeString(label, param=param)


class VehicleKills(_VehsListCondition):

    def __init__(self, path, data):
        super(VehicleKills, self).__init__(b'vehicleKills', dict(data), path)
        return

    def getVehiclesData(self):
        return _prepareVehData(self._getVehIntCDs(self._data))

    def getLabelKey(self):
        if self.getFireStarted() or self.getAttackReason() == ATTACK_REASON.FIRE:
            return QUESTS.DETAILS_CONDITIONS_FIREKILLS
        if self.getAttackReason() == ATTACK_REASON.RAM:
            return QUESTS.DETAILS_CONDITIONS_RAMKILLS
        return QUESTS.DETAILS_CONDITIONS_VEHICLESKILLS

    def __repr__(self):
        return b'VehicleKills<%s=%d>' % (self._relation, self._relationValue)


class VehicleKillsCumulative(VehicleKills, Cumulativable):

    def __init__(self, path, data, bonusCond):
        super(VehicleKillsCumulative, self).__init__(path, dict(data))
        self._name = b'vehicleKillsCumulative'
        self._bonus = weakref.proxy(bonusCond)
        return

    def __repr__(self):
        return b'VehicleKills<key=%s; %s=%d; total=%d>' % (
         self.getKey(), self._relation, self._relationValue,
         self.getTotalValue())

    def getUserString(self):
        return i18n.makeString(self.getLabelKey())

    def getTotalValue(self):
        return self._relationValue

    def getBonusData(self):
        return self._bonus

    def getKey(self):
        return b'vehicleKills'


class _CountOrTotalEventsCondition(_VehsListCondition):

    def isEventCount(self):
        return _getNodeValue(self._data, b'eventCount', default=False)


class VehicleDamage(_CountOrTotalEventsCondition):

    def __init__(self, path, data):
        super(VehicleDamage, self).__init__(b'vehicleDamage', dict(data), path)
        return

    def __repr__(self):
        return b'VehicleDamage<%s=%d>' % (self._relation, self._relationValue)

    def getVehiclesData(self):
        return _prepareVehData(self._getVehIntCDs(self._data))

    def getLabelKey(self):
        if self.getFireStarted() or self.getAttackReason() == ATTACK_REASON.FIRE:
            key = QUESTS.DETAILS_CONDITIONS_FIREDAMAGE
        elif self.getAttackReason() == ATTACK_REASON.RAM:
            key = QUESTS.DETAILS_CONDITIONS_RAMDAMAGE
        else:
            key = QUESTS.DETAILS_CONDITIONS_VEHICLEDAMAGE
        if self.isEventCount():
            key += b'/eventCount'
        return key


class VehicleDamageCumulative(VehicleDamage, Cumulativable):

    def __init__(self, path, data, bonusCond):
        super(VehicleDamageCumulative, self).__init__(path, dict(data))
        self._name = b'vehicleDamageCumulative'
        self._bonus = weakref.proxy(bonusCond)
        return

    def __repr__(self):
        return b'VehicleDamage<key=%s; %s=%d; total=%d>' % (
         self.getKey(), self._relation, self._relationValue,
         self.getTotalValue())

    def getUserString(self):
        return i18n.makeString(self.getLabelKey())

    def getTotalValue(self):
        return self._relationValue

    def getBonusData(self):
        return self._bonus

    def getKey(self):
        return b'vehicleDamage'


class VehicleStun(_CountOrTotalEventsCondition):

    def __init__(self, path, data):
        super(VehicleStun, self).__init__(b'vehicleStun', dict(data), path)
        return

    def __repr__(self):
        return b'VehicleStun<%s=%d>' % (self._relation, self._relationValue)

    def getVehiclesData(self):
        return _prepareVehData(self._getVehIntCDs(self._data))

    def getLabelKey(self):
        if self.isEventCount():
            return QUESTS.DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT
        return QUESTS.DETAILS_CONDITIONS_VEHICLESTUN


class VehicleStunCumulative(VehicleStun, Cumulativable):

    def __init__(self, path, data, bonusCond):
        super(VehicleStunCumulative, self).__init__(path, dict(data))
        self._name = b'vehicleStunCumulative'
        self._bonus = weakref.proxy(bonusCond)
        return

    def __repr__(self):
        return b'VehicleStun<key=%s; %s=%d; total=%d>' % (
         self.getKey(), self._relation, self._relationValue,
         self.getTotalValue())

    def getUserString(self):
        return i18n.makeString(self.getLabelKey())

    def getTotalValue(self):
        return self._relationValue

    def getBonusData(self):
        return self._bonus

    def getLabelKey(self):
        return super(VehicleStunCumulative, self).getLabelKey() + b'/cumulative'

    def getKey(self):
        return b'vehicleStun'


class MultiStunEvent(_Condition, _Negatable):

    def __init__(self, path, data):
        super(MultiStunEvent, self).__init__(b'multiStunEvent', dict(data), path)
        self._relation = _findRelation(self._data.keys())
        self._relationValue = _getNodeValue(self._data, self._relation)
        self._stunnedByShot = _getNodeValue(self._data, b'stunnedByShot')
        self._isNegative = False
        return

    def __repr__(self):
        return b'MultiStunEvent<%d, %s=%d>' % (self.stunnedByShot, self.relation, self.relationValue)

    def isNegative(self):
        return self._isNegative

    def negate(self):
        self._isNegative = not self._isNegative
        return

    @property
    def stunnedByShot(self):
        return self._stunnedByShot

    @property
    def relationValue(self):
        return self._relationValue

    @property
    def relation(self):
        return self._relation


class FirstBlood(_Condition, _Negatable):

    def __init__(self, path, data):
        super(FirstBlood, self).__init__(b'firstBlood', dict(data), path)
        self._isFirstBlood = True
        return

    def __repr__(self):
        return b'FirstBlood<value=%r>' % self._isFirstBlood

    def negate(self):
        self._isFirstBlood = not self._isFirstBlood
        return

    def getValue(self):
        return self._isFirstBlood


class CumulativeSum(Cumulativable):

    def __init__(self, path, data, bonusCond):
        super(CumulativeSum, self).__init__(b'cumulativeSum', dict(data), path)
        self._relation = _findRelation(self._data.keys())
        self._relationValue = _getNodeValue(self._data, self._relation)
        self._bonus = weakref.proxy(bonusCond)
        return

    def __repr__(self):
        conditions = tuple(value[1] for value in self._data.get(b'sum', ()))
        return b'CumulativeSum<conditions=%s>' % conditions

    def getBonusData(self):
        return self._bonus

    def getKey(self):
        return b'sum'

    def getTotalValue(self):
        return self._relationValue


def getProgressFromQuestWithSingleAccumulative(quest):
    conditions = quest.bonusCond.getConditions()
    if conditions and len(conditions.items) == 1:
        item = conditions.items[0]
        if isinstance(item, Cumulativable):
            currentProgress, totalProgress = item.getProgressPerGroup().get(None, [])[:2]
            return (
             currentProgress, totalProgress)
    return (None, None)
