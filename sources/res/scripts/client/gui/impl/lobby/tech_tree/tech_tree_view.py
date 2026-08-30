import json
from logging import getLogger
import typing, Event, nations
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NATIONS_VISITED
from frameworks_common.state_machine import BaseStateObserver, visitor
from frameworks.wulf import ViewSettings, WindowFlags
from frameworks.wulf.view.array import fillStringsArray
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getPremiumVehiclesUrl
from gui.Scaleform.daapi.view.lobby.techtree import dumpers
from gui.Scaleform.daapi.view.lobby.techtree.data import NationTreeData
from gui.Scaleform.daapi.view.lobby.techtree.listeners import TTListenerDecorator
from gui.Scaleform.daapi.view.lobby.techtree.settings import NODE_STATE
from gui.Scaleform.daapi.view.lobby.techtree.settings import SelectedNation
from gui.Scaleform.daapi.view.lobby.techtree.sound_constants import TECHTREE_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.techtree.states import TechtreeState
from gui.Scaleform.daapi.view.lobby.techtree.techtree_dp import g_techTreeDP
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.backport import BackportContextMenuWindow, createContextMenuData, BackportTooltipWindow
from gui.impl.backport import createTooltipData
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.tech_tree.tech_tree_view_model import TechTreeViewModel, NationEnum
from gui.impl.gui_decorators import args2params
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.lobby.hangar.presenters.utils import GUINode
from gui.lobby_state_machine.routable_view import IRoutableView
from gui.lobby_state_machine.router import SubstateRouter
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showVehicleHubModules
from gui.shared.utils.vehicle_collector_helper import hasCollectibleVehicles
from gui.sounds.ambients import LobbySubViewEnv
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext
if typing.TYPE_CHECKING:
    from typing import Tuple, List, Set, Dict, Optional
    from gui.Scaleform.daapi.view.lobby.techtree.settings import UnlockProps
    from gui.Scaleform.daapi.view.lobby.techtree.nodes import RealNode
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
    from frameworks_common.state_machine import State
    from gui.shared.events import NavigationEvent
_logger = getLogger(__name__)
_VEHICLE_URL_FILTER_PARAM = 1

