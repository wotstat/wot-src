import itertools
from collections import defaultdict
import BigWorld
from constants import ARENA_BONUS_TYPE
from gui import GUI_NATIONS
from gui.shared.utils import mapTextureToTheMemory, removeTextureFromMemory
from shared_utils import findFirst, CONST_CONTAINER
from debug_utils import LOG_ERROR, LOG_WARNING
from items import parseIntCompactDescr
from gui.event_boards import event_boards_timer
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER
from helpers import time_utils
from gui.Scaleform.locale.RES_ICONS import RES_ICONS

class CALCULATION_METHODS(CONST_CONTAINER):
    MAX = b'max'
    SUMN = b'sumN'
    SUMSEQN = b'sumSeqN'
    SUMALL = b'sumAll'
    SUMMSEQN = b'sumMSeqN'
    BATTLECOUNTSTAT3 = b'battleCountStat3'


class OBJECTIVE_PARAMETERS(CONST_CONTAINER):
    ORIGINALXP = b'originalXP'
    XP = b'xp'
    DAMAGEDEALT = b'damageDealt'
    DAMAGEASSISTED = b'damageAssisted'
    WINS = b'wins'


class EVENT_TYPE(CONST_CONTAINER):
    VEHICLE = b'vehicle'
    NATION = b'nation'
    LEVEL = b'level'
    CLASS = b'class'
    TEAMS = b'teams'
    ROLE = b'role'


class EVENT_STATE(CONST_CONTAINER):
    UNDEFINED = 0
    JOINED = 1
    CANCELED = 2


class PLAYER_STATE_REASON(CONST_CONTAINER):
    BYWINRATE = 1
    BYAGE = 2
    BYBATTLESCOUNT = 3
    BYBAN = 4
    WASUNREGISTERED = 5
    SPECIALACCOUNT = 6
    VEHICLESMISSING = 7


class SET_DATA_STATUS_CODE(CONST_CONTAINER):
    OK = 0
    ERROR = 1
    RETURN = 2


class EVENTS_ERROR_CODE(CONST_CONTAINER):
    GET_DATA = 0
    JOIN = 1
    LEAVE = 2


class EVENT_DATE_TYPE(CONST_CONTAINER):
    PUBLISH = 0
    START = 1
    END = 2
    PARTICIPANTS_FREEZE = 3
    REWARDING = 4


EVENTS_TYPES = EVENT_TYPE.ALL()
WOODEN_RIBBON = 5

class EventBoardsSettings(object):

    def __init__(self):
        self.__eventsSettings = EventsSettings()
        self.__playerEventsData = PlayerEventsData()
        self.__myEventsTop = MyEventsTop()
        return

    def getPlayerEventsData(self):
        return self.__playerEventsData

    def getEventsSettings(self):
        return self.__eventsSettings

    def getMyEventsTop(self):
        return self.__myEventsTop

    def hasEvents(self):
        eventsSettings = self.__eventsSettings.getEvents()
        return eventsSettings and len(eventsSettings)

    def fini(self):
        self.__eventsSettings.fini()
        return

    def cleanEventsData(self):
        self.__eventsSettings.cleanData()
        self.__playerEventsData.cleanData()
        self.__myEventsTop.cleanData()
        return


class EventsSettings(object):
    EXPECTED_FIELDS = [
     0, 1, 2, 3, 4, 5, 
     6, 7, 8, 9, 10, 
     11, 
     12, 13, 14, 15, 16]
    EXPECTED_FIELDS_PRIME_TIMES = [b'server', b'start_time', b'end_time']
    EXPECTED_FIELDS_LIMITS = [20, 21, 22, 23, 
     24, 25, 26, 27, 28]
    EXPECTED_FIELDS_REWARDS_CATEGORIES = [b'leaderboard_id', b'categories']
    EXPECTED_FIELDS_REWARDS_CATEGORIES_CATEGORY = [b'rank_min', b'rank_max', b'reward_category_number']
    EXPECTED_FIELDS_REWARDS_BY_RANK = [b'leaderboard_id', b'reward_groups']
    EXPECTED_FIELDS_REWARDS_BY_RANK_GROUP = [b'reward_category_number', b'rank_min', b'rank_max', b'rewards']
    EXPECTED_FIELDS_METHOD = [b'name']

    def __init__(self):
        self.__events = []
        return

    def fini(self):
        for event in self.__events:
            event.removeImages()

        return

    def cleanData(self):
        for event in self.__events:
            event.removeImages()

        self.__events = []
        return

    def setData(self, rawData, prefetchKeyArtBig=True):
        oldEvents = {event.getEventID(): event for event in self.__events}
        self.__events = []
        if not self.__isDataStructureValid(rawData):
            if rawData:
                LOG_WARNING(b'EventsSettings setData error: data structure error')
            return SET_DATA_STATUS_CODE.ERROR
        else:
            for event in rawData:
                eventSettings = EventSettings()
                eventSettings.setData(event)
                oldEvent = oldEvents.pop(eventSettings.getEventID(), None)
                eventSettings.setImages(oldEvent.getImages() if oldEvent else {}, prefetchKeyArtBig)
                self.__events.append(eventSettings)

            for event in oldEvents.values():
                event.removeImages()

            return SET_DATA_STATUS_CODE.OK

    def getEvents(self):
        return self.__events

    def getEvent(self, eventId):
        for event in self.__events:
            if event.getEventID() == eventId:
                return event

        return

    def getEventForVehicle(self, vehCD):
        for event in self.__events:
            if vehCD in event.getLimits().getVehiclesWhiteList():
                return event

        return

    def hasActiveEvents(self):
        for event in self.__events:
            if event.isActive():
                return True

        return False

    def hasAnotherActiveEvents(self, eventID):
        for event in self.__events:
            if event.isActive() and event.getEventID() != eventID:
                return True

        return False

    def hasActiveEventsByState(self, hangarFlagData):
        if hangarFlagData is not None:
            for eID, eState in hangarFlagData.items():
                event = self.getEvent(eID)
                if event is not None:
                    regIsFailed = event.isRegistrationFinished() and eState != EVENT_STATE.JOINED
                    if event.isActive() and eState != EVENT_STATE.CANCELED and not regIsFailed:
                        return True

        return False

    def __isDataStructureValid(self, data):
        if not data:
            return False
        for item in data:
            if not isDataSchemaValid(self.EXPECTED_FIELDS, item):
                return False
            for primeTimeItem in item[b'prime_times']:
                if not isDataSchemaValid(self.EXPECTED_FIELDS_PRIME_TIMES, primeTimeItem):
                    return False

            if not isDataSchemaValid(self.EXPECTED_FIELDS_METHOD, item[b'method']):
                return False
            if not isDataSchemaValid(self.EXPECTED_FIELDS_LIMITS, item[b'limits']):
                return False
            for rewardsByRank in item[b'rewards_by_rank']:
                if not isDataSchemaValid(self.EXPECTED_FIELDS_REWARDS_BY_RANK, rewardsByRank):
                    return False
                for rGroup in rewardsByRank[b'reward_groups']:
                    if not isDataSchemaValid(self.EXPECTED_FIELDS_REWARDS_BY_RANK_GROUP, rGroup):
                        return False

        return True


