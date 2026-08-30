from __future__ import absolute_import
import typing
from CurrentVehicle import g_currentPreviewVehicle
from account_helpers import AccountSettings
from account_helpers.AccountSettings import BECOME_ELITE_VEHICLES_WATCHED
from frameworks.wulf.view.array import fillIntsArray
from gui.shared import events
from gui.shared.event_dispatcher import showVehPostProgressionView, showVehicleHubModules
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.impl.backport import createTooltipData
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.hangar.presenters.utils import GUINode
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.lobby.tooltips.veh_post_progression_entry_point_tooltip import VehPostProgressionEntryPointTooltip
from gui.impl.lobby.vehicle_hub.sub_presenters.sub_presenter_base import SubPresenterBase
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.modules_model import ModulesModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_model import ResearchItemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.research_item_display_model import ResearchItemDisplayModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.lobby.techtree import dumpers
from gui.Scaleform.daapi.view.lobby.techtree.listeners import TTListenerDecorator
from gui.Scaleform.daapi.view.lobby.techtree.data import ResearchItemsData
from gui.Scaleform.daapi.view.lobby.techtree.settings import NODE_STATE
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS
from gui.shared.utils.module_upd_available_helper import updateViewedItems
from gui.veh_post_progression.helpers import needToShowCounter
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
from helpers import dependency
if typing.TYPE_CHECKING:
    from typing import Optional

class ModulesTreeViewDumper(dumpers.ResearchItemsObjDumper):
    _itemsCache = dependency.descriptor(IItemsCache)

    def _getItemData(self, node, rootItem):
        itemId = node.getNodeCD()
        item = self._itemsCache.items.getItemByCD(itemId)
        nodePrice = item.getBuyPrice()
        nodePriceCurrency = nodePrice.getCurrency()
        nodeUnlockProps = node.getUnlockProps()
        nodeState = node.getState()
        if node.isVehicle():
            mechanics = set()
            vClass = self._vClassInfo.getInfoByTags(node.getTags())
            imageName = item.name
        else:
            vClass = {b'name': (node.getTypeName())}
            mechanics = {m.guiName for m in item.getModuleMechanicItems(rootItem.descriptor) if not m.isHidden}
            imageName = item.iconName
        return {b'id': itemId, 
           b'image': imageName, 
           b'userName': (node.getShortUserName()), 
           b'primaryClass': vClass, 
           b'level': (node.getLevel()), 
           b'state': (node.getState()), 
           b'requiredXp': (nodeUnlockProps.xpCost), 
           b'isDiscountedXp': (nodeUnlockProps.xpCost < nodeUnlockProps.xpFullCost), 
           b'earnedXp': (node.getEarnedXP()), 
           b'priceAmount': (nodePrice.price.get(nodePriceCurrency)), 
           b'priceCurrency': nodePriceCurrency, 
           b'isDiscountedPrice': (nodePrice.isActionPrice()), 
           b'isResearched': (NODE_STATE.isUnlocked(nodeState)), 
           b'hasEnoughCurrency': (bool(nodeState & NODE_STATE_FLAGS.ENOUGH_MONEY)), 
           b'hasEnoughXP': (bool(nodeState & NODE_STATE_FLAGS.ENOUGH_XP)), 
           b'isElite': (bool(nodeState & NODE_STATE_FLAGS.ELITE)), 
           b'isDisabled': (bool(nodeState & NODE_STATE_FLAGS.LOCKED)), 
           b'autoUnlocked': (bool(nodeState & NODE_STATE_FLAGS.AUTO_UNLOCKED)), 
           b'isInstalled': (NODE_STATE.isInstalled(nodeState)), 
           b'isInInventory': (NODE_STATE.inInventory(nodeState)), 
           b'mechanics': mechanics, 
           b'displayInfo': (node.getDisplayInfo())}


