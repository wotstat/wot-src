from __future__ import absolute_import
import typing
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.impl import backport
from gui.impl.gen import R
from gui.lobby_state_machine.states import ViewLobbyState, SubScopeTopLayerState, LobbyStateDescription
if typing.TYPE_CHECKING:
    from gui.Scaleform.daapi.view.lobby.manual.manual_chapter_view import ManualChapterView

def registerStates(machine):
    machine.addState(ManualState())
    machine.addState(ManualChapterState())
    return


def registerTransitions(machine):
    return


@SubScopeTopLayerState.parentOf
class ManualState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.WIKI_VIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.WIKI_VIEW)

    @classmethod
    def goTo(cls, chapterIndex=None, pageIndex=None):
        super(ManualState, cls).goTo(chapterIndex=chapterIndex, pageIndex=pageIndex)
        return

    def compareParams(self, params, otherParams):
        return True

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)
        return

    def getNavigationDescription(self):
        return LobbyStateDescription(title=backport.text(R.strings.menu.headerButtons.wiki()))

    def _getViewLoadCtx(self, event):
        return {b'ctx': (event.params)}


@SubScopeTopLayerState.parentOf
class ManualChapterState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.MANUAL_CHAPTER_VIEW
    VIEW_KEY = ViewKey(VIEW_ALIAS.MANUAL_CHAPTER_VIEW)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(ManualChapterState, self).__init__(flags=flags)
        self.__cachedParams = {}
        return

    @classmethod
    def goTo(cls, chapterIndex, pageIndex=None):
        super(ManualChapterState, cls).goTo(chapterIndex=chapterIndex, pageIndex=pageIndex)
        return

    def registerTransitions(self):
        lsm = self.getMachine()
        lsm.addNavigationTransitionFromParent(self)
        return

    def getNavigationDescription(self):
        view = self.getMachine().getRelatedView(self)
        title = view.chapterData[b'details'][0][b'chapterTitle']
        return LobbyStateDescription(title=title)

    def serializeParams(self):
        return self.__cachedParams

    def _getViewLoadCtx(self, event):
        return {b'ctx': (event.params)}

    def _onEntered(self, event):
        self.__cachedParams = event.params
        super(ManualChapterState, self)._onEntered(event)
        return

    def _onExited(self):
        self.__cachedParams = {}
        super(ManualChapterState, self)._onExited()
        return