class EventSettings(object):
    __mapping = {(EVENT_TYPE.VEHICLE): (b'vehicles', b'vehicles', None), 
       (EVENT_TYPE.NATION): (
                           b'nations', b'nation', GUI_NATIONS), 
       (EVENT_TYPE.LEVEL): (
                          b'vehicles_levels', b'level', range(1, 11)), 
       (EVENT_TYPE.CLASS): (
                          b'vehicles_classes', b'class', VEHICLE_TYPES_ORDER), 
       (EVENT_TYPE.TEAMS): (b'teams', b'team', None), 
       (EVENT_TYPE.ROLE): (b'roles', b'role', None)}
    __CUSTOM_UI_BATTLE_TYPES = (
     ARENA_BONUS_TYPE.COMP7,)
    EVENT_DAYS_LEFT_TO_START = 5
    EVENT_FINISHED_DURATION = 5 * time_utils.ONE_DAY
    EVENT_STARTED_DURATION_PERCENTAGE = 0.1
    EVENT_TO_END_DATA_DURATION_PERCENTAGE = 0.1

    def __init__(self):
        self.__eventID = None
        self.__name = None
        self.__type = None
        self.__objectiveParameter = None
        self.__method = Method()
        self.__publishDate = None
        self.__startDate = None
        self.__participantsFreezeDeadline = None
        self.__endDate = None
        self.__rewardingDate = None
        self.__manual = None
        self.__battleType = None
        self.__isSquadAllowed = None
        self.__pageSize = None
        self.__leaderboardViewSize = None
        self.__primeTimes = PrimeTimes()
        self.__limits = Limits()
        self.__rewardsByRank = RewardsByRank()
        self.__keyArtBig = None
        self.__keyArtSmall = None
        self.__promoBonuses = None
        self.__leaderboards = {}
        self.__leaderboardsIndex = {}
        self.__images = {}
        return

    def setImages(self, images, prefetchKeyArtBig):
        self.__images = images
        self.__prefetchImages(prefetchKeyArtBig)
        return

    def getImages(self):
        return self.__images

    def removeImages(self):
        for image in self.__images.values():
            if image:
                removeTextureFromMemory(image)

        return

    def setData(self, rawData):
        self.__eventID = rawData[b'event_id']
        self.__name = rawData[b'name']
        self.__type = rawData[b'type']
        self.__objectiveParameter = rawData[b'objective_parameter']
        self.__method.setData(rawData[b'method'])
        self.__publishDate = rawData[b'publish_date']
        self.__startDate = rawData[b'start_date']
        self.__participantsFreezeDeadline = rawData[b'participants_freeze_deadline']
        self.__endDate = rawData[b'end_date']
        self.__rewardingDate = rawData[b'rewarding_date']
        self.__manual = rawData[b'manual']
        self.__battleType = rawData[b'battle_type']
        self.__isSquadAllowed = rawData[b'is_squad_allowed']
        self.__pageSize = rawData[b'leaderboard_page_size']
        self.__leaderboardViewSize = rawData[b'leaderboard_view_size']
        self.__limits.setData(rawData[b'limits'])
        self.__primeTimes.setData(rawData[b'prime_times'])
        self.__rewardsByRank.setData(rawData[b'rewards_by_rank'])
        self.__keyArtBig = rawData.get(b'key_art_big')
        self.__keyArtSmall = rawData.get(b'key_art_small')
        self.__promoBonuses = rawData.get(b'promo_bonuses')
        self.__makeLeaderboards(rawData[b'limits'])
        return

    def getLeaderboards(self):
        if self.__type in self.__mapping:
            _, _, order = self.__mapping[self.__type]
            if order:
                inversed = self.__leaderboardsIndex
                return [(inversed[value], value) for value in order if value in inversed]
        return self.__leaderboards.items()

    def getLeaderboard(self, leaderboardID):
        return self.__leaderboards.get(leaderboardID)

    def getLeaderboardID(self, value):
        return self.__leaderboardsIndex.get(value)

    def getEventID(self):
        return self.__eventID

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getObjectiveParameter(self):
        return self.__objectiveParameter

    def getMethod(self):
        return self.__method.getName()

    def getPublishDate(self):
        return self.__publishDate

    def getStartDate(self):
        return self.__startDate

    def getStartDateTs(self):
        return event_boards_timer.getTimeStampFromDate(self.__startDate)

    def isAtBeginning(self):
        startTs = self.getStartDateTs()
        duration = (self.getEndDateTs() - startTs) * self.EVENT_STARTED_DURATION_PERCENTAGE
        passed = event_boards_timer.getCurrentUTCTimeTs() - startTs
        return 0 < passed < duration

    def isAfterEnd(self):
        passed = event_boards_timer.getCurrentUTCTimeTs() - self.getEndDateTs()
        return 0 < passed < self.EVENT_FINISHED_DURATION

    def getParticipantsFreezeDeadline(self):
        return self.__participantsFreezeDeadline

    def getParticipantsFreezeDeadlineTs(self):
        return event_boards_timer.getTimeStampFromDate(self.__participantsFreezeDeadline)

    def getEndDate(self):
        return self.__endDate

    def getEndDateTs(self):
        return event_boards_timer.getTimeStampFromDate(self.__endDate)

    def getFormattedRemainingTime(self, dateType):
        if dateType == EVENT_DATE_TYPE.PUBLISH:
            return event_boards_timer.getFormattedRemainingTime(self.__publishDate)
        if dateType == EVENT_DATE_TYPE.START:
            return event_boards_timer.getFormattedRemainingTime(self.__startDate)
        if dateType == EVENT_DATE_TYPE.PARTICIPANTS_FREEZE:
            return event_boards_timer.getFormattedRemainingTime(self.__participantsFreezeDeadline)
        if dateType == EVENT_DATE_TYPE.END:
            return event_boards_timer.getFormattedRemainingTime(self.__endDate)
        if dateType == EVENT_DATE_TYPE.REWARDING:
            return event_boards_timer.getFormattedRemainingTime(self.__rewardingDate)
        return event_boards_timer.getFormattedRemainingTime(b'')

    def isStarted(self):
        value, _ = event_boards_timer.getTimeStatus(self.__startDate)
        return value < 0

    def isRegistrationFinished(self):
        value, _ = event_boards_timer.getTimeStatus(self.__participantsFreezeDeadline)
        return value < 0

    def isFinished(self):
        value, _ = event_boards_timer.getTimeStatus(self.__endDate)
        return value < 0

    def isStartSoon(self):
        value, period = event_boards_timer.getTimeStatus(self.__startDate)
        if period == event_boards_timer.FORMAT_DAY_STR:
            return self.EVENT_DAYS_LEFT_TO_START > value > 0
        return value > 0

    def isEndSoon(self):
        return event_boards_timer.isPeriodCloseToEnd(self.__startDate, self.__endDate, self.EVENT_TO_END_DATA_DURATION_PERCENTAGE)

    def isRegistrationFinishSoon(self):
        return event_boards_timer.isPeriodCloseToEnd(self.__startDate, self.__participantsFreezeDeadline, self.EVENT_TO_END_DATA_DURATION_PERCENTAGE)

    def isActive(self):
        value1, _ = event_boards_timer.getTimeStatus(self.__startDate)
        value2, _ = event_boards_timer.getTimeStatus(self.__endDate)
        return value1 < 0 < value2

    def getRewardingDate(self):
        return self.__rewardingDate

    def getCardinality(self):
        return self.__method.getCardinality()

    def getDistance(self):
        return self.__method.getDistance()

    def getManual(self):
        return self.__manual

    def getBattleType(self):
        return self.__battleType

    def getIsSquadAllowed(self):
        return self.__isSquadAllowed

    def getLeaderboardViewSize(self):
        return self.__leaderboardViewSize

    def getPageSize(self):
        return self.__pageSize

    def getLimits(self):
        return self.__limits

    def getPrimeTimes(self):
        return self.__primeTimes

    def getRewardsByRank(self):
        return self.__rewardsByRank

    def isAvailableServer(self, peripheryID):
        if self.__primeTimes.isEmpty():
            return True
        else:
            return findFirst((lambda pt: pt.isActive() and pt.getServer() == str(peripheryID)), self.__primeTimes.getPrimeTimes(), None) is not None

    def getAvailableServers(self):
        return [pt for pt in self.__primeTimes.getPrimeTimes() if pt.isActive()]

    def getKeyArtBig(self):
        return self.__getImage(self.__keyArtBig, RES_ICONS.MAPS_ICONS_EVENTBOARDS_BLANK_EVENT_BGR_LANDING_BLANK)

    def getKeyArtSmall(self):
        return self.__getImage(self.__keyArtSmall, RES_ICONS.MAPS_ICONS_EVENTBOARDS_BLANK_TOOLTIP_BACKGROUND_BLANK)

    def getPromoBonuses(self):
        return self.__getImage(self.__promoBonuses, RES_ICONS.MAPS_ICONS_EVENTBOARDS_BLANK_EVENT_PROMO_REWARD_BLANK)

    def hasCustomUI(self):
        return self.__battleType in self.__CUSTOM_UI_BATTLE_TYPES

    def __requestImage(self, url):
        bwPlayer = BigWorld.player()
        if url and bwPlayer:
            bwPlayer.customFilesCache.get(url, self.__onImageReceive)
        return

    def __onImageReceive(self, url, img):
        if img:
            self.__images[url] = mapTextureToTheMemory(img, temp=False)
        return

    def __getImage(self, url, default):
        if url not in self.__images:
            self.__requestImage(url)
            return default
        return (b'img://{}').format(self.__images[url])

    def __prefetchImages(self, prefetchKeyArtBig):
        if prefetchKeyArtBig:
            self.getKeyArtBig()
        self.getKeyArtSmall()
        self.getPromoBonuses()
        return

    def __makeLeaderboards(self, rawData):
        self.__leaderboards = {}
        self.__leaderboardsIndex = {}
        if self.__type in self.__mapping:
            listKey, itemKey, _ = self.__mapping[self.__type]
            leaderboards = rawData[listKey]
            if leaderboards is not None:
                for leaderboard in leaderboards:
                    key = int(leaderboard[b'leaderboard_id'])
                    val = leaderboard[itemKey]
                    if isinstance(val, list):
                        val = val[0]
                    self.__leaderboards[key] = val
                    self.__leaderboardsIndex[val] = key

        else:
            LOG_WARNING(b'__makeLeaderboards: Unknown event type')
        return


