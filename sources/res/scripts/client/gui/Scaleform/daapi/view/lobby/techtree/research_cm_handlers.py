from __future__ import absolute_import
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import MODULE, SimpleVehicleCMHandler, VEHICLE
from gui.Scaleform.daapi.view.lobby.techtree.settings import NODE_STATE, UnlockProps
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.shop import canBuyGoldForVehicleThroughWeb
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED

class ResearchItemContextMenuHandler(AbstractContextMenuHandler, EventSystemEntity):
    _itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, cmProxy, ctx=None):
        super(ResearchItemContextMenuHandler, self).__init__(cmProxy, ctx, {(MODULE.INFO): b'showModuleInfo', 
           (MODULE.UNLOCK): b'unlockModule', 
           (MODULE.BUY_AND_EQUIP): b'buyModule', 
           (MODULE.EQUIP): b'equipModule', 
           (MODULE.SELL): b'sellModule'})
        return

    def showModuleInfo(self):
        vehicle = self._itemsCache.items.getItemByCD(self._rootCD)
        if vehicle:
            shared_events.showModuleInfo(self._nodeCD, vehicle.descriptor)
        return

    def unlockModule(self):
        vehicle = self._itemsCache.items.getItemByCD(self._rootCD)
        unlockIdx, xpCost, required = vehicle.getUnlockDescrByIntCD(self._nodeCD)
        unlockProps = UnlockProps(self._rootCD, unlockIdx, xpCost, required, 0, xpCost)
        ItemsActionsFactory.doAction(ItemsActionsFactory.UNLOCK_ITEM, self._nodeCD, unlockProps)
        return

    def buyModule(self):
        ItemsActionsFactory.doAction(ItemsActionsFactory.BUY_AND_INSTALL_AND_SELL_ITEM, self._nodeCD, self._rootCD)
        return

    def equipModule(self):
        ItemsActionsFactory.doAction(ItemsActionsFactory.INSTALL_ITEM, self._nodeCD, self._rootCD)
        return

    def sellModule(self):
        ItemsActionsFactory.doAction(ItemsActionsFactory.SELL_ITEM, self._nodeCD)
        return

    def _initFlashValues(self, ctx):
        self._nodeCD = int(ctx.nodeCD)
        self._rootCD = int(ctx.rootCD)
        self._hasUrgent = bool(ctx.hasUrgent)
        self._nodeState = int(ctx.nodeState)
        return

    def _clearFlashValues(self):
        self._nodeCD = None
        self._rootCD = None
        self._nodeState = None
        return

    def _generateOptions(self, ctx=None):
        options = [
         self._makeItem(MODULE.INFO, MENU.contextmenu(MODULE.INFO)),
         self._makeSeparator(),
         self._makeItem(MODULE.UNLOCK, MENU.contextmenu(MODULE.UNLOCK), {b'enabled': (NODE_STATE.isAvailable2Unlock(self._nodeState))})]
        if NODE_STATE.isUnlocked(self._nodeState):
            if NODE_STATE.inInventory(self._nodeState) or NODE_STATE.isInstalled(self._nodeState):
                options.extend([
                 self._makeItem(MODULE.EQUIP, MENU.contextmenu(MODULE.EQUIP), {b'enabled': (self._isAvailable2Install())}),
                 self._makeSeparator(),
                 self._makeItem(MODULE.SELL, MENU.CONTEXTMENU_SELLFROMINVENTORY, {b'enabled': (not NODE_STATE.isInstalled(self._nodeState))})])
            else:
                options.extend([
                 self._makeItem(MODULE.BUY_AND_EQUIP, MENU.CONTEXTMENU_BUYANDEQUIP, {b'enabled': (self._isAvailable2Buy())}),
                 self._makeSeparator(),
                 self._makeItem(MODULE.SELL, MENU.CONTEXTMENU_SELLFROMINVENTORY, {b'enabled': (NODE_STATE.isAvailable2Sell(self._nodeState))})])
        else:
            options.extend([
             self._makeItem(MODULE.BUY_AND_EQUIP, MENU.CONTEXTMENU_BUYANDEQUIP, {b'enabled': False}),
             self._makeSeparator(),
             self._makeItem(MODULE.SELL, MENU.CONTEXTMENU_SELLFROMINVENTORY, {b'enabled': False})])
        return options

    def _isAvailable2Install(self):
        return not NODE_STATE.isInstalled(self._nodeState) and NODE_STATE.inInventory(self._nodeState) and self._canInstallItems() and not self._hasUrgent

    def _isAvailable2Buy(self):
        return not NODE_STATE.isInstalled(self._nodeState) and NODE_STATE.isAvailable2Buy(self._nodeState) and self._canInstallItems()

    def _canInstallItems(self):
        rootItem = self._itemsCache.items.getItemByCD(self._rootCD)
        return rootItem.isInInventory and not rootItem.isLocked and not rootItem.repairCost


