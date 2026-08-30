from collections import namedtuple
from itertools import chain
import typing
from future.utils import itervalues
import Event
from PlayerEvents import g_playerEvents
from constants import MAX_VEHICLE_LEVEL, MIN_VEHICLE_LEVEL, BATTLE_MODE_VEHICLE_TAGS
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.system_factory import collectLimitedUITokens, registerLimitedUITokens
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from items import getTypeOfCompactDescr
from personal_missions import PM_BRANCH
from skeletons.gui.battle_matters import IBattleMattersController
from skeletons.gui.game_control import IBattlePassController, IAchievementsController
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Optional, Union, Tuple, Callable
LimitedUITokenInfo = namedtuple(b'LimitedUITokenInfo', (b'tokenID', b'clazz', b'args'))
LimitedUITokenInfo.__new__.__defaults__ = (b'', None, None)

class LimitedUICondition(object):
    __slots__ = (b'__value', b'__tokenID', b'__isActive', b'onConditionValueUpdated')

    def __init__(self, tokenID):
        self.__tokenID = tokenID
        self.__value = None
        self.__isActive = False
        self.onConditionValueUpdated = Event.Event()
        return

    def initialize(self, *args):
        return

    @property
    def tokenID(self):
        return self.__tokenID

    def value(self):
        if self.__isActive:
            return self.__value
        return self._getValue()

    def activate(self):
        self.__subscribe()
        self.__value = self._getValue()
        self.__isActive = True
        return

    def deactivate(self):
        self.__isActive = False
        self.__unsubscribe()
        self.__value = None
        return

    def finalize(self):
        self.__unsubscribe()
        self._clear()
        self.onConditionValueUpdated.clear()
        return

    def _getValue(self):
        raise NotImplementedError
        return

    def _getEvents(self):
        return tuple()

    def _getCallbacks(self):
        return tuple()

    def __subscribe(self):
        for event, handler in self._getEvents():
            event += handler

        g_clientUpdateManager.addCallbacks(dict(self._getCallbacks()))
        return

    def __unsubscribe(self):
        for event, handler in self._getEvents():
            event -= handler

        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def _clear(self):
        return

    def _update(self, *_, **__):
        newValue = self._getValue()
        if self.__value != newValue:
            self.__value = newValue
            self.onConditionValueUpdated(self.__tokenID)
        return


class _PermanentTrue(LimitedUICondition):
    __slots__ = ()

    def _getValue(self):
        return True


class _PermanentFalse(LimitedUICondition):
    __slots__ = ()

    def _getValue(self):
        return False


class _BattleCountCondition(LimitedUICondition):
    __slots__ = ()
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getValue(self):
        if not self.__itemsCache.items.stats.isSynced():
            return 0
        return self.__itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount()

    def _getEvents(self):
        return (
         (
          g_playerEvents.onDossiersResync, self._update),
         (
          self.__itemsCache.onSyncCompleted, self.__onSyncCompleted))

    def __onSyncCompleted(self, reason, diff):
        if reason in (CACHE_SYNC_REASON.SHOW_GUI,
         CACHE_SYNC_REASON.CLIENT_UPDATE,
         CACHE_SYNC_REASON.DOSSIER_RESYNC):
            self._update()
        return


class _BattleMattersCompletedQuests(LimitedUICondition):
    __slots__ = ()
    __battleMattersController = dependency.descriptor(IBattleMattersController)
    __eventsCache = dependency.descriptor(IEventsCache)

    def _getValue(self):
        return self.__battleMattersController.getCompletedBattleMattersQuestsCount()

    def _getEvents(self):
        return (
         (
          self.__eventsCache.onSyncCompleted, self._update),)


class _VehicleInventoryUpdater(object):
    __itemsCache = dependency.descriptor(IItemsCache)
    _instance = None

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        super(_VehicleInventoryUpdater, self).__init__()
        self.__subscribers = set()
        self.__isActive = False
        self.__inventoryVehicles = None
        self.__criteria = REQ_CRITERIA.INVENTORY
        self.__criteria |= ~REQ_CRITERIA.VEHICLE.RENT
        self.__criteria |= ~REQ_CRITERIA.SECRET
        self.__criteria |= ~REQ_CRITERIA.VEHICLE.HAS_ANY_TAG(BATTLE_MODE_VEHICLE_TAGS)
        self.onValueUpdated = Event.Event()
        return

    def clear(self):
        if not self.__subscribers:
            self.__clearCache()
        return

    def subscribe(self, ruleID):
        self.__subscribers.add(ruleID)
        self.__updateActivity()
        return

    def unsubscribe(self, ruleID):
        if ruleID in self.__subscribers:
            self.__subscribers.remove(ruleID)
            self.__updateActivity()
        return

    def getValue(self, criteria):
        if not self.__itemsCache.isSynced():
            return 0
        if not self.__inventoryVehicles:
            self.__updateCache()
        count = 0
        for item in self.__inventoryVehicles.itervalues():
            if criteria(item):
                count += 1

        return count

    def __updateActivity(self):
        if self.__isActive is False and self.__subscribers:
            self.__activate()
        elif self.__isActive and not self.__subscribers:
            self.__deactivate()
        return

    def __activate(self):
        g_clientUpdateManager.addCallbacks({b'inventory.1': (self.__update)})
        self.__isActive = True
        return

    def __deactivate(self):
        self.__isActive = False
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__clearCache()
        return

    def __update(self, *_):
        if not self.__itemsCache.isSynced():
            return 0
        self.__updateCache()
        self.onValueUpdated()
        return

    def __updateCache(self):
        self.__inventoryVehicles = self.__itemsCache.items.getVehicles(self.__criteria)
        return

    def __clearCache(self):
        if self.__inventoryVehicles is not None:
            self.__inventoryVehicles.clear()
            self.__inventoryVehicles = None
        return