class PrimeTimes(object):

    def __init__(self):
        self.__primeTimes = None
        return

    def setData(self, data):
        if data is not None:
            self.__primeTimes = []
            for serverData in data:
                primeTime = PrimeTime()
                primeTime.setData(serverData)
                self.__primeTimes.append(primeTime)

        return

    def getPrimeTimes(self):
        return self.__primeTimes

    def isEmpty(self):
        return len(self.__primeTimes) is 0


class PrimeTime(object):

    def __init__(self):
        self.__server = None
        self.__startTime = None
        self.__endTime = None
        return

    def setData(self, data):
        self.__server = data[b'server']
        self.__startTime = data[b'start_time']
        self.__endTime = data[b'end_time']
        return

    def getServer(self):
        return self.__server

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def getStartLocalTime(self):
        return event_boards_timer.getPeripheryTime(self)[0]

    def getEndLocalTime(self):
        return event_boards_timer.getPeripheryTime(self)[1]

    def isActive(self):
        return event_boards_timer.isPeripheryActiveAtCurrentMoment(self)[0]

    def timeToActive(self):
        return event_boards_timer.isPeripheryActiveAtCurrentMoment(self)[1]


class Method(object):

    def __init__(self):
        self.__cardinality = None
        self.__distance = None
        self.__name = None
        return

    def setData(self, data):
        self.__cardinality = data.get(b'cardinality', None)
        self.__distance = data.get(b'distance', None)
        self.__name = data[b'name']
        return

    def getCardinality(self):
        return self.__cardinality

    def getDistance(self):
        return self.__distance

    def getName(self):
        return self.__name


