from __future__ import absolute_import
import logging, typing, adisp
from BWUtil import AsyncReturn
from WeakMethod import WeakMethodProxy
from frameworks_common.state_machine import StateFlags
from frameworks_common.state_machine.transitions import TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.game_control.loadout_controller import updateInteractor
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.hangar.easy_tank_equip_state import generateEasyTankEquipStates, EasyTankEquipStatePrototype
from gui.impl.lobby.hangar.random.sound_manager import ALL_VEHICLES_SOUND_SPACE
from gui.impl.lobby.tank_setup.tank_setup_sounds import playEnterTankSetupView, playExitTankSetupView
from gui.lobby_state_machine.states import SFViewLobbyState, LobbyState, LobbyStateDescription, TopScopeTopLayerState, SubScopeSubLayerState, LobbyStateFlags
from gui.shared import events, EVENT_BUS_SCOPE
from helpers import dependency
from helpers.events_handler import EventsHandler
from skeletons.gui.game_control import ILoadoutController
from skeletons.gui.lobby_context import ILobbyContext
from sound_gui_manager import ViewSoundExtension
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
from gui.lobby_state_machine.transitions import ConditionalTransition
from wg_async import await_callback, wg_async, BrokenPromiseError, wg_await
if typing.TYPE_CHECKING:
    from gui.shared.events import NavigationEvent
_logger = logging.getLogger(__name__)

class _HangarStatePrototype(SFViewLobbyState):
    VIEW_KEY = ViewKey(VIEW_ALIAS.LOBBY_HANGAR)


class _DefaultHangarStatePrototype(LobbyState):

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.hangar()))

    def _onEntered(self, event):
        super(_DefaultHangarStatePrototype, self)._onEntered(event)
        lsm = self.getMachine()
        lsm.getRelatedView(self).blur.disable()
        return


class _AllVehiclesStatePrototype(LobbyState):
    __soundExtension = ViewSoundExtension(ALL_VEHICLES_SOUND_SPACE)

    def _onEntered(self, event):
        super(_AllVehiclesStatePrototype, self)._onEntered(event)
        self.__soundExtension.initSoundManager()
        self.__soundExtension.startSoundSpace()
        lsm = self.getMachine()
        lsm.getRelatedView(self).blur.enable()
        return

    def _onExited(self):
        self.__soundExtension.destroySoundManager()
        super(_AllVehiclesStatePrototype, self)._onExited()
        return

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.allVehicles()))


class _LoadoutStatePrototype(LobbyState):
    __loadoutController = dependency.descriptor(ILoadoutController)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.loadout()))

    def _onEntered(self, event):
        super(_LoadoutStatePrototype, self)._onEntered(event)
        playEnterTankSetupView()
        lsm = self.getMachine()
        lsm.getRelatedView(self).blur.enable()
        return

    @wg_async
    def _onExited(self):
        yield await_callback(self.__loadoutController.interactor.applyQuit)(skipApplyAutoRenewal=False)
        playExitTankSetupView()
        super(_LoadoutStatePrototype, self)._onExited()
        return


class _LoadoutConfirmStatePrototype(LobbyState):
    __loadoutController = dependency.descriptor(ILoadoutController)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_LoadoutConfirmStatePrototype, self).__init__(flags)
        self.__dialog = None
        return

    def getNavigationDescription(self):
        return

    @wg_async
    def waitForResult(self):
        result = yield self.__dialog()
        raise AsyncReturn(result.result)
        return

    @wg_async
    def _onEntered(self, event):
        super(_LoadoutConfirmStatePrototype, self)._onEntered(event)
        interactor = self.__loadoutController.interactor
        if event.params.get(b'forcedRollback', False):
            yield updateInteractor(interactor, False, True)
            self.__forwardEvent(event)
            return
        self.__dialog = interactor.showExitConfirmDialog
        if self.__dialog and event.targetStateID != self.getStateID():
            try:
                result = yield self.__dialog()
                if not result.result:
                    TopScopeTopLayerState.goTo()
                    return
                confirmed, data = result.result
                rollback = data.get(b'rollBack', False)
                proceed = confirmed or rollback
                yield updateInteractor(interactor, confirmed, rollback)
                if proceed:
                    self.__forwardEvent(event)
                else:
                    TopScopeTopLayerState.goTo()
            except BrokenPromiseError:
                _logger.debug(b'%r dialog closed without user decision.', self.__class__.__name__)

        return

    def _onExited(self):
        super(_LoadoutConfirmStatePrototype, self)._onExited()
        self.__dialog = None
        return

    def __forwardEvent(self, event):
        self.getMachine().post(event)
        return


