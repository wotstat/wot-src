import typing, nations
from gui import SystemMessages
from gui.Scaleform.daapi import LobbySubView
from gui.impl.lobby.techtree.sound_constants import TECHTREE_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import getTreeNodeCompareData
from gui.Scaleform.daapi.view.meta.ResearchViewMeta import ResearchViewMeta
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS
from gui.impl.lobby.early_access.early_access_window_events import showEarlyAccessQuestsView, showBuyTokensWindow
from gui.techtree.listeners import TTListenerDecorator, IPage
from gui.shared import event_dispatcher as shared_events
from gui.sounds.ambients import LobbySubViewEnv
from helpers import dependency
from logging import getLogger
from skeletons.gui.game_control import IWalletController, IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
_logger = getLogger(__name__)

class ResearchView(LobbySubView, ResearchViewMeta, IPage):
    __sound_env__ = LobbySubViewEnv
    _COMMON_SOUND_SPACE = TECHTREE_SOUND_SPACE
    _itemsCache = dependency.descriptor(IItemsCache)
    _wallet = dependency.descriptor(IWalletController)
    _cmpBasket = dependency.descriptor(IVehicleComparisonBasket)
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, data):
        super(ResearchView, self).__init__()
        self._data = data
        self._canBeClosed = True
        self._listener = TTListenerDecorator()
        return

    def goToBlueprintView(self, vehicleCD):
        shared_events.showBlueprintView(vehicleCD, self._createExitEvent())
        return

    def goToEarlyAccessQuestsView(self):
        showEarlyAccessQuestsView()
        return

    def goToEarlyAccessBuyView(self, vehCD):
        showBuyTokensWindow(parent=self.getParentWindow(), desiredVehCD=vehCD)
        return

    def goToNationChangeView(self, vehicleCD):
        shared_events.showChangeVehicleNationDialog(vehicleCD)
        return

    def goToVehicleCollection(self, nationName):
        nationID = nations.INDICES.get(nationName, nations.NONE_INDEX)
        shared_events.showCollectibleVehicles(nationID)
        return

    def redraw(self):
        raise NotImplementedError(b'Must be overridden in subclass')
        return

    def showSystemMessage(self, typeString, message):
        msgType = SystemMessages.SM_TYPE.lookup(typeString)
        if msgType is None:
            msgType = SystemMessages.SM_TYPE.Error
        SystemMessages.pushMessage(message, msgType)
        return

    def clearSelectedNation(self):
        return

    def invalidateCredits(self):
        result = self._data.invalidateCredits()
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.ENOUGH_MONEY, result)
        return

    def invalidateGold(self):
        result = self._data.invalidateGold()
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.ENOUGH_MONEY, result)
        self.invalidateFreeXP()
        self.invalidateCredits()
        return

    def invalidateFreeXP(self):
        result = self._data.invalidateFreeXP()
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.ENOUGH_XP, result)
        return

    def invalidateElites(self, elites):
        result = self._data.invalidateElites(elites)
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.ELITE, result)
        return

    def invalidateVTypeXP(self, xps):
        self.as_setVehicleTypeXPS(xps.items())
        result = self._data.invalidateVTypeXP()
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.ENOUGH_XP, result)
        return

    def invalidateUnlocks(self, unlocks):
        next2Unlock, unlocked, prevUnlocked = self._data.invalidateUnlocks(unlocks)
        if unlocked:
            _logger.debug(b'unlocked: %s', (b' ').join(str(intCD) for intCD in unlocked))
            self._updateUnlockedItems(unlocked)
        if next2Unlock:
            _logger.debug(b'next2Unlock: %s', (b' ').join(str(intCD) for intCD in next2Unlock))
            self.as_setNext2UnlockS(next2Unlock)
        if prevUnlocked:
            _logger.info(b'previouslyUnlocked %s', prevUnlocked)
            self._updatePrevUnlockedItems(prevUnlocked)
        return

    def invalidateInventory(self, data):
        result = self._data.invalidateInventory(data)
        if result:
            self.as_setInventoryItemsS(result)
        return

    def invalidateBlueprints(self, blueprints):
        raise NotImplementedError(b'Must be overridden in subclass')
        return

    def invalidatePrbState(self):
        result = self._data.invalidatePrbState()
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.VEHICLE_CAN_BE_CHANGED, result)
        return

    def invalidateDiscounts(self, data):
        if self._data.invalidateDiscounts(data):
            self._data.invalidateCredits()
            self._data.invalidateGold()
            self.redraw()
        return

    def invalidateVehLocks(self, locks):
        raise NotImplementedError(b'Must be overridden in subclass')
        return

    def invalidateWalletStatus(self, status):
        raise NotImplementedError(b'Must be overridden in subclass')
        return

    def invalidateRent(self, vehicles):
        raise NotImplementedError(b'Must be overridden in subclass')
        return

    def invalidateRestore(self, vehicles):
        raise NotImplementedError(b'Must be overridden in subclass')
        return

    def request4Info(self, itemCD, rootCD):
        vehicle = self._itemsCache.items.getItemByCD(int(rootCD))
        if vehicle:
            shared_events.showModuleInfo(int(itemCD), vehicle.descriptor)
        return

    def invalidateVehCompare(self):
        getVehicle = self._itemsCache.items.getItemByCD

        def getNodeData(vehCD):
            return getTreeNodeCompareData(getVehicle(vehCD))

        self.as_setNodeVehCompareDataS([(v, getNodeData(v)) for v in self._data.getVehicleCDs()])
        return

    def invalidateVehicleCollectorState(self):
        result = self._data.invalidateVehicleCollectorState()
        if result:
            self.as_setNodesStatesS(NODE_STATE_FLAGS.PURCHASE_DISABLED, result)
        return

    def invalidateVehPostProgression(self):
        return

    def invalidateEarlyAccess(self):
        return

    def _updateUnlockedItems(self, unlocked):
        self.as_setNodesStatesS(NODE_STATE_FLAGS.UNLOCKED, unlocked)
        return

    def _updatePrevUnlockedItems(self, prevUnlocked):
        return

    def _createExitEvent(self):
        return

    def _populate(self):
        super(ResearchView, self)._populate()
        self._listener.startListen(self)
        return

    def _dispose(self):
        self._listener.stopListen()
        super(ResearchView, self)._dispose()
        if self._data is not None:
            self._data.clear(full=True)
            self._data = None
        return
