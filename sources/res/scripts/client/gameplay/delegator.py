import BigWorld
from frameworks_common.state_machine import StringEvent
from frameworks_common.state_machine import StateMachine
from frameworks_common.state_machine import BaseStateObserver
from frameworks_common.state_machine import OneshotStateIdsObserver
from gameplay import listeners
from gameplay.blockers import BlockingStateMixin
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager, DisconnectReason
from skeletons.gui.login_manager import ILoginManager
from skeletons.gameplay import IGameplayLogic, PlayerEventID

class GameplayLogic(IGameplayLogic):
    __slots__ = (b'__machine', b'__adaptor')
    connectionMgr = dependency.descriptor(IConnectionManager)
    loginMgr = dependency.descriptor(ILoginManager)

    def __init__(self, machine):
        super(GameplayLogic, self).__init__()
        self.__machine = machine
        self.__adaptor = listeners.PlayerEventsAdaptor(self.__machine)
        return

    def start(self):
        self.__adaptor.startListening()
        self.__machine.configure()
        self.__machine.start()
        return

    def stop(self):
        self.__adaptor.stopListening()
        self.__machine.stop()
        return

    def addStateObserver(self, observer):
        self.__machine.connect(observer)
        return

    def addOneshotObserver(self, gameplayStateIDs, observerLifetimeObj, enterFn=None, exitFn=None):
        self.__machine.connect(OneshotStateIdsObserver(gameplayStateIDs, self.__machine, observerLifetimeObj, enterFn, exitFn))
        return

    def removeStateObserver(self, observer):
        self.__machine.disconnect(observer)
        return

    def postStateEvent(self, eventID, **kwargs):
        self.__machine.post(StringEvent(eventID, **kwargs))
        return

    def tick(self):
        self.__machine.post(StringEvent(b''))
        return

    def addStateEnterBlocker(self, stateID, event):
        state = self.__machine.getStateByID(stateID)
        state.addEnterBlocker(event)
        return

    def addStateExitBlocker(self, stateID, event):
        state = self.__machine.getStateByID(stateID)
        state.addExitBlocker(event)
        return

    def goToLoginByRQ(self):
        self.connectionMgr.disconnect()
        self.postStateEvent(PlayerEventID.NON_PLAYER_BECOME_PLAYER, disconnectReason=DisconnectReason.REQUEST)
        return

    def goToLoginByDisconnectRQ(self):
        self.loginMgr.tryPrepareWGCLogin()
        self.goToLoginByRQ()
        return

    def goToLoginByEvent(self):
        self.postStateEvent(PlayerEventID.NON_PLAYER_BECOME_PLAYER, disconnectReason=DisconnectReason.EVENT)
        return

    def goToLoginByKick(self, reason, kickReasonType, expiryTime):
        self.postStateEvent(PlayerEventID.NON_PLAYER_BECOME_PLAYER, disconnectReason=DisconnectReason.KICK, kickReason=reason, kickReasonType=kickReasonType, expiryTime=expiryTime)
        return

    def goToLoginByError(self, reason):
        self.connectionMgr.disconnect()
        self.postStateEvent(PlayerEventID.NON_PLAYER_BECOME_PLAYER, disconnectReason=DisconnectReason.ERROR, kickReason=reason)
        return

    @staticmethod
    def quitFromGame():
        BigWorld.quit()
        return
