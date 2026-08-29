import BattleReplay, BigWorld
from PlayerEvents import g_playerEvents
from adisp import adisp_process
from constants import ARENA_GUI_TYPE, ACCOUNT_KICK_REASONS
from gui import DialogsInterface
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.app_loader.settings import APP_NAME_SPACE
from gui.game_loading import loading as gameLoading
from gui.game_loading.state_machine.const import GameLoadingStates
from gui.impl.gen import R
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import LobbySimpleEvent, LoginEvent, ViewEventType, BCLoginEvent, CloseWindowEvent
from gui.shared.utils.decorators import ReprInjector
from helpers import dependency, isPlayerAvatar
from skeletons.connection_mgr import DisconnectReason, IConnectionManager
from skeletons.gameplay import IGameplayLogic
from skeletons.gui.app_loader import IGlobalSpace, GuiGlobalSpaceID as _SPACE_ID, ApplicationStateID
from skeletons.gui.game_control import IReloginController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.login_manager import ILoginManager
from skeletons.gui.shared.utils import IHangarSpace
_REASON = DisconnectReason

def _disableTimeWarpInReplay():
    BattleReplay.g_replayCtrl.disableTimeWarp()
    return


def _acceptVersionDiffering():
    BattleReplay.g_replayCtrl.acceptVersionDiffering()
    return


def _stopBattleReplay():
    BattleReplay.g_replayCtrl.stop()
    return


def _onReplayBattleLoadingFinished():
    BattleReplay.g_replayCtrl.onBattleLoadingFinished()
    return


class ShowDialogAction(object):
    __slots__ = ()

    def getAppNS(self):
        return APP_NAME_SPACE.SF_LOBBY

    def doAction(self):
        raise NotImplementedError
        return


class DisconnectDialogAction(ShowDialogAction):
    __slots__ = (b'__reason', b'__kickReasonType', b'__expiryTime')

    def __init__(self, reason, kickReasonType=ACCOUNT_KICK_REASONS.UNKNOWN, expiryTime=None):
        super(DisconnectDialogAction, self).__init__()
        self.__reason = reason
        self.__kickReasonType = kickReasonType
        self.__expiryTime = expiryTime
        return

    def doAction(self):
        DialogsInterface.showDisconnect(self.__reason, self.__kickReasonType, self.__expiryTime)
        return


class ReplayVersionDiffersDialogAction(ShowDialogAction):
    __slots__ = ()

    @adisp_process
    def doAction(self):
        result = yield DialogsInterface.showI18nConfirmDialog(b'replayNotification')
        if result:
            _acceptVersionDiffering()
        else:
            _stopBattleReplay()
        return


class ReplayFinishDialogAction(ShowDialogAction):

    def getAppNS(self):
        return APP_NAME_SPACE.SF_BATTLE

    @adisp_process
    def doAction(self):
        result = yield DialogsInterface.showI18nConfirmDialog(b'replayStopped')
        if result:
            BigWorld.callback(0.0, _stopBattleReplay)
        return


class CloseWaitingListenerMixin(object):

    def __init__(self, *args, **kwargs):
        super(CloseWaitingListenerMixin, self).__init__(*args, **kwargs)
        self.__callbackID = None
        return

    def init(self, *args, **kwargs):
        super(CloseWaitingListenerMixin, self).init(*args, **kwargs)
        for scope in (EVENT_BUS_SCOPE.LOBBY, EVENT_BUS_SCOPE.BATTLE):
            g_eventBus.addListener(LobbySimpleEvent.WAITING_HIDDEN, self.__waitingHiddenHandler, scope=scope)

        return

    def fini(self, *args, **kwargs):
        self._unsubscribe()
        super(CloseWaitingListenerMixin, self).fini(*args, **kwargs)
        return

    def _onWaitingHidden(self):
        return

    def _unsubscribe(self):
        self.__cancelCallback()
        for scope in (EVENT_BUS_SCOPE.LOBBY, EVENT_BUS_SCOPE.BATTLE):
            g_eventBus.removeListener(LobbySimpleEvent.WAITING_HIDDEN, self.__waitingHiddenHandler, scope=scope)

        return

    def __cancelCallback(self):
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        return

    def __waitingHiddenHandler(self, _):
        self.__cancelCallback()
        self.__callbackID = BigWorld.callback(0, self.__delayedWaitingHiddenHandler)
        return

    def __delayedWaitingHiddenHandler(self):
        self.__callbackID = None
        if not Waiting.isVisible():
            self._unsubscribe()
            self._onWaitingHidden()
        return


