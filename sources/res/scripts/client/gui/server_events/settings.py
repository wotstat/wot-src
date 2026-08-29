import time, logging
from contextlib import contextmanager
from account_helpers.AccountSettings import DOG_TAGS, WOT_PLUS, TELECOM_RENTALS
from gui.shared import utils
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
_logger = logging.getLogger(__name__)

class _PMSettings(utils.SettingRecord):

    def __init__(self, introShown=False, operationsVisited=None, headerAlert=False):
        super(_PMSettings, self).__init__(introShown=introShown, operationsVisited=operationsVisited or set(), headerAlert=headerAlert)
        return

    def markOperationAsVisited(self, operationID):
        self.update(operationsVisited=self.operationsVisited | {operationID})
        return


class _DQSettings(utils.SettingRecord):

    def __init__(self, lastVisitedDQTabIdx=None, premMissionsTabDiscovered=False, lastBonusMissionVisited=None, dailyQuestsIntroSeen=False, *args, **kwargs):
        super(_DQSettings, self).__init__(lastVisitedDQTabIdx=lastVisitedDQTabIdx, premMissionsTabDiscovered=premMissionsTabDiscovered, lastBonusMissionVisited=lastBonusMissionVisited, dailyQuestsIntroSeen=dailyQuestsIntroSeen)
        return

    def setLastVisitedDQTab(self, lastVisitedDQTabIdx):
        self.update(lastVisitedDQTabIdx=lastVisitedDQTabIdx)
        return

    def setPremMissionsTabDiscovered(self, premMissionsTabDiscovered):
        self.update(premMissionsTabDiscovered=premMissionsTabDiscovered)
        return

    def setLastBonusMissionVisited(self, lastBonusMissionVisited):
        self.update(lastBonusMissionVisited=lastBonusMissionVisited)
        return

    def setDailyQuestsIntroSeen(self, dailyQuestsIntroSeen):
        self.update(dailyQuestsIntroSeen=dailyQuestsIntroSeen)
        return


class _DogTagsRootSettings(utils.SettingRootRecord):

    def __init__(self, lastVisitedDogTagsTabIdx=None, onboardingEnabled=True, seenComps=None):
        super(_DogTagsRootSettings, self).__init__(lastVisitedDogTagsTabIdx=lastVisitedDogTagsTabIdx, onboardingEnabled=onboardingEnabled, seenComps=seenComps or set())
        return

    def setLastVisitedDogTagsTab(self, lastVisitedDogTagsTabIdx):
        self.update(lastVisitedDogTagsTabIdx=lastVisitedDogTagsTabIdx)
        return

    def setOnboardingEnabled(self, onboardingEnabled):
        self.update(onboardingEnabled=onboardingEnabled)
        return

    def markComponentAsSeen(self, compId):
        self.update(seenComps=self.seenComps | {compId})
        return

    @classmethod
    def _getSettingName(cls):
        return DOG_TAGS


