from __future__ import absolute_import
import weakref
from logging import getLogger
from future.utils import viewitems
from collector_vehicle import CollectorVehicleConsts
from PlayerEvents import g_playerEvents
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from skeletons.gui.game_control import IWalletController, IVehicleComparisonBasket, IRentalsController, IRestoreController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
_logger = getLogger(__name__)
_INV_ITEM_VCDESC_KEY = b'compDescr'
_CACHE_VEHS_LOCK_KEY = b'vehsLock'
_STAT_DIFF_KEY = b'stats'
_INVENTORY_DIFF_KEY = b'inventory'
_CACHE_DIFF_KEY = b'cache'
_GOODIES_DIFF_KEY = b'goodies'
_STAT_DIFF_FORMAT = _STAT_DIFF_KEY + b'.{0:>s}'
_CREDITS_DIFF_KEY = _STAT_DIFF_FORMAT.format(b'credits')
_GOLD_DIFF_KEY = _STAT_DIFF_FORMAT.format(b'gold')
_FREE_XP_DIFF_KEY = _STAT_DIFF_FORMAT.format(b'freeXP')
_UNLOCKS_DIFF_KEY = _STAT_DIFF_FORMAT.format(b'unlocks')
_VEH_XP_DIFF_KEY = _STAT_DIFF_FORMAT.format(b'vehTypeXP')
_ELITE_DIFF_KEY = _STAT_DIFF_FORMAT.format(b'eliteVehicles')
_BLUEPRINT_DIFF_KEY = b'blueprints'
_BLUEPRINT_SETTINGS_KEY = b'serverSettings.blueprints_config'

class _Listener(object):

    def __init__(self):
        super(_Listener, self).__init__()
        self._page = None
        return

    def __del__(self):
        _logger.debug(b'Listener deleted: %s', self.__class__.__name__)
        return

    def startListen(self, page):
        self._page = page
        return

    def stopListen(self):
        self._page = None
        return


