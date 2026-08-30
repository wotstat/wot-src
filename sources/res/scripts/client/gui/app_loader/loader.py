import logging, typing, Event
from constants import ARENA_GUI_TYPE
from gui import GUI_CTRL_MODE_FLAG as _CTRL_FLAG
from gui.app_loader.observers import GameplayStatesObserver
from gui.shared import g_eventBus, events
from gui.app_loader import spaces
from skeletons.gui.app_loader import IAppLoader, IAppFactory, ApplicationStateID
from skeletons.gui.app_loader import IWaitingWorker, IGlobalSpace
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

class _EmptyWaitingWorker(IWaitingWorker):
    __slots__ = ()

    def getWaitingView(self, isBlocking):
        _logger.error(b'Waiting widget is not defined')
        return

    def isWaitingShown(self, messageID=None):
        return False

    def getWaitingTask(self, messageID):
        _logger.error(b'Waiting task is not defined')
        return

    def getSuspendedWaitingTask(self, messageID):
        _logger.error(b'Waiting suspended task is not defined')
        return

    def show(self, messageID, isSingle=False, interruptCallback=None, isBlocking=True, isAlwaysOnTop=False, backgroundImage=None, softStart=False, showBg=True):
        _logger.error(b'Waiting is not found. Method "show" is ignored: %r', messageID)
        return

    def hide(self, messageID):
        _logger.error(b'Waiting is not found. Method "hide" is ignored: %r', messageID)
        return

    def suspend(self, lockerID=None):
        _logger.error(b'Waiting is not found. Method "suspend" is ignored')
        return

    def isResumeLocked(self):
        return False

    def resume(self, lockerID=None, hard=False):
        _logger.error(b'Waiting is not found. Method "resumed" is ignored')
        return

    def isSuspended(self):
        return False

    def close(self):
        _logger.error(b'Waiting is not found. Method "close" is ignored')
        return

    def rollback(self):
        _logger.error(b'Waiting is not found. Method "rollback" is ignored')
        return

    def cancelCallback(self):
        _logger.error(b'Waiting is not found. Method "cancelCallback" is ignored')
        return


class _EmptyFactory(IAppFactory):
    __slots__ = ()

    def getWaitingWorker(self):
        return _EmptyWaitingWorker()


