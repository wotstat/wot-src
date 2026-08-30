from __future__ import absolute_import
import logging, math, typing
from functools import partial
import BigWorld, adisp
from BWUtil import AsyncReturn
from ClientSelectableCameraObject import ClientSelectableCameraObject
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from WeakMethod import WeakMethodProxy
from frameworks_common.state_machine import StateFlags, visitor
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey, ViewKeyDynamic
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams
from gui.impl import backport
from gui.lobby_state_machine.states import LobbyState, SFViewLobbyState, GuiImplViewLobbyState, UntrackedState, SubScopeSubLayerState, SubScopeTopLayerState, TopScopeTopLayerState, LobbyStateDescription
from gui.lobby_state_machine.transitions import NavigationTransition, GuardTransition
from gui.impl.dialogs import dialogs
from gui.impl.dialogs.builders import ResPureDialogBuilder
from gui.impl.gen import R
from gui.impl.pub.dialog_window import DialogButtons
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from gui.shared.event_dispatcher import showHangar
from gui.shared.events import NavigationEvent, LoadGuiImplViewEvent
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider, SubhangarStateGroups, SubhangarStateGroupConfig
from helpers import dependency
from helpers.events_handler import EventsHandler
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.impl import IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from vehicle_systems.stricted_loading import makeCallbackWeak
from wg_async import wg_await, wg_async, BrokenPromiseError
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
_logger = logging.getLogger(__name__)

def registerStates(machine):
    machine.addState(CustomizationState())
    machine.addState(_CustomizationMidState())
    machine.addState(_CustomizationTopState())
    return


def registerTransitions(machine):
    customization = machine.getStateByCls(CustomizationState)
    machine.addNavigationTransitionFromParent(customization)
    return


@SubScopeSubLayerState.parentOf
class CustomizationState(LobbyState, EventsHandler, SubhangarStateGroupConfigProvider):
    STATE_ID = b'customization'
    __CAMERA_NAME = b'Customization'
    __ENVIRONMENT_NAME = b'Customization'
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __c11n = dependency.descriptor(ICustomizationService)

    @classmethod
    def goTo(cls, vehInvID=None, callback=None, season=None, modeId=None, tabId=None, itemCD=None):
        super(CustomizationState, cls).goTo(vehInvID=vehInvID, callback=callback, season=season, modeId=modeId, tabId=tabId, itemCD=itemCD)
        return

    def registerStates(self):
        self.addChildState(_LoadingState(StateFlags.INITIAL))
        self.addChildState(_MainState())
        self.addChildState(_ExitState())
        return

    def registerTransitions(self):
        machine = self.getMachine()
        loading = machine.getStateByCls(_LoadingState)
        main = machine.getStateByCls(_MainState)
        loading.addNavigationTransition(main)
        return

    def getSubhangarStateGroupConfig(self):
        return SubhangarStateGroupConfig((
         SubhangarStateGroups.Customization,), environmentName=self.__ENVIRONMENT_NAME)

    def makeTransition(self, transitionType, record):
        return _CustomizationTransition(transitionType, record)

    def serializeParams(self):
        ctx = self.__c11n.getCtx()
        return {b'season': (ctx.season), 
           b'modeId': (ctx.modeId), 
           b'tabId': (ctx.mode.tabId), 
           b'source': (ctx.mode.source), 
           b'itemCD': (ctx.mode.selectedItem), 
           b'callback': None}

    def _onEntered(self, event):
        super(CustomizationState, self)._onEntered(event)
        self._subscribe()
        return

    def _onExited(self):
        self._unsubscribe()
        super(CustomizationState, self)._onExited()
        if self.__hangarSpace.spaceInited:
            self.__hangarSpace.space.turretAndGunAngles.reset()
        return

    def _getViewLoadCtx(self, event):
        return {b'ctx': (event.params)}

    def _getListeners(self):
        return (
         (
          events.CustomizationEvent.CLOSE, self.__showHangar, EVENT_BUS_SCOPE.LOBBY),)

    def _getEvents(self):
        return (
         (
          self.__hangarSpace.onSpaceChanged, self.__onSpaceChanged),)

    @staticmethod
    def __showHangar(event):
        showHangar()
        return

    def __onSpaceChanged(self):
        machine = self.getMachine()
        mainState = machine.getStateByCls(_MainState)
        mainState.proceedWithoutSave = True
        showHangar()
        return


