import typing
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared import g_eventBus
if typing.TYPE_CHECKING:
    from Event import Event
    from frameworks.wulf import View, ViewEvent, Window

class SubModelPresenter(object):
    __slots__ = (b'__viewModel', b'__isLoaded', b'__parentView')

    def __init__(self, viewModel, parentView):
        self.__parentView = parentView
        self.__viewModel = viewModel
        self.__isLoaded = False
        return

    @property
    def isLoaded(self):
        return self.__isLoaded

    @property
    def parentView(self):
        return self.__parentView

    def getParentWindow(self):
        return self.parentView.getParentWindow()

    def getViewModel(self):
        return self.__viewModel

    def initialize(self, *args, **kwargs):
        self.__subscribe()
        self.__isLoaded = True
        return

    def finalize(self):
        self.__isLoaded = False
        self.__unsubscribe()
        return

    def clear(self):
        self.__viewModel = None
        return

    def createToolTipContent(self, event, contentID):
        return

    def createPopOverContent(self, event):
        return

    def createContextMenuContent(self, event):
        return

    def createToolTip(self, event):
        return

    def createPopOver(self, event):
        return

    def createContextMenu(self, event):
        return

    def _getEvents(self):
        return ()

    def _getListeners(self):
        return tuple()

    def _getCallbacks(self):
        return tuple()

    def __subscribe(self):
        g_clientUpdateManager.addCallbacks(dict(self._getCallbacks()))
        for eventBusArgs in self._getListeners():
            g_eventBus.addListener(*eventBusArgs)

        for event, handler in self._getEvents():
            event += handler

        return

    def __unsubscribe(self):
        for event, handler in self._getEvents():
            event -= handler

        for eventBusArgs in reversed(self._getListeners()):
            g_eventBus.removeListener(*eventBusArgs[:3])

        g_clientUpdateManager.removeObjectCallbacks(self)
        return


class PageSubModelPresenter(SubModelPresenter):
    __slots__ = ()

    @property
    def pageId(self):
        raise NotImplementedError
        return