class AppLoader(IAppLoader):

    def __init__(self):
        super(AppLoader, self).__init__()
        self.__space = spaces.WaitingSpace()
        self.__appsStates = {}
        self.__appFactory = _EmptyFactory()
        self.__observer = GameplayStatesObserver(self)
        self.onGUISpaceLeft = Event.Event()
        self.onGUISpaceBeforeEnter = Event.Event()
        self.onGUISpaceEntered = Event.Event()
        self.onGUIInitialized = Event.Event()
        return

    def init(self, appFactory):
        self.__appFactory = appFactory
        self.__observer.init()
        add = g_eventBus.addListener
        appEvent = events.AppLifeCycleEvent
        add(appEvent.INITIALIZING, self.__onAppInitializing)
        add(appEvent.INITIALIZED, self.__onAppInitialized)
        add(appEvent.DESTROYED, self.__onAppDestroyed)
        return

    def fini(self):
        if self.__appFactory:
            self.__appFactory.destroy()
            self.__appFactory = None
        self.__observer.clear()
        remove = g_eventBus.removeListener
        appEvent = events.AppLifeCycleEvent
        remove(appEvent.INITIALIZING, self.__onAppInitializing)
        remove(appEvent.INITIALIZED, self.__onAppInitialized)
        remove(appEvent.DESTROYED, self.__onAppDestroyed)
        return

    def getSpaceID(self):
        return self.__space.getSpaceID()

    def getAppStateID(self, appNS):
        return self.__appsStates.get(appNS, ApplicationStateID.NOT_CREATED)

    def getApp(self, appNS=None):
        app = None
        if self.__appFactory:
            app = self.__appFactory.getApp(appNS=appNS)
        return app

    def getDefLobbyApp(self):
        app = None
        if self.__appFactory:
            app = self.__appFactory.getDefLobbyApp()
        return app

    def getDefBattleApp(self):
        app = None
        if self.__appFactory:
            app = self.__appFactory.getDefBattleApp()
        return app

    def getWaitingWorker(self):
        return self.__appFactory.getWaitingWorker()

    def changeSpace(self, space):
        return self.__updateSpace(space)

    def setupSpace(self, *args, **kwargs):
        self.__space.setup(*args, **kwargs)
        return

    def createLobby(self):
        self.__appFactory.createLobby()
        return

    def destroyLobby(self):
        self.changeSpace(spaces.WaitingSpace())
        self.__appFactory.destroyLobby()
        return

    def showLobby(self):
        return self.changeSpace(spaces.LobbySpace())

    def switchAccountEntity(self):
        self.changeSpace(spaces.WaitingSpace())
        self.__appFactory.destroyLobby()
        self.__appFactory.createLobby()
        return

    def createBattle(self, arenaGuiType=ARENA_GUI_TYPE.UNKNOWN):
        self.__appFactory.createBattle(arenaGuiType)
        return

    def destroyBattle(self):
        self.changeSpace(spaces.WaitingSpace())
        self.__appFactory.destroyBattle()
        return

    def attachCursor(self, appNS, flags=_CTRL_FLAG.CURSOR_VISIBLE):
        self.__appFactory.attachCursor(appNS, flags=flags)
        return

    def detachCursor(self, appNS):
        self.__appFactory.detachCursor(appNS)
        return

    def syncCursor(self, appNS, flags=_CTRL_FLAG.CURSOR_VISIBLE):
        self.__appFactory.syncCursor(appNS, flags=flags)
        return

    def handleKey(self, appNS, isDown, key, mods):
        return self.__appFactory.handleKey(appNS, isDown, key, mods)

    def __updateSpace(self, newSpace):
        result = False
        if newSpace.getSpaceID() != self.__space.getSpaceID():
            _logger.info(b'Space is changed: %r -> %r', self.__space, newSpace)
            self.onGUISpaceLeft(self.__space.getSpaceID())
            self.__space.fini()
            self.__space.hideGUI(self.__appFactory, newSpace)
            self.__space = newSpace
            self.__space.init()
            self.onGUISpaceBeforeEnter(self.__space.getSpaceID())
            for appNS, appState in self.__getCreatedApps():
                self.__space.showGUI(self.__appFactory, appNS, appState)

            result = True
            self.onGUISpaceEntered(self.__space.getSpaceID())
        else:
            _logger.info(b'Space is updated: %s', self.__space)
            for appNS, appState in self.__getCreatedApps():
                self.__space.update()
                self.__space.updateGUI(self.__appFactory, appNS)

        return result

    def __getCreatedApps(self):
        for appNS, appState in self.__appsStates.iteritems():
            if appState != ApplicationStateID.NOT_CREATED:
                yield (
                 appNS, appState)

        return

    def __onAppInitializing(self, event):
        appNS = event.ns
        if self.__appFactory.hasApp(appNS):
            _logger.info(b'App is initializing: %s', appNS)
            self.__appsStates[appNS] = ApplicationStateID.INITIALIZING
            self.__space.showGUI(self.__appFactory, appNS, ApplicationStateID.INITIALIZING)
        return

    def __onAppInitialized(self, event):
        appNS = event.ns
        if self.__appFactory.hasApp(appNS):
            _logger.info(b'App is initialized: %s', appNS)
            self.__appsStates[appNS] = ApplicationStateID.INITIALIZED
            self.__space.showGUI(self.__appFactory, appNS, ApplicationStateID.INITIALIZED)
            self.onGUIInitialized()
        return

    def __onAppDestroyed(self, event):
        appNS = event.ns
        if self.__appFactory.hasApp(appNS):
            _logger.info(b'App is destroyed: %s', appNS)
            self.__appsStates[appNS] = ApplicationStateID.NOT_CREATED
        return