class _CustomizationTransition(NavigationTransition):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)

    def execute(self, event):
        if super(_CustomizationTransition, self).execute(event):
            vehInvID = event.params.get(b'vehInvID')
            vehGuiItem = self.__itemsCache.items.getVehicle(vehInvID) if vehInvID is not None else None
            vehCustomizationEnabled = vehGuiItem.isCustomizationEnabled() if vehGuiItem else True
            return self.__lobbyContext.isHeaderNavigationPossible() and vehCustomizationEnabled
        else:
            return


@CustomizationState.parentOf
class _LoadingState(LobbyState, EventsHandler):
    STATE_ID = b'loading'
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_LoadingState, self).__init__(flags=flags)
        self.__params = {}
        return

    def _onEntered(self, event):
        super(_LoadingState, self)._onEntered(event)
        self.__params = dict(**event.params)
        Waiting.show(b'loadContent')
        vehInvID = event.params.get(b'vehInvID')
        shouldSelectVehicle = vehInvID is not None and (g_currentVehicle.invID != vehInvID or g_currentPreviewVehicle.isPresent())
        if not self.__hangarSpace.spaceInited or not self.__hangarSpace.isModelLoaded or shouldSelectVehicle:
            self._subscribe()
            if shouldSelectVehicle:
                if g_currentPreviewVehicle.isPresent():
                    g_currentPreviewVehicle.selectNoVehicle()
                BigWorld.callback(0.0, makeCallbackWeak(g_currentVehicle.selectVehicle, vehInvID=vehInvID))
        else:
            self.__goToMain()
        return

    def _onExited(self):
        super(_LoadingState, self)._onExited()
        self._unsubscribe()
        self.__params.clear()
        Waiting.hide(b'loadContent')
        return

    def _getEvents(self):
        return (
         (
          g_currentVehicle.onChanged, self.__onVehicleChanged),
         (
          g_currentPreviewVehicle.onChanged, self.__onVehicleChanged),
         (
          self.__hangarSpace.onSpaceChanged, self.__onSpaceChanged))

    def __onVehicleChanged(self):
        self.__goToMain()
        return

    def __onSpaceChanged(self):
        if self.__hangarSpace.spaceInited and self.__hangarSpace.isModelLoaded:
            self.__goToMain()
        return

    def __goToMain(self):
        BigWorld.callback(0.0, partial(_MainState.goTo, **self.__params))
        return


