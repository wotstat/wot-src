import logging
from frameworks.wulf import WindowStatus, WindowFlags
from gui.Scaleform.Waiting import Waiting
from helpers import dependency
from skeletons.gui.impl import IWindowLoaderController, IGuiLoader
_logger = logging.getLogger(__name__)

class WindowLoaderController(IWindowLoaderController):
    __slots__ = (b'__callbackID', b'__loadingWindows', b'__isWaitingShown')
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self):
        super(WindowLoaderController, self).__init__()
        self.__loadingWindows = []
        self.__isWaitingShown = False
        return

    def init(self):
        self.__gui.windowsManager.onWindowStatusChanged += self.__windowStatusChanged
        return

    def fini(self):
        self.__gui.windowsManager.onWindowStatusChanged -= self.__windowStatusChanged
        return

    def __windowStatusChanged(self, uniqueID, newStatus):
        from gui.Scaleform.framework.entities.sf_window import SFWindow
        window = self.__gui.windowsManager.getWindow(uniqueID)
        if window is None or WindowFlags.WINDOW_MODAL != window.modalityFlag:
            return
        isSFWindow = isinstance(window, SFWindow)
        if newStatus == WindowStatus.LOADING:
            if isSFWindow:
                window.onContentLoaded += self.__onDAAPIContentLoaded
            self.__loadingWindows.append(uniqueID)
            self.__triggerWaiting()
        elif newStatus == WindowStatus.LOADED and not isSFWindow:
            self.__loadingWindows.remove(uniqueID)
            self.__triggerWaiting()
        elif newStatus == WindowStatus.DESTROYING and uniqueID in self.__loadingWindows:
            if isSFWindow:
                window.onContentLoaded -= self.__onDAAPIContentLoaded
            self.__loadingWindows.remove(uniqueID)
            self.__triggerWaiting()
        return

    def __triggerWaiting(self):
        self.__callbackID = None
        hasLoading = bool(self.__loadingWindows)
        if self.__isWaitingShown:
            if not hasLoading:
                self.__isWaitingShown = False
                Waiting.hide(b'loadModalWindow')
                _logger.debug(b'Release screen from waiting.')
        elif hasLoading:
            self.__isWaitingShown = True
            _logger.debug(b'Lock screen with waiting.')
            Waiting.show(b'loadModalWindow', softStart=True)
        return

    def __onDAAPIContentLoaded(self, window):
        window.onContentLoaded -= self.__onDAAPIContentLoaded
        self.__loadingWindows.remove(window.uniqueID)
        self.__triggerWaiting()
        return
