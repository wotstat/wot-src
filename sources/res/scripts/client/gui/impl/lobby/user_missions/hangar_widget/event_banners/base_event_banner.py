from abc import ABCMeta
from helpers import time_utils
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState

class BaseEventBanner(object):
    __metaclass__ = ABCMeta
    NAME = b''

    def __init__(self):
        super(BaseEventBanner, self).__init__()
        self._isVisible = False
        return

    @property
    def bannerState(self):
        return EventBannerState.INACTIVE

    @property
    def isMode(self):
        return False

    @property
    def hasRewards(self):
        return False

    @property
    def borderColor(self):
        return b''

    @property
    def title(self):
        return b''

    @property
    def iconsPath(self):
        return b''

    @property
    def videosPath(self):
        return b''

    @property
    def introDescription(self):
        return b''

    @property
    def inProgressDescription(self):
        return b''

    @property
    def timerText(self):
        return b''

    @property
    def timerValue(self):
        return 0

    @property
    def eventStartDate(self):
        return 0

    @property
    def eventEndDate(self):
        return 0

    @property
    def playAppearAnim(self):
        return False

    @property
    def showTimerBeforeEventEnd(self):
        hoursBeforeEnd = 72
        return hoursBeforeEnd * time_utils.ONE_HOUR

    @property
    def isVisible(self):
        return self._isVisible

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
