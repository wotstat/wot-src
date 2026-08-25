import time
from contextlib import contextmanager
from account_helpers.AccountSettings import DOG_TAGS, WOT_PLUS, TELECOM_RENTALS, PERSONAL_RESERVES, COMMENDATIONS
from gui.shared import utils
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class _PMSettings(utils.SettingRecord):

    def __init__(self, introShown=False, operationsVisited=None, headerAlert=False):
        super(_PMSettings, self).__init__(introShown=introShown, operationsVisited=operationsVisited or set(), headerAlert=headerAlert)
        return

    def markOperationAsVisited(self, operationID):
        self.update(operationsVisited=self.operationsVisited | {operationID})
        return


class _DQSettings(utils.SettingRecord):

    def __init__(self, lastVisitedDQTabIdx=None, premMissionsTabDiscovered=False, *args, **kwargs):
        super(_DQSettings, self).__init__(lastVisitedDQTabIdx=lastVisitedDQTabIdx, premMissionsTabDiscovered=premMissionsTabDiscovered)
        return

    def setLastVisitedDQTab(self, lastVisitedDQTabIdx):
        self.update(lastVisitedDQTabIdx=lastVisitedDQTabIdx)
        return

    def onPremMissionsTabDiscovered(self):
        self.update(premMissionsTabDiscovered=True)
        return


class _DogTagsRootSettings(utils.SettingRootRecord):

    def __init__(self, lastVisitedDogTagsTabIdx=None, onboardingEnabled=True, seenComps=None, selectedAnimated=None, selectedCustomizable=None, animatedDogTagsVisited=False, customizableDogTagsVisited=False):
        super(_DogTagsRootSettings, self).__init__(lastVisitedDogTagsTabIdx=lastVisitedDogTagsTabIdx, onboardingEnabled=onboardingEnabled, seenComps=seenComps or set(), selectedAnimated=selectedAnimated or [], selectedCustomizable=selectedCustomizable or [], animatedDogTagsVisited=animatedDogTagsVisited, customizableDogTagsVisited=customizableDogTagsVisited)
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

    def setSelectedAnimated(self, selectedAnimated):
        self.update(selectedAnimated=selectedAnimated)
        return

    def setSelectedCustomizable(self, selectedCustomizable):
        self.update(selectedCustomizable=selectedCustomizable)
        return

    def setAnimatedDogTagsVisited(self, animatedDogTagsVisited):
        self.update(animatedDogTagsVisited=animatedDogTagsVisited)
        return

    def setCustomizableDogTagsVisited(self, customizableDogTagsVisited):
        self.update(customizableDogTagsVisited=customizableDogTagsVisited)
        return

    @classmethod
    def _getSettingName(cls):
        return DOG_TAGS


class _WotPlusSettings(utils.SettingRootRecord):

    def __init__(self, isFirstTime=True, isWotPlusEnabled=False, isGoldReserveEnabled=False, isPassiveXpEnabled=False, isFreeDemountingEnabled=False, isExcludedMapEnabled=False, isDailyAttendancesEnabled=False, amountOfDailyAttendance=0, isBattleBonusesEnabled=False, isBadgesEnabled=False, isAdditionalXPEnabled=False, isOptionalDevicesAssistantEnabled=False, isCrewAssistantEnabled=False, isServiceRecordCustomizationEnabled=False, isProBoostEnabled=False, isBattlePassEnabled=False, **_):
        super(_WotPlusSettings, self).__init__(isFirstTime=isFirstTime, isWotPlusEnabled=isWotPlusEnabled, isGoldReserveEnabled=isGoldReserveEnabled, isPassiveXpEnabled=isPassiveXpEnabled, isFreeDemountingEnabled=isFreeDemountingEnabled, isExcludedMapEnabled=isExcludedMapEnabled, isDailyAttendancesEnabled=isDailyAttendancesEnabled, amountOfDailyAttendance=amountOfDailyAttendance, isBattleBonusesEnabled=isBattleBonusesEnabled, isBadgesEnabled=isBadgesEnabled, isAdditionalXPEnabled=isAdditionalXPEnabled, isOptionalDevicesAssistantEnabled=isOptionalDevicesAssistantEnabled, isCrewAssistantEnabled=isCrewAssistantEnabled, isServiceRecordCustomizationEnabled=isServiceRecordCustomizationEnabled, isProBoostEnabled=isProBoostEnabled, isBattlePassEnabled=isBattlePassEnabled)
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

    def setDailyAttendancesState(self, isEnabled):
        self.update(isDailyAttendancesEnabled=isEnabled)
        return

    def setAmountOfDailyAttendance(self, amount):
        self.update(amountOfDailyAttendance=amount)
        return

    def increaseDailyAttendance(self):
        self.setAmountOfDailyAttendance(self.get(b'amountOfDailyAttendance', 0) + 1)
        return

    def setBattleBonusesState(self, isEnabled):
        self.update(isBattleBonusesEnabled=isEnabled)
        return

    def setBadgesEnabled(self, isEnabled):
        self.update(isBadgesEnabled=isEnabled)
        return

    def setAdditionalXPEnabled(self, isEnabled):
        self.update(isAdditionalXPEnabled=isEnabled)
        return

    def setOptionalDevicesAssistantEnabled(self, isEnabled):
        self.update(isOptionalDevicesAssistantEnabled=isEnabled)
        return

    def setCrewAssistantEnabled(self, isEnabled):
        self.update(isCrewAssistantEnabled=isEnabled)
        return

    def setServiceRecordCustomizationEnabled(self, isEnabled):
        self.update(isServiceRecordCustomizationEnabled=isEnabled)
        return

    def setProBoostEnabled(self, isEnabled):
        self.update(isProBoostEnabled=isEnabled)
        return

    def setBattlePassEnabled(self, isEnabled):
        self.update(isBattlePassEnabled=isEnabled)
        return

    @classmethod
    def _getSettingName(cls):
        return WOT_PLUS