class ResearchVehicleContextMenuHandler(SimpleVehicleCMHandler):
    _comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    _hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, cmProxy, ctx=None):
        super(ResearchVehicleContextMenuHandler, self).__init__(cmProxy, ctx, {(VEHICLE.INFO): b'showVehicleInfo', 
           (VEHICLE.UNLOCK): b'unlockVehicle', 
           (VEHICLE.BUY): b'buyVehicle', 
           (VEHICLE.SELL): b'sellVehicle', 
           (VEHICLE.SELECT): b'selectVehicle', 
           (VEHICLE.STATS): b'showVehicleStats', 
           (VEHICLE.COMPARE): b'compareVehicle', 
           (VEHICLE.NATION_CHANGE): b'changeVehicleNation'})
        return

    def getVehCD(self):
        return self._nodeCD

    def getVehInvID(self):
        return self._nodeInvID

    def unlockVehicle(self):
        vehicleCD = self._nodeCD
        level = self.itemsCache.items.getItemByCD(vehicleCD).level
        unlockProps = g_techTreeDP.getUnlockProps(vehicleCD, level)
        ItemsActionsFactory.doAction(ItemsActionsFactory.UNLOCK_ITEM, vehicleCD, unlockProps)
        return

    def selectVehicle(self):
        shared_events.selectVehicleInHangar(self._nodeCD)
        return

    def compareVehicle(self):
        self._comparisonBasket.addVehicle(self._nodeCD)
        return

    def buyVehicle(self):
        vehicle = self.itemsCache.items.getItemByCD(self._nodeCD)
        if canBuyGoldForVehicleThroughWeb(vehicle):
            shared_events.showVehicleBuyDialog(vehicle)
        else:
            super(ResearchVehicleContextMenuHandler, self).buyVehicle()
        return

    def changeVehicleNation(self):
        ItemsActionsFactory.doAction(ItemsActionsFactory.CHANGE_NATION, self._nodeCD)
        return

    def _initFlashValues(self, ctx):
        self._nodeCD = int(ctx.vehCD)
        self._nodeState = int(ctx.nodeState)
        vehicle = self.itemsCache.items.getItemByCD(self._nodeCD)
        self._nodeInvID = vehicle.invID if vehicle is not None else None
        self._previewAlias = getattr(ctx, b'previewAlias', VIEW_ALIAS.LOBBY_TECHTREE)
        self._newCM = getattr(ctx, b'newCM', False)
        return

    def _clearFlashValues(self):
        self._nodeCD = None
        self._nodeState = None
        self._nodeInvID = None
        self._previewAlias = None
        self._newCM = None
        return

    def _generateOptions(self, ctx=None):
        if self._newCM:
            return self.__generateOptionsForNewCM(ctx)
        return self.__generateOptionsOldCM(ctx)

    def __generateOptionsForNewCM(self, ctx=None):
        vehicle = self.itemsCache.items.getItemByCD(self._nodeCD)
        options = [
         self._makeItem(VEHICLE.INFO, MENU.CONTEXTMENU_VEHICLEINFOEX)]
        if NODE_STATE.isWasInBattle(self._nodeState):
            options.append(self._makeItem(VEHICLE.STATS, MENU.CONTEXTMENU_SHOWVEHICLESTATISTICS))
        self._manageVehCompareItem(options, vehicle)
        options.append(self._makeItem(VEHICLE.SELECT, MENU.CONTEXTMENU_SELECTVEHICLEINHANGAR, {b'enabled': (NODE_STATE.inInventory(self._nodeState) or NODE_STATE.isRentalOver(self._nodeState))}))
        return options

    def __generateOptionsOldCM(self, ctx=None):
        vehicle = self.itemsCache.items.getItemByCD(self._nodeCD)
        options = [
         self._makeItem(VEHICLE.INFO, MENU.CONTEXTMENU_VEHICLEINFOEX)]
        if NODE_STATE.isWasInBattle(self._nodeState):
            options.append(self._makeItem(VEHICLE.STATS, MENU.CONTEXTMENU_SHOWVEHICLESTATISTICS))
        self._manageVehCompareItem(options, vehicle)
        options.append(self._makeSeparator())
        if vehicle.isUnlocked:
            if not vehicle.isPremiumIGR and (not vehicle.isInInventory or vehicle.isRented):
                if vehicle.isRestoreAvailable():
                    label = MENU.CONTEXTMENU_RESTORE
                elif vehicle.canTradeIn:
                    label = MENU.CONTEXTMENU_BUYORTRADEIN
                else:
                    label = MENU.CONTEXTMENU_BUY
                options.append(self._makeItem(VEHICLE.BUY, label, {b'enabled': (NODE_STATE.isAvailable2Buy(self._nodeState))}))
        else:
            options.append(self._makeItem(VEHICLE.UNLOCK, MENU.CONTEXTMENU_UNLOCK, {b'enabled': (NODE_STATE.isAvailable2Unlock(self._nodeState) and not NODE_STATE.isPremium(self._nodeState))}))
        if vehicle.hasNationGroup:
            if vehicle.isInInventory or vehicle.isRented:
                isNationChangeAvailable = vehicle.isNationChangeAvailable
                nationChangeIsNew = not AccountSettings.getSettings(NATION_CHANGE_VIEWED)
            else:
                isNationChangeAvailable = False
                nationChangeIsNew = False
            options.append(self._makeItem(VEHICLE.NATION_CHANGE, MENU.CONTEXTMENU_NATIONCHANGE, {b'enabled': isNationChangeAvailable, b'isNew': nationChangeIsNew}))
        if not vehicle.isPremiumIGR and not vehicle.isTelecomRent:
            isAvailable2SellOrRemove = NODE_STATE.isAvailable2Sell(self._nodeState)
            if isAvailable2SellOrRemove:
                options.append(self._makeItem(VEHICLE.SELL, MENU.CONTEXTMENU_VEHICLEREMOVE if vehicle.isRented else MENU.CONTEXTMENU_SELL, {b'enabled': isAvailable2SellOrRemove}))
        options.extend([
         self._makeSeparator(),
         self._makeItem(VEHICLE.SELECT, MENU.CONTEXTMENU_SELECTVEHICLEINHANGAR, {b'enabled': (NODE_STATE.inInventory(self._nodeState) or NODE_STATE.isRentalOver(self._nodeState))})])
        return options

    def _manageVehCompareItem(self, optionsRef, vehicle):
        if self._comparisonBasket.isEnabled():
            optionsRef.append(self._makeItem(VEHICLE.COMPARE, MENU.contextmenu(VEHICLE.COMPARE), {b'enabled': (self._comparisonBasket.isReadyToAdd(vehicle))}))
        return