class Limits(object):

    def __init__(self):
        self.__winRateMin = None
        self.__winRateMax = None
        self.__registrationDateMax = None
        self.__isRegistrationNeeded = None
        self.__battlesCountMin = None
        self.__vehicles = {}
        self.__nations = None
        self.__vehiclesLevels = None
        self.__vehiclesClasses = None
        return

    def setData(self, data):
        self.__winRateMin = data[b'win_rate_min']
        self.__winRateMax = data[b'win_rate_max']
        self.__registrationDateMax = data[b'registration_date_max']
        self.__isRegistrationNeeded = data[b'is_registration_needed']
        self.__battlesCountMin = data[b'battles_count_min']
        self.__vehicles = {}
        if data[b'vehicles'] is not None:
            for leaderboard in data[b'vehicles']:
                self.__vehicles[int(leaderboard[b'leaderboard_id'])] = [vehicle for vehicle in leaderboard[b'vehicles'] if self.__doesVehicleExist(vehicle)]

        if data[b'nations'] is not None:
            self.__nations = []
            for nation in data[b'nations']:
                self.__nations.append(nation[b'nation'])

        if data[b'vehicles_levels'] is not None:
            self.__vehiclesLevels = []
            for vehicleLevels in data[b'vehicles_levels']:
                self.__vehiclesLevels.append(vehicleLevels[b'levels'])

        if data[b'vehicles_classes'] is not None:
            self.__vehiclesClasses = []
            for vehicleClasses in data[b'vehicles_classes']:
                self.__vehiclesClasses.append(vehicleClasses[b'class'])

        return

    def getWinRateMin(self):
        return self.__winRateMin

    def getWinRateMax(self):
        return self.__winRateMax

    def getRegistrationDateMax(self):
        return self.__registrationDateMax

    def getRegistrationDateMaxTs(self):
        return event_boards_timer.getTimeStampFromDate(self.__registrationDateMax)

    def getIsRegistrationNeeded(self):
        return self.__isRegistrationNeeded

    def getBattlesCountMin(self):
        return self.__battlesCountMin

    def getVehicles(self, leaderboardID):
        return self.__vehicles.get(leaderboardID)

    def getNations(self):
        return self.__nations

    def getVehiclesLevels(self):
        return self.__vehiclesLevels

    def getVehiclesClasses(self):
        return self.__vehiclesClasses

    def getVehiclesWhiteList(self):
        return tuple(set(itertools.chain(*self.__vehicles.itervalues())))

    def __doesVehicleExist(self, vehIntCD):
        itemTypeID, _, _ = parseIntCompactDescr(vehIntCD)
        if itemTypeID == GUI_ITEM_TYPE.VEHICLE:
            return True
        return False


class RewardsByRank(object):

    def __init__(self):
        self.__rewardsByRank = None
        return

    def setData(self, data):
        if data is not None:
            self.__rewardsByRank = []
            for reward in data:
                rewardByRank = RewardByRank()
                rewardByRank.setData(reward)
                self.__rewardsByRank.append(rewardByRank)

        return

    def getRewardsByRank(self):
        return self.__rewardsByRank

    def getRewardByRank(self, leaderboardID):
        try:
            return next(itertools.ifilter((lambda l: l.getLeaderboardID() is leaderboardID), self.__rewardsByRank))
        except StopIteration:
            LOG_ERROR(b'leaderboardID not found in data. leaderboardID=', leaderboardID)
            return

        return


class RewardByRank(object):

    def __init__(self):
        self.__leaderboardID = None
        self.__rewardGroups = None
        return

    def setData(self, rawData):
        if rawData is not None:
            self.__leaderboardID = int(rawData[b'leaderboard_id'])
            self.__rewardGroups = []
            for rewardGroup in rawData[b'reward_groups']:
                rewardGroupItem = RewardGroups()
                rewardGroupItem.setData(rewardGroup)
                self.__rewardGroups.append(rewardGroupItem)

        return

    def getLeaderboardID(self):
        return self.__leaderboardID

    def getRewardGroups(self):
        return self.__rewardGroups

    def getRewardCategoryNumber(self, myPosition):
        if myPosition is not None and self.__rewardGroups is not None:
            for group in self.__rewardGroups:
                minPos, maxPos = group.getRankMinMax()
                if minPos <= myPosition <= maxPos:
                    return group.getRewardCategoryNumber()

        return

    def getCategoryMinMax(self, category):
        groups = [g for g in self.__rewardGroups if g.getRewardCategoryNumber() is category]
        minimum = min(groups, key=(lambda group: group.getRankMinMax()[0]))
        maximum = max(groups, key=(lambda group: group.getRankMinMax()[1]))
        return (minimum.getRankMinMax()[0], maximum.getRankMinMax()[1])


class RewardGroups(object):

    def __init__(self):
        self.__rewardCategoryNumber = None
        self.__rankMin = None
        self.__rankMax = None
        self.__rewards = []
        return

    def setData(self, data):
        if data is not None:
            from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import convertRewardsDictToBonusObjects
            self.__rewardCategoryNumber = data[b'reward_category_number']
            self.__rewards = convertRewardsDictToBonusObjects(data, b'rewards')
            self.__rankMin = data[b'rank_min']
            self.__rankMax = data[b'rank_max']
        return

    def getRewards(self):
        return self.__rewards

    def getRewardCategoryNumber(self):
        return self.__rewardCategoryNumber

    def getRankMinMax(self):
        return (
         self.__rankMin, self.__rankMax)


class RewardGroup(object):

    def __init__(self):
        self.__rewardType = None
        self.__rewardsAmount = None
        return

    def setData(self, data):
        self.__rewardType = data[b'reward_type']
        self.__rewardsAmount = data[b'rewards_amount']
        return

    def getRewardType(self):
        return self.__rewardType

    def getRewardsAmount(self):
        return self.__rewardsAmount


