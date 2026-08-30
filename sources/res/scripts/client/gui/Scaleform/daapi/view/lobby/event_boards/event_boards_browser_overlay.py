from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.event_boards.browser_in_view_component import BrowserInViewComponent

class EventBoardsBrowserOverlay(BrowserInViewComponent):

    def setOpener(self, view):
        self.setUrl(view.ctx.get(b'url'))
        self.as_setTitleS(view.ctx.get(b'title'))
        return
