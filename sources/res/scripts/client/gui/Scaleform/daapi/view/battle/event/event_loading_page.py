from __future__ import absolute_import
from PlayerEvents import g_playerEvents
from gui.Scaleform.daapi.view.meta.EventLoadingMeta import EventLoadingMeta
from gui.battle_control.arena_info.interfaces import IArenaLoadController
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
PATH_BACKGROUNDS = b'../maps/icons/event/loading/{0}_{1}.png'
LINKAGE_BACKGROUNDS = b'{0}Page{1}UI'

class EventLoadingPage(EventLoadingMeta, IArenaLoadController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, ctx):
        super(EventLoadingPage, self).__init__()
        self._tutorialPages = ctx.get(b'tutorialPages', [])
        return

    def _populate(self):
        super(EventLoadingPage, self)._populate()
        self.sessionProvider.addArenaCtrl(self)
        g_playerEvents.onDisconnected += self._onDisconnected
        listSmall = []
        listBig = []
        for pageId in self._tutorialPages:
            listSmall.append(self._getTutorialPageVO(pageId, False))
            listBig.append(self._getTutorialPageVO(pageId, True))

        self.as_setDataS({b'lessonPagesSmallData': listSmall, 
           b'lessonPagesBigData': listBig, 
           b'navigationButtonsVisible': (len(listSmall) > 1)})
        return

    def _dispose(self):
        self.sessionProvider.removeArenaCtrl(self)
        super(EventLoadingPage, self)._dispose()
        g_playerEvents.onDisconnected -= self._onDisconnected
        return

    def updateSpaceLoadProgress(self, progress):
        self.as_updateProgressS(progress)
        return

    def _onDisconnected(self):
        self.destroy()
        return

    @staticmethod
    def _getTutorialPageVO(pageId, bigSize):
        pathBackgroundSize = b'big' if bigSize else b'small'
        linkageBackgroundSize = b'Big' if bigSize else b'Small'
        voSettings = {b'background': (PATH_BACKGROUNDS.format(pageId, pathBackgroundSize)), 
           b'rendererLinkage': (LINKAGE_BACKGROUNDS.format(pageId, linkageBackgroundSize))}
        return voSettings
