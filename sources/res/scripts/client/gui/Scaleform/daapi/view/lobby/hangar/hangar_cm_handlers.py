from __future__ import absolute_import
from logging import getLogger
from typing import TYPE_CHECKING
import BigWorld
from CurrentVehicle import g_currentVehicle
from adisp import adisp_process
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getTradeInVehiclesUrl
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler, CM_BUY_COLOR
from gui.Scaleform.locale.MENU import MENU
from gui.impl.lobby.hangar.buy_vehicle_view import VehicleBuyActionTypes
from gui.prb_control import prbDispatcherProperty
from gui.shared import event_dispatcher as shared_events
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showShop, showTelecomRentalPage
from gui.shared.events import HangarVehicleEvent
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.processors.vehicle import VehicleFavoriteProcessor
from helpers import dependency
from items import UNDEFINED_ITEM_CD
from skeletons.gui.game_control import IVehicleComparisonBasket, IEpicBattleMetaGameController, ITradeInController, IVehiclePlaylistsController, IHangarGuiController, IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED
_logger = getLogger(__name__)
if TYPE_CHECKING:
    from typing import Optional
    from gui.shared.gui_items import Vehicle

class MODULE(object):
    INFO = b'moduleInfo'
    CANCEL_BUY = b'cancelBuy'
    UNLOAD = b'unload'
    UNLOCK = b'unlock'
    EQUIP = b'equip'
    SELL = b'sell'
    BUY_AND_EQUIP = b'buyAndEquip'


class VEHICLE(object):
    EXCHANGE = b'exchange'
    INFO = b'vehicleInfo'
    PREVIEW = b'preview'
    STATS = b'showVehicleStatistics'
    UNLOCK = b'unlock'
    SELECT = b'selectVehicle'
    SELL = b'sell'
    BUY = b'buy'
    RESEARCH = b'vehicleResearch'
    POST_PROGRESSION = b'vehiclePostProgression'
    RENEW = b'vehicleRentRenew'
    REMOVE = b'vehicleRemove'
    CHECK = b'vehicleCheck'
    UNCHECK = b'vehicleUncheck'
    COMPARE = b'compare'
    BLUEPRINT = b'blueprint'
    NATION_CHANGE = b'nationChange'
    GO_TO_COLLECTION = b'goToCollection'
    TELECOM_RENT = b'telecomRent'
    VEH_SKILL_TREE = b'vehSkillTree'
    MANAGE_PLAYLISTS = b'managePlaylists'
    CREATE_PLAYLIST = b'createPlaylist'


class TechnicalMaintenanceCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, cmProxy, ctx=None):
        super(TechnicalMaintenanceCMHandler, self).__init__(cmProxy, ctx, {(MODULE.INFO): b'showModuleInfo', 
           (MODULE.CANCEL_BUY): b'resetSlot', 
           (MODULE.UNLOAD): b'resetSlot'})
        return

    def showModuleInfo(self):
        if self._equipmentCD is not None and g_currentVehicle.isPresent():
            shared_events.showModuleInfo(self._equipmentCD, g_currentVehicle.item.descriptor)
        return

    def resetSlot(self):
        self.fireEvent(events.TechnicalMaintenanceEvent(events.TechnicalMaintenanceEvent.RESET_EQUIPMENT, ctx={b'eqCD': (self._equipmentCD)}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _initFlashValues(self, ctx):
        self._equipmentCD = ctx.equipmentCD
        self._isCanceled = bool(ctx.isCanceled)
        return

    def _clearFlashValues(self):
        self._equipmentCD = None
        self._isCanceled = None
        return

    def _generateOptions(self, ctx=None):
        options = [self._makeItem(MODULE.INFO, MENU.contextmenu(MODULE.INFO))]
        equipment = self.itemsCache.items.getItemByCD(int(self._equipmentCD))
        if equipment is not None and equipment.isBuiltIn:
            return options
        else:
            if self._isCanceled:
                options.append(self._makeItem(MODULE.CANCEL_BUY, MENU.contextmenu(MODULE.CANCEL_BUY)))
            else:
                options.append(self._makeItem(MODULE.UNLOAD, MENU.contextmenu(MODULE.UNLOAD)))
            return options


class SimpleVehicleCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache = dependency.descriptor(IItemsCache)

    def getVehCD(self):
        raise NotImplementedError
        return

    def getVehInvID(self):
        raise NotImplementedError
        return

    def showVehicleInfo(self):
        shared_events.showVehicleInfo(self.getVehCD())
        return

    def showVehicleStats(self):
        shared_events.showVehicleStats(self.getVehCD())
        return

    def sellVehicle(self):
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        if vehicle:
            shared_events.showVehicleSellDialog(self.getVehInvID())
        return

    def buyVehicle(self):
        ItemsActionsFactory.doAction(ItemsActionsFactory.BUY_VEHICLE, self.getVehCD(), False, VehicleBuyActionTypes.BUY)
        return

    def _generateOptions(self, ctx=None):
        return []


class VehicleContextMenuHandler(SimpleVehicleCMHandler):
    _comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    _epicController = dependency.descriptor(IEpicBattleMetaGameController)
    _tradeInController = dependency.descriptor(ITradeInController)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    __hangarGuiCtrl = dependency.descriptor(IHangarGuiController)
    __vehiclePlaylistsCtrl = dependency.descriptor(IVehiclePlaylistsController)
    _wotPlusController = dependency.descriptor(IWotPlusController)

    def __init__(self, cmProxy, ctx=None):
        super(VehicleContextMenuHandler, self).__init__(cmProxy, ctx, {(VEHICLE.EXCHANGE): b'showVehicleExchange', 
           (VEHICLE.INFO): b'showVehicleInfo', 
           (VEHICLE.SELL): b'sellVehicle', 
           (VEHICLE.RESEARCH): b'toResearch', 
           (VEHICLE.POST_PROGRESSION): b'showPostProgression', 
           (VEHICLE.CHECK): b'checkFavoriteVehicle', 
           (VEHICLE.UNCHECK): b'uncheckFavoriteVehicle', 
           (VEHICLE.STATS): b'showVehicleStats', 
           (VEHICLE.BUY): b'buyVehicle', 
           (VEHICLE.COMPARE): b'compareVehicle', 
           (VEHICLE.NATION_CHANGE): b'changeVehicleNation', 
           (VEHICLE.GO_TO_COLLECTION): b'goToCollection', 
           (VEHICLE.TELECOM_RENT): b'showTelecomRent', 
           (VEHICLE.VEH_SKILL_TREE): b'showVehSkillTree', 
           (VEHICLE.MANAGE_PLAYLISTS): b'showManagePlaylists', 
           (VEHICLE.CREATE_PLAYLIST): b'showManagePlaylists'})
        return

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def getVehCD(self):
        return self.vehCD

    def getVehInvID(self):
        return self.vehInvID

    def toResearch(self):
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        if vehicle is not None:
            shared_events.showVehicleHubModules(vehicle.intCD)
        else:
            _logger.error(b'Can not go to Research because id for current vehicle is None')
        return

    def showPostProgression(self):
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        shared_events.showVehPostProgressionView(vehicle.intCD)
        return

    def showVehSkillTree(self):
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        shared_events.showVehicleHubVehSkillTree(vehicle.intCD)
        return

    def showManagePlaylists(self):
        self.fireEvent(HangarVehicleEvent(HangarVehicleEvent.ON_CONTEXT_MENU_CLICKED, ctx={b'vehicleIntCD': (self.getVehCD())}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def showVehicleExchange(self):
        oldSellVeh = self._tradeInController.getSelectedVehicleToSell()
        self._tradeInController.selectVehicleToSell(self.vehCD)
        if not oldSellVeh or oldSellVeh.intCD != self.vehCD:
            self._tradeInController.selectVehicleToBuy(UNDEFINED_ITEM_CD)
        showShop(getTradeInVehiclesUrl())
        return

    def checkFavoriteVehicle(self):
        self.__favoriteVehicle(True)
        return

    def uncheckFavoriteVehicle(self):
        self.__favoriteVehicle(False)
        return

    def compareVehicle(self):
        self._comparisonBasket.addVehicle(self.vehCD)
        return

    def changeVehicleNation(self):
        ItemsActionsFactory.doAction(ItemsActionsFactory.CHANGE_NATION, self.vehCD)
        return

    def goToCollection(self):
        vehicle = self.itemsCache.items.getVehicle(self.vehInvID)
        shared_events.showCollectibleVehicles(vehicle.nationID)
        return

    def showTelecomRent(self):
        showTelecomRentalPage()
        return

    def _initFlashValues(self, ctx):
        self.vehInvID = int(ctx.inventoryId)
        vehicle = self.itemsCache.items.getVehicle(self.vehInvID)
        self.vehCD = vehicle.intCD if vehicle is not None else None
        return

    def _clearFlashValues(self):
        self.vehInvID = None
        self.vehCD = None
        return

    def _generateOptions(self, ctx=None):
        options = []
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        vehicleWasInBattle = False
        accDossier = self.itemsCache.items.getAccountDossier(None)
        if vehicle is None:
            return options
        else:
            isEventVehicle = vehicle.isOnlyForEventBattles
            if accDossier:
                wasInBattleSet = set(accDossier.getTotalStats().getVehicles().keys())
                wasInBattleSet.update(accDossier.getGlobalMapStats().getVehicles().keys())
                if vehicle.intCD in wasInBattleSet:
                    vehicleWasInBattle = True
            if vehicle is not None:
                if vehicle.canTradeOff:
                    options.append(self._makeItem(VEHICLE.EXCHANGE, MENU.contextmenu(VEHICLE.EXCHANGE), {b'enabled': (vehicle.isReadyToTradeOff), 
                       b'textColor': CM_BUY_COLOR}))
                options.extend([
                 self._makeItem(VEHICLE.INFO, MENU.contextmenu(VEHICLE.INFO)),
                 self._makeItem(VEHICLE.STATS, MENU.contextmenu(VEHICLE.STATS), {b'enabled': vehicleWasInBattle})])
                self._manageVehCompareOptions(options, vehicle)
                if self.prbDispatcher is not None:
                    isNavigationEnabled = not self.prbDispatcher.getFunctionalState().isNavigationDisabled()
                else:
                    isNavigationEnabled = True
                if not vehicle.isOnlyForEpicBattles:
                    options.append(self._makeItem(VEHICLE.RESEARCH, MENU.contextmenu(VEHICLE.RESEARCH), {b'enabled': isNavigationEnabled}))
                if vehicle.isPostProgressionExists:
                    if vehicle.postProgression.isVehSkillTree():
                        options.append(self._makeItem(VEHICLE.VEH_SKILL_TREE, MENU.contextmenu(VEHICLE.VEH_SKILL_TREE), {b'enabled': isNavigationEnabled}))
                    else:
                        options.append(self._makeItem(VEHICLE.POST_PROGRESSION, MENU.contextmenu(VEHICLE.POST_PROGRESSION), {b'enabled': isNavigationEnabled}))
                if vehicle.isCollectible:
                    options.append(self._makeItem(VEHICLE.GO_TO_COLLECTION, MENU.contextmenu(VEHICLE.GO_TO_COLLECTION), {b'enabled': (self._lobbyContext.getServerSettings().isCollectorVehicleEnabled())}))
                if vehicle.hasNationGroup:
                    isNew = not AccountSettings.getSettings(NATION_CHANGE_VIEWED)
                    options.append(self._makeItem(VEHICLE.NATION_CHANGE, MENU.CONTEXTMENU_NATIONCHANGE, {b'enabled': (vehicle.isNationChangeAvailable), b'isNew': isNew}))
                if vehicle.isRented:
                    canSell = vehicle.canSell and vehicle.rentalIsOver
                    if vehicle.isWotPlus:
                        canSell = not self._wotPlusController.getSettingsStorage().isExclusiveVehicleEnabled()
                    elif not vehicle.isPremiumIGR:
                        items = self.itemsCache.items
                        enabled = vehicle.mayObtainWithMoneyExchange(items.stats.money, proxy=items.shop)
                        label = MENU.CONTEXTMENU_RESTORE if vehicle.isRestoreAvailable() else MENU.CONTEXTMENU_BUY
                        options.append(self._makeItem(VEHICLE.BUY, label, {b'enabled': enabled}))
                    if vehicle.isTelecomRent:
                        canSell = False
                        serverSettings = self._lobbyContext.getServerSettings()
                        isRentalEnabled = serverSettings.isTelecomRentalsEnabled()
                        isActive = BigWorld.player().telecomRentals.isActive()
                        options.append(self._makeItem(VEHICLE.TELECOM_RENT, MENU.contextmenu(VEHICLE.TELECOM_RENT), {b'enabled': (isRentalEnabled and isActive)}))
                    options.append(self._makeItem(VEHICLE.SELL, MENU.contextmenu(VEHICLE.REMOVE), {b'enabled': canSell}))
                else:
                    options.append(self._makeItem(VEHICLE.SELL, MENU.contextmenu(VEHICLE.SELL), {b'enabled': (vehicle.canSell and not isEventVehicle)}))
                helper = self.__hangarGuiCtrl.currentGuiProvider.getVehiclePlaylistsHelper()
                if self.__vehiclePlaylistsCtrl.isEnabled and helper is not None and helper.isPlaylistsSupported():
                    if any(self.__vehiclePlaylistsCtrl.iterPlaylists()):
                        options.append(self._makeItem(VEHICLE.MANAGE_PLAYLISTS, MENU.contextmenu(VEHICLE.MANAGE_PLAYLISTS), {b'enabled': True}))
                    else:
                        options.append(self._makeItem(VEHICLE.CREATE_PLAYLIST, MENU.contextmenu(VEHICLE.CREATE_PLAYLIST), {b'enabled': True}))
                if vehicle.isFavorite:
                    options.append(self._makeItem(VEHICLE.UNCHECK, MENU.contextmenu(VEHICLE.UNCHECK)))
                else:
                    options.append(self._makeItem(VEHICLE.CHECK, MENU.contextmenu(VEHICLE.CHECK), {b'enabled': (not isEventVehicle)}))
            return options

    def _manageVehCompareOptions(self, options, vehicle):
        if self._comparisonBasket.isEnabled():
            options.append(self._makeItem(VEHICLE.COMPARE, MENU.contextmenu(VEHICLE.COMPARE), {b'enabled': (self._comparisonBasket.isReadyToAdd(vehicle))}))
        return

    @adisp_process
    def __favoriteVehicle(self, isFavorite):
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        if vehicle is not None:
            result = yield VehicleFavoriteProcessor(vehicle, bool(isFavorite)).request()
            if not result.success:
                _logger.error(b'Cannot set selected vehicle as favorite due to following error: %s', result.userMsg)
        return