@CustomizationState.parentOf
class _MainState(SFViewLobbyState, EventsHandler):
    STATE_ID = b'main'
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOBBY_CUSTOMIZATION)
    __CAMERA_NAME = b'Customization'
    __GUN_PITCH_ANGLE = 0.0
    __TURRET_YAW_ANGLE = 0.0
    __RESTRICTED_EVENTS = [
     events.PrbInvitesEvent.ACCEPT,
     events.PrbActionEvent.SELECT,
     events.PrbActionEvent.LEAVE,
     events.TrainingEvent.RETURN_TO_TRAINING_ROOM]
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __c11n = dependency.descriptor(ICustomizationService)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_MainState, self).__init__(flags=flags)
        self.proceedWithoutSave = False
        return

    def registerTransitions(self):
        machine = self.getMachine()
        edit = machine.getStateByCls(_CustomizationEditState)
        confirm = machine.getStateByCls(_ConfirmLeaveState)
        self.addGuardTransition(confirm, WeakMethodProxy(self.mustConfirmExit))
        self.addNavigationTransition(edit)
        return

    def mustConfirmExit(self, event):
        ctx = self.__c11n.getCtx()
        if self.proceedWithoutSave or not ctx or ctx.applyingItems:
            return False
        return ctx.isOutfitsModified()

    def getNavigationDescription(self):
        return

    def getBackNavigationDescription(self, params):
        if self.getMachine().getStateByCls(_CustomizationMidState).isEntered():
            return None
        else:
            return backport.text(R.strings.pages.titles.customization())

    def _onEntered(self, event):
        super(_MainState, self)._onEntered(event)
        self.__hangarSpace.space.turretAndGunAngles.set(gunPitch=self.__GUN_PITCH_ANGLE, turretYaw=self.__TURRET_YAW_ANGLE)
        vEntity = self.__hangarSpace.space.getVehicleEntity()
        if vEntity is not None:
            vEntity.appearance.rotateTurretForAnchor(None, None)
            vEntity.appearance.rotateGunToDefault()
        ClientSelectableCameraObject.deselectAll()
        self.__hangarSpace.space.getVehicleEntity().onSelect(True)
        self.__setupTankTransformation()
        self.__c11n.onVisibilityChanged(True)
        self.__c11n.createCtx(**{k: event.params.get(k) for k in (b'season', b'modeId', b'tabId', b'itemCD')})
        self._subscribe()
        self.__lobbyContext.addPlatoonCreationConfirmator(self.__confirmatorWrapper)
        self.__lobbyContext.addHeaderNavigationConfirmator(self.__confirmatorWrapper)
        _CustomizationEditState.goTo()
        if event.params[b'callback']:
            event.params[b'callback']()
        return

    def _onExited(self):
        self._unsubscribe()
        self.__lobbyContext.deletePlatoonCreationConfirmator(self.__confirmatorWrapper)
        self.__lobbyContext.deleteHeaderNavigationConfirmator(self.__confirmatorWrapper)
        g_eventBus.handleEvent(events.HangarCustomizationEvent(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM), scope=EVENT_BUS_SCOPE.LOBBY)
        self.__c11n.onVisibilityChanged(False)
        super(_MainState, self)._onExited()
        return

    def _getRestrictions(self):
        return ((event, self.__handleRestrictedEvent, EVENT_BUS_SCOPE.LOBBY) for event in self.__RESTRICTED_EVENTS)

    def _onViewExternallyDestroyed(self):
        self.__cleanup()
        super(_MainState, self)._onViewExternallyDestroyed()
        return

    def __cleanup(self, _=None):
        if self.__c11n.getCtx():
            _logger.debug(b'Destroying c11n context')
            self.__c11n.saveLastWrittenDataFromCtx()
            self.__c11n.destroyCtx()
        return

    def __setupTankTransformation(self):
        from gui.ClientHangarSpace import customizationHangarCFG
        cfg = customizationHangarCFG()
        isForwardPipeline = BigWorld.getGraphicsSetting(b'RENDER_PIPELINE') == 1
        targetPos = cfg[b'v_start_pos']
        yaw = math.radians(cfg[b'v_start_angles'][0])
        pitch = math.radians(cfg[b'v_start_angles'][1])
        roll = math.radians(cfg[b'v_start_angles'][2])
        shadowYOffset = cfg[b'shadow_forward_y_offset'] if isForwardPipeline else cfg[b'shadow_deferred_y_offset']
        g_eventBus.handleEvent(events.HangarCustomizationEvent(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, ctx={b'targetPos': targetPos, 
           b'rotateYPR': (
                        yaw, pitch, roll), 
           b'shadowYOffset': shadowYOffset}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    @wg_async
    def __handleRestrictedEvent(self, event=None):
        if not self.mustConfirmExit(event):
            raise AsyncReturn(True)
        _ConfirmLeaveState.goTo()
        try:
            confirmState = self.getMachine().getStateByCls(_ConfirmLeaveState)
            self.proceedWithoutSave = yield confirmState.waitForResult()
            if self.proceedWithoutSave:
                self.goBack()
            else:
                confirmState.goBack()
        except BrokenPromiseError:
            self.proceedWithoutSave = False

        raise AsyncReturn(self.proceedWithoutSave)
        return

    @adisp.adisp_async
    @wg_async
    def __confirmatorWrapper(self, callback):
        result = yield wg_await(self.__handleRestrictedEvent())
        callback(result)
        return


@CustomizationState.parentOf
class _ExitState(LobbyState):
    STATE_ID = b'exit'

    def _onEntered(self, event):
        super(_ExitState, self)._onEntered(event)
        self.getParent().goBack()
        self.getMachine().post(event)
        return


class _ExitTransition(GuardTransition):

    def getPriority(self):
        return super(_ExitTransition, self).getPriority() - 1


@TopScopeTopLayerState.parentOf
class _CustomizationTopState(LobbyState):
    STATE_ID = b'customization'

    def registerStates(self):
        self.addChildState(_ConfirmLeaveState(StateFlags.INITIAL))
        return


@_CustomizationTopState.parentOf
class _ConfirmLeaveState(LobbyState):
    STATE_ID = b'confirmLeave'
    __c11n = dependency.descriptor(ICustomizationService)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_ConfirmLeaveState, self).__init__(flags)
        self.__dialog = None
        self.__waitFuture = None
        return

    def getNavigationDescription(self):
        return

    @wg_async
    def waitForResult(self):
        self.__waitFuture = self.__dialog.wait()
        result = yield self.__waitFuture
        raise AsyncReturn(result.result in dialogs.DialogButtons.ACCEPT_BUTTONS)
        return

    @wg_async
    def _onEntered(self, event):
        super(_ConfirmLeaveState, self)._onEntered(event)
        message = R.strings.dialogs.customization.close
        if UntrackedState.LOAD_PARAMS_KEY in event.params:
            loadParams = event.params[UntrackedState.LOAD_PARAMS_KEY].loadParams
            if loadParams.viewKey.alias == VIEW_ALIAS.LOBBY_STORE:
                message = R.strings.dialogs.customization.exitToShop
        builder = ResPureDialogBuilder()
        builder.setMessagesAndButtons(message, focused=DialogButtons.CANCEL)
        self.__dialog = builder.build()
        self.__dialog.load()
        self.__c11n.getCtx().events.onCloseDialogShown(ViewKeyDynamic(self.__dialog.decorator.layoutID))
        if event.targetStateID != self.getStateID():
            try:
                proceed = yield self.waitForResult()
                if proceed:
                    machine = self.getMachine()
                    mainState = machine.getStateByCls(_MainState)
                    mainState.proceedWithoutSave = True
                    mainState.goBack()
                    self.getMachine().post(event)
                else:
                    self.goBack()
            except BrokenPromiseError:
                _logger.debug(b'%s dialog closed without user decision.', self.__class__.__name__)

        return

    def _onExited(self):
        super(_ConfirmLeaveState, self)._onExited()
        self.__waitFuture.cancel()
        self.__waitFuture = None
        self.__dialog.destroy()
        self.__dialog = None
        ctx = self.__c11n.getCtx()
        if ctx:
            ctx.events.onCloseDialogClosed()
        return


@SubScopeTopLayerState.parentOf
class _CustomizationMidState(LobbyState):
    STATE_ID = b'customization'

    def registerStates(self):
        self.addChildState(_CustomizationEditState(StateFlags.INITIAL))
        self.addChildState(CustomizationCartState())
        self.addChildState(ProgressiveItemsState())
        return

    def registerTransitions(self):
        machine = self.getMachine()
        edit = machine.getStateByCls(_CustomizationEditState)
        cart = machine.getStateByCls(CustomizationCartState)
        progressiveItems = machine.getStateByCls(ProgressiveItemsState)
        exit = machine.getStateByCls(_ExitState)
        edit.addNavigationTransition(cart, record=True)
        edit.addNavigationTransition(progressiveItems, record=True)
        for state in self.getChildrenStates():
            state.addGuardTransition(machine.getStateByCls(_ConfirmLeaveState), WeakMethodProxy(self.mustConfirmExit))

        self.addTransition(_ExitTransition(WeakMethodProxy(self.__shouldRedirectToExit)), exit)
        return

    def mustConfirmExit(self, event):
        machine = self.getMachine()
        if isinstance(event, NavigationEvent):
            targetState = machine.getStateByID(event.targetStateID)
            if visitor.isDescendantOf(targetState, self):
                return False
        main = machine.getStateByCls(_MainState)
        return self.__shouldRedirectToExit(event) and main.mustConfirmExit(event)

    def _onEntered(self, event):
        super(_CustomizationMidState, self)._onEntered(event)
        machine = self.getMachine()
        machine.getStateByCls(_MainState).proceedWithoutSave = False
        return

    def __shouldRedirectToExit(self, event):
        machine = self.getMachine()
        target = machine.getStateByID(event.targetStateID)
        if target is machine.getEmptyStateInSubtreeOf(self):
            return False
        if target is machine.findOwningSubtree(self):
            return True
        return machine.findOwningSubtree(target) is not machine.findOwningSubtree(self)


@_CustomizationMidState.parentOf
class _CustomizationEditState(LobbyState):
    STATE_ID = b'edit'

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.customization()))