class _WotPlusSettings(utils.SettingRootRecord):

    def __init__(self, isFirstTime=True, isWotPlusEnabled=False, isGoldReserveEnabled=False, isPassiveXpEnabled=False, isFreeDemountingEnabled=False, isExcludedMapEnabled=False, isSubscrbExcludedMapSlotsEnabled=False, isExcludedMapsKillSwitchInitialized=False, isDailyAttendancesEnabled=False, isDailyQuestsExtraRewardsEnabled=False, isTeamCreditsBonusEnabled=False, isExclusiveVehicleEnabled=False, rentPendingVehCD=None, amountOfDailyAttendance=0, **kwargs):
        if kwargs:
            _logger.warning(b'Not expected argument in WotPlus settings. Check preference.xml. kwargs=%r', kwargs)
        super(_WotPlusSettings, self).__init__(isFirstTime=isFirstTime, isWotPlusEnabled=isWotPlusEnabled, isGoldReserveEnabled=isGoldReserveEnabled, isPassiveXpEnabled=isPassiveXpEnabled, isFreeDemountingEnabled=isFreeDemountingEnabled, isExcludedMapEnabled=isExcludedMapEnabled, isSubscrbExcludedMapSlotsEnabled=isSubscrbExcludedMapSlotsEnabled, isExcludedMapsKillSwitchInitialized=isExcludedMapsKillSwitchInitialized, isDailyAttendancesEnabled=isDailyAttendancesEnabled, isExclusiveVehicleEnabled=isExclusiveVehicleEnabled, isDailyQuestsExtraRewardsEnabled=isDailyQuestsExtraRewardsEnabled, isTeamCreditsBonusEnabled=isTeamCreditsBonusEnabled, amountOfDailyAttendance=amountOfDailyAttendance)
        return

    def setIsFirstTime(self, isFirstTime):
        self.update(isFirstTime=isFirstTime)
        return

    def setWotPlusEnabledState(self, isEnabled):
        self.update(isWotPlusEnabled=isEnabled)
        return

    def setGoldReserveEnabledState(self, isEnabled):
        self.update(isGoldReserveEnabled=isEnabled)
        return

    def setPassiveXpState(self, isEnabled):
        self.update(isPassiveXpEnabled=isEnabled)
        return

    def setFreeDemountingState(self, isEnabled):
        self.update(isFreeDemountingEnabled=isEnabled)
        return

    def setExcludedMapState(self, isEnabled):
        self.update(isExcludedMapEnabled=isEnabled)
        return

    def setSubscrbExcludedMapSlotsState(self, isEnabled):
        self.update(isSubscrbExcludedMapSlotsEnabled=isEnabled)
        return

    def setExcludedMapsKillSwitchInitialized(self, isInitialized):
        self.update(isExcludedMapsKillSwitchInitialized=isInitialized)
        return

    def setDailyAttendancesState(self, isEnabled):
        self.update(isDailyAttendancesEnabled=isEnabled)
        return

    def setDailyQuestsExtraRewardsState(self, isEnabled):
        self.update(isDailyQuestsExtraRewardsEnabled=isEnabled)
        return

    def setExclusiveVehicleState(self, isEnabled):
        self.update(isExclusiveVehicleEnabled=isEnabled)
        return

    def setTeamCreditsBonusState(self, isEnabled):
        self.update(isTeamCreditsBonusEnabled=isEnabled)
        return

    def setAmountOfDailyAttendance(self, amount):
        self.update(amountOfDailyAttendance=amount)
        return

    def increaseDailyAttendance(self):
        self.setAmountOfDailyAttendance(self.get(b'amountOfDailyAttendance', 0) + 1)
        return

    @classmethod
    def _getSettingName(cls):
        return WOT_PLUS


class _TelecomRentalsSettings(utils.SettingRootRecord):

    def __init__(self, isTelecomRentalsEnabled=False, isTelecomRentalsBlocked=False, pendingRentals=None):
        super(_TelecomRentalsSettings, self).__init__(isTelecomRentalsEnabled=isTelecomRentalsEnabled, isTelecomRentalsBlocked=isTelecomRentalsBlocked, pendingRentals=pendingRentals or set())
        return

    def setTelecomRentalsEnabledState(self, isEnabled):
        self.update(isTelecomRentalsEnabled=isEnabled)
        return

    def setTelecomRentalsBlockedState(self, isBlocked):
        self.update(isTelecomRentalsBlocked=isBlocked)
        return

    def setRentPending(self, vehCD):
        self.update(pendingRentals=self.pendingRentals | {vehCD})
        return

    def resetRentPending(self, vehCD):
        self.pendingRentals.discard(vehCD)
        self.update(pendingRentals=self.pendingRentals)
        return

    @classmethod
    def _getSettingName(cls):
        return TELECOM_RENTALS