class PlayerEventsData(object):
    EXPECTED_FIELDS = [
     b'all_battles_count', b'win_rate', b'events_list']
    EXPECTED_FIELDS_EVENTS_LIST = [3, 4, 5, 6, 7]

    def __init__(self):
        self.__winRate = None
        self.__allBattlesCount = None
        self.__eventsList = None
        return

    def cleanData(self):
        self.__winRate = None
        self.__allBattlesCount = None
        self.__eventsList = []
        return

    def setData(self, rawData):
        if not self.__isDataStructureValid(rawData):
            if rawData:
                LOG_WARNING(b'PlayerEventsData setData error: data structure error')
            return SET_DATA_STATUS_CODE.ERROR
        self.__eventsList = []
        self.__winRate = rawData[b'win_rate']
        self.__allBattlesCount = rawData[b'all_battles_count']
        for eventData in rawData[b'events_list']:
            eventModel = EventsList()
            eventModel.setData(eventData)
            self.__eventsList.append(eventModel)

        return SET_DATA_STATUS_CODE.OK

    def clearData(self):
        self.__eventsList = None
        return

    def getWinRate(self):
        return self.__winRate

    def getBattlesCount(self):
        return self.__allBattlesCount

    def getPlayerStateByEventId(self, eventId):
        if self.__eventsList:
            for eventData in self.__eventsList:
                if eventData and eventData.getEventID() == eventId:
                    return eventData

        return

    def getEventsList(self):
        return self.__eventsList

    def __isDataStructureValid(self, data):
        if data and isDataSchemaValid(self.EXPECTED_FIELDS, data):
            for item in data[b'events_list']:
                if not isDataSchemaValid(self.EXPECTED_FIELDS_EVENTS_LIST, item):
                    return False

            return True
        return False


class EventsList(object):

    def __init__(self):
        self.__eventID = None
        self.__playerState = None
        self.__canJoin = None
        self.__playersInEvent = None
        self.__playerStateReasons = None
        return

    def setData(self, data):
        self.__eventID = data[b'event_id']
        self.__playerState = data[b'player_state']
        self.__canJoin = data[b'can_join']
        self.__playersInEvent = data[b'players_in_event']
        self.__playerStateReasons = data[b'player_state_reasons']
        return

    def updateStateReason(self, reason):
        self.__canJoin = False
        self.__playerStateReasons.append(reason)
        return

    def getEventID(self):
        return self.__eventID

    def getPlayerState(self):
        return self.__playerState

    def getCanJoin(self):
        return self.__canJoin

    def getPlayersInEvent(self):
        return self.__playersInEvent

    def getPlayerStateReasons(self):
        return self.__playerStateReasons


class MyEventsTop(object):
    EXPECTED_FIELDS = [
     b'data', b'event_id']
    EXPECTED_FIELDS_DATA = [b'meta', b'data']
    EXPECTED_FIELDS_ITEM_DATA = [3, 4, 5, 6, 
     7]
    EXPECTED_FIELDS_ITEM_META = [b'recalculation_interval', b'last_leaderboard_recalculation_ts',
     b'next_leaderboard_recalculation_ts']

    def __init__(self):
        self.__myEventsTopList = []
        self.__myEventsTopMeta = defaultdict()
        return

    def cleanData(self):
        self.__myEventsTopList = []
        self.__myEventsTopMeta = defaultdict()
        return

    def setData(self, data):
        if not self.__isDataStructureValid(data):
            if data:
                LOG_WARNING(b'MyEventsTop setData error: data structure error')
            return SET_DATA_STATUS_CODE.ERROR
        self.__myEventsTopList = []
        for eventTopData in data:
            dataItem = eventTopData[b'data']
            topMetaItem = TopMetaItem()
            topMetaItem.setData(dataItem[b'meta'])
            self.__myEventsTopMeta[eventTopData[b'event_id']] = topMetaItem
            for dataTopItem in dataItem[b'data']:
                topItem = TopItem()
                topItem.setData(dataTopItem, eventTopData[b'event_id'])
                self.__myEventsTopList.append(topItem)

        return SET_DATA_STATUS_CODE.OK

    def getMyEventsTopList(self):
        return self.__myEventsTopList

    def getMyEventTop(self, eventId):
        return [eventTop for eventTop in self.__myEventsTopList if eventTop.getEventID() == eventId]

    def getMyLeaderboardEventTop(self, eventId, leadeboardId):
        return findFirst((lambda eventTop: eventTop.getEventID() == eventId and eventTop.getLeaderboardID() == leadeboardId), self.__myEventsTopList, None)

    def getMyEventsTopMeta(self, eventID):
        return self.__myEventsTopMeta.get(eventID)

    def __isDataStructureValid(self, rawData):
        if not rawData:
            return False
        else:
            for data in rawData:
                if data is None:
                    return False
                if not isDataSchemaValid(self.EXPECTED_FIELDS, data):
                    return False
                itemData = data[b'data']
                if not isDataSchemaValid(self.EXPECTED_FIELDS_DATA, itemData):
                    return False
                if not isDataSchemaValid(self.EXPECTED_FIELDS_ITEM_META, itemData[b'meta']):
                    return False
                for dataItem in itemData[b'data']:
                    if not isDataSchemaValid(self.EXPECTED_FIELDS_ITEM_DATA, dataItem):
                        return False

            return True


class TopMetaItem(object):

    def __init__(self):
        self.__recalculationInterval = None
        self.__lastLeaderboardRecalculationTS = None
        self.__nextLeaderboardRecalculationTS = None
        return

    def setData(self, data):
        self.__recalculationInterval = data[b'recalculation_interval']
        self.__lastLeaderboardRecalculationTS = data[b'last_leaderboard_recalculation_ts']
        self.__nextLeaderboardRecalculationTS = data[b'next_leaderboard_recalculation_ts']
        return

    def getRecalculationInterval(self):
        return self.__recalculationInterval

    def getLastLeaderboardRecalculationTS(self):
        return self.__lastLeaderboardRecalculationTS

    def getNextLeaderboardRecalculationTS(self):
        return self.__nextLeaderboardRecalculationTS