class _LoadoutSectionStatePrototype(LobbyState, EventsHandler):
    __loadoutController = dependency.descriptor(ILoadoutController)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __RESTRICTED_EVENTS = [
     events.PrbInvitesEvent.ACCEPT,
     events.PrbActionEvent.SELECT,
     events.PrbActionEvent.LEAVE]

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(_LoadoutSectionStatePrototype, self).__init__(flags=flags)
        self.__cachedParams = {}
        return

    def serializeParams(self):
        return self.__cachedParams

    def _getRestrictions(self):
        return ((event, self.__handleRestrictedEvent, EVENT_BUS_SCOPE.LOBBY) for event in self.__RESTRICTED_EVENTS)

    def _interactorConfirm(self, event):
        interactor = self.__loadoutController.interactor
        if interactor is None:
            return False
        else:
            interactorHasChanged = self.__loadoutController.interactor.hasChanged()
            if event is None:
                return interactorHasChanged
            targetingSelf = event.targetStateID == self.getStateID()
            return not targetingSelf and interactorHasChanged

    def _getConfirmationState(self):
        return self.getMachine().getStateByID(self.STATE_ID)

    def _onEntered(self, event):
        self.__cachedParams = event.params
        super(_LoadoutSectionStatePrototype, self)._onEntered(event)
        self.__lobbyContext.addPlatoonCreationConfirmator(self.__confirmatorWrapper)
        self.__lobbyContext.addHeaderNavigationConfirmator(self.__confirmatorWrapper)
        return

    def _onExited(self):
        self.__cachedParams = {}
        super(_LoadoutSectionStatePrototype, self)._onExited()
        self.__lobbyContext.deletePlatoonCreationConfirmator(self.__confirmatorWrapper)
        self.__lobbyContext.deleteHeaderNavigationConfirmator(self.__confirmatorWrapper)
        return

    @wg_async
    def __handleRestrictedEvent(self, event=None):
        interactor = self.__loadoutController.interactor
        if not self._interactorConfirm(event):
            SubScopeSubLayerState.goTo()
            raise AsyncReturn(True)
        state = self._getConfirmationState()
        state.goTo()
        try:
            confirmed, data = yield state.waitForResult()
            rollback = data.get(b'rollBack', False)
            self.proceed = confirmed or rollback
            yield updateInteractor(interactor, confirmed, rollback)
            if self.proceed:
                SubScopeSubLayerState.goTo()
            else:
                TopScopeTopLayerState.goTo()
        except BrokenPromiseError:
            self.proceed = False

        raise AsyncReturn(self.proceed)
        return

    @adisp.adisp_async
    @wg_async
    def __confirmatorWrapper(self, callback):
        result = yield wg_await(self.__handleRestrictedEvent())
        callback(result)
        return


class _ShellsLoadoutStatePrototype(LobbyState):

    def isStateReachable(self, event):
        return True

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.loadout.shells()))


class _EquipmentLoadoutStatePrototype(LobbyState):

    def isStateReachable(self, event):
        return True

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.loadout.equipment()))


class _InstructionsLoadoutStatePrototype(LobbyState):

    def isStateReachable(self, event):
        return True

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.loadout.instructions()))


class _ConsumablesLoadoutStatePrototype(LobbyState):

    def isStateReachable(self, event):
        return True

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.pages.titles.loadout.consumables()))