class _NationTreeViewDumper(dumpers._BaseDumper):

    def __init__(self, cache=None):
        if cache is None:
            cache = {b'techTreeNodes': {}, b'nodeOverrides': {}}
        super(_NationTreeViewDumper, self).__init__(cache)
        return

    def clear(self, full=False):
        self._cache[b'techTreeNodes'].clear()
        self._cache[b'nodeOverrides'].clear()
        if full:
            self._vClassInfo.clear()
        return

    def dump(self, data):
        self.clear()
        nodeRows = {node.getNodeCD(): node.getDisplayInfo()[b'row'] for node in data.getNodes()}
        techTreeNodes = self._cache[b'techTreeNodes']
        for node in data.getNodes():
            techTreeNodes[node.getNodeCD()] = self._getTechTreeNodes(node, nodeRows)

        nodeOverrides = self._cache[b'nodeOverrides']
        for node in data.getNodes():
            nodeOverrides[node.getNodeCD()] = self._getNodeOverrides(node)

        return self._cache

    def _getTechTreeNodes(self, node, nodeRows):
        displayInfo = node.getDisplayInfo()
        currentNodeRow = displayInfo[b'row']
        childIds = [inPin[b'childID'] for line in displayInfo[b'lines'] for inPin in line[b'inPins']]
        childBranchOrders = [nodeRows[childId] - currentNodeRow for childId in childIds]
        nodeTags = node.getTags()
        nodeState = node.getState()
        return {b'id': (node.getNodeCD()), 
           b'name': (node.getShortUserName()), 
           b'techName': (node.getItem().name), 
           b'nation': (nations.NAMES[node.getNationID()]), 
           b'type': (self._vClassInfo.getInfoByTags(nodeTags)[b'name']), 
           b'level': (node.getLevel()), 
           b'orderPriority': currentNodeRow, 
           b'childIds': childIds, 
           b'childBranchOrders': childBranchOrders, 
           b'isPremium': (NODE_STATE.isPremium(nodeState))}

    def _getNodeOverrides(self, node):
        nodeState = node.getState()
        nodeUnlockProps = node.getUnlockProps()
        nodePrice = node.getItem().getBuyPrice()
        nodePriceCurrency = nodePrice.getCurrency()
        nodeCompareData = node.getCompareData()
        return {b'id': (node.getNodeCD()), 
           b'isResearched': (NODE_STATE.isUnlocked(nodeState)), 
           b'readyForResearch': (NODE_STATE.isNext2Unlock(nodeState)), 
           b'hasEnoughXp': (bool(nodeState & NODE_STATE_FLAGS.ENOUGH_XP)), 
           b'requiredXp': (nodeUnlockProps.xpCost), 
           b'isDiscountedXp': (nodeUnlockProps.xpCost < nodeUnlockProps.xpFullCost), 
           b'earnedXp': (node.getEarnedXP()), 
           b'isElite': (bool(nodeState & NODE_STATE_FLAGS.ELITE)), 
           b'isInInventory': (NODE_STATE.inInventory(nodeState)), 
           b'hasEnoughCurrency': (bool(nodeState & NODE_STATE_FLAGS.ENOUGH_MONEY)), 
           b'highlightedForPurchase': (bool(nodeState & NODE_STATE_FLAGS.LAST_2_BUY)), 
           b'priceAmount': (nodePrice.price.get(nodePriceCurrency)), 
           b'priceCurrency': nodePriceCurrency, 
           b'isDiscountedPrice': (nodePrice.isActionPrice()), 
           b'readyForRecovery': (bool(nodeState & NODE_STATE_FLAGS.RESTORE_AVAILABLE)), 
           b'isRented': (bool(nodeState & NODE_STATE_FLAGS.VEHICLE_IN_RENT)), 
           b'readyForTradeIn': (bool(nodeState & NODE_STATE_FLAGS.CAN_TRADE_IN)), 
           b'readyForComparison': (nodeCompareData.get(b'modeAvailable', False) and not nodeCompareData.get(b'cmpBasketFull', False))}


class _TechTreeStatesObserver(BaseStateObserver):

    def __init__(self):
        super(_TechTreeStatesObserver, self).__init__()
        self.onSwitchNation = Event.Event()
        return

    def clear(self):
        super(_TechTreeStatesObserver, self).clear()
        self.onSwitchNation.clear()
        return

    def isObservingState(self, state):
        lsm = state.getMachine()
        return visitor.isDescendantOf(state, lsm.getStateByCls(TechtreeState))

    def onEnterState(self, state, event):
        if event is None:
            return
        else:
            self.onSwitchNation(event.params)
            return


def _getVehCDs(invalidationResult):
    return {r[0] for r in invalidationResult}


