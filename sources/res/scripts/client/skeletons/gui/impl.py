import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from Event import Event
    from frameworks.wulf import ViewModel
    from frameworks.wulf.tutorial import Tutorial
    from frameworks.wulf.ui_logger import UILogger
    from frameworks.wulf.markers_manager import MarkersManager

class IGuiLoader(object):
    __slots__ = ()

    @property
    def resourceManager(self):
        raise NotImplementedError
        return

    @property
    def windowsManager(self):
        raise NotImplementedError
        return

    @property
    def systemLocale(self):
        raise NotImplementedError
        return

    @property
    def tutorial(self):
        raise NotImplementedError
        return

    @property
    def markers(self):
        raise NotImplementedError
        return

    @property
    def uiLogger(self):
        raise NotImplementedError
        return

    def init(self, tutorialModel, uiLoggerModel):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return


class INotificationWindowController(IGameController):
    __slots__ = (b'onPostponedQueueUpdated',)
    if typing.TYPE_CHECKING:
        onPostponedQueueUpdated = None

    def append(self, window):
        raise NotImplementedError
        return

    def hasWindow(self, window):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isExecuting(self):
        raise NotImplementedError
        return

    def postponeActive(self):
        raise NotImplementedError
        return

    def releasePostponed(self):
        raise NotImplementedError
        return

    def lock(self, key):
        raise NotImplementedError
        return

    def unlock(self, key):
        raise NotImplementedError
        return

    def hasLock(self, key):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    @property
    def postponedCount(self):
        raise NotImplementedError
        return


class IFullscreenManager(object):
    __slots__ = ()

    def setEnabled(self, value):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return


class IWindowLoaderController(IGameController):
    __slots__ = ()


class IOverlaysManager(object):
    __slots__ = ()

    def isSuspended(self, window):
        raise NotImplementedError
        return

    def suspend(self, condition=None):
        raise NotImplementedError
        return

    def release(self):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return


class INewYearNavigation(object):
    onObjectStateChanged = None
    onUpdateCurrentView = None
    onChangeView = None

    @classmethod
    def closeMainView(cls):
        raise NotImplementedError
        return

    @classmethod
    def showMainView(cls, objectName, instantly=False, viewAlias=None, *args, **kwargs):
        raise NotImplementedError
        return

    @classmethod
    def showInfoView(cls, previousViewAlias=None, *args, **kwargs):
        raise NotImplementedError
        return

    @classmethod
    def showNavigationView(cls, viewAlias=None):
        raise NotImplementedError
        return

    @classmethod
    def switchToIntro(cls):
        raise NotImplementedError
        return

    @classmethod
    def switchByAnchorName(cls, anchorName):
        raise NotImplementedError
        return

    @classmethod
    def switchFromStyle(cls, objectName, viewAlias=None, tabName=None, *args, **kwargs):
        raise NotImplementedError
        return

    @classmethod
    def getCurrentObject(cls):
        raise NotImplementedError
        return

    @classmethod
    def getCurrentViewName(cls):
        raise NotImplementedError
        return

    @classmethod
    def getPreviousObject(cls):
        raise NotImplementedError
        return

    @classmethod
    def showViewAfterPrbSwitch(cls, aliasName, *args, **kwargs):
        raise NotImplementedError
        return

    @classmethod
    def switchToView(cls, aliasName, tabName=None, instantly=False, *args, **kwargs):
        raise NotImplementedError
        return

    @classmethod
    def switchTo(cls, objectName, instantly=False, viewAlias=None, withFade=False, *args, **kwargs):
        raise NotImplementedError
        return

    @classmethod
    def clear(cls):
        raise NotImplementedError
        return
