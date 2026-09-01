from __future__ import absolute_import
import BigWorld
from frameworks.wulf import WindowLayer
from frameworks_common.state_machine.transitions import TransitionType
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lootbox_system.main_view_model import SubViewID
from gui.lootbox_system.base.awards_manager import AwardsManager
from gui.shared.event_dispatcher import showHangar
from gui.lootbox_system.base.common import REROLLABLE_BOX_OPEN_COUNT, getTextResource
from gui.Scaleform.framework.entities.View import ViewKey
from gui.lobby_state_machine.states import StateFlags, LobbyStateFlags, SubScopeSubLayerState, LobbyState, LobbyStateDescription, SFViewLobbyState
from gui.shared.system_factory import collectLootBoxInfoPage, collectLootBoxMainView
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.app_loader import IAppLoader
from helpers import dependency
from skeletons.gui.game_control import ILootBoxSystemController
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
_REWARD_SUBVIEW_IDS = (
 SubViewID.SINGLE_BOX_REWARDS, SubViewID.MULTIPLE_BOXES_REWARDS)

def registerStates(machine):
    machine.addState(LootBoxState())
    return


def registerTransitions(machine):
    lootBox = machine.getStateByCls(LootBoxState)
    machine.addNavigationTransitionFromParent(lootBox)
    return


class _LootBoxBaseState(SFViewLobbyState):
    _lootBoxes = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_LootBoxBaseState, self).__init__(flags)
        self._shouldRedirectToHangar = True
        self.__cachedParams = {}
        return

    @classmethod
    def goTo(cls, ctx):
        super(_LootBoxBaseState, cls).goTo(ctx=ctx)
        return

    def getNavigationDescription(self):
        eventName = self.__cachedParams.get(b'ctx', {}).get(b'eventName')
        return LobbyStateDescription(title=backport.text(getTextResource([b'preview', b'backLabel'], eventName)()))

    def registerTransitions(self):
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import StylePreviewState
        from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import ConfigurableVehiclePreviewState
        lsm = self.getMachine()
        self.addNavigationTransition(lsm.getStateByCls(ShopState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(StylePreviewState), record=True)
        self.addNavigationTransition(lsm.getStateByCls(ConfigurableVehiclePreviewState), record=True)
        return

    def serializeParams(self):
        ctx = self.__cachedParams.get(b'ctx', {})
        ctx.update({b'isReopen': True})
        return {b'ctx': ctx}

    def isLootBoxesAvailable(self):
        eventName = self.__cachedParams.get(b'ctx', {}).get(b'eventName')
        return self._lootBoxes.isAvailable(eventName) and self._lootBoxes.getActiveBoxes(eventName)

    def updateCachedCtx(self, params):
        ctx = self.__cachedParams.get(b'ctx', {})
        ctx.update(params)
        self.__cachedParams[b'ctx'] = ctx
        return

    def _getEvents(self):
        return (
         (
          self._lootBoxes.onStatusChanged, self.__onStatusChanged),
         (
          self._lootBoxes.onBoxesAvailabilityChanged, self.__onStatusChanged))

    def _subscribe(self):
        for event, handler in self._getEvents():
            event += handler

        return

    def _unsubscribe(self):
        for event, handler in self._getEvents():
            event -= handler

        return

    def _onEntered(self, event):
        super(_LootBoxBaseState, self)._onEntered(event)
        self._subscribe()
        self.__cachedParams = event.params
        if not self.isLootBoxesAvailable() and self._shouldRedirectToHangar:
            showHangar()
        return

    def _onExited(self):
        super(_LootBoxBaseState, self)._onExited()
        self._unsubscribe()
        return

    def _getViewLoadCtx(self, event):
        return {b'ctx': (event.params.get(b'ctx', {}))}

    def __onStatusChanged(self):
        if not self.isLootBoxesAvailable() and self._shouldRedirectToHangar:
            showHangar()
        return


@SubScopeSubLayerState.parentOf
class LootBoxState(LobbyState):
    __appLoader = dependency.instance(IAppLoader)

    def __init__(self):
        super(LootBoxState, self).__init__()
        self.__previouslyVisibleLayers = []
        return

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(LootBoxMainState(LobbyStateFlags.INITIAL))
        lsm.addState(LootBoxInfoState())
        lsm.addState(LootBoxAutoOpenState())
        return

    def registerTransitions(self):
        for state in self.getChildrenStates():
            self.getParent().addNavigationTransition(state)
            self.addNavigationTransition(state)

        return

    def _onEntered(self, event):
        super(LootBoxState, self)._onEntered(event)
        containerManager = self.__appLoader.getApp().containerManager
        self.__previouslyVisibleLayers = containerManager.getVisibleLayers()
        containerManager.setVisibleLayers(self._getVisibleLayers())
        BigWorld.worldDrawEnabled(False)
        return

    def _onExited(self):
        super(LootBoxState, self)._onExited()
        self.__appLoader.getApp().containerManager.setVisibleLayers(self.__previouslyVisibleLayers)
        BigWorld.worldDrawEnabled(True)
        return

    def _getVisibleLayers(self):
        return [WindowLayer.TOP_WINDOW, WindowLayer.FULLSCREEN_WINDOW, WindowLayer.TOOLTIP, WindowLayer.OVERLAY]


@LootBoxState.parentOf
class LootBoxInfoState(_LootBoxBaseState):
    STATE_ID = b'lootBoxInfoState'
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOOT_BOXES_INFO_VIEW)

    def getViewKey(self, params=None):
        for validator, viewKey in collectLootBoxInfoPage():
            if validator():
                return viewKey

        return self.VIEW_KEY