class TechTreeView(ViewImpl, IRoutableView):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __cmpBasket = dependency.descriptor(IVehicleComparisonBasket)
    __sound_env__ = LobbySubViewEnv
    _COMMON_SOUND_SPACE = TECHTREE_SOUND_SPACE

    def __init__(self, layoutID, ctx=None):
        self.__ctx = ctx
        self.__nationTreeData = NationTreeData(_NationTreeViewDumper())
        settings = ViewSettings(layoutID)
        settings.model = TechTreeViewModel()
        self.__techTreeStatesObserver = _TechTreeStatesObserver()
        self.__listener = TTListenerDecorator()
        self.__router = None
        super(TechTreeView, self).__init__(settings)
        return

    def _onLoading(self, *args, **kwargs):
        super(TechTreeView, self)._onLoading(*args, **kwargs)
        self.__onInitNation(self.__ctx)
        self.__listener.startListen(self)
        return

    def _onLoaded(self, *args, **kwargs):
        lsm = getLobbyStateMachine()
        lsm.connect(self.__techTreeStatesObserver)
        self.__router = SubstateRouter(lsm, self, lsm.getStateByCls(TechtreeState))
        self.__router.init()
        return

    def _finalize(self):
        super(TechTreeView, self)._finalize()
        self.__listener.stopListen()
        self.__listener = None
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__techTreeStatesObserver)
        self.__techTreeStatesObserver = None
        self.__router.fini()
        self.__router = None
        return

    @property
    def viewModel(self):
        return super(TechTreeView, self).getViewModel()

    def getRouterModel(self):
        return self.getViewModel().router

    def redraw(self):
        self.__fullUpdateOfViewModel()
        return

    def createToolTip(self, event):
        tooltipData = None
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument(b'tooltipId')
            if tooltipId == TOOLTIPS_CONSTANTS.TECHTREE_VEHICLE:
                vehCD = event.getArgument(b'vehCD', 0)
                vehCD = int(vehCD)
                if not vehCD:
                    return
                thisNode = self.__nationTreeData.getNodeByItemCD(vehCD)
                guiNode = GUINode(vehCD, thisNode.getState(), thisNode.getUnlockProps())
                parentNodeCD = first(g_techTreeDP.getTopLevel(vehCD))
                if not parentNodeCD:
                    rootItem = self.__nationTreeData.getRootItem()
                    if rootItem:
                        parentNodeCD = rootItem.getNodeCD()
                    else:
                        parentNodeCD = 0
                tooltipData = createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=(
                 guiNode,
                 parentNodeCD))
            elif tooltipId == TOOLTIPS_CONSTANTS.VEHICLE_COLLECTOR_INFO:
                tooltipData = createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=(
                 SelectedNation.getName(),))
            elif tooltipId == TOOLTIPS_CONSTANTS.TRADE_IN:
                vehCD = event.getArgument(b'vehCD', 0)
                vehCD = int(vehCD)
                if not vehCD:
                    return
                tooltipData = createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=(
                 vehCD,))
        if tooltipData is not None:
            window = BackportTooltipWindow(tooltipData, self.getWindow())
            window.load()
            return window
        else:
            return super(TechTreeView, self).createToolTip(event)

    def createContextMenu(self, event):
        if event.contentID != R.aliases.common.contextMenu.Backport():
            return
        else:
            menuArgs = event.getArgument(b'menuArgs', None)
            args = json.loads(menuArgs)
            vehCD = args.get(b'vehCD')
            node = self.__nationTreeData.getNodeByItemCD(vehCD)
            if not node:
                _logger.warning(b"Couldn't find node by vehCD=%d", vehCD)
                return
            contextMenuArgs = {b'vehCD': vehCD, 
               b'nodeState': (node.getState()), 
               b'newCM': True}
            contextMenuData = createContextMenuData(event.getArgument(b'menuId'), contextMenuArgs)
            window = BackportContextMenuWindow(contextMenuData, self.getWindow())
            window.load()
            return window

    def _getEvents(self):
        events = (
         (
          self.__techTreeStatesObserver.onSwitchNation, self.__onSwitchNation),
         (
          self.viewModel.onOpenAboutVehicle, self.__onOpenAboutVehicle),
         (
          self.viewModel.onAddToCompare, self.__onAddToCompare),
         (
          self.viewModel.onOpenCollectableVehicles, self.__onOpenCollectableVehicles),
         (
          self.viewModel.onOpenPremiumShop, self.__onOpenPremiumShop))
        return events

    def __onInitNation(self, args):
        nation = args.get(b'nation', None)
        if nation is not None and nation in nations.INDICES:
            nationIdx = nations.INDICES[nation]
            SelectedNation.select(nationIdx)
        else:
            SelectedNation.byDefault()
        self.__fullUpdateOfViewModel()
        return

    @args2params(str)
    def __onSwitchNation(self, nation):
        if nation == SelectedNation.getName():
            return
        nationID = nations.INDICES[nation]
        SelectedNation.select(nationID)
        self.__fullUpdateOfViewModel()
        return

    @args2params(int, str)
    def __onOpenAboutVehicle(self, vehCD, route):
        showVehicleHubModules(vehCD)
        return

    @args2params(int)
    def __onAddToCompare(self, vehCD):
        self.__cmpBasket.addVehicle(vehCD)
        return

    @args2params(str)
    def __onOpenCollectableVehicles(self, nation):
        nationID = nations.INDICES.get(nation, nations.NONE_INDEX)
        shared_events.showCollectibleVehicles(nationID)
        return

    @args2params(str, int)
    def __onOpenPremiumShop(self, nation, level):
        params = {b'nation': nation, b'level': level, b'vehicleFilterByUrl': _VEHICLE_URL_FILTER_PARAM}
        shared_events.showShop(url=getPremiumVehiclesUrl(), params=params)
        return

    def __getCollectableVehiclesSate(self):
        isVehicleCollectorEnabled = self.__lobbyContext.getServerSettings().isCollectorVehicleEnabled()
        return isVehicleCollectorEnabled and hasCollectibleVehicles(SelectedNation.getIndex())

    def __fullUpdateOfViewModel(self):
        visitedNations = AccountSettings.getSettings(NATIONS_VISITED)
        self.__nationTreeData.load(SelectedNation.getIndex())
        nationTreeDump = self.__nationTreeData.dump()
        nation = SelectedNation.getName()
        nationIdx = SelectedNation.getIndex()
        with self.viewModel.transaction() as vm:
            vm.setSelectedNation(NationEnum(nation))
            vm.setCollectableVehiclesAvailable(self.__getCollectableVehiclesSate())
            vm.setFirstHighlightedLevel(g_techTreeDP.getDisplaySettings(nationIdx)[b'firstLevelToHighlight'])
            vm.setShowWelcomeAnimation(nationIdx not in visitedNations)
            fillStringsArray(g_techTreeDP.getAvailableNations(), vm.getAvailableNations())
            self.__fillTechTreeNodes(vm, nationTreeDump[b'techTreeNodes'])
            self.__fillNodeOverrides(vm, nationTreeDump[b'nodeOverrides'])
        visitedNations.add(nationIdx)
        AccountSettings.setSettings(NATIONS_VISITED, visitedNations)
        return

    def __fillTechTreeNodes(self, vm, techTreeNodesDump):
        techTreeNodes = vm.getTechTreeNodes()
        techTreeNodes.clear()
        for vehId, vehData in techTreeNodesDump.iteritems():
            techTreeNodes.set(vehId, json.dumps(vehData))

        return

    def __fillNodeOverrides(self, vm, nodeOverridesDump):
        nodeOverrides = vm.getNodeOverrides()
        nodeOverrides.clear()
        for vehId, vehData in nodeOverridesDump.iteritems():
            nodeOverrides.set(vehId, json.dumps(vehData))

        return

    def __updateAllNodeOverrides(self):
        nationTreeDump = self.__nationTreeData.dump()
        with self.viewModel.transaction() as vm:
            self.__fillNodeOverrides(vm, nationTreeDump[b'nodeOverrides'])
        return

    def __updateCollectableVehiclesState(self):
        with self.viewModel.transaction() as vm:
            vm.setCollectableVehiclesAvailable(self.__getCollectableVehiclesSate())
        return

    def __updateNodeOverrides(self, nodesToUpdate):
        if not nodesToUpdate:
            return
        nodeOverridesDump = self.__nationTreeData.dump()[b'nodeOverrides']
        with self.viewModel.transaction() as vm:
            nodeOverrides = vm.getNodeOverrides()
            for vehId in nodesToUpdate:
                if vehId not in nodeOverrides:
                    _logger.error(b'Vehicle with id %d is not in node overrides model', vehId)
                    continue
                if vehId not in nodeOverridesDump:
                    _logger.error(b'Vehicle with id %d is not in node overrides dump', vehId)
                    continue
                nodeOverrides.set(vehId, json.dumps(nodeOverridesDump[vehId]))

        return

    def __invalidateAllCurrencies(self):
        nodesToUpdate = set()
        nodesToUpdate |= _getVehCDs(self.__nationTreeData.invalidateGold())
        nodesToUpdate |= _getVehCDs(self.__nationTreeData.invalidateFreeXP())
        nodesToUpdate |= _getVehCDs(self.__nationTreeData.invalidateCredits())
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateBlueprintMode(self, isEnabled):
        return

    def invalidateVehLocks(self, locks):
        if self.__nationTreeData.invalidateLocks(locks):
            self.__updateAllNodeOverrides()
        return

    def invalidateVTypeXP(self, xps):
        nodesToUpdate = set()
        for vehCD, xp in xps.iteritems():
            node = self.__nationTreeData.getNodeByItemCD(vehCD)
            if node:
                node.setEarnedXP(xp)
                nodesToUpdate.add(vehCD)

        nodesToUpdate |= _getVehCDs(self.__nationTreeData.invalidateVTypeXP())
        nodesToUpdate |= _getVehCDs(self.__nationTreeData.invalidateXpCosts())
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateWalletStatus(self, status):
        self.__invalidateAllCurrencies()
        return

    def invalidateRent(self, vehicles):
        return

    def invalidateRestore(self, vehicles):
        if self.__nationTreeData.invalidateRestore(vehicles):
            self.__updateAllNodeOverrides()
        return

    def invalidateBlueprints(self, blueprints):
        if not blueprints:
            return
        nodesToUpdate = _getVehCDs(self.__nationTreeData.invalidateBlueprints(blueprints))
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateVehicleCollectorState(self):
        self.__updateCollectableVehiclesState()
        return

    def invalidateCredits(self):
        nodesToUpdate = _getVehCDs(self.__nationTreeData.invalidateCredits())
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateGold(self):
        self.__invalidateAllCurrencies()
        return

    def invalidateFreeXP(self):
        nodesToUpdate = _getVehCDs(self.__nationTreeData.invalidateFreeXP())
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateElites(self, elites):
        nodesToUpdate = _getVehCDs(self.__nationTreeData.invalidateElites(elites))
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateUnlocks(self, unlocks):
        next2Unlock, unlocked, prevUnlocked = self.__nationTreeData.invalidateUnlocks(unlocks)
        nodesToUpdate = _getVehCDs(next2Unlock) | _getVehCDs(unlocked) | _getVehCDs(prevUnlocked)
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidateInventory(self, data):
        nodesToUpdate = _getVehCDs(self.__nationTreeData.invalidateInventory(data))
        self.__updateNodeOverrides(nodesToUpdate)
        return

    def invalidatePrbState(self):
        return

    def invalidateDiscounts(self, data):
        if self.__nationTreeData.invalidateDiscounts(data):
            self.__invalidateAllCurrencies()
            self.__updateAllNodeOverrides()
        return

    def invalidateVehCompare(self):
        self.__updateAllNodeOverrides()
        return

    def invalidateVehPostProgression(self):
        return

    def clearSelectedNation(self):
        SelectedNation.clear()
        return


class TechTreeWindow(WindowImpl):

    def __init__(self, layer, **kwargs):
        self.__background_alpha__ = 1.0
        layoutID = R.views.mono.tech_tree.main()
        super(TechTreeWindow, self).__init__(WindowFlags.WINDOW, layer=layer, content=TechTreeView(layoutID, kwargs[b'ctx']))
        return