@_CustomizationMidState.parentOf
class CustomizationCartState(LobbyState):
    STATE_ID = b'cart'
    VIEW_KEY = ViewKey(R.views.lobby.customization.CustomizationCart())

    def _getViewLoadCtx(self, event):
        return {b'ctx': (event.params.get(b'ctx'))}

    def _onEntered(self, event):
        from gui.impl.lobby.customization.customization_cart.customization_cart_view import CustomizationCartView
        super(CustomizationCartState, self)._onEntered(event)
        uiLoader = dependency.instance(IGuiLoader)
        viewAlias = self.getViewKey().alias
        if uiLoader.windowsManager.getViewByLayoutID(viewAlias):
            return
        else:
            customizationView = event.params.get(b'ctx', {}).get(b'c11nView', None)
            parentWindow = None
            if customizationView:
                parentWindow = customizationView.getParentWindow()
            g_eventBus.handleEvent(LoadGuiImplViewEvent(GuiImplViewLoadParams(viewAlias, CustomizationCartView, ScopeTemplates.LOBBY_SUB_SCOPE, parent=parentWindow), **self._getViewLoadCtx(event)), scope=EVENT_BUS_SCOPE.LOBBY)
            return

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.customization.cart()))


@_CustomizationMidState.parentOf
class ProgressiveItemsState(GuiImplViewLobbyState):
    STATE_ID = b'progressiveItems'
    VIEW_KEY = ViewKey(R.views.lobby.customization.progressive_items_view.ProgressiveItemsView())

    def __init__(self, flags=StateFlags.UNDEFINED):
        from gui.impl.lobby.customization.progressive_items_view.progressive_items_view import ProgressiveItemsView
        super(ProgressiveItemsState, self).__init__(ProgressiveItemsView, ScopeTemplates.LOBBY_SUB_SCOPE, flags=flags)
        return

    @classmethod
    def goTo(cls, itemIntCD=None):
        super(ProgressiveItemsState, cls).goTo(itemIntCD=itemIntCD)
        return

    def _onExited(self):
        super(ProgressiveItemsState, self)._onExited()
        uiLoader = dependency.instance(IGuiLoader)
        windowsManager = uiLoader.windowsManager
        view = windowsManager.getViewByLayoutID(self.getViewKey().alias)
        if view:
            view.destroy()
        return

    @dependency.replace_none_kwargs(appLoader=IAppLoader)
    def _getViewLoadCtx(self, event, appLoader=None):
        c11nView = appLoader.getApp().containerManager.getViewByKey(_MainState.VIEW_KEY)
        return {b'c11nView': c11nView, 
           b'itemIntCD': (event.params.get(b'itemIntCD'))}

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.customization.progressive_items()))
