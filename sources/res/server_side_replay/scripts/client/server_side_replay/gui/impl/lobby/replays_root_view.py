from __future__ import absolute_import
import logging, typing
from frameworks.wulf import ViewFlags, ViewSettings
from server_side_replay.gui.impl.gen.view_models.views.lobby.root_view_model import RootViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.tab_model import TabModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.enums import ReplaysViews
from gui.impl.gui_decorators import args2params
from server_side_replay.gui.impl.lobby.replays_lobby_sounds import REPLAYS_SOUND_SPACE
from server_side_replay.gui.impl.lobby.pages.best_replays_page import BestReplaysPage
from server_side_replay.gui.impl.lobby.pages.my_replays_page import MyReplaysPage
from server_side_replay.gui.impl.lobby.pages.find_replay_page import FindReplayPage
from gui.impl.pub import ViewImpl
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.shared.event_dispatcher import showHangar
if typing.TYPE_CHECKING:
    from server_side_replay.gui.impl.lobby.pages import PageSubModelPresenter
_logger = logging.getLogger(__name__)

class ReplaysRootView(ViewImpl, IGlobalListener):
    __slots__ = (b'__pages', b'__tabId')
    _COMMON_SOUND_SPACE = REPLAYS_SOUND_SPACE

    def __init__(self, layoutID, *args, **kwargs):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = RootViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(ReplaysRootView, self).__init__(settings)
        self.__pages = {}
        self.__tabId = ReplaysViews.BESTREPLAYS
        return

    @property
    def viewModel(self):
        return super(ReplaysRootView, self).getViewModel()

    @property
    def tabId(self):
        return self.__tabId

    def createToolTip(self, event):
        if self.__currentPage.isLoaded:
            window = self.__currentPage.createToolTip(event)
            if window is not None:
                return window
        return super(ReplaysRootView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if self.__currentPage.isLoaded:
            content = self.__currentPage.createToolTipContent(event, contentID)
            if content is not None:
                return content
        return super(ReplaysRootView, self).createToolTipContent(event, contentID)

    def createContextMenu(self, event):
        if self.__currentPage.isLoaded:
            window = self.__currentPage.createContextMenu(event)
            if window is not None:
                return window
        return super(ReplaysRootView, self).createContextMenu(event)

    def createPopOver(self, event):
        if self.__currentPage.isLoaded:
            window = self.__currentPage.createPopOver(event)
            if window is not None:
                return window
        return super(ReplaysRootView, self).createPopOver(event)

    def switchPage(self, tabId, *args, **kwargs):
        if self.__currentPage.isLoaded:
            self.__currentPage.finalize()
        page = self.__pages[tabId]
        page.initialize(*args, **kwargs)
        self.viewModel.setPageViewId(page.pageId)
        self.__tabId = tabId
        g_eventDispatcher.updateUI()
        return

    def _finalize(self):
        self.__removeListeners()
        self.__clearPages()
        return

    def _onLoading(self, *args, **kwargs):
        tabId = kwargs.pop(b'tabId', None)
        if tabId is not None:
            if tabId in tuple(ReplaysViews):
                self.__tabId = tabId
            else:
                _logger.error(b'Wrong tabId: %s', tabId)
        self.__initPages()
        self.__updateTabs()
        page = self.__pages[self.__tabId]
        page.initialize(*args, **kwargs)
        self.viewModel.setPageViewId(page.pageId)
        self.__addListeners()
        return

    @property
    def __currentPage(self):
        return self.__pages[self.__tabId]

    def __addListeners(self):
        self.viewModel.onClose += self.__onClose
        self.viewModel.sidebar.onSideBarTabChange += self.__onSideBarTabChanged
        self.startGlobalListening()
        return

    def __removeListeners(self):
        self.viewModel.onClose -= self.__onClose
        self.viewModel.sidebar.onSideBarTabChange -= self.__onSideBarTabChanged
        self.stopGlobalListening()
        return

    def __initPages(self):
        pages = (
         BestReplaysPage(self.viewModel.bestReplays, self),
         MyReplaysPage(self.viewModel.myReplays, self),
         FindReplayPage(self.viewModel.findReplay, self))
        self.__pages = {p.pageId: p for p in pages}
        return

    def __clearPages(self):
        if self.__pages and self.__currentPage.isLoaded:
            self.__currentPage.finalize()
        self.__pages.clear()
        return

    def __updateTabs(self):
        with self.viewModel.transaction() as tx:
            tabs = tx.sidebar.getItems()
            tabs.clear()
            for tab in tuple(ReplaysViews):
                tabModel = TabModel()
                tabModel.setId(tab)
                tabs.addViewModel(tabModel)

            tabs.invalidate()
        return

    def __onClose(self):
        showHangar()
        return

    @args2params(int)
    def __onSideBarTabChanged(self, tabId):
        if tabId == self.__tabId:
            return
        if tabId not in self.__pages:
            _logger.error(b'Wrong tabId: %s', tabId)
            return
        self.switchPage(tabId)
        return