class _PersonalReservesSettings(utils.SettingRootRecord):

    def __init__(self, isFirstTimeNotificationShown=False, isIntroPageShown=False, boosterCardHintsSeen=None, **_):
        super(_PersonalReservesSettings, self).__init__(isFirstTimeNotificationShown=isFirstTimeNotificationShown, isIntroPageShown=isIntroPageShown, boosterCardHintsSeen=boosterCardHintsSeen or set())
        return

    def setIsFirstTimeNotificationShown(self, isFirstTimeNotificationShown):
        self.update(isFirstTimeNotificationShown=isFirstTimeNotificationShown)
        return

    def setIsIntroPageShown(self, isIntroPageShown):
        self.update(isIntroPageShown=isIntroPageShown)
        return

    def addBoosterToCardHintsSeen(self, boosterID):
        self[b'boosterCardHintsSeen'].add(boosterID)
        return

    def clearCardHintsSeen(self):
        self.update(boosterCardHintsSeen=set())
        return

    @classmethod
    def _getSettingName(cls):
        return PERSONAL_RESERVES


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


class _CommendationsSettings(utils.SettingRootRecord):

    def __init__(self, isMessagesEnable=True, isLiveTagsEnable=True):
        super(_CommendationsSettings, self).__init__(isMessagesEnable=isMessagesEnable, isLiveTagsEnable=isLiveTagsEnable)
        return

    def setMessageEnable(self, isEnable):
        self.update(isMessagesEnable=isEnable)
        return

    def setLiveTagsEnable(self, isEnable):
        self.update(isLiveTagsEnable=isEnable)
        return

    @classmethod
    def _getSettingName(cls):
        return COMMENDATIONS


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
    if svrEvent.isAvailable()[0]:
        setting = b'visited'
    else:
        setting = b'naVisited'
    return settings is not None and svrEvent.getID() not in settings[setting] and not svrEvent.isCompleted() and not svrEvent.isOutOfDate()


def isGroupMinimized(groupID, settings=None):
    settings = settings or get()
    return groupID in settings[b'minimized']


def getNewCommonEvents(events):
    settings = get()
    return [e for e in events if isNewCommonEvent(e, settings)]


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def visitEventGUI(event, counters=(), eventsCache=None):
    if event is None:
        return
    else:
        s = get()
        isNaVisitedChanged = s.updateVisited(b'naVisited', event.getID())
        if event.isAvailable()[0]:
            isVisitedChanged = s.updateVisited(b'visited', event.getID())
        else:
            isVisitedChanged = False
        if isNaVisitedChanged or isVisitedChanged:
            s.save()
            converted = {}
            for counter in counters:
                key, value = counter(eventsCache)
                converted[key] = value

            eventsCache.onEventsVisited(converted)
        return


def visitEventsGUI(events):
    if events:
        for event in events:
            visitEventGUI(event)

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
    s.removeCompleted(set(e.getID() for e in svrEvents.itervalues() if e.isCompleted()))
    s.save()
    return


def _updatePMSettings(**kwargs):
    settings = get()
    settings.personalMissions.update(**kwargs)
    settings.save()
    return


def isPMOperationNew(operationID, pmSettings=None):
    pqSettings = pmSettings or get()
    return operationID not in pqSettings.personalMissions.operationsVisited


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


def getPersonalReservesSettings():
    return _PersonalReservesSettings.load()


@contextmanager
def personalReservesSettings():
    s = getPersonalReservesSettings()
    yield s
    s.save()
    return


def getCommendationsSettings():
    return _CommendationsSettings.load()


@contextmanager
def commendationsSettings():
    s = getCommendationsSettings()
    yield s
    s.save()
    return