def generateBasicLoadoutStateClasses(parentHangarStateCls, loadoutResource, loadoutStatePrototypeCls=_LoadoutStatePrototype, confirmStatePrototypeCls=_LoadoutConfirmStatePrototype, sectionStatePrototypeCls=_LoadoutSectionStatePrototype, shellsStatePrototypeCls=_ShellsLoadoutStatePrototype, equipmentStatePrototypeCls=_EquipmentLoadoutStatePrototype, instructionsStatePrototypeCls=_InstructionsLoadoutStatePrototype, consumablesStatePrototypeCls=_ConsumablesLoadoutStatePrototype):

    @parentHangarStateCls.parentOf
    class GeneratedLoadoutState(loadoutStatePrototypeCls):
        STATE_ID = loadoutStatePrototypeCls.STATE_ID or b'loadout'

        def registerStates(self):
            lsm = self.getMachine()
            lsm.addState(GeneratedShellsLoadoutState(flags=StateFlags.INITIAL))
            lsm.addState(GeneratedEquipmentLoadoutState())
            lsm.addState(GeneratedInstructionsLoadoutState())
            lsm.addState(GeneratedConsumablesLoadoutState())
            lsm.addState(GeneratedLoadoutConfirmState())
            super(GeneratedLoadoutState, self).registerStates()
            return

        def registerTransitions(self):
            lsm = self.getMachine()
            lsm.addNavigationTransitionFromParent(self)
            generatedClasses = (
             lsm.getStateByCls(GeneratedShellsLoadoutState),
             lsm.getStateByCls(GeneratedEquipmentLoadoutState),
             lsm.getStateByCls(GeneratedInstructionsLoadoutState),
             lsm.getStateByCls(GeneratedConsumablesLoadoutState))
            parent = self.getParent()
            for state in generatedClasses:
                parent.addTransition(ConditionalTransition(WeakMethodProxy(state.isStateReachable)), state)
                self.addTransition(ConditionalTransition(WeakMethodProxy(state.isStateReachable)), state)
                state.addTransition(ConditionalTransition(WeakMethodProxy(state.isStateReachable), transitionType=TransitionType.EXTERNAL), state)

            super(GeneratedLoadoutState, self).registerTransitions()
            return

    @TopScopeTopLayerState.parentOf
    class confirmStatePrototypeCls(confirmStatePrototypeCls):
        STATE_ID = confirmStatePrototypeCls.STATE_ID or b'loadoutConfirmLeave'

    class GeneratedLoadoutSectionState(sectionStatePrototypeCls):

        def registerTransitions(self):
            self.addGuardTransition(self._getConfirmationState(), WeakMethodProxy(self._interactorConfirm))
            return

        def _getConfirmationState(self):
            lsm = self.getMachine()
            return lsm.getStateByCls(GeneratedLoadoutConfirmState)

    @GeneratedLoadoutState.parentOf
    class shellsStatePrototypeCls(GeneratedLoadoutSectionState, shellsStatePrototypeCls):
        STATE_ID = shellsStatePrototypeCls.STATE_ID or b'shells'

    @GeneratedLoadoutState.parentOf
    class equipmentStatePrototypeCls(GeneratedLoadoutSectionState, equipmentStatePrototypeCls):
        STATE_ID = equipmentStatePrototypeCls.STATE_ID or b'equipment'

    @GeneratedLoadoutState.parentOf
    class instructionsStatePrototypeCls(GeneratedLoadoutSectionState, instructionsStatePrototypeCls):
        STATE_ID = instructionsStatePrototypeCls.STATE_ID or b'instructions'

    @GeneratedLoadoutState.parentOf
    class consumablesStatePrototypeCls(GeneratedLoadoutSectionState, consumablesStatePrototypeCls):
        STATE_ID = consumablesStatePrototypeCls.STATE_ID or b'consumables'

    return (
     GeneratedLoadoutState,
     GeneratedLoadoutConfirmState,
     GeneratedLoadoutSectionState,
     GeneratedShellsLoadoutState,
     GeneratedEquipmentLoadoutState,
     GeneratedInstructionsLoadoutState,
     GeneratedConsumablesLoadoutState)


def generateBasicHangarStateClasses(parentStateCls, hangarResource, hangarPrototypeCls=_HangarStatePrototype, defaultHangarPrototypeCls=_DefaultHangarStatePrototype, allVehiclesPrototypeCls=_AllVehiclesStatePrototype, easyTankEquipPrototypeCls=EasyTankEquipStatePrototype):

    @parentStateCls.parentOf
    class GeneratedHangarState(hangarPrototypeCls):
        STATE_ID = hangarPrototypeCls.STATE_ID or b'hangar'

        def __init__(self, flags=StateFlags.UNDEFINED):
            super(GeneratedHangarState, self).__init__(flags=flags | LobbyStateFlags.HANGAR)
            return

        def registerStates(self):
            lsm = self.getMachine()
            lsm.addState(GeneratedDefaultHangarState(flags=StateFlags.INITIAL))
            lsm.addState(GeneratedAllVehiclesState())
            lsm.addState(_generatedEasyTankEquipStateCls())
            super(GeneratedHangarState, self).registerStates()
            return

        def registerTransitions(self):
            lsm = self.getMachine()
            lsm.addNavigationTransitionFromParent(lsm.getStateByCls(GeneratedDefaultHangarState))
            lsm.addNavigationTransitionFromParent(lsm.getStateByCls(GeneratedAllVehiclesState))
            lsm.addNavigationTransitionFromParent(lsm.getStateByCls(_generatedEasyTankEquipStateCls))
            super(GeneratedHangarState, self).registerTransitions()
            return

    @GeneratedHangarState.parentOf
    class GeneratedDefaultHangarState(defaultHangarPrototypeCls):
        STATE_ID = defaultHangarPrototypeCls.STATE_ID or b'{root}'

        def __init__(self, flags=StateFlags.UNDEFINED):
            super(GeneratedDefaultHangarState, self).__init__(flags=flags | LobbyStateFlags.HANGAR)
            return

    @GeneratedHangarState.parentOf
    class allVehiclesPrototypeCls(allVehiclesPrototypeCls):
        STATE_ID = allVehiclesPrototypeCls.STATE_ID or b'allVehicles'

    _generatedEasyTankEquipStateCls, = generateEasyTankEquipStates(GeneratedHangarState, easyTankEquipPrototypeCls)
    return (
     GeneratedHangarState,
     GeneratedDefaultHangarState,
     GeneratedAllVehiclesState,
     _generatedEasyTankEquipStateCls)
