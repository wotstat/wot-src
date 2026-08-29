import logging
from account_helpers.AccountSettings import AccountSettings, LOBBY_MENU_MANUAL_TRIGGER_SHOWN
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.doc_loaders.manual_xml_data_reader import ManualPageTypes
from helpers import dependency
from skeletons.gui.game_control import IManualController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import IBootcampController
from gui.app_loader import sf_lobby
from gui.doc_loaders import manual_xml_data_reader
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from PlayerEvents import g_playerEvents
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA
_logger = logging.getLogger(__name__)

class ManualController(IManualController):
    lobbyContext = dependency.descriptor(ILobbyContext)
    bootcamp = dependency.descriptor(IBootcampController)

    def __init__(self):
        super(ManualController, self).__init__()
        self.__chapters = None
        self._isChapterViewOnScreen = False
        return

    def init(self):
        g_eventBus.addListener(events.ManualEvent.CHAPTER_CLOSED, self.__onChapterClosed, EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onAccountBecomePlayer += self.__onAccountBecomePlayer
        return

    def fini(self):
        g_eventBus.removeListener(events.ManualEvent.CHAPTER_CLOSED, self.__onChapterClosed, EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onAccountBecomePlayer -= self.__onAccountBecomePlayer
        return

    @sf_lobby
    def app(self):
        return

    def getChaptersUIData(self):
        chaptersUIData = [i[b'uiData'] for i in self.__getChapters()]
        return chaptersUIData

    def getChapterUIData(self, chapterIndex):
        chapterFilename = None
        chapterTitle = b''
        for chapter in self.__getChapters():
            if chapter[b'uiData'][b'index'] == chapterIndex:
                chapterFilename = chapter[b'filePath']
                chapterTitle = chapter[b'uiData'].get(b'label', b'')

        currentChapter = manual_xml_data_reader.getChapterData(chapterFilename, self.pageFilter, self.getBootcampRunCount(), chapterTitle)
        return currentChapter

    def pageFilter(self, pageType):
        if pageType == ManualPageTypes.BOOTCAMP_PAGE:
            return self.__isBootcampEnabled()
        if pageType == ManualPageTypes.MAPS_TRAINING_PAGE:
            return self.lobbyContext.getServerSettings().isMapsTrainingEnabled()
        return True

    def clear(self):
        self.__chapters = None
        return

    def isActivated(self):
        return self.lobbyContext.getServerSettings().isManualEnabled()

    def getBootcampRunCount(self):
        return self.bootcamp.runCount()

    def getChapterView(self):
        windowContainer = self.app.containerManager.getContainer(WindowLayer.TOP_SUB_VIEW)
        return windowContainer.getView(criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.MANUAL_CHAPTER_VIEW)})

    def getView(self):
        windowContainer = self.app.containerManager.getContainer(WindowLayer.SUB_VIEW)
        return windowContainer.getView(criteria={(POP_UP_CRITERIA.VIEW_ALIAS): (VIEW_ALIAS.WIKI_VIEW)})

    def show(self, lessonID=None, backCallback=None):
        view = self.getView()
        ctx = {b'backCallback': backCallback}
        if not lessonID:
            g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.WIKI_VIEW), ctx=ctx), EVENT_BUS_SCOPE.LOBBY)
        else:
            for chapterIndex, chapter in enumerate(self.__getChapters()):
                pageIndex = next((pageIndex for pageIndex, pageID in enumerate(chapter[b'pageIDs']) if pageID == lessonID), None)
                if pageIndex is not None:
                    if view:
                        self.showChapterView(chapterIndex, pageIndex)
                    else:
                        ctx.update({b'chapterIndex': chapterIndex, b'pageIndex': pageIndex})
                        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.WIKI_VIEW), ctx=ctx), EVENT_BUS_SCOPE.LOBBY)
                    return

            _logger.debug(b'Cant found page to show lesson with id %d', lessonID)
        return

    def isChapterViewOnScreen(self):
        return self._isChapterViewOnScreen

    def runBootcamp(self):
        _logger.debug(b'ManualChapterView. Requested bootcamp start.')
        self.bootcamp.runBootcamp()
        return

    def showChapterView(self, chapterIndex=0, pageIndex=0):
        self._isChapterViewOnScreen = True
        chapterView = self.getChapterView()
        if chapterView:
            chapterView.setData(chapterIndex, pageIndex)
            return
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.MANUAL_CHAPTER_VIEW), ctx={b'chapterIndex': chapterIndex, b'pageIndex': pageIndex}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def collectUnreadPages(self, chapters):
        return [chapter[b'newPageIDs'] for chapter in chapters]

    def getNewContentCount(self):
        number = self.__countNewContent()
        if number and AccountSettings.getManualData(LOBBY_MENU_MANUAL_TRIGGER_SHOWN):
            return number
        return 0

    def __getChapters(self):
        if self.__chapters is None:
            self.__chapters = manual_xml_data_reader.getChapters(self.pageFilter)
        return self.__chapters

    def __isBootcampEnabled(self):
        return self.lobbyContext.getServerSettings().isBootcampEnabled()

    def __onChapterClosed(self, _):
        self._isChapterViewOnScreen = False
        return

    def __onAccountBecomePlayer(self):
        self.__initChaptersSettings()
        return

    def __initChaptersSettings(self):
        chapters = AccountSettings.getManualUnreadPages()
        if chapters is None:
            chapters = self.collectUnreadPages(self.__getChapters())
            AccountSettings.setManualUnreadPages(chapters)
        return

    def __countNewContent(self):
        return sum(len(i) for i in AccountSettings.getManualUnreadPages())