class BlueprintVehicleContextMenuHandler(SimpleVehicleCMHandler):
    __comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, cmProxy, ctx=None):
        super(BlueprintVehicleContextMenuHandler, self).__init__(cmProxy, ctx, {(VEHICLE.UNLOCK): b'unlockVehicle', 
           (VEHICLE.BLUEPRINT): b'showVehicleBlueprint'})
        return

    def getVehCD(self):
        return self._nodeCD

    def getVehInvID(self):
        return

    def unlockVehicle(self):
        level = self.itemsCache.items.getItemByCD(self._nodeCD).level
        unlockProps = g_techTreeDP.getUnlockProps(self._nodeCD, level)
        ItemsActionsFactory.doAction(ItemsActionsFactory.UNLOCK_ITEM, self._nodeCD, unlockProps)
        return

    def showVehicleBlueprint(self):
        shared_events.showBlueprintView(self._nodeCD)
        return

    def _initFlashValues(self, ctx):
        self._nodeCD = int(ctx.vehCD)
        self._nodeState = int(ctx.nodeState)
        self._previewAlias = getattr(ctx, b'previewAlias', VIEW_ALIAS.LOBBY_TECHTREE)
        return

    def _clearFlashValues(self):
        self._nodeCD = None
        self._nodeState = None
        self._previewAlias = None
        return

    def _generateOptions(self, ctx=None):
        options = [self._makeItem(VEHICLE.BLUEPRINT, MENU.CONTEXTMENU_GOTOBLUEPRINT),
         self._makeItem(VEHICLE.UNLOCK, MENU.CONTEXTMENU_UNLOCK, {b'enabled': (NODE_STATE.isAvailable2Unlock(self._nodeState))})]
        return options