@LootBoxState.parentOf
class LootBoxMainState(_LootBoxBaseState):
    STATE_ID = b'lootBoxMainState'
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOOT_BOXES_MAIN_VIEW)

    def _onEntered(self, event):
        super(LootBoxMainState, self)._onEntered(event)
        uiLoader = dependency.instance(IGuiLoader)
        windowsManager = uiLoader.windowsManager
        window = windowsManager.getViewByLayoutID(R.views.mono.lootbox.main())
        ctx = event.params.get(b'ctx', {})
        if ctx is not None and window is not None:
            eventName = ctx.get(b'eventName')
            if eventName is not None and ctx.get(b'subViewID') not in _REWARD_SUBVIEW_IDS:
                for box in self._lootBoxes.getActiveBoxes(eventName):
                    category = box.getCategory()
                    rewards = self._lootBoxes.getPendingRerollRewards(eventName, category)
                    if rewards is not None:
                        ctx.update({b'count': REROLLABLE_BOX_OPEN_COUNT, 
                           b'bonuses': [
                                      AwardsManager.composeBonuses(eventName, [rewards])], 
                           b'category': category, 
                           b'subViewID': (SubViewID.SINGLE_BOX_REWARDS), 
                           b'isReopen': True})
                        break

            window.switchToSubView(**ctx)
        return

    def getViewKey(self, params=None):
        for validator, viewKey in collectLootBoxMainView():
            if validator():
                return viewKey

        return self.VIEW_KEY

    def registerTransitions(self):
        super(LootBoxMainState, self).registerTransitions()
        from gui.Scaleform.daapi.view.lobby.store.browser.states import ShopState
        machine = self.getMachine()
        info = machine.getStateByCls(LootBoxInfoState)
        shop = machine.getStateByCls(ShopState)
        self.addNavigationTransition(self, transitionType=TransitionType.EXTERNAL)
        self.addNavigationTransition(info, record=True)
        self.addNavigationTransition(shop, record=True)
        return


@LootBoxState.parentOf
class LootBoxAutoOpenState(_LootBoxBaseState):
    STATE_ID = b'lootBoxAutoOpenState'
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOOT_BOXES_AUTO_OPEN_VIEW)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(LootBoxAutoOpenState, self).__init__(flags)
        self._shouldRedirectToHangar = False
        return