class _BlueprintsListener(_Listener):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def startListen(self, page):
        super(_BlueprintsListener, self).startListen(page)
        g_clientUpdateManager.addCallbacks({_BLUEPRINT_DIFF_KEY: (self._onBlueprintsUpdate), 
           _BLUEPRINT_SETTINGS_KEY: (self.__onBlueprintsModeChanged)})
        return

    def stopListen(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(_BlueprintsListener, self).stopListen()
        return

    def _onBlueprintsUpdate(self, blueprints):
        self._page.invalidateBlueprints(blueprints)
        return

    def __onBlueprintsModeChanged(self, _):
        isEnabled = self.__lobbyContext.getServerSettings().blueprintsConfig.isBlueprintsAvailable()
        self._page.invalidateBlueprintMode(isEnabled)
        return


class _StatsListener(_Listener):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def startListen(self, page):
        super(_StatsListener, self).startListen(page)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged
        g_clientUpdateManager.addCallbacks({_CREDITS_DIFF_KEY: (self._onCreditsUpdate), 
           _GOLD_DIFF_KEY: (self._onGoldUpdate), 
           _FREE_XP_DIFF_KEY: (self._onFreeXPUpdate), 
           _UNLOCKS_DIFF_KEY: (self._onUnlocksUpdate), 
           _VEH_XP_DIFF_KEY: (self._onVehiclesXPUpdate), 
           _ELITE_DIFF_KEY: (self._onEliteVehiclesUpdate)})
        return

    def stopListen(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(_StatsListener, self).stopListen()
        return

    def _onCreditsUpdate(self, _):
        self._page.invalidateCredits()
        return

    def _onGoldUpdate(self, _):
        self._page.invalidateGold()
        return

    def _onFreeXPUpdate(self, _):
        self._page.invalidateFreeXP()
        return

    def _onEliteVehiclesUpdate(self, elites):
        self._page.invalidateElites(elites)
        return

    def _onVehiclesXPUpdate(self, xps):
        newXPs = {key: value if value else 0 for key, value in viewitems(xps)}
        self._page.invalidateVTypeXP(newXPs)
        return

    def _onUnlocksUpdate(self, unlocks):
        self._page.invalidateUnlocks(unlocks)
        return

    def __onServerSettingsChanged(self, diff):
        if self.__lobbyContext.getServerSettings().isShopDataChangedInDiff(diff, b'isEnabled'):
            self._onGoldUpdate(None)
        if CollectorVehicleConsts.CONFIG_NAME in diff:
            self._page.invalidateVehicleCollectorState()
        return


class _ItemsCacheListener(_Listener):
    __itemsCache = dependency.descriptor(IItemsCache)
    __comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self):
        super(_ItemsCacheListener, self).__init__()
        self.__invalidated = set()
        return

    def startListen(self, page):
        super(_ItemsCacheListener, self).startListen(page)
        g_clientUpdateManager.addCallbacks({_INVENTORY_DIFF_KEY: (self.__onInventoryUpdate), 
           _CACHE_DIFF_KEY: (self.__onCacheUpdate), 
           _GOODIES_DIFF_KEY: (self.__onGoodiesUpdate)})
        g_playerEvents.onCenterIsLongDisconnected += self.__center_onIsLongDisconnected
        self.__itemsCache.onSyncCompleted += self.__items_onSyncCompleted
        self.__comparisonBasket.onChange += self.__onVehCompareBasketChanged
        self.__comparisonBasket.onSwitchChange += self.__onVehCompareBasketSwitchChange
        return

    def stopListen(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        g_playerEvents.onCenterIsLongDisconnected -= self.__center_onIsLongDisconnected
        self.__itemsCache.onSyncCompleted -= self.__items_onSyncCompleted
        self.__comparisonBasket.onChange -= self.__onVehCompareBasketChanged
        self.__comparisonBasket.onSwitchChange -= self.__onVehCompareBasketSwitchChange
        super(_ItemsCacheListener, self).stopListen()
        return

    def __onInventoryUpdate(self, _):
        self._page.invalidateInventory(self.__invalidated)
        return

    def __onGoodiesUpdate(self, goodies):
        invalidated = set()
        vehicleDiscounts = self.__itemsCache.items.shop.getVehicleDiscountDescriptions()
        for goodieID in goodies:
            vehicleDiscount = vehicleDiscounts.get(goodieID)
            if vehicleDiscount:
                invalidated.add(vehicleDiscount.target.targetValue)

        self._page.invalidateDiscounts(invalidated)
        return

    def __onCacheUpdate(self, cache):
        if _CACHE_VEHS_LOCK_KEY in cache:
            vehLocks = cache.get(_CACHE_VEHS_LOCK_KEY)
            if vehLocks:
                self._page.invalidateVehLocks(vehLocks)
        return

    def __items_onSyncCompleted(self, reason, invalidated):
        self.__invalidated = set()
        for itemTypeID, uniqueIDs in viewitems(invalidated):
            if itemTypeID in GUI_ITEM_TYPE.VEHICLE_MODULES or itemTypeID == GUI_ITEM_TYPE.VEHICLE:
                self.__invalidated |= uniqueIDs

        if reason == CACHE_SYNC_REASON.SHOP_RESYNC:
            self._page.redraw()
        if GUI_ITEM_TYPE.VEH_POST_PROGRESSION in invalidated:
            self._page.invalidateVehPostProgression()
        return

    def __center_onIsLongDisconnected(self, _):
        self._page.redraw()
        return

    def __onVehCompareBasketChanged(self, changedData):
        if changedData.isFullChanged:
            self._page.invalidateVehCompare()
        return

    def __onVehCompareBasketSwitchChange(self):
        self._page.invalidateVehCompare()
        return


class _WalletStatusListener(_Listener):
    __wallet = dependency.descriptor(IWalletController)

    def startListen(self, page):
        super(_WalletStatusListener, self).startListen(page)
        self.__wallet.onWalletStatusChanged += self.__onWalletStatusChanged
        return

    def stopListen(self):
        self.__wallet.onWalletStatusChanged -= self.__onWalletStatusChanged
        super(_WalletStatusListener, self).stopListen()
        return

    def __onWalletStatusChanged(self, status):
        self._page.invalidateWalletStatus(status)
        return


class _RentChangeListener(_Listener):
    __rentals = dependency.descriptor(IRentalsController)

    def startListen(self, page):
        super(_RentChangeListener, self).startListen(page)
        self.__rentals.onRentChangeNotify += self.__onRentChange
        return

    def stopListen(self):
        self.__rentals.onRentChangeNotify -= self.__onRentChange
        super(_RentChangeListener, self).stopListen()
        return

    def __onRentChange(self, vehicles):
        self._page.invalidateRent(vehicles)
        return


class _RestoreListener(_Listener):
    __restores = dependency.descriptor(IRestoreController)

    def startListen(self, page):
        self.__restores.onRestoreChangeNotify += self.__onRestoreChanged
        super(_RestoreListener, self).startListen(page)
        return

    def stopListen(self):
        self.__restores.onRestoreChangeNotify -= self.__onRestoreChanged
        super(_RestoreListener, self).stopListen()
        return

    def __onRestoreChanged(self, vehicles):
        self._page.invalidateRestore(vehicles)
        return


class _PrbGlobalListener(_Listener, IGlobalListener):

    def startListen(self, page):
        super(_PrbGlobalListener, self).startListen(page)
        g_playerEvents.onDisconnected += self.__onDisconnected
        self.startGlobalListening()
        return

    def stopListen(self):
        super(_PrbGlobalListener, self).stopListen()
        g_playerEvents.onDisconnected -= self.__onDisconnected
        self.stopGlobalListening()
        return

    def onPrbEntitySwitched(self):
        self._page.invalidatePrbState()
        return

    def onPreQueueSettingsChanged(self, diff):
        self._page.invalidatePrbState()
        return

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        if accountInfo.isCurrentPlayer():
            self._page.invalidatePrbState()
        return

    def onUnitPlayerStateChanged(self, pInfo):
        if pInfo.isCurrentPlayer():
            self._page.invalidatePrbState()
        return

    def __onDisconnected(self):
        self._page.clearSelectedNation()
        return


class TTListenerDecorator(_Listener):
    __slots__ = (b'_stats', b'_items', b'_wallet', b'_prbListener', b'_rent', b'_restore', b'_blueprints')

    def __init__(self):
        super(TTListenerDecorator, self).__init__()
        self._stats = _StatsListener()
        self._items = _ItemsCacheListener()
        self._wallet = _WalletStatusListener()
        self._prbListener = _PrbGlobalListener()
        self._rent = _RentChangeListener()
        self._restore = _RestoreListener()
        self._blueprints = _BlueprintsListener()
        return

    def startListen(self, page):
        proxy = weakref.proxy(page)
        self._stats.startListen(proxy)
        self._items.startListen(proxy)
        self._wallet.startListen(proxy)
        self._prbListener.startListen(proxy)
        self._rent.startListen(proxy)
        self._restore.startListen(proxy)
        self._blueprints.startListen(proxy)
        return

    def stopListen(self):
        self._stats.stopListen()
        self._items.stopListen()
        self._wallet.stopListen()
        self._prbListener.stopListen()
        self._rent.stopListen()
        self._restore.stopListen()
        self._blueprints.stopListen()
        return
