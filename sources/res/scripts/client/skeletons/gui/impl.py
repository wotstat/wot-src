from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Callable
    from Event import Event
    from frameworks.wulf import ViewModel
    from frameworks.wulf.resource_manager import ResourceManager
    from frameworks.wulf.system_locale import SystemLocale
    from frameworks.wulf.formatters import Formatters
    from frameworks.wulf.tutorial import Tutorial
    from frameworks.wulf.ui_logger import UILogger
    from frameworks.wulf.windows_system.windows_manager import WindowsManager

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
    def formatters(self):
        raise NotImplementedError
        return

    @property
    def tutorial(self):
        raise NotImplementedError
        return

    @property
    def uiLogger(self):
        raise NotImplementedError
        return

    @property
    def scale(self):
        raise NotImplementedError
        return

    def init(self, tutorialModel, uiLoggerModel, serverTimeCallback):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return


class INotificationWindowController(IGameController):
    if typing.TYPE_CHECKING:
        onPostponedQueueUpdated = None

    def append(self, command):
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

    @property
    def activeQueueLength(self):
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
