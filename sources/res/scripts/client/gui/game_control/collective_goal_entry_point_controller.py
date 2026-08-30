import bisect, json, logging, typing
from Event import EventManager, EventsSubscriber, Event
from bootcamp.BootCampEvents import g_bootcampEvents
from constants import Configs
from gui.shared.utils.requesters.collective_goal_requester import CollectiveGoalRequester
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from helpers import dependency, time_utils, getLocalizedData
from skeletons.gui.game_control import ICollectiveGoalEntryPointController, IBootcampController
from skeletons.gui.lobby_context import ILobbyContext
from helpers.server_settings import serverSettingsChangeListener
if typing.TYPE_CHECKING:
    from helpers.server_settings import _CollectiveGoalEntryPointConfig
_logger = logging.getLogger(__name__)
_DEFAULTS = {b'currentPoints': 0, 
   b'startDate': 0, 
   b'endDate': 0, 
   b'discounts': {}}

class CollectiveGoalEntryPointController(ICollectiveGoalEntryPointController):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __bootcamp = dependency.descriptor(IBootcampController)

    def __init__(self):
        super(CollectiveGoalEntryPointController, self).__init__()
        self.__eventsManager = EventManager()
        self.__eventsSubscriber = EventsSubscriber()
        self.__requester = CollectiveGoalRequester()
        self.__notifier = SimpleNotifier(self.__getTimeLeft, self.__onEventStatusChanged)
        self.__data = _DEFAULTS
        self.onDataUpdated = Event(self.__eventsManager)
        self.onEventUpdated = Event(self.__eventsManager)
        self.onSettingsChanged = Event(self.__eventsManager)
        return

    def init(self):
        g_bootcampEvents.onBootcampStarted += self.__onEnterBootcamp
        return

    def onLobbyInited(self, event):
        self.__eventsSubscriber.subscribeToEvent(self.__requester.onUpdated, self.__onRequesterUpdated)
        self.__eventsSubscriber.subscribeToEvent(self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChanged)
        self.__startRequester()
        self.__notifier.startNotification()
        return

    def onAccountBecomeNonPlayer(self):
        self.__eventsSubscriber.unsubscribeFromAllEvents()
        self.__requester.stop()
        self.__notifier.stopNotification()
        return

    def fini(self):
        g_bootcampEvents.onBootcampStarted -= self.__onEnterBootcamp
        self.__eventsSubscriber.unsubscribeFromAllEvents()
        self.__requester.clear()
        self.__eventsManager.clear()
        self.__notifier.stopNotification()
        self.__notifier.clear()
        self.__data = _DEFAULTS
        return

    def isEnabled(self):
        serverTime = time_utils.getServerUTCTime()
        config = self.__getConfig()
        return config.isEnabled and config.startTime <= serverTime <= config.finishTime and not self.__bootcamp.isInBootcamp()

    def isStarted(self):
        serverTime = time_utils.getServerUTCTime()
        startTime = self.getActivePhaseStartTime()
        if startTime:
            return startTime <= serverTime
        return False

    def isFinished(self):
        serverTime = time_utils.getServerUTCTime()
        finishTime = self.getActivePhaseFinishTime()
        if finishTime:
            return finishTime < serverTime
        return False

    def isCompleted(self):
        discounts = self.__data[b'discounts']
        if discounts:
            return self.__data[b'currentPoints'] >= max(discounts.keys())
        return False

    def isForbidden(self):
        return not self.__data[b'discounts'] or self.__data[b'currentPoints'] < 0

    def getEventStartTime(self):
        return self.__getConfig().startTime

    def getEventFinishTime(self):
        return self.__getConfig().finishTime

    def getMarathonPrefix(self):
        return self.__getConfig().marathonPrefix

    def getActivePhaseStartTime(self):
        return self.__data[b'startDate']

    def getActivePhaseFinishTime(self):
        return self.__data[b'endDate']

    def getCurrentPoints(self):
        return self.__data[b'currentPoints']

    def getStagePoints(self):
        currentPoints = self.getCurrentPoints()
        discounts = self.getDiscounts()
        if not discounts:
            return 0
        points = sorted(discounts.keys())
        ind = bisect.bisect_right(points, currentPoints, 0, len(points) - 1)
        left = points[ind - 1] if ind > 0 else 0
        right = points[ind]
        return (currentPoints - left, right - left)

    def getDiscounts(self):
        return self.__data[b'discounts']

    def getCurrentDiscount(self):
        discounts = self.__data[b'discounts']
        if not discounts:
            return (-1, None)
        else:
            currentPoints = self.__data[b'currentPoints']
            points = sorted(discounts.keys())
            ind = bisect.bisect_right(points, currentPoints, 0, len(points) - 1)
            return (ind + 1, discounts[points[ind]])

    def getMarathonName(self):
        return getLocalizedData({b'marathonName': (self.__getConfig().marathonName)}, b'marathonName')

    def getGoalType(self):
        return self.__getConfig().goalType

    def getGoalDescription(self):
        return getLocalizedData({b'goalDescription': (self.__getConfig().goalDescription)}, b'goalDescription')

    def getRulesCaption(self):
        return getLocalizedData({b'rulesCaption': (self.__getConfig().rulesCaption)}, b'rulesCaption')

    def __getConfig(self):
        return self.__lobbyContext.getServerSettings().collectiveGoalEntryPointConfig

    def __startRequester(self):
        if self.isEnabled():
            self.__requester.start(self.__getConfig().hermodChannelName)
        return

    def __getTimeLeft(self):
        serverTime = time_utils.getServerUTCTime()
        config = self.__getConfig()
        if serverTime <= config.startTime:
            return config.startTime - serverTime
        if self.__data:
            activePhaseStart = self.getActivePhaseStartTime()
            if activePhaseStart and serverTime <= activePhaseStart:
                return activePhaseStart - serverTime
            activePhaseEnd = self.getActivePhaseFinishTime()
            if activePhaseEnd and serverTime <= activePhaseEnd:
                return activePhaseEnd - serverTime
        if serverTime <= config.finishTime:
            return config.finishTime - serverTime
        return 0

    def __updateData(self, rawData):
        self.__data[b'currentPoints'] = rawData.get(b'currentPoints', _DEFAULTS[b'currentPoints'])
        self.__data[b'startDate'] = rawData.get(b'startDate', _DEFAULTS[b'startDate'])
        self.__data[b'endDate'] = rawData.get(b'endDate', _DEFAULTS[b'endDate'])
        self.__data[b'discounts'] = {i.get(b'points', 0): i.get(b'discount', 0) for i in rawData.get(b'discounts', [])}
        return

    def __onRequesterUpdated(self):
        message = self.__requester.getMessage()
        if message:
            try:
                message = json.loads(message)
                oldStartDate = self.__data[b'startDate']
                oldEndDate = self.__data[b'endDate']
                self.__updateData(message)
                if self.__data[b'startDate'] != oldStartDate or self.__data[b'endDate'] != oldEndDate:
                    self.__notifier.startNotification()
                    self.__onEventStatusChanged()
                self.onDataUpdated()
            except ValueError:
                _logger.error(b'Invalid JSON data received from service')

        return

    def __onEventStatusChanged(self):
        self.onEventUpdated()
        return

    @serverSettingsChangeListener(Configs.COLLECTIVE_GOAL_ENTRY_POINT_CONFIG.value)
    def __onServerSettingsChanged(self, diff):
        collectiveGoalDiff = diff[Configs.COLLECTIVE_GOAL_ENTRY_POINT_CONFIG.value]
        if self.__requester.isActive:
            if not self.isEnabled():
                self.__requester.stop()
                self.__data = _DEFAULTS
            elif b'hermodChannelName' in collectiveGoalDiff:
                self.__requester.stop()
                self.__startRequester()
        elif self.isEnabled():
            self.__startRequester()
        if self.__getConfig().isEnabled and (b'startTime' in collectiveGoalDiff or b'finishTime' in collectiveGoalDiff):
            self.__notifier.startNotification()
        if {b'isEnabled', b'startTime', b'finishTime'}.intersection(collectiveGoalDiff):
            self.__onEventStatusChanged()
        self.onSettingsChanged()
        return

    def __onEnterBootcamp(self):
        if self.__requester.isActive:
            self.__requester.stop()
        return