class _VehicleCondition(LimitedUICondition):
    __slots__ = (b'__criteria',)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, tokenID):
        super(_VehicleCondition, self).__init__(tokenID)
        self.__criteria = None
        return

    def initialize(self, level, *args):
        self.__criteria = self._makeCriteria(level)
        return

    @property
    def criteria(self):
        return self.__criteria

    def _makeCriteria(self, level):
        criteria = REQ_CRITERIA.VEHICLE.LEVELS(range(level, MAX_VEHICLE_LEVEL + 1))
        criteria |= ~REQ_CRITERIA.VEHICLE.RENT
        criteria |= ~REQ_CRITERIA.SECRET
        criteria |= ~REQ_CRITERIA.VEHICLE.HAS_ANY_TAG(BATTLE_MODE_VEHICLE_TAGS)
        return criteria

    def _getValue(self):
        if not self.__itemsCache.isSynced():
            return 0
        return len(self.__itemsCache.items.getVehicles(self.__criteria))


class _VehicleInventoryCondition(_VehicleCondition):
    __slots__ = (b'__vehicleUpdater',)

    def __init__(self, tokenID):
        super(_VehicleInventoryCondition, self).__init__(tokenID)
        self.__vehicleUpdater = None
        return

    def initialize(self, level, *args):
        super(_VehicleInventoryCondition, self).initialize(level, *args)
        self.__vehicleUpdater = _VehicleInventoryUpdater.getInstance()
        return

    def activate(self):
        self.__vehicleUpdater.subscribe(self.tokenID)
        super(_VehicleInventoryCondition, self).activate()
        return

    def deactivate(self):
        self.__vehicleUpdater.unsubscribe(self.tokenID)
        super(_VehicleInventoryCondition, self).deactivate()
        return

    def finalize(self):
        self.__vehicleUpdater.unsubscribe(self.tokenID)
        super(_VehicleInventoryCondition, self).finalize()
        return

    def _clear(self):
        self.__vehicleUpdater.clear()
        self.__vehicleUpdater = None
        super(_VehicleInventoryCondition, self)._clear()
        return

    def _getValue(self):
        return self.__vehicleUpdater.getValue(self.criteria)

    def _getEvents(self):
        return (
         (
          self.__vehicleUpdater.onValueUpdated, self._update),)


class _MinVehicleLevel(_VehicleInventoryCondition):
    __slots__ = ()

    def _makeCriteria(self, level):
        criteria = super(_MinVehicleLevel, self)._makeCriteria(level)
        criteria |= REQ_CRITERIA.INVENTORY
        return criteria


class _MinNonPremiumVehicleLevel(_MinVehicleLevel):
    __slots__ = ()

    def _makeCriteria(self, level):
        criteria = super(_MinNonPremiumVehicleLevel, self)._makeCriteria(level)
        criteria |= ~REQ_CRITERIA.VEHICLE.PREMIUM
        return criteria


class _MinUnlockedVehicleLevel(_VehicleCondition):
    __slots__ = ()

    def _makeCriteria(self, level):
        criteria = super(_MinUnlockedVehicleLevel, self)._makeCriteria(level)
        criteria |= ~REQ_CRITERIA.VEHICLE.PREMIUM
        criteria |= ~REQ_CRITERIA.CUSTOM((lambda item: item.isSpecial))
        criteria |= REQ_CRITERIA.UNLOCKED
        return criteria

    def _getCallbacks(self):
        return (
         (
          b'stats.unlocks', self.__onUnlocksUpdate),)

    def __onUnlocksUpdate(self, unlocks):
        if any(getTypeOfCompactDescr(intCD) == GUI_ITEM_TYPE.VEHICLE for intCD in unlocks):
            self._update()
        return


class _DailyMissionsCompletedCount(LimitedUICondition):
    __slots__ = ()
    __eventsCache = dependency.descriptor(IEventsCache)

    def _getValue(self):
        quests = self.__eventsCache.getDailyQuests(filterFunc=(lambda q: q.isCompleted()))
        return len(quests.keys())

    def _getEvents(self):
        return (
         (
          self.__eventsCache.onSyncCompleted, self._update),)