class TopItem(object):

    def __init__(self):
        self.__eventID = None
        self.__leaderboardID = None
        self.__myPosition = None
        self.__battlesCount = None
        self.__myValue = None
        self.__lastInLeaderboardValue = None
        return

    def setData(self, data, eventID):
        self.__eventID = eventID
        self.__leaderboardID = int(data[b'leaderboard_id'])
        self.__myPosition = data[b'my_position']
        self.__battlesCount = data[b'battles_count']
        self.__myValue = data[b'my_value']
        self.__lastInLeaderboardValue = data[b'last_in_leaderboard_value']
        return

    def getLeaderboardID(self):
        return self.__leaderboardID

    def getMyPosition(self):
        return self.__myPosition

    def getBattlesCount(self):
        return self.__battlesCount

    def getMyValue(self):
        return self.__myValue

    def getLastInLeaderboardValue(self):
        return self.__lastInLeaderboardValue

    def getEventID(self):
        return self.__eventID


class MyInfoInLeaderBoard(object):
    EXPECTED_FIELDS = [
     0, 1, 2, 3, 4, 5, 6, 
     7, 8, 9]

    def __init__(self):
        self.__eventID = None
        self.__leaderboardID = None
        self.__rank = None
        self.__p1 = None
        self.__p2 = None
        self.__p3 = None
        self.__pageNumber = None
        self.__isInsideViewsize = None
        self.__lastInLeaderboardValue = None
        self.__battlesCount = None
        self.__clanTag = None
        self.__clanColor = None
        return

    def setData(self, rawData, eventID, leaderboardID):
        if not self.__isDataStructureValid(rawData):
            if rawData:
                LOG_WARNING(b'MyInfoInLeaderBoard setData error: data structure error')
            return SET_DATA_STATUS_CODE.ERROR
        self.__eventID = eventID
        self.__leaderboardID = leaderboardID
        self.__rank = rawData[b'rank']
        self.__p1 = rawData[b'p1']
        self.__p2 = rawData[b'p2']
        self.__p3 = rawData[b'p3']
        self.__pageNumber = rawData[b'page_number']
        self.__isInsideViewsize = rawData[b'is_inside_viewsize']
        self.__lastInLeaderboardValue = rawData[b'last_in_leaderboard_value']
        self.__battlesCount = rawData[b'battles_count']
        self.__clanTag = rawData[b'clan_tag']
        self.__clanColor = rawData[b'clan_color']
        return SET_DATA_STATUS_CODE.OK

    def getEventID(self):
        return self.__eventID

    def getLeaderboardID(self):
        return self.__leaderboardID

    def getRank(self):
        return self.__rank

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def getP3(self):
        return self.__p3

    def getPageNumber(self):
        return self.__pageNumber

    def getIsInsideViewsize(self):
        return self.__isInsideViewsize

    def getLastInLeaderboardValue(self):
        return self.__lastInLeaderboardValue

    def getBattlesCount(self):
        return self.__battlesCount

    def getClanTag(self):
        return self.__clanTag

    def getClanColor(self):
        return self.__clanColor

    def __isDataStructureValid(self, data):
        if data and isDataSchemaValid(self.EXPECTED_FIELDS, data):
            return True
        return False


class LeaderBoard(object):
    EXPECTED_FIELDS = [
     b'meta', b'data']
    EXPECTED_FIELDS_META = [2, 3, 4, 5, 
     6, 7]
    EXPECTED_FIELDS_DATA = [8, 9, 10, 11, 12, 13, 14, 15, 16]
    EXPECTED_FIELDS_META_REWARDS = [b'reward_category_number', b'page_number']
    CALCULATION_METHODS_EXPECTED_FIELDS = {(CALCULATION_METHODS.MAX): [
                                 18, 
                                 19, 20, 21, 
                                 22, 23, 
                                 24, 
                                 25, 26], 
       (CALCULATION_METHODS.SUMN): [
                                  18, 
                                  19, 20, 21, 
                                  22, 23, 
                                  24, 
                                  25], 
       (CALCULATION_METHODS.SUMSEQN): [
                                     18, 
                                     19, 20, 
                                     21, 22, 
                                     23, 
                                     24, 
                                     25], 
       (CALCULATION_METHODS.SUMALL): [
                                    b'avg_exp', b'avg_damage_dealt', b'avg_damage_assisted', b'win_rate'], 
       (CALCULATION_METHODS.SUMMSEQN): [
                                      18, 
                                      19, 
                                      20, 
                                      21, 
                                      22, 
                                      23, 
                                      24, 
                                      25, 
                                      31], 
       (CALCULATION_METHODS.BATTLECOUNTSTAT3): []}

    def __init__(self):
        self.__infoByType = {}
        self.__leaderboardID = None
        self.__leaderboardType = None
        self.__pageNumber = 1
        self.__pagesAmount = None
        self.__recalculationInterval = None
        self.__lastLeaderboardRecalculationTS = None
        self.__nextLeaderboardRecalculationTS = None
        self.__rewards = []
        self.__excelItems = []
        return

    def setData(self, rawData, leaderboardID, infoType, leaderboardType):
        if not self.__isDataStructureValid(rawData, infoType):
            if rawData:
                LOG_WARNING(b'LeaderBoard setData error: data structure error')
            return SET_DATA_STATUS_CODE.ERROR
        else:
            meta = rawData[b'meta']
            data = rawData[b'data']
            self.__infoByType = {}
            self.__leaderboardID = leaderboardID
            self.__leaderboardType = leaderboardType
            self.__pageNumber = meta[b'page_number']
            self.__pagesAmount = meta[b'pages_amount']
            self.__recalculationInterval = meta[b'recalculation_interval']
            self.__lastLeaderboardRecalculationTS = meta[b'last_leaderboard_recalculation_ts']
            self.__nextLeaderboardRecalculationTS = meta[b'next_leaderboard_recalculation_ts']
            rewardCategoryPage = 1
            self.__rewards = []
            for reward in meta[b'rewards']:
                rewardItem = RewardItem()
                rewardItem.setData(reward, rewardCategoryPage)
                rewardCategoryPage = reward[b'page_number']
                self.__rewards.append(rewardItem)

            if rewardCategoryPage is not None:
                rewardItem = RewardItem()
                rewardCat = defaultdict()
                rewardCat[b'reward_category_number'] = 5
                rewardItem.setData(rewardCat, rewardCategoryPage)
                self.__rewards.append(rewardItem)
            self.__excelItems = []
            for item in data:
                excelItem = ExcelItem()
                excelItem.setData(item, infoType)
                self.__excelItems.append(excelItem)

            return SET_DATA_STATUS_CODE.OK

    def getLeaderboardID(self):
        return self.__leaderboardID

    def getLeaderboardType(self):
        return self.__leaderboardType

    def getPageNumber(self):
        return self.__pageNumber

    def getPagesAmount(self):
        return self.__pagesAmount

    def getRewards(self):
        return self.__rewards

    def getExcelItems(self):
        return self.__excelItems

    def getRecalculationInterval(self):
        return self.__recalculationInterval

    def getLastLeaderboardRecalculationTS(self):
        return self.__lastLeaderboardRecalculationTS

    def getNextLeaderboardRecalculationTS(self):
        return self.__nextLeaderboardRecalculationTS

    def __isDataStructureValid(self, rawData, infoType):
        if not rawData or not isDataSchemaValid(self.EXPECTED_FIELDS, rawData):
            return False
        data = rawData[b'data']
        meta = rawData[b'meta']
        if not isDataSchemaValid(self.EXPECTED_FIELDS_META, meta):
            return False
        for rewardItem in meta[b'rewards']:
            if not isDataSchemaValid(self.EXPECTED_FIELDS_META_REWARDS, rewardItem):
                return False

        singleMethods = (
         CALCULATION_METHODS.MAX, CALCULATION_METHODS.SUMALL)
        if infoType in singleMethods:
            for dataItem in data:
                if not isDataSchemaValid(self.EXPECTED_FIELDS_DATA, dataItem):
                    return False
                if not isDataSchemaValid(self.CALCULATION_METHODS_EXPECTED_FIELDS[infoType], dataItem[b'info']):
                    return False

        else:
            for dataItem in data:
                if not isDataSchemaValid(self.EXPECTED_FIELDS_DATA, dataItem):
                    return False
                for infoItem in dataItem[b'info']:
                    if not isDataSchemaValid(self.CALCULATION_METHODS_EXPECTED_FIELDS[infoType], infoItem):
                        return False

        return True


