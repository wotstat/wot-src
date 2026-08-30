import typing
from Event import Event
from constants import ARENA_GUI_TYPE

class GuiGlobalSpaceID(object):
    UNDEFINED = 0
    WAITING = 1
    LOGIN = 2
    LOBBY = 3
    BATTLE_LOADING = 4
    BATTLE = 5


class ApplicationStateID(object):
    NOT_CREATED = 0
    INITIALIZING = 1
    INITIALIZED = 2


class IGlobalSpace(object):
    __slots__ = ()

    def getSpaceID(self):
        return GuiGlobalSpaceID.UNDEFINED

    def init(self):
        return

    def update(self):
        return

    def fini(self):
        return

    def setup(self, *args, **kwargs):
        return

    def showGUI(self, appFactory, appNS, appState):
        return

    def updateGUI(self, appFactory, appNS):
        return

    def hideGUI(self, appFactory, newState):
        return


class IWaitingWidget(object):

    def showWaiting(self, messageID, softStart=False):
        return

    def hideWaiting(self):
        return

    def setCallback(self, callback=None):
        return

    def cancelCallback(self):
        return

    def setBackgroundImage(self, image, showSparks):
        return


class IWaitingWorker(object):
    __slots__ = ()

    def getWaitingView(self, isBlocking):
        raise NotImplementedError
        return

    def isWaitingShown(self, messageID=None):
        raise NotImplementedError
        return

    def getWaitingTask(self, messageID):
        raise NotImplementedError
        return

    def getSuspendedWaitingTask(self, messageID):
        raise NotImplementedError
        return

    def show(self, messageID, isSingle=False, interruptCallback=None, isBlocking=True, isAlwaysOnTop=False, backgroundImage=None, softStart=False, showSparks=True):
        raise NotImplementedError
        return

    def hide(self, messageID):
        raise NotImplementedError
        return

    def suspend(self, lockerID=None):
        raise NotImplementedError
        return

    def isResumeLocked(self):
        raise NotImplementedError
        return

    def resume(self, lockerID=None, hard=False):
        raise NotImplementedError
        return

    def isSuspended(self):
        raise NotImplementedError
        return

    def close(self):
        raise NotImplementedError
        return

    def rollback(self):
        raise NotImplementedError
        return

    def cancelCallback(self):
        raise NotImplementedError
        return

    def snapshort(self):
        return {}


class IAppFactory(object):
    __slots__ = ()

    def hasApp(self, appNS):
        return False

    def getApp(self, appNS=None):
        return

    def getDefLobbyApp(self):
        return

    def getDefBattleApp(self):
        return

    def getWaitingWorker(self):
        return

    def createLobby(self):
        return

    def reloadLobbyPackages(self):
        return

    def destroyLobby(self):
        return

    def showLobby(self):
        return

    def hideLobby(self):
        return

    def showBattle(self):
        return

    def hideBattle(self):
        return

    def createBattle(self, arenaGuiType):
        return

    def destroyBattle(self):
        return

    def destroy(self):
        return

    def attachCursor(self, appNS, flags=0):
        return

    def detachCursor(self, appNS):
        return

    def syncCursor(self, appNS, flags=0):
        return

    def goToLogin(self, appNS):
        return

    def goToLobby(self, appNS):
        return

    def loadBattlePage(self, appNS, arenaGuiType=ARENA_GUI_TYPE.UNKNOWN):
        return

    def goToBattleLoading(self, appNS):
        return

    def goToBattlePage(self, appNS):
        return

    def handleKey(self, appNS, isDown, key, mods):
        return False


class IAppLoader(object):
    onGUISpaceLeft = None
    onGUISpaceBeforeEnter = None
    onGUISpaceEntered = None
    onGUIInitialized = None

    def init(self, appFactory):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def getSpaceID(self):
        raise NotImplementedError
        return

    def getAppStateID(self, appNS):
        raise NotImplementedError
        return

    def getApp(self, appNS=None):
        raise NotImplementedError
        return

    def getDefLobbyApp(self):
        raise NotImplementedError
        return

    def getDefBattleApp(self):
        raise NotImplementedError
        return

    def getWaitingWorker(self):
        raise NotImplementedError
        return

    def changeSpace(self, space):
        raise NotImplementedError
        return

    def createLobby(self):
        raise NotImplementedError
        return

    def destroyLobby(self):
        raise NotImplementedError
        return

    def showLobby(self):
        raise NotImplementedError
        return

    def switchAccountEntity(self):
        raise NotImplementedError
        return

    def createBattle(self, arenaGuiType=ARENA_GUI_TYPE.UNKNOWN):
        raise NotImplementedError
        return

    def destroyBattle(self):
        raise NotImplementedError
        return

    def attachCursor(self, appNS, flags=0):
        raise NotImplementedError
        return

    def detachCursor(self, appNS):
        raise NotImplementedError
        return

    def syncCursor(self, appNS, flags=0):
        raise NotImplementedError
        return

    def handleKey(self, appNS, isDown, key, mods):
        raise NotImplementedError
        return
