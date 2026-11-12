from helpers import dependency
from helpers.events_handler import EventsHandler
from new_year.helpers.ny_leaderboard_tank_reward import getUnseenLeaderboardTankReward, shouldShowLeaderboardTankReward
from new_year.skeletons.new_year import INewYearController
from skeletons.gui.shared.utils import IHangarSpace

class NewYearLeaderboardTankRewardController(EventsHandler):
    __slots__ = (b'__isPresenting', b'__isSubscribed')
    _hangarSpace = dependency.descriptor(IHangarSpace)
    _nyController = dependency.descriptor(INewYearController)

    def __init__(self):
        super(NewYearLeaderboardTankRewardController, self).__init__()
        self.__isPresenting = False
        self.__isSubscribed = False
        return

    def fini(self):
        self.__unsubscribeSafe()
        return

    def onConnected(self):
        self.__subscribeSafe()
        return

    def onDisconnected(self):
        self.__isPresenting = False
        self.__unsubscribeSafe()
        return

    def onAvatarBecomePlayer(self):
        self.__isPresenting = False
        self.__unsubscribeSafe()
        return

    def onAccountBecomePlayer(self):
        self.__subscribeSafe()
        return

    def shouldShow(self, seasonId=None):
        return shouldShowLeaderboardTankReward(seasonId)

    def isBlockedByFirstEnter(self):
        firstEnter = self._nyController.firstEnterVideo
        return firstEnter.isActive or firstEnter.shouldStartIntro()

    def canPresentNow(self):
        return not self.__isPresenting and self._hangarSpace.spaceInited and not self.isBlockedByFirstEnter() and self.shouldShow()

    def requestPresent(self):
        return self.__tryPresent()

    def notifyPresentedFinished(self):
        self.__isPresenting = False
        self.requestPresent()
        return

    def _getEvents(self):
        return (
         (
          self._hangarSpace.onSpaceCreate, self.__onHangarSpaceCreated),
         (
          self._nyController.firstEnterVideo.onIntroComplete, self.__onFirstEnterComplete))

    def __subscribeSafe(self):
        if self.__isSubscribed:
            return
        self._subscribe()
        self.__isSubscribed = True
        return

    def __unsubscribeSafe(self):
        if not self.__isSubscribed:
            return
        self._unsubscribe()
        self.__isSubscribed = False
        return

    def __onHangarSpaceCreated(self):
        self.requestPresent()
        return

    def __onFirstEnterComplete(self):
        self.requestPresent()
        return

    def __tryPresent(self):
        if not self.canPresentNow():
            return False
        else:
            pending = getUnseenLeaderboardTankReward()
            if pending is None:
                return False
            seasonId, entry = pending
            self.__isPresenting = True
            from new_year.gui.shared.event_dispatcher import showNYVideoRewardWindow
            showNYVideoRewardWindow(seasonId=seasonId, vehicleCD=entry.get(b'vehicleCD'), rewards=entry.get(b'rewards') or {})
            return True