class _QuestSettings(utils.SettingRootRecord):

    def __init__(self, lastVisitTime=-1, visited=None, naVisited=None, minimized=None, personalMissions=None, dailyQuests=None, questDeltas=None):
        super(_QuestSettings, self).__init__(lastVisitTime=lastVisitTime, visited=visited or set(), naVisited=naVisited or set(), minimized=minimized or set(), personalMissions=_PMSettings(**(personalMissions or {})), dailyQuests=_DQSettings(**(dailyQuests or {})), questDeltas=questDeltas or dict())
        return

    def updateVisited(self, visitSettingName, eventID):
        settingsValue = set(self[visitSettingName])
        if eventID not in settingsValue:
            self.update(**{visitSettingName: (tuple(settingsValue | {eventID}))})
            return True
        return False

    def removeCompleted(self, completedIDs):
        self.update(visited=tuple(set(self.visited).difference(completedIDs)))
        self.update(naVisited=tuple(set(self.naVisited).difference(completedIDs)))
        return

    def updateExpanded(self, eventID, isExpanded):
        settingsValue = set(self[b'minimized'])
        if isExpanded:
            self.update(minimized=tuple(settingsValue.difference([eventID])))
        else:
            self.update(minimized=tuple(settingsValue.union([eventID])))
        return

    def save(self):
        self.update(lastVisitTime=time.time())
        super(_QuestSettings, self).save()
        return

    def _asdict(self):
        result = super(_QuestSettings, self)._asdict()
        result.update(personalMissions=self.personalMissions._asdict())
        result.update(dailyQuests=self.dailyQuests._asdict())
        return result

    @classmethod
    def _getSettingName(cls):
        return b'quests'


def get():
    return _QuestSettings.load()


def isNewCommonEvent(svrEvent, settings=None):
    settings = settings or get()
    if settings is not None and not svrEvent.isCompleted() and not svrEvent.isOutOfDate():
        eventID = svrEvent.getSeenSettingID()
        isVisitedSettings = eventID in settings[b'visited']
        isNaVisitedSettings = eventID in settings[b'naVisited']
        if isVisitedSettings and isNaVisitedSettings:
            return False
        if svrEvent.isAvailable()[0]:
            return not isVisitedSettings
        return not isNaVisitedSettings
    else:
        return False


def isGroupMinimized(groupID, settings=None):
    settings = settings or get()
    return groupID in settings[b'minimized']


def getNewCommonEvents(events):
    settings = get()
    return [e for e in events if isNewCommonEvent(e, settings)]


def visitEventGUI(event):
    if event is None:
        return
    else:
        s = get()
        isNaVisitedChanged = s.updateVisited(b'naVisited', event.getSeenSettingID())
        if event.isAvailable()[0]:
            isVisitedChanged = s.updateVisited(b'visited', event.getSeenSettingID())
        else:
            isVisitedChanged = False
        if isNaVisitedChanged or isVisitedChanged:
            s.save()
        return isNaVisitedChanged or isVisitedChanged


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def visitEventsGUI(events, counters=(), eventsCache=None):
    visitedEvents = set()
    if events:
        for event in events:
            if visitEventGUI(event):
                visitedEvents.add(event)

    if visitedEvents:
        converted = {}
        for counter in counters:
            key, value = counter(eventsCache)
            converted[key] = value

    return


def expandGroup(groupID, isExpanded):
    if groupID is None:
        return
    else:
        s = get()
        s.updateExpanded(groupID, isExpanded)
        s.save()
        return


def updateCommonEventsSettings(svrEvents):
    s = get()
    s.removeCompleted(set(e.getSeenSettingID() for e in svrEvents.itervalues() if e.isCompleted()))
    s.save()
    return


def _updatePMSettings(**kwargs):
    settings = get()
    settings.personalMissions.update(**kwargs)
    settings.save()
    return


def isPMOperationNew(operationID, pmQuestsSettings=None):
    settings = pmQuestsSettings or get()
    return operationID not in settings.personalMissions.operationsVisited


def isNeedToShowHeaderAlert():
    return get().personalMissions.headerAlert


def markHeaderAlertAsVisited():
    _updatePMSettings(headerAlert=True)
    return


def getDQSettings():
    return get().dailyQuests


@contextmanager
def dailyQuestSettings():
    s = get()
    yield s.dailyQuests
    s.save()
    return


def getDogTagsSettings():
    return _DogTagsRootSettings.load()


@contextmanager
def dogTagsSettings():
    s = getDogTagsSettings()
    yield s
    s.save()
    return


def getWotPlusSettings():
    return _WotPlusSettings.load()


@contextmanager
def wotPlusSettings():
    s = getWotPlusSettings()
    yield s
    s.save()
    return


def getTelecomRentalsSettings():
    return _TelecomRentalsSettings.load()


@contextmanager
def telecomRentalsSettings():
    s = getTelecomRentalsSettings()
    yield s
    s.save()
    return