class Comp7LeaderBoard(LeaderBoard):
    __CUSTOM_EXPECTED_FIELDS_META = [
     b'elite_rank_position_threshold', b'elite_rank_points_threshold', b'master_rank_position_threshold']
    EXPECTED_FIELDS_META = LeaderBoard.EXPECTED_FIELDS_META + __CUSTOM_EXPECTED_FIELDS_META

    def __init__(self):
        super(Comp7LeaderBoard, self).__init__()
        self.__lastEliteUserPosition = None
        self.__lastEliteUserRating = None
        self.__lastMasterRankPositionThreshold = None
        return

    def setData(self, rawData, leaderboardID, infoType, leaderboardType):
        result = super(Comp7LeaderBoard, self).setData(rawData, leaderboardID, infoType, leaderboardType)
        meta = rawData[b'meta']
        self.__lastEliteUserPosition = meta[b'elite_rank_position_threshold']
        self.__lastEliteUserRating = meta[b'elite_rank_points_threshold']
        self.__lastMasterRankPositionThreshold = meta[b'master_rank_position_threshold'] or 0
        return result

    def getRecordsCount(self):
        return self.__lastMasterRankPositionThreshold

    def getLastEliteUserPosition(self):
        return self.__lastEliteUserPosition

    def getLastEliteUserRating(self):
        return self.__lastEliteUserRating


class InfoItem(object):

    def __init__(self, methodType):
        self.__methodType = methodType
        return

    def getMethodType(self):
        return self.__methodType


class InfoMax(InfoItem):

    def __init__(self, methodType, data):
        super(InfoMax, self).__init__(methodType)
        self.__battleTs = data[b'battle_ts']
        self.__vehicleCd = data[b'vehicle_cd']
        self.__battleResult = data[b'battle_result']
        self.__isInSquad = data[b'is_in_squad']
        self.__exp = data[b'exp']
        self.__damage = data[b'damage']
        self.__assistedDamage = data[b'assisted_damage']
        self.__frags = data[b'frags']
        self.__blockedDamage = data[b'blocked_damage']
        return

    def getBattleTs(self):
        return self.__battleTs

    def getVehicleCd(self):
        return self.__vehicleCd

    def getBattleResult(self):
        return self.__battleResult

    def getIsInSquad(self):
        return self.__isInSquad

    def getExp(self):
        return self.__exp

    def getDamage(self):
        return self.__damage

    def getAssistedDamage(self):
        return self.__assistedDamage

    def getFrags(self):
        return self.__frags

    def getBlockedDamage(self):
        return self.__blockedDamage


class InfoSumM(InfoItem):

    def __init__(self, methodType, data):
        super(InfoSumM, self).__init__(methodType)
        self.__battleTs = data[b'battle_ts']
        self.__vehicleCd = data[b'vehicle_cd']
        self.__battleResult = data[b'battle_result']
        self.__isInSquad = data[b'is_in_squad']
        self.__exp = data[b'exp']
        self.__damage = data[b'damage']
        self.__assistedDamage = data[b'assisted_damage']
        self.__frags = data[b'frags']
        return

    def getBattleTs(self):
        return self.__battleTs

    def getVehicleCd(self):
        return self.__vehicleCd

    def getBattleResult(self):
        return self.__battleResult

    def getIsInSquad(self):
        return self.__isInSquad

    def getExp(self):
        return self.__exp

    def getDamage(self):
        return self.__damage

    def getAssistedDamage(self):
        return self.__assistedDamage

    def getFrags(self):
        return self.__frags


class InfoSumSeqN(InfoItem):

    def __init__(self, methodType, data):
        super(InfoSumSeqN, self).__init__(methodType)
        self.__battleTs = data[b'battle_ts']
        self.__vehicleCd = data[b'vehicle_cd']
        self.__battleResult = data[b'battle_result']
        self.__isInSquad = data[b'is_in_squad']
        self.__exp = data[b'exp']
        self.__damage = data[b'damage']
        self.__assistedDamage = data[b'assisted_damage']
        self.__frags = data[b'frags']
        return

    def getBattleTs(self):
        return self.__battleTs

    def getVehicleCd(self):
        return self.__vehicleCd

    def getBattleResult(self):
        return self.__battleResult

    def getIsInSquad(self):
        return self.__isInSquad

    def getExp(self):
        return self.__exp

    def getDamage(self):
        return self.__damage

    def getAssistedDamage(self):
        return self.__assistedDamage

    def getFrags(self):
        return self.__frags


