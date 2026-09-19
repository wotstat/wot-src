from __future__ import absolute_import
from typing import TYPE_CHECKING
from helpers import time_utils
if TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.widget.event_banner_model import EventBannerModel

class BaseEventBanner(object):
    NAME = b''

    def __init__(self):
        super(BaseEventBanner, self).__init__()
        self._isVisible = False
        return

    @property
    def isVisible(self):
        return self._isVisible

    @property
    def showTimerBeforeEventEnd(self):
        hoursBeforeEnd = 72
        return hoursBeforeEnd * time_utils.ONE_HOUR

    @property
    def playAppearAnim(self):
        return False

    def fillModel(self, model):
        model.setName(self.NAME)
        model.setShowTimerBeforeEventEnd(self.showTimerBeforeEventEnd)
        return

    def createToolTipContent(self, event):
        return

    def onClick(self):
        return

    def onAppearAnimationPlayed(self):
        return

    def prepare(self):
        return

    def onAppear(self):
        self._isVisible = True
        return

    def onDisappear(self):
        self._isVisible = False
        return

    def startPersistentListening(self):
        return

    def stopPersistentListening(self):
        return