class _BattlePassPoints(LimitedUICondition):
    __slots__ = ()
    __battlePass = dependency.descriptor(IBattlePassController)

    def _getValue(self):
        chaptersIDs = self.__battlePass.getChapterIDs()
        points = sum([self.__battlePass.getPointsInChapter(chapterID) for chapterID in chaptersIDs])
        freePoints = self.__battlePass.getFreePoints()
        return points + freePoints

    def _getEvents(self):
        return (
         (
          self.__battlePass.onPointsUpdated, self._update),)


class _PersonalMissionsActive(LimitedUICondition):
    __slots__ = ()
    __eventsCache = dependency.descriptor(IEventsCache)

    def _getValue(self):
        for branch in PM_BRANCH.ALL:
            operations = self.__eventsCache.getPersonalMissions().getOperationsForBranch(branch)
            if any(operation.isInProgress() for operation in itervalues(operations)):
                return True

        return False

    def _getEvents(self):
        return (
         (
          self.__eventsCache.onSyncCompleted, self._update),
         (
          self.__eventsCache.onProgressUpdated, self._update))


class _BluePrintsAvailability(LimitedUICondition):
    __slots__ = ()
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getValue(self):
        if not self.__itemsCache.isSynced():
            return False
        return self.__itemsCache.items.blueprints.hasBlueprintsOrFragments()

    def _getCallbacks(self):
        return (
         b'blueprints', self._update)


class _PersonalReservesAvailability(LimitedUICondition):
    __slots__ = ()
    __goodiesCache = dependency.descriptor(IGoodiesCache)
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getValue(self):
        if not self.__itemsCache.isSynced():
            return False
        return bool(self.__goodiesCache.getBoosters(criteria=REQ_CRITERIA.BOOSTER.IN_ACCOUNT))

    def _getEvents(self):
        return (
         (
          self.__itemsCache.onSyncCompleted, self._update),)


class _WereRealMoneyExpenses(LimitedUICondition):
    __slots__ = ()
    __itemsCache = dependency.descriptor(IItemsCache)
    __REAL_MONEY_EXPENSES_ENTITLEMENT = b'real_money_expenses'

    def _getValue(self):
        if not self.__itemsCache.isSynced():
            return False
        return self.__itemsCache.items.stats.entitlements.get(self.__REAL_MONEY_EXPENSES_ENTITLEMENT, 0) > 0

    def _getCallbacks(self):
        return (
         (
          b'cache.entitlements', self.__updateEntitlements),)

    def __updateEntitlements(self, entitlements):
        if entitlements.get(self.__REAL_MONEY_EXPENSES_ENTITLEMENT, 0):
            self._update()
        return


class _AdvancedAchievementsCount(LimitedUICondition):
    __slots__ = ()
    __advAchmntCtrl = dependency.descriptor(IAchievementsController)

    def _getValue(self):
        return self.__advAchmntCtrl.getTotalAchievementsCount()

    def _getEvents(self):
        return (
         (
          self.__advAchmntCtrl.onNewAchievementsEarned, self._update),)


_VEHICLE_LEVEL_TOKENS = tuple(tokenInfo for tokenInfo in chain.from_iterable((LimitedUITokenInfo((b'minVehicleLevel_{}').format(vehLevel), _MinVehicleLevel, (vehLevel,)), LimitedUITokenInfo((b'minNonPremiumVehicleLevel_{}').format(vehLevel), _MinNonPremiumVehicleLevel, (vehLevel,)), LimitedUITokenInfo((b'minUnlockedVehicleLevel_{}').format(vehLevel), _MinUnlockedVehicleLevel, (vehLevel,))) for vehLevel in range(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1)))
_REGISTER_TOKENS = (
 LimitedUITokenInfo(b'permanentTrue', _PermanentTrue, None),
 LimitedUITokenInfo(b'permanentFalse', _PermanentFalse, None),
 LimitedUITokenInfo(b'battlesCount', _BattleCountCondition, None),
 LimitedUITokenInfo(b'bmCompletedQuests', _BattleMattersCompletedQuests, None),
 LimitedUITokenInfo(b'dailyMissionsCompleted', _DailyMissionsCompletedCount, None),
 LimitedUITokenInfo(b'battlePassPoints', _BattlePassPoints, None),
 LimitedUITokenInfo(b'pmHasActiveMission', _PersonalMissionsActive, None),
 LimitedUITokenInfo(b'hasBlueprint', _BluePrintsAvailability, None),
 LimitedUITokenInfo(b'hasPersonalReserve', _PersonalReservesAvailability, None),
 LimitedUITokenInfo(b'wereRealMoneyExpenses', _WereRealMoneyExpenses, None),
 LimitedUITokenInfo(b'advancedAchievementsCount', _AdvancedAchievementsCount, None)) + _VEHICLE_LEVEL_TOKENS
registerLimitedUITokens(_REGISTER_TOKENS)

def getTokensInfo():
    return collectLimitedUITokens()