class InfoSumAll(InfoItem):

    def __init__(self, methodType, data):
        super(InfoSumAll, self).__init__(methodType)
        self.__exp = data[b'avg_exp']
        self.__avgDamageDealt = data[b'avg_damage_dealt']
        self.__avgAssistedDamage = data[b'avg_damage_assisted']
        self.__winRate = data[b'win_rate']
        return

    def getExp(self):
        return self.__exp

    def getAvgDamageDealt(self):
        return self.__avgDamageDealt

    def getAvgAssistedDamage(self):
        return self.__avgAssistedDamage

    def getWinRate(self):
        return self.__winRate


class InfoSumMSeqN(InfoItem):

    def __init__(self, methodType, data):
        super(InfoSumMSeqN, self).__init__(methodType)
        self.__battleTs = data[b'battle_ts']
        self.__vehicleCd = data[b'vehicle_cd']
        self.__battleResult = data[b'battle_result']
        self.__isInSquad = data[b'is_in_squad']
        self.__exp = data[b'exp']
        self.__damage = data[b'damage']
        self.__assistedDamage = data[b'assisted_damage']
        self.__frags = data[b'frags']
        self.__usedInCalculations = data[b'used_in_calculations']
        return

    def getBattleTs(self):
        return self.__battleTs

    def getVehicleCd(self):
        return self.__vehicleCd

    def getBattleResult(self):
        return self.__battleResult

    def getIsInSquad(self):
        return self.__isInSquad

    def getExp(self):
        return self.__exp

    def getDamage(self):
        return self.__damage

    def getAssistedDamage(self):
        return self.__assistedDamage

    def getFrags(self):
        return self.__frags

    def getUsedInCalculations(self):
        return self.__usedInCalculations


CALCULATION_METHODS_TYPE = {(CALCULATION_METHODS.MAX): InfoMax, 
   (CALCULATION_METHODS.SUMN): InfoSumM, 
   (CALCULATION_METHODS.SUMSEQN): InfoSumSeqN, 
   (CALCULATION_METHODS.SUMALL): InfoSumAll, 
   (CALCULATION_METHODS.SUMMSEQN): InfoSumMSeqN}

class ExcelItem(object):

    def __init__(self):
        self.__spaId = None
        self.__name = None
        self.__clanTag = None
        self.__clanColor = None
        self.__rank = None
        self.__p1 = None
        self.__p2 = None
        self.__p3 = None
        self.__info = None
        return

    def setData(self, data, methodType):
        self.__spaId = data[b'spa_id']
        self.__name = data[b'name']
        self.__clanTag = data[b'clan_tag']
        self.__clanColor = data[b'clan_color']
        self.__rank = data[b'rank']
        self.__p1 = data[b'p1']
        self.__p2 = data[b'p2']
        self.__p3 = data[b'p3']
        if methodType in CALCULATION_METHODS_TYPE and b'info' in data:
            self.__setInfoData(methodType, data[b'info'])
        return

    def getSpaId(self):
        return self.__spaId

    def getName(self):
        return self.__name

    def getClanTag(self):
        return self.__clanTag

    def getClanColor(self):
        return self.__clanColor

    def getRank(self):
        return self.__rank

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def getP3(self):
        return self.__p3

    def getInfo(self):
        return self.__info

    def __setInfoData(self, methodType, data):
        singleMethods = (
         CALCULATION_METHODS.MAX, CALCULATION_METHODS.SUMALL)
        if methodType in singleMethods:
            self.__info = CALCULATION_METHODS_TYPE[methodType](methodType, data)
        else:
            self.__info = []
            for item in data:
                self.__info.append(CALCULATION_METHODS_TYPE[methodType](methodType, item))

        return


class RewardItem(object):

    def __init__(self):
        self.__pageNumber = None
        self.__rewardCategoryNumber = None
        return

    def setData(self, data, pageNumber):
        self.__pageNumber = pageNumber
        self.__rewardCategoryNumber = data[b'reward_category_number']
        return

    def getPageNumber(self):
        return self.__pageNumber

    def getRewardCategoryNumber(self):
        return self.__rewardCategoryNumber


class HangarFlagData(object):
    EXPECTED_FIELDS = [
     b'meta', b'data']
    EXPECTED_FIELDS_META = [b'is_special_account']
    EXPECTED_FIELDS_DATA = [b'event_id', b'player_state']

    def __init__(self):
        self.__isSpecialAccount = False
        self.__hangarFlags = defaultdict()
        return

    def cleanEventsData(self):
        self.__isSpecialAccount = False
        self.__hangarFlags.clear()
        return

    def setData(self, rawData):
        if not self.__isDataStructureValid(rawData):
            if rawData:
                LOG_WARNING(b'HangarFlagData setData error: data structure error')
            return SET_DATA_STATUS_CODE.ERROR
        self.__isSpecialAccount = rawData[b'meta'][b'is_special_account']
        self.__hangarFlags.clear()
        for event in rawData[b'data']:
            self.__hangarFlags[event[b'event_id']] = event[b'player_state']

        return SET_DATA_STATUS_CODE.OK

    def getHangarFlags(self):
        return self.__hangarFlags

    def isSpecialAccount(self):
        return self.__isSpecialAccount

    def isRegistered(self, eventID):
        playerEventState = self.__hangarFlags.get(eventID, None)
        if playerEventState is not None:
            return playerEventState == EVENT_STATE.JOINED
        else:
            return False

    def canJoin(self, eventID):
        playerEventState = self.__hangarFlags.get(eventID, None)
        if playerEventState is not None:
            return playerEventState == EVENT_STATE.UNDEFINED
        else:
            return False

    def wasCanceled(self, eventID):
        playerEventState = self.__hangarFlags.get(eventID, None)
        if playerEventState is not None:
            return playerEventState == EVENT_STATE.CANCELED
        else:
            return False

    def __isDataStructureValid(self, rawData):
        if rawData:
            if not isDataSchemaValid(self.EXPECTED_FIELDS, rawData):
                return False
            if not isDataSchemaValid(self.EXPECTED_FIELDS_META, rawData[b'meta']):
                return False
            for event in rawData[b'data']:
                if not isDataSchemaValid(self.EXPECTED_FIELDS_DATA, event):
                    return False

            return True
        return False


def isDataSchemaValid(expectedFields, data):
    if expectedFields is None or data is None:
        return False
    for field in expectedFields:
        if field not in data:
            return False

    return True
