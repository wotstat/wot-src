import json, logging
from collections import defaultdict
import typing, Event, wg_async
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventEnabled
from gui.clans.clan_cache import g_clanCache
from gui.game_control.reactive_comm import Subscription
from helpers import dependency
from shared_utils import CONST_CONTAINER
from skeletons.gui.game_control import IReactiveCommunicationService
_logger = logging.getLogger(__name__)

class FrozenVehiclesConstants(CONST_CONTAINER):
    ALL_VEHICLES_FROZEN = b'ALL_VEHICLES_FROZEN'
    E_VEHICLE_FREEZE = b'vehicle_freeze'
    E_VEHICLE_FREEZE_ALL = b'vehicle_freeze_all'
    E_VEHICLE_UNFREEZE = b'vehicle_unfreeze'
    E_VEHICLE_UNFREEZE_ALL = b'vehicle_unfreeze_all'
    E_SPARE_PARTS_CHANGED = b'spare_parts_changed'


class FrozenVehiclesRequester(object):
    __slots__ = (b'onUpdated', b'__cache', b'__isStarted', b'__subscription', b'__eventsManager')
    __RCService = dependency.descriptor(IReactiveCommunicationService)

    def __init__(self):
        super(FrozenVehiclesRequester, self).__init__()
        self.__cache = self.__defaultCache()
        self.__isStarted = False
        self.__subscription = None
        self.__eventsManager = Event.EventManager()
        self.onUpdated = Event.Event(self.__eventsManager)
        return

    @property
    def isStarted(self):
        return self.__isStarted

    @property
    def canStart(self):
        return getStrongholdEventEnabled() and g_clanCache.isInClan

    def start(self):
        if not self.__isStarted and self.canStart:
            self.__isStarted = True
            self.__subscribe()
        return

    def stop(self):
        self.__isStarted = False
        self.__clearSubscription()
        self.__cache = self.__defaultCache()
        return

    def getCache(self):
        return self.__cache

    def getSparePartsBalance(self):
        return self.__cache[b'parts_balance']

    def getFrozenVehicles(self, spaID):
        return self.__cache[b'frozen_vehicles'].get(spaID, set())

    def getUnfreezePrice(self, vehicleCD):
        return self.__cache[b'unfreeze_prices'].get(vehicleCD, -1)

    def isCacheEmpty(self):
        return self.__cache == self.__defaultCache()

    def removeFromFrozenVehicle(self, playerSpaID, vehicleCD):
        currentFrozenVehicles = self.__cache[b'frozen_vehicles'][playerSpaID]
        newFrozenVehicles = currentFrozenVehicles - {vehicleCD}
        self.__cache[b'frozen_vehicles'][playerSpaID] = newFrozenVehicles
        return

    def setInitialDataAndStart(self, data):
        if not isinstance(data, dict):
            return
        else:
            self.__cache[b'parts_balance'] = data.get(b'spare_parts_balance', 0)
            for playerData in data.get(b'accounts', []):
                if not isinstance(playerData, dict):
                    continue
                spaID = playerData.get(b'spa_id')
                if spaID is None:
                    continue
                allVehicles = playerData.get(b'all_vehicles', False)
                if allVehicles:
                    self.__cache[b'frozen_vehicles'][spaID] = FrozenVehiclesConstants.ALL_VEHICLES_FROZEN
                else:
                    self.__cache[b'frozen_vehicles'][spaID] = set([v.get(b'vehicle_cd', -1) for v in playerData.get(b'vehicles', [])])
                self.__cache[b'unfreeze_prices'].update({v.get(b'vehicle_cd', -1): v.get(b'repair_price', 0) for v in playerData.get(b'vehicles', [])})

            if not self.isCacheEmpty():
                self.onUpdated(self.__cache[b'frozen_vehicles'].keys())
            self.start()
            return

    def _onMessage(self, message):
        updatedSpaIDs = []
        message = json.loads(message)
        for record in message:
            event = record.get(b'event')
            if event is None:
                continue
            if event == FrozenVehiclesConstants.E_SPARE_PARTS_CHANGED:
                self.__cache[b'parts_balance'] = record.get(b'new_spare_parts', 0)
                continue
            spaID = record.get(b'spa_id')
            if event == FrozenVehiclesConstants.E_VEHICLE_UNFREEZE_ALL and spaID is None:
                updatedSpaIDs.extend(self.__cache[b'frozen_vehicles'].keys())
                self.__cache[b'frozen_vehicles'].clear()
                continue
            if spaID is None:
                continue
            vehicleCds = set([v[b'cd'] for v in record.get(b'vehicles', [])])
            unfreezePrices = {v.get(b'cd', -1): v.get(b'repair_price', 0) for v in record.get(b'vehicles', [])}
            currentFrozenVehicles = self.__cache[b'frozen_vehicles'][spaID]
            if event == FrozenVehiclesConstants.E_VEHICLE_UNFREEZE:
                newFrozenVehicles = currentFrozenVehicles - vehicleCds
            elif event == FrozenVehiclesConstants.E_VEHICLE_UNFREEZE_ALL:
                newFrozenVehicles = set()
            elif event == FrozenVehiclesConstants.E_VEHICLE_FREEZE_ALL:
                newFrozenVehicles = FrozenVehiclesConstants.ALL_VEHICLES_FROZEN
            elif event == FrozenVehiclesConstants.E_VEHICLE_FREEZE:
                newFrozenVehicles = currentFrozenVehicles | vehicleCds
            self.__cache[b'frozen_vehicles'][spaID] = newFrozenVehicles
            if unfreezePrices:
                self.__cache[b'unfreeze_prices'].update(unfreezePrices)
            updatedSpaIDs.append(spaID)

        if updatedSpaIDs:
            self.onUpdated(updatedSpaIDs)
        return

    def __onClosed(self, reason):
        self.__clearSubscription()
        return

    @wg_async.wg_async
    def __subscribe(self):
        self.__subscription = Subscription(self.__getChannelName())
        result = yield wg_async.wg_await(self.__RCService.subscribeToChannel(self.__subscription))
        if result:
            self.__subscription.onMessage += self._onMessage
            self.__subscription.onClosed += self.__onClosed
        else:
            self.__clearSubscription()
        return

    def __clearSubscription(self):
        if self.__subscription is not None:
            self.__subscription.onMessage -= self._onMessage
            self.__subscription.onClosed -= self.__onClosed
            self.__RCService.unsubscribeFromChannel(self.__subscription)
            self.__subscription = None
        return

    @staticmethod
    def __getChannelName():
        return (b'wgshevents_clan_{}').format(g_clanCache.clanDBID)

    @staticmethod
    def __defaultCache():
        return {b'parts_balance': 0, 
           b'frozen_vehicles': (defaultdict(set)), 
           b'unfreeze_prices': {}}
