import logging, weakref, typing
from helpers.events_handler import EventsHandler
if typing.TYPE_CHECKING:
    from typing import Optional
    from frameworks.wulf import View, ViewEvent, Window
_logger = logging.getLogger(__name__)

class SubModelPresenter(EventsHandler):
    __slots__ = (b'__viewModel', b'__isLoaded', b'__parentView')

    def __init__(self, viewModel, parentView):
        self.__parentView = parentView
        self.__viewModel = weakref.proxy(viewModel)
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
        self._subscribe()
        self.__isLoaded = True
        return

    def finalize(self):
        if not self.__isLoaded:
            _logger.warning(b'Try to destroy %r which is not loaded', type(self))
            return
        self.__isLoaded = False
        self._unsubscribe()
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