@ReprInjector.simple()
class LoginSpace(IGlobalSpace):
    __slots__ = (b'_action', b'_isPlayerLoadingActive')
    hangarSpace = dependency.descriptor(IHangarSpace)
    connectionMgr = dependency.descriptor(IConnectionManager)
    loginManager = dependency.descriptor(ILoginManager)
    reloginCtrl = dependency.descriptor(IReloginController)

    def __init__(self, action=None):
        super(LoginSpace, self).__init__()
        self._action = action
        self._isPlayerLoadingActive = False
        return

    def getSpaceID(self):
        return _SPACE_ID.LOGIN

    def init(self):
        self._clearEntitiesAndSpaces()
        BigWorld.notifySpaceChange(b'spaces/login_space')
        self.connectionMgr.onQueued += self._onLoginFailed
        self.connectionMgr.onConnected += self._onTryToLogin
        self.connectionMgr.onDisconnected += self._onDisconnected
        self.connectionMgr.onKickWhileLoginReceived += self._onLoginFailed
        self.loginManager.onConnectionInitiated += self._onTryToLogin
        self.loginManager.onConnectionRejected += self._onLoginFailed
        g_eventBus.addListener(LoginEvent.LOGIN_VIEW_READY, self._loginViewReadyHandler)
        g_eventBus.addListener(BCLoginEvent.HIDE_GAME_LOADING, self._bcQueueHideLoadingHandler, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(LoginEvent.CONNECTION_FAILED, self._onLoginFailed)
        g_eventBus.addListener(CloseWindowEvent.EULA_CLOSED, self._onEULAClosed)
        return

    def fini(self):
        self.connectionMgr.onQueued -= self._onLoginFailed
        self.connectionMgr.onConnected -= self._onTryToLogin
        self.connectionMgr.onDisconnected -= self._onDisconnected
        self.connectionMgr.onKickWhileLoginReceived -= self._onLoginFailed
        self.loginManager.onConnectionInitiated -= self._onTryToLogin
        self.loginManager.onConnectionRejected -= self._onLoginFailed
        g_eventBus.removeListener(LoginEvent.LOGIN_VIEW_READY, self._loginViewReadyHandler)
        g_eventBus.removeListener(BCLoginEvent.HIDE_GAME_LOADING, self._bcQueueHideLoadingHandler, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(LoginEvent.CONNECTION_FAILED, self._onLoginFailed)
        g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self._loadViewHandler, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(CloseWindowEvent.EULA_CLOSED, self._onEULAClosed)
        return

    @property
    def __isReconnectActive(self):
        from gui.prb_control.dispatcher import g_prbLoader
        invitesManager = g_prbLoader.getInvitesManager()
        return self.reloginCtrl.isActive or invitesManager.isAcceptChainActive

    def setup(self, action=None):
        self._action = action
        return

    def update(self):
        self._clearEntitiesAndSpaces()
        return

    def showGUI(self, appFactory, appNS, appState):
        if appState == ApplicationStateID.INITIALIZED:
            appFactory.attachCursor(appNS)
            appFactory.goToLogin(appNS)
            g_eventBus.addListener(ViewEventType.LOAD_VIEW, self._loadViewHandler, EVENT_BUS_SCOPE.LOBBY)
            self._doActionIfNeed(appNS)
        return

    def updateGUI(self, appFactory, appNS):
        self._doActionIfNeed(appNS)
        return

    def hideGUI(self, appFactory, newState):
        worker = appFactory.getWaitingWorker()
        if worker.isWaitingShown(messageID=R.strings.waiting.login()):
            worker.hide(R.strings.waiting.login())
        self._action = None
        return

    def _doActionIfNeed(self, appNS):
        if self._action is not None and self._action.getAppNS() == appNS:
            self._action.doAction()
        return

    def _onDisconnected(self, *_):
        if not self.__isReconnectActive:
            self._onLoginFailed()
        return

    def _onLoginFailed(self, *_):
        gameLoading.getLoader().loginScreen()
        self._isPlayerLoadingActive = False
        return

    def _onTryToLogin(self, *_):
        if not self._isPlayerLoadingActive:
            gameLoading.getLoader().playerLoading()
            self._isPlayerLoadingActive = True
        return

    def _onEULAClosed(self, event):
        if event.isAgree:
            gameLoading.getLoader().playerLoading(True)
            self._isPlayerLoadingActive = True
        return

    def _loginViewReadyHandler(self, *_):
        if not self._isPlayerLoadingActive and not self.__isReconnectActive:
            gameLoading.getLoader().loginScreen()
        return

    def _bcQueueHideLoadingHandler(self, *_):
        gameLoading.getLoader().loginScreen()
        return

    def _loadViewHandler(self, event):
        self._isPlayerLoadingActive = False
        alias = event.alias
        if alias == VIEW_ALIAS.BOOTCAMP_INTRO:
            gameLoading.getLoader().idl()
        elif alias == VIEW_ALIAS.BOOTCAMP_QUEUE_DIALOG_SHOW:
            pass
        elif alias == VIEW_ALIAS.BOOTCAMP_QUEUE_DIALOG_CLOSE:
            pass
        else:
            gameLoading.getLoader().loginScreen()
        return

    @classmethod
    def _clearEntitiesAndSpaces(cls):
        keepClientOnlySpaces = False
        if cls.hangarSpace is not None and cls.hangarSpace.inited:
            keepClientOnlySpaces = cls.hangarSpace.spaceLoading()
        BigWorld.clearEntitiesAndSpaces(keepClientOnlySpaces)
        return


@ReprInjector.simple()
class WaitingSpace(IGlobalSpace):
    __slots__ = ()

    def getSpaceID(self):
        return _SPACE_ID.WAITING


@ReprInjector.simple()
class LobbySpace(CloseWaitingListenerMixin, IGlobalSpace):
    __slots__ = ()
    gameplay = dependency.descriptor(IGameplayLogic)

    def init(self, *args, **kwargs):
        super(LobbySpace, self).init(*args, **kwargs)
        g_eventBus.addListener(LoginEvent.DISCONNECTION_STARTED, self._disconnectStartHandler)
        return

    def fini(self, *args, **kwargs):
        g_eventBus.removeListener(LoginEvent.DISCONNECTION_STARTED, self._disconnectStartHandler)
        super(LobbySpace, self).fini(*args, **kwargs)
        return

    def getSpaceID(self):
        return _SPACE_ID.LOBBY

    def showGUI(self, appFactory, appNS, appState):
        if appState == ApplicationStateID.INITIALIZED:
            appFactory.attachCursor(appNS)
            appFactory.goToLobby(appNS)
            if gameLoading.getLoader().isStateEntered(GameLoadingStates.LOGIN_SCREEN.value):
                gameLoading.getLoader().idl()
        return

    def hideGUI(self, appFactory, newState):
        appFactory.detachCursor(APP_NAME_SPACE.SF_LOBBY)
        return

    def _onWaitingHidden(self):
        gameLoading.getLoader().idl()
        return

    @staticmethod
    def _disconnectStartHandler(*_):
        gameLoading.getLoader().playerLoading()
        return


class _ArenaSpace(IGlobalSpace):
    __slots__ = (b'_arenaGuiType',)

    def __init__(self, arenaGuiType=ARENA_GUI_TYPE.UNKNOWN):
        super(_ArenaSpace, self).__init__()
        self._arenaGuiType = arenaGuiType
        return


@ReprInjector.simple()
class BattleLoadingSpace(CloseWaitingListenerMixin, _ArenaSpace):
    __slots__ = ()

    def __init__(self, arenaGuiType=ARENA_GUI_TYPE.UNKNOWN):
        super(BattleLoadingSpace, self).__init__(arenaGuiType=arenaGuiType)
        return

    def getSpaceID(self):
        return _SPACE_ID.BATTLE_LOADING

    def hideGUI(self, appFactory, newState):
        if newState.getSpaceID() == _SPACE_ID.BATTLE:
            _onReplayBattleLoadingFinished()
        else:
            appFactory.hideBattle()
            appFactory.reloadLobbyPackages()
            appFactory.destroyBattle()
            appFactory.createLobby()
            appFactory.showLobby()
        return

    def showGUI(self, appFactory, appNS, appState):
        isValidAvatar = isPlayerAvatar() and not g_playerEvents.isPlayerEntityChanging
        if appState == ApplicationStateID.INITIALIZED and isValidAvatar:
            appFactory.loadBattlePage(appNS, arenaGuiType=self._arenaGuiType)
        return

    def updateGUI(self, appFactory, appNS):
        if appNS != APP_NAME_SPACE.SF_BATTLE:
            return
        appFactory.showBattle()
        appFactory.goToBattleLoading(appNS)
        if BattleReplay.g_replayCtrl.getAutoStartFileName():
            gameLoading.getLoader().idl()
        return

    def _onWaitingHidden(self):
        lobbyContext = dependency.instance(ILobbyContext)
        if lobbyContext.getGuiCtx().get(b'skipShowGUI', False):
            return
        if not BattleReplay.g_replayCtrl.getAutoStartFileName():
            gameLoading.getLoader().idl()
        return


@ReprInjector.simple()
class ReplayLoadingSpace(BattleLoadingSpace):
    __slots__ = ()

    def showGUI(self, appFactory, appNS, appState):
        if appState == ApplicationStateID.INITIALIZED:
            appFactory.destroyLobby()
            appFactory.showBattle()
            appFactory.loadBattlePage(appNS, self._arenaGuiType)
            appFactory.goToBattleLoading(appNS)
        return

    def hideGUI(self, appFactory, newState):
        _onReplayBattleLoadingFinished()
        return


@ReprInjector.simple()
class BattleSpace(_ArenaSpace):
    __slots__ = ()

    def getSpaceID(self):
        return _SPACE_ID.BATTLE

    def showGUI(self, appFactory, appNS, appState):
        if appState == ApplicationStateID.INITIALIZED:
            appFactory.goToBattlePage(appNS)
        return


@ReprInjector.simple()
class ReplayBattleSpace(BattleSpace):
    __slots__ = ()

    def hideGUI(self, appFactory, newState):
        _disableTimeWarpInReplay()
        return