class ModulesSubPresenter(SubPresenterBase):
    _c11nService = dependency.descriptor(ICustomizationService)

    def __init__(self, model, parentView):
        super(ModulesSubPresenter, self).__init__(model, parentView)
        self.__listener = None
        self._data = None
        self._eliteWatchedList = None
        return

    @property
    def vehicle(self):
        return self._data.getRootItem()

    def redraw(self):
        self._data.load()
        self.updateResearchItems()
        self.__updateFieldModification()
        return

    def updateResearchItems(self):
        with self.viewModel.transaction() as model:
            researchItems = model.getResearchItems()
            researchItems.clear()
            self.__fillResearchModels(self._data.dump()[b'top'], model.getPrevResearchItems(), researchItems)
            self.__fillResearchModels(self._data.dump()[b'nodes'], model.getCurrentResearchItems(), researchItems)
        return

    def setVehicleHubCtx(self, vhCtx):
        super(ModulesSubPresenter, self).setVehicleHubCtx(vhCtx)
        if not self._data:
            self._data = ResearchItemsData(ModulesTreeViewDumper())
        self._data.setRootCD(self.vehicleHubCtx.intCD)
        self._data.load()
        self.redraw()
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @property
    def isUnlockShowed(self):
        return self._eliteWatchedList is not None and self.vehicle.intCD in self._eliteWatchedList

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(ModulesSubPresenter, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId == TOOLTIPS_CONSTANTS.TECHTREE_MODULE:
            nodeCD = event.getArgument(b'nodeCD', 0)
            nodeCD = int(nodeCD)
            if not nodeCD:
                return
            thisNode = self._data.getNodeByItemCD(nodeCD)
            guiNode = GUINode(nodeCD, thisNode.getState(), thisNode.getUnlockProps())
            return createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=(
             guiNode,
             self.vehicleHubCtx.intCD))
        else:
            if tooltipId == TOOLTIPS_CONSTANTS.TECHTREE_VEHICLE:
                vehCD = int(event.getArgument(b'vehCD', 0))
                if not vehCD:
                    return
                topLevel = event.getArgument(b'topLevel', False)
                thisNode = self._data.getTopLevelByItemCD(vehCD) if topLevel else self._data.getNodeByItemCD(vehCD)
                guiNode = GUINode(vehCD, thisNode.getState(), thisNode.getUnlockProps())
                return createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=(
                 guiNode,
                 self.vehicleHubCtx.intCD))
            return

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.tooltips.VehPostProgressionEntryPointTooltip():
            return VehPostProgressionEntryPointTooltip(self.vehicle.intCD)
        return super(ModulesSubPresenter, self).createToolTipContent(event=event, contentID=contentID)

    def initialize(self, vhCtx, *args, **kwargs):
        super(ModulesSubPresenter, self).initialize(vhCtx, *args, **kwargs)
        self.updateResearchItems()
        self.__updateFieldModification()
        updateViewedItems(vehicle=self.vehicle)
        return

    def finalize(self):
        super(ModulesSubPresenter, self).finalize()
        if self._data is not None:
            self._data.clear(full=True)
            self._data = None
        self._eliteWatchedList = None
        return

    def invalidateCredits(self):
        self.__updateResearchItemsMap(self._data.invalidateCredits())
        return

    def invalidateGold(self):
        self.__updateResearchItemsMap(self._data.invalidateGold())
        self.invalidateFreeXP()
        self.invalidateCredits()
        return

    def invalidateFreeXP(self):
        self.__updateResearchItemsMap(self._data.invalidateFreeXP())
        return

    def invalidateElites(self, elites):
        elitesResult = self._data.invalidateElites(elites)
        self.__updateResearchItemsMap(elitesResult)
        return

    def invalidateVTypeXP(self, _):
        vTypeXPResult = self._data.invalidateVTypeXP()
        self.__updateResearchItemsMap(vTypeXPResult)
        return

    def invalidateUnlocks(self, unlocks):
        _, unlocked, _ = self._data.invalidateUnlocks(unlocks)
        if unlocked:
            self.redraw()
        return

    def invalidateInventory(self, _):
        installedResult = self._data.invalidateInstalled()
        for installedItem in installedResult:
            if NODE_STATE.isInstalled(installedItem[1]):
                g_currentPreviewVehicle.selectVehicle(self.vehicle.intCD, vehicleStrCD=self.vehicle.strCD, outfit=self.vehicle.getOutfit(self._c11nService.lastAppliedSeason))

        self.redraw()
        return

    def invalidateBlueprints(self, blueprints):
        if blueprints:
            self.redraw()
        return

    def invalidateBlueprintMode(self, _):
        return

    def invalidatePrbState(self):
        self._data.invalidatePrbState()
        self.redraw()
        return

    def invalidateDiscounts(self, data):
        if self._data.invalidateDiscounts(data):
            self._data.invalidateCredits()
            self._data.invalidateGold()
            self.redraw()
        return

    def invalidateVehLocks(self, locks):
        if self._data.invalidateLocks(locks):
            self.redraw()
        return

    def invalidateWalletStatus(self, _):
        self.invalidateFreeXP()
        return

    def invalidateRent(self, vehicles):
        if self._data.getRootCD() in vehicles:
            self.redraw()
        return

    def invalidateRestore(self, vehicles):
        if self._data.getRootCD() in vehicles:
            self.redraw()
        return

    def invalidateVehCompare(self):
        return

    def invalidateVehicleCollectorState(self):
        return

    def invalidateVehPostProgression(self):
        self.redraw()
        return

    def clearSelectedNation(self):
        return

    def _subscribe(self):
        super(ModulesSubPresenter, self)._subscribe()
        self.__listener = TTListenerDecorator()
        self.__listener.startListen(self)
        return

    def _unsubscribe(self):
        if self.__listener is not None:
            self.__listener.stopListen()
            self.__listener = None
        super(ModulesSubPresenter, self)._unsubscribe()
        return

    def _getEvents(self):
        return super(ModulesSubPresenter, self)._getEvents() + (
         (
          self.viewModel.fieldModificationModel.onVehiclePostProgression, self.__onPostProgression),
         (
          self.viewModel.onVehicleChange, self.__changeVehicle),
         (
          self.viewModel.onInstallItem, self.__installItem),
         (
          self.viewModel.onUnlockItem, self.__unlockItem),
         (
          self.viewModel.onBuyAndInstallItem, self.__buyAndInstallItem),
         (
          self.viewModel.onSellItem, self.__sellItem),
         (
          self._itemsCache.onSyncCompleted, self._onSyncCompleted))

    def _getCallbacks(self):
        callbacksTuple = super(ModulesSubPresenter, self)._getCallbacks()
        return callbacksTuple + (
         (
          b'stats.eliteVehicles', self.__onVehicleBecomeElite),
         (
          b'stats.vehTypeXP', self.__updateVehTypeXP),
         (
          b'stats.unlocks', self.__onVehicleBecomeUnlock))

    def _getListeners(self):
        return super(ModulesSubPresenter, self)._getListeners() + (
         (
          events.CloseWindowEvent.BUY_VEHICLE_VIEW_CLOSED, self.__onBuyVehicleWindowClosed),
         (
          events.CloseWindowEvent.ELITE_WINDOW_CLOSED, self.__onEliteWindowClosed))

    def __onEliteWindowClosed(self, _):
        self.__updateFieldModification()
        return

    def __onBuyVehicleWindowClosed(self, event):
        if not event.isAgree:
            self.__updateFieldModification()
        return

    def __onPostProgression(self):
        if not self.isUnlockShowed:
            self._eliteWatchedList.add(self.vehicle.intCD)
            AccountSettings.setSettings(BECOME_ELITE_VEHICLES_WATCHED, self._eliteWatchedList)
            self.__updateFieldModification()
        showVehPostProgressionView(self.vehicle.intCD)
        return

    def __updateFieldModification(self):
        postProgression = self.viewModel.fieldModificationModel
        state = postProgression.HIDDEN
        if self.vehicle.isPostProgressionExists and not self.vehicle.postProgression.isVehSkillTree():
            state = postProgression.UNLOCKED if self.vehicle.postProgressionAvailability(unlockOnly=True) else postProgression.LOCKED
        self._eliteWatchedList = AccountSettings.getSettings(BECOME_ELITE_VEHICLES_WATCHED)
        counter = 1 if needToShowCounter(self.vehicle) or state == postProgression.UNLOCKED and not self.isUnlockShowed else 0
        postProgression.setState(state)
        postProgression.setCounter(counter)
        return

    def __updateVehTypeXP(self, diff):
        vehicleCDs = self._data.getVehicleCDs()
        if any(key in vehicleCDs for key in diff.keys()):
            self.redraw()
        return

    def __fillResearchModels(self, data, researchItemsModel, researchItemsMap):
        researchItemsModel.clear()
        for item in data:
            researchItemModel = self.__fillResearchItemModel(item)
            researchItemDisplayModel = self.__fillResearchItemDisplayModel(item)
            researchItemsMap.set(researchItemModel.getId(), researchItemModel)
            researchItemsModel.addViewModel(researchItemDisplayModel)

        researchItemsModel.invalidate()
        return

    def __fillResearchItemModel(self, item):
        researchItemModel = ResearchItemModel()
        displayInfo = item[b'displayInfo']
        researchItemModel.setId(item[b'id'])
        researchItemModel.setImage(item[b'image'])
        researchItemModel.setRenderer(displayInfo[b'renderer'])
        researchItemModel.setUserName(item[b'userName'])
        researchItemModel.setLevel(item[b'level'])
        researchItemModel.setState(item[b'state'])
        researchItemModel.setRequiredXp(item[b'requiredXp'])
        researchItemModel.setIsDiscountedXp(item[b'isDiscountedXp'])
        researchItemModel.setPrimaryClass(item[b'primaryClass'][b'name'])
        researchItemModel.setEarnedXp(item[b'earnedXp'])
        researchItemModel.setPriceAmount(item[b'priceAmount'])
        researchItemModel.setPriceCurrency(item[b'priceCurrency'])
        researchItemModel.setIsDiscountedPrice(item[b'isDiscountedPrice'])
        researchItemModel.setIsResearched(item[b'isResearched'])
        researchItemModel.setHasEnoughXP(item[b'hasEnoughXP'])
        researchItemModel.setHasEnoughCurrency(item[b'hasEnoughCurrency'])
        researchItemModel.setIsElite(item[b'isElite'])
        researchItemModel.setAutoUnlocked(item[b'autoUnlocked'])
        researchItemModel.setIsInstalled(item[b'isInstalled'])
        researchItemModel.setIsDisabled(item[b'isDisabled'])
        researchItemModel.setIsInInventory(item[b'isInInventory'])
        fillIntsArray(displayInfo[b'path'], researchItemModel.getPath())
        mechanics = researchItemModel.getMechanics()
        mechanics.clear()
        for mechanicName in item.get(b'mechanics'):
            mechanicModel = VehicleMechanicModel()
            mechanicModel.setName(mechanicName)
            mechanics.addViewModel(mechanicModel)

        mechanics.invalidate()
        if displayInfo[b'renderer'] == b'item':
            urgentIds = [id for id, _ in self._data.getUrgentIds(item[b'id'])]
            fillIntsArray(urgentIds, researchItemModel.getUrgentIds())
        return researchItemModel

    def __fillResearchItemDisplayModel(self, item):
        researchItemDisplayModel = ResearchItemDisplayModel()
        displayInfo = item[b'displayInfo']
        researchItemDisplayModel.setId(item[b'id'])
        researchItemDisplayModel.setLevel(displayInfo[b'level'])
        researchItemDisplayModel.setRenderer(displayInfo[b'renderer'])
        fillIntsArray(displayInfo[b'path'], researchItemDisplayModel.getPath())
        return researchItemDisplayModel

    def __getNodesToUpdate(self, invalidationResult):
        return {r[0] for r in invalidationResult}

    def __updateResearchItemsMap(self, invalidationResult):
        nodesToUpdate = self.__getNodesToUpdate(invalidationResult)
        if not nodesToUpdate:
            return
        else:
            with self.viewModel.transaction() as model:
                researchItems = model.getResearchItems()
                for intCD in nodesToUpdate:
                    item = self._data.invalidateItem(intCD)
                    if item is not None:
                        researchItems.set(intCD, self.__fillResearchItemModel(item))

            return

    @args2params(int)
    def __changeVehicle(self, itemCD):
        showVehicleHubModules(itemCD)
        return

    def __onVehicleBecomeElite(self, elite):
        if self.vehicle.intCD in elite:
            self.invalidateElites(elite)
            self.__updateFieldModification()
        return

    def __onVehicleBecomeUnlock(self, unlocks):
        if self.vehicle.intCD in unlocks:
            self.__updateFieldModification()
        return

    def _onSyncCompleted(self, _, diff):
        if self.vehicle.intCD in diff.get(GUI_ITEM_TYPE.VEH_POST_PROGRESSION, {}):
            self.__updateFieldModification()
        return

    @args2params(int)
    def __buyAndInstallItem(self, itemCD):
        ItemsActionsFactory.doAction(ItemsActionsFactory.BUY_AND_INSTALL_AND_SELL_ITEM, itemCD, self._data.getRootCD(), skipConfirm=False)
        return

    @args2params(int)
    def __unlockItem(self, itemCD):
        node = self._data.getNodeByItemCD(itemCD)
        unlockProps = node.getUnlockProps() if node is not None else None
        if unlockProps is not None:
            ItemsActionsFactory.doAction(ItemsActionsFactory.UNLOCK_ITEM, itemCD, unlockProps, skipConfirm=False)
        return

    @args2params(int)
    def __installItem(self, itemCD):
        ItemsActionsFactory.doAction(ItemsActionsFactory.INSTALL_ITEM, itemCD, self._data.getRootCD())
        return

    @args2params(int)
    def __sellItem(self, itemCD):
        ItemsActionsFactory.doAction(ItemsActionsFactory.SELL_ITEM, itemCD)
        return
