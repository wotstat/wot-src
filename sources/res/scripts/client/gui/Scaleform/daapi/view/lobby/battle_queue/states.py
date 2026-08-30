from __future__ import absolute_import
import logging
from functools import partial
import typing
from frameworks.state_machine import StateFlags
from gui import SystemMessages
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import SFViewLobbyState, SubScopeSubLayerState, LobbyState, LobbyStateDescription, LobbyStateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.prb_control import prbDispatcherProperty
from helpers.time_utils import getCurrentTimestamp
_logger = logging.getLogger(__name__)

def registerStates(machine):
    machine.addState(BattleQueueContainerState())
    return


def registerTransitions(_):
    return


@SubScopeSubLayerState.parentOf
class BattleQueueContainerState(LobbyState):
    STATE_ID = b'battleQueue'

    def registerStates(self):
        lsm = self.getMachine()
        lsm.addState(InitialQueueState(StateFlags.INITIAL))
        lsm.addState(CommonBattleQueueState())
        lsm.addState(StrongholdsBattleQueueState())
        return

    def registerTransitions(self):
        parent = self.getParent()
        for child in self.getChildrenStates():
            if isinstance(child, InitialQueueState):
                continue
            parent.addNavigationTransition(child)
            child.addGuardTransition(child, partial(self.__preventTransitionCheck, state=child))

        return

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def __preventTransitionCheck(self, event, state=None):
        from gui.impl.lobby.battle_results.states import PostBattleResultsEntryProto
        allowedStates = [
         PostBattleResultsEntryProto] + [type(s) for s in self.getChildrenStates()]
        if not state.isEntered():
            return False
        else:
            if self.prbDispatcher is None or not self.prbDispatcher.getFunctionalState().isNavigationDisabled():
                return False
            targetID = event.targetStateID
            lsm = state.getMachine()
            target = lsm.getStateByID(targetID)
            prevent = not any(isinstance(target, cls) for cls in allowedStates)
            if prevent:
                SystemMessages.pushI18nMessage(b'#system_messages:queue/isInQueue', type=SystemMessages.SM_TYPE.Error, priority=b'high')
            return prevent


@BattleQueueContainerState.parentOf
class InitialQueueState(LobbyState):
    STATE_ID = b'initial'

    def _onEntered(self, event):
        _logger.warning(b'%s state should never be entered. Enter specific battle queue states via .goTo method.', self.__class__.__name__)
        super(InitialQueueState, self)._onEntered(event)
        return


@BattleQueueContainerState.parentOf
class CommonBattleQueueState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.BATTLE_QUEUE
    VIEW_KEY = ViewKey(VIEW_ALIAS.BATTLE_QUEUE)

    def __init__(self, flags=LobbyStateFlags.UNDEFINED):
        super(CommonBattleQueueState, self).__init__(flags=flags)
        self.__createTime = None
        return

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.waiting.prebattle.battle_queue()))

    def serializeParams(self):
        return {b'createTime': (self.__createTime)}

    def _getViewLoadCtx(self, event):
        return {b'ctx': {b'createTime': (self.__createTime)}}

    def _onEntered(self, event):
        self.__createTime = event.params.get(b'createTime', getCurrentTimestamp())
        super(CommonBattleQueueState, self)._onEntered(event)
        return

    def _onExited(self):
        self.__createTime = None
        super(CommonBattleQueueState, self)._onExited()
        return


@BattleQueueContainerState.parentOf
class StrongholdsBattleQueueState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE
    VIEW_KEY = ViewKey(VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE)

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.waiting.prebattle.battle_queue()))
