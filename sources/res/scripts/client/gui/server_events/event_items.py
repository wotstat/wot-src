import operator, time
from abc import ABCMeta
from collections import namedtuple
import typing, constants, nations
from debug_utils import LOG_ERROR
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.Scaleform.locale.PERSONAL_MISSIONS_30 import PERSONAL_MISSIONS_30
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles.ranked_helpers import getQualificationBattlesCountFromID, isQualificationQuestID
from gui.server_events import events_helpers, finders
from gui.server_events.events_constants import BATTLE_MATTERS_QUEST_ID, BATTLE_MATTERS_INTERMEDIATE_QUEST_ID, BATTLE_MATTERS_COMPENSATION_QUEST_ID
from gui.server_events.bonuses import compareBonuses, getBonuses
from gui.server_events.events_helpers import isDailyQuest, isWeeklyQuest, isPremium, getIdxFromQuestID, WeeklyQuestInfo
from gui.server_events.formatters import getLinkedActionID
from gui.server_events.modifiers import compareModifiers, getModifierObj
from gui.server_events.parsers import AccountRequirements, BonusConditions, PostBattleConditions, PreBattleConditions, TokenQuestAccountRequirements, VehicleRequirements, MapsTrainingPostBattleConditions
from gui.shared.gui_items import Vehicle
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER
from gui.shared.system_factory import registerQuestBuilders
from gui.shared.utils import ValidationResult
from gui.shared.utils.requesters.QuestsProgressRequester import PersonalMissionsProgressRequester
from helpers import dependency, getLocalizedData, i18n, time_utils
from personal_missions import PM_BRANCH, PM_BRANCH_TO_FINAL_PAWN_COST, PM_FLAG, PM_STATE as _PMS
from personal_missions_config import getQuestConfig
from personal_missions_constants import DISPLAY_TYPE
from shared_utils import findFirst, first
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from gui.server_events.bonuses import SimpleBonus
from constants import QUEST_PROGRESS_STATE
if typing.TYPE_CHECKING:
    from typing import Dict, List, Union
    from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import EventPostBattleInfo
    import potapov_quests

class DEFAULTS_GROUPS(object):
    FOR_CURRENT_VEHICLE = b'currentlyAvailable'
    UNGROUPED_ACTIONS = b'ungroupedActions'
    UNGROUPED_QUESTS = b'ungroupedQuests'
    REGULAR_GROUPED_QUESTS = b'regularGroupedQuests'
    MOTIVE_QUESTS = b'motiveQuests'
    MARATHON_QUESTS = b'marathonQuests'
    PREMIUM_QUESTS = b'premiumQuests'


NEWBIES_QUESTS_PASS_TOKEN = b'ndq_pass'

def getGroupTypeByID(groupID):
    if groupID in (DEFAULTS_GROUPS.UNGROUPED_QUESTS,
     DEFAULTS_GROUPS.MOTIVE_QUESTS):
        return groupID
    if events_helpers.isMarathon(groupID):
        return DEFAULTS_GROUPS.MARATHON_QUESTS
    if events_helpers.isPremium(groupID):
        return DEFAULTS_GROUPS.PREMIUM_QUESTS
    return DEFAULTS_GROUPS.REGULAR_GROUPED_QUESTS


class CONTITIONS_SCOPE(object):
    MAIN = b'main'
    FULL = b'full'
    DIFF = b'add'


class TOKEN_SHOP(object):
    SHOW = b'show'
    HIDE = b'hide'
    WEB = b'web'


PM3_ROLE_TO_ICON_NAME = {(constants.COMMON_ROLE.ASSAULT): b'assault', 
   (constants.COMMON_ROLE.SNIPER): b'sniper', 
   (constants.COMMON_ROLE.SUPPORT): b'support'}

class ServerEventAbstract(object):
    __metaclass__ = ABCMeta
    __slots__ = (b'_id', b'_data', b'_groupID')
    _connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self, eID, data):
        self._id = eID
        self._data = dict(data)
        self._groupID = None
        return

    def isGuiDisabled(self):
        return self._data.get(b'disableGui', False)

    def isHidden(self):
        return self._data.get(b'hidden', False) or not self.__isForCurrentPeriphery()

    def isShowedPostBattle(self):
        return self._data.get(b'showPostBattleStat', False)

    def getWeekDays(self):
        return self._data.get(b'weekDays', set())

    def getActiveTimeIntervals(self):
        if b'activeTimeIntervals' in self._data:
            return [(l[0] * 3600 + l[1] * 60, h[0] * 3600 + h[1] * 60) for l, h in self._data[b'activeTimeIntervals']]
        return []

    def getID(self):
        return self._id

    def getIconID(self):
        return self._data.get(b'uiDecoration', None)

    def setGroupID(self, groupID):
        self._groupID = groupID
        return

    def getGroupID(self):
        return self._groupID

    def getPriority(self):
        return self._data.get(b'priority', 0)

    def getData(self):
        return self._data

    def getType(self):
        return self._data.get(b'type', 0)

    def getStartTimeRaw(self):
        if b'startTime' in self._data:
            return self._data[b'startTime']
        return time.time()

    def getFinishTimeRaw(self):
        if b'finishTime' in self._data:
            return self._data[b'finishTime']
        return time.time()

    def getFinishTimeRawInUTC(self):
        if b'finishTime' in self._data:
            return self._data[b'finishTime']
        return time_utils.getServerUTCTime()

    def getStartTime(self):
        if b'startTime' in self._data:
            return time_utils.makeLocalServerTime(self._data[b'startTime'])
        return time.time()

    def getFinishTime(self):
        if b'finishTime' in self._data:
            return time_utils.makeLocalServerTime(self._data[b'finishTime'])
        return time.time()

    def getUserName(self):
        return getLocalizedData(self._data, b'name')

    def getDescription(self):
        return getLocalizedData(self._data, b'description')

    def getNotificationText(self):
        return getLocalizedData(self._data, b'notificationText')

    def getTimeFromStartTillNow(self):
        return time_utils.getTimeDeltaTillNow(self.getStartTime())

    def getStartTimeLeft(self):
        return time_utils.getTimeDeltaFromNowInLocal(self.getStartTime())

    def getFinishTimeLeft(self):
        return time_utils.getTimeDeltaFromNowInLocal(self.getFinishTime())

    def isOutOfDate(self):
        return self.getFinishTimeLeft() <= 0

    def isStarted(self):
        return self.getStartTimeLeft() <= 0

    def getUserType(self):
        return b''

    def isIGR(self):
        return self._data.get(b'isIGR', False)

    def isCompleted(self, progress=None):
        return False

    def isTokensOnSale(self):
        state = self._getTokenSaleState()
        return state == TOKEN_SHOP.SHOW

    def isTokensOnSaleDynamic(self):
        return self._getTokenSaleState() == TOKEN_SHOP.WEB

    def getNearestActivityTimeLeft(self):
        timeLeft = None
        if self.getStartTimeLeft() > 0:
            timeLeft = (
             self.getStartTimeLeft(), (0, time_utils.ONE_DAY))
        else:
            weekDays, timeIntervals = self.getWeekDays(), self.getActiveTimeIntervals()
            if weekDays or timeIntervals:
                timeLeft = next(time_utils.ActivityIntervalsIterator(time_utils.getServerTimeCurrentDay(), time_utils.getServerRegionalWeekDay(), weekDays, timeIntervals))
        return timeLeft

    def hasPremIGRVehBonus(self):
        return False

    def isAvailable(self):
        if self.getStartTimeLeft() > 0:
            return ValidationResult(False, b'in_future')
        if self.isOutOfDate():
            return ValidationResult(False, b'out_of_date')
        weekDays = self.getWeekDays()
        if weekDays and time_utils.getServerRegionalWeekDay() not in weekDays:
            return ValidationResult(False, b'invalid_weekday')
        intervals = self.getActiveTimeIntervals()
        serverTime = time_utils.getServerTimeCurrentDay()
        if intervals:
            for low, high in intervals:
                if low <= serverTime <= high:
                    break
            else:
                return ValidationResult(False, b'invalid_time_interval')

        if not self._checkConditions():
            return ValidationResult(False, b'requirements')
        return ValidationResult(True, b'')

    def isRawAvailable(self, now=None):
        now = now or time.time()
        return self.getStartTimeRaw() <= now < self.getFinishTimeRaw()

    def isValidVehicleCondition(self, vehicle):
        return self._checkVehicleConditions(vehicle)

    def getBonuses(self, bonusName=None, isCompensation=False):
        return []

    def getParents(self):
        return []

    def getParentsName(self):
        return []

    def _checkConditions(self):
        return True

    def _checkVehicleConditions(self, vehicle):
        return True

    def _getTokenSaleState(self):
        return self._data.get(b'shopButton', TOKEN_SHOP.HIDE)

    def __isForCurrentPeriphery(self):
        peripheryIDs = self._data.get(b'peripheryIDs')
        if not peripheryIDs:
            return True
        return self._connectionMgr.peripheryID in peripheryIDs

    def __repr__(self):
        return b'%s(qID = %s, groupID = %s)' % (
         self.__class__.__name__, self._id, self._groupID)


class Group(ServerEventAbstract):

    def getGroupEvents(self):
        return self._data.get(b'groupContent', [])

    def getGroupContent(self, srvEvents):
        groupQuests = []
        for questID in self.getGroupEvents():
            quest = srvEvents.get(questID)
            if quest is not None:
                groupQuests.append(quest)

        return groupQuests

    def isMarathon(self):
        return events_helpers.isMarathon(self.getID())

    def isPremium(self):
        return events_helpers.isPremium(self.getID())

    def isRegularQuest(self):
        return events_helpers.isRegularQuest(self.getID())

    def isMapsTrainingQuest(self):
        return events_helpers.isMapsTraining(self.getID())

    def getLinkedAction(self, actions):
        return getLinkedActionID(self.getID(), actions)

    def getMainQuest(self, events):
        if not self.isMarathon():
            LOG_ERROR(b'Trying to find main quest in non-marathon group', self.getID())
            return
        else:
            for quest in events:
                if events_helpers.isMarathon(quest.getID()):
                    return quest

            LOG_ERROR(b'There is no main token quest in the marathon', self.getID())
            return

    def getUserName(self):
        if self.isMapsTrainingQuest():
            return backport.text(R.strings.static_quests.mt_battle_quests.dyn(self.getID()).name())
        return getLocalizedData(self._data, b'name')


class Quest(ServerEventAbstract):
    itemsCache = dependency.descriptor(IItemsCache)
    eventsCache = dependency.descriptor(IEventsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)
    __slots__ = ServerEventAbstract.__slots__ + (b'_progress', b'_children', b'_parents', b'_parentsName', b'accountReqs', b'vehicleReqs', b'preBattleCond', b'bonusCond', b'postBattleCond', b'__linkedActions', b'_meta', b'_conditions')

    def __init__(self, qID, data, progress=None):
        super(Quest, self).__init__(qID, data)
        self._progress = progress
        self._children, self._parents, self._parentsName = {}, {}, {}
        self._meta = data.get(b'meta', {})
        self._conditions = dict(data[b'conditions'])
        preBattle = dict(self._conditions[b'preBattle'])
        self.accountReqs = AccountRequirements(preBattle[b'account'])
        self.vehicleReqs = VehicleRequirements(preBattle[b'vehicle'])
        self.preBattleCond = PreBattleConditions(preBattle[b'battle'])
        self.bonusCond = BonusConditions(self._conditions[b'common'], self.getProgressData(), self.preBattleCond)
        self.postBattleCond = PostBattleConditions(self._conditions[b'postBattle'], self.preBattleCond)
        self._groupID = DEFAULTS_GROUPS.UNGROUPED_QUESTS
        self.__linkedActions = []
        return

    @classmethod
    def postBattleInfo(cls):
        return

    @classmethod
    def showMissionAction(cls):
        return

    def getConditionsDescription(self):
        description = self._conditions.get(b'description')
        if description:
            if b'key' in description:
                return i18n.makeString(description[b'key'])
            return getLocalizedData(self._conditions, b'description')
        else:
            return

    def isCompensationPossible(self):
        return events_helpers.isMarathon(self.getGroupID()) and bool(self.getBonuses(b'tokens'))

    def shouldBeShown(self):
        if events_helpers.isMapsTraining(self.getGroupID()):
            return self.isAvailable().isValid and self.lobbyContext.getServerSettings().isMapsTrainingEnabled()
        return True

    def getGroupType(self):
        return getGroupTypeByID(self.getGroupID())

    def isAvailable(self):
        if self.bonusCond.getBonusLimit() is not None and self.bonusCond.isDaily() and self.isCompleted():
            return ValidationResult(False, b'dailyComplete')
        else:
            return super(Quest, self).isAvailable()

    @property
    def linkedActions(self):
        return self.__linkedActions

    @linkedActions.setter
    def linkedActions(self, value):
        self.__linkedActions = value
        return

    def getUserType(self):
        return i18n.makeString(QUESTS.ITEM_TYPE_QUEST)

    def getProgressExpiryTime(self):
        return self._data.get(b'progressExpiryTime', time.time())

    def isCompletedByGroup(self, groupByKey):
        bonusLimit = self.bonusCond.getBonusLimit()
        if bonusLimit is not None:
            if self.bonusCond.getGroupByValue() is None:
                return self.isCompleted()
            if self._progress is not None:
                return bonusLimit <= self.getBonusCount(groupByKey)
        return False

    def isCompleted(self, progress=None):
        progress = progress or self._progress
        bonusLimit = self.bonusCond.getBonusLimit()
        if bonusLimit is not None:
            groupBy = self.bonusCond.getGroupByValue()
            if groupBy is None:
                return self.getBonusCount(progress=progress) >= bonusLimit
            if progress is not None:
                if groupBy == b'nation':
                    return self.__checkGroupedCompletion(nations.AVAILABLE_NAMES, progress, bonusLimit)
                if groupBy == b'level':
                    return self.__checkGroupedCompletion(xrange(1, constants.MAX_VEHICLE_LEVEL + 1), progress, bonusLimit, keyMaker=(lambda lvl: b'level %d' % lvl))
                if groupBy == b'class':
                    return self.__checkGroupedCompletion(constants.VEHICLE_CLASSES, progress, bonusLimit)
                if groupBy == b'vehicle':
                    pass
        return super(Quest, self).isCompleted()

    def setChildren(self, children):
        self._children = children
        return

    def getChildren(self):
        return self._children

    def setParents(self, parents):
        self._parents = parents
        return

    def getParents(self):
        return self._parents

    def setParentsName(self, parentsName):
        self._parentsName = parentsName
        return

    def getParentsName(self):
        return self._parentsName

    def getBonusCount(self, groupByKey=None, progress=None):
        progress = progress or self._progress
        if progress is not None:
            groupBy = self.bonusCond.getGroupByValue()
            if groupBy is None:
                return progress.get(None, {}).get(b'bonusCount', 0)
            if groupByKey is not None:
                return progress.get(groupByKey, {}).get(b'bonusCount', 0)
            return sum(p.get(b'bonusCount', 0) for p in progress.itervalues())
        else:
            return 0

    def getProgressData(self):
        return self._progress or {}

    def getRawBonuses(self):
        return self.getData().get(b'bonus', {})

    def getBonuses(self, bonusName=None, isCompensation=False, bonusData=None, ctx=None):
        result = []
        bonusData = bonusData or self.getRawBonuses()
        if bonusName is None:
            for name, value in bonusData.iteritems():
                for bonus in getBonuses(self, name, value, isCompensation, ctx=ctx):
                    result.append(self._bonusDecorator(bonus))

                if name == b'vehicles':
                    stylesData = self.__getVehicleStyleBonuses(value)
                    if stylesData:
                        for bonus in getBonuses(self, b'customizations', stylesData, isCompensation, ctx=ctx):
                            result.append(self._bonusDecorator(bonus))

        elif bonusName in bonusData:
            for bonus in getBonuses(self, bonusName, bonusData[bonusName], isCompensation, ctx=ctx):
                result.append(self._bonusDecorator(bonus))

        return sorted(result, cmp=compareBonuses, key=operator.methodcaller(b'getName'))

    @staticmethod
    def __getVehicleStyleBonuses(vehiclesData):
        stylesData = []
        for vehData in vehiclesData.itervalues():
            customization = vehData.get(b'customization', None)
            if customization is not None:
                styleData = {b'value': 1, b'custType': b'style', 
                   b'id': (customization.get(b'styleId', -1)), 
                   b'customCompensation': (customization.get(b'customCompensation', None))}
                stylesData.append(styleData)

        return stylesData

    def getCompensation(self):
        compensatedToken = findFirst((lambda t: t.isDisplayable()), self.accountReqs.getTokens())
        if compensatedToken:
            return {(compensatedToken.getID()): (self.getBonuses(isCompensation=True))}
        return {}

    def hasPremIGRVehBonus(self):
        vehBonuses = self.getBonuses(b'vehicles')
        for vehBonus in vehBonuses:
            vehicles = vehBonus.getValue()
            for intCD, data in vehicles.iteritems():
                item = self.itemsCache.items.getItemByCD(intCD)
                if item.isPremiumIGR and data.get(b'rent', None) is not None:
                    return True

        return False

    def getSuitableVehicles(self):
        return self.vehicleReqs.getSuitableVehicles()

    def hasBonusType(self, bonusType):
        bonusTypesCond = self.preBattleCond.getConditions().find(b'bonusTypes')
        return bonusTypesCond is None or bonusType in bonusTypesCond.getValue()

    @staticmethod
    def _bonusDecorator(bonus):
        return bonus

    def __checkGroupedCompletion(self, values, progress, bonusLimit=None, keyMaker=(lambda v: v)):
        bonusLimit = bonusLimit or self.bonusCond.getBonusLimit()
        for value in values:
            if bonusLimit > self.getBonusCount(groupByKey=keyMaker(value), progress=progress):
                return False

        return True

    def _checkConditions(self):
        return self.accountReqs.isAvailable() and (self.vehicleReqs.isAnyVehicleAcceptable() or self.vehicleReqs.getSuitableVehicles())

    def _checkVehicleConditions(self, vehicle):
        return self.vehicleReqs.isAnyVehicleAcceptable() or vehicle in self.vehicleReqs.getSuitableVehicles()


class TokenQuest(Quest):

    def __init__(self, qID, data, progress=None):
        super(TokenQuest, self).__init__(qID, data, progress)
        self.accountReqs = TokenQuestAccountRequirements(self.accountReqs.getSection())
        return

    def _checkConditions(self):
        return self.accountReqs.isAvailable()


class BattleMattersQuest(Quest):

    def _checkConditions(self):
        res = _isBattleMattersQuestAvailable(self)
        if res is None:
            res = super(BattleMattersQuest, self)._checkConditions()
        return res

    def getUserName(self):
        return backport.text(R.strings.static_quests.battle_matters_quests.dyn(self.getID()).name())

    def getOrder(self):
        return getIdxFromQuestID(self.getID())

    def getDescription(self):
        return backport.text(R.strings.static_quests.battle_matters_quests.dyn(self.getID()).description())

    def getConditionLbl(self):
        return backport.text(R.strings.static_quests.battle_matters_quests.dyn(self.getID()).conditions.description())


class BattleMattersTokenQuest(TokenQuest):

    def _checkConditions(self):
        res = _isBattleMattersQuestAvailable(self)
        if res is None:
            res = super(BattleMattersTokenQuest, self)._checkConditions()
        return res

    def getUserName(self):
        if self.getID().startswith(BATTLE_MATTERS_QUEST_ID):
            return backport.text(R.strings.static_quests.battle_matters_quests.dyn(self.getID()).name())
        return getLocalizedData(self._data, b'name')

    def getOrder(self):
        return getIdxFromQuestID(self.getID())

    def getDescription(self):
        return backport.text(R.strings.static_quests.battle_matters_quests.dyn(self.getID()).description())

    def getConditionLbl(self):
        return backport.text(R.strings.static_quests.battle_matters_quests.dyn(self.getID()).conditions.description())


def _getConditionLbl(data):
    descriptionLbl = b'description'
    conditions = data.get(b'conditions')
    for itemName, itemData in conditions:
        if itemName == descriptionLbl:
            return i18n.makeString(getLocalizedData({descriptionLbl: itemData}, descriptionLbl))

    return b''


class PremiumQuest(Quest):

    def getUserName(self):
        return backport.text(R.strings.quests.premiumQuests.quests.dyn(self.getID()).title())


class DailyQuest(Quest):

    def getLevel(self):
        return self._meta and self._meta.get(b'level')

    def isBonus(self):
        return self.getLevel() == constants.DailyQuestsLevels.BONUS

    def getSortKey(self):
        return constants.DailyQuestsLevels.DAILY.index(self.getLevel())

    def getUserName(self):
        return backport.text(R.strings.quests.dailyQuests.postBattle.dyn(b'genericTitle_%s' % self.getLevel())())


class DailyEpicTokenQuest(TokenQuest):

    def getUserName(self):
        return backport.text(R.strings.quests.dailyQuests.postBattle.genericTitle_epic())

    def getDescription(self):
        return backport.text(R.strings.quests.dailyQuests.postBattle.epic.description())


class WeeklyQuest(Quest):

    def getInfo(self):
        return WeeklyQuestInfo(self._id)

    def getUserName(self):
        return backport.text(R.strings.weekly_quests.postBattle.genericTitle())


class PersonalQuest(Quest):
    __slots__ = Quest.__slots__ + (b'expiryTime',)

    def __init__(self, qID, data, progress=None, expiryTime=None):
        super(PersonalQuest, self).__init__(qID, data, progress)
        self.expiryTime = expiryTime
        return

    def getFinishTimeRawInUTC(self):
        finishTime = super(PersonalQuest, self).getFinishTimeRawInUTC()
        if self.expiryTime is not None:
            return min(finishTime, self.expiryTime)
        else:
            return finishTime

    def getFinishTime(self):
        if self.expiryTime is not None:
            return min(super(PersonalQuest, self).getFinishTime(), self.expiryTime)
        else:
            return super(PersonalQuest, self).getFinishTime()

    def getRequiredToken(self):
        return self._data.get(b'requiredToken', None)


class RankedQuest(Quest):
    __slots__ = Quest.__slots__ + (b'__rankedData', b'__qualificationBattlesCount', b'__isQualificationQuest')

    def __init__(self, qID, data, progress=None):
        super(RankedQuest, self).__init__(qID, data, progress)
        self.__rankedData = self.__parseRankSeasonData(data)
        self.__isQualificationQuest = isQualificationQuestID(qID)
        self.__qualificationBattlesCount = getQualificationBattlesCountFromID(qID) if self.__isQualificationQuest else 0
        return

    def getRank(self):
        return self.__rankedData.get(b'rank')

    def getSeasonID(self):
        return self.__rankedData.get(b'season')

    def getCycleID(self):
        return self.__rankedData.get(b'cycle')

    def isProcessedAtCycleEnd(self):
        return self.__rankedData[b'subtype'] == b'cycle'

    def isForRank(self):
        return self.__rankedData[b'subtype'] == b'rank'

    def isQualificationQuest(self):
        return self.__isQualificationQuest

    def getQualificationBattlesCount(self):
        return self.__qualificationBattlesCount

    @classmethod
    def __parseRankSeasonData(cls, data):
        conditionsDict = cls.__dictMaker(data.get(b'conditions', {}))
        rankedData = conditionsDict.get(b'common', {})
        result = {}
        if rankedData:
            for key in (b'season', b'cycle'):
                if key in rankedData:
                    result[key] = rankedData[key][b'value']

            if b'maxRank' in rankedData:
                rank = rankedData[b'maxRank']
                if b'and' in rank:
                    rankBounds = rank[b'and']
                    result[b'rank'] = int(first(rankBounds.values())[b'value'])
                else:
                    result[b'rank'] = int(rank[b'greaterOrEqual'][b'value'])
        result[b'subtype'] = data.get(b'subtype')
        return result

    @classmethod
    def __dictMaker(cls, kVList):
        result = {}
        for key, value in dict(kVList).iteritems():
            if isinstance(value, (list, tuple)) and value:
                result[key] = cls.__dictMaker(value)
            else:
                result[key] = value

        return result


ActionData = namedtuple(b'ActionData', b'discountObj priority uiDecoration')

class Action(ServerEventAbstract):
    __slots__ = ServerEventAbstract.__slots__ + (b'__linkedQuests',)

    def __init__(self, qID, data):
        super(Action, self).__init__(qID, data)
        self._groupID = DEFAULTS_GROUPS.UNGROUPED_ACTIONS
        self.__linkedQuests = []
        return

    @property
    def linkedQuests(self):
        return self.__linkedQuests

    @linkedQuests.setter
    def linkedQuests(self, value):
        self.__linkedQuests = value
        return

    def getUserType(self):
        return i18n.makeString(QUESTS.ITEM_TYPE_ACTION)

    def getActions(self):
        result = {}
        if b'steps' not in self._data:
            return result
        else:
            for stepData in self._data[b'steps']:
                if b'name' in stepData:
                    mName = stepData[b'name']
                else:
                    mName = None
                if b'priority' in stepData:
                    priority = stepData[b'priority']
                else:
                    priority = None
                if b'params' in stepData:
                    params = stepData[b'params']
                else:
                    params = None
                if b'uiDecoration' in stepData:
                    uiDecoration = stepData[b'uiDecoration']
                else:
                    uiDecoration = None
                m = getModifierObj(mName, params)
                if m is None:
                    continue
                modifiers = m.splitModifiers()
                for modifier in modifiers:
                    if mName in result:
                        result[mName].append(ActionData(modifier, priority, uiDecoration))
                    else:
                        result[mName] = [ActionData(modifier, priority, uiDecoration)]

            return result

    def getModifiers(self):
        result = {}
        for stepData in self._data.get(b'steps'):
            mName = stepData.get(b'name')
            m = getModifierObj(mName, stepData.get(b'params'))
            if m is None:
                continue
            if mName in result:
                result[mName].update(m)
            else:
                result[mName] = m

        return sorted(result.itervalues(), key=operator.methodcaller(b'getName'), cmp=compareModifiers)


class PMCampaign(object):
    __slots__ = (b'__id', b'__info', b'__operations', b'__isUnlocked', b'__PM3CampaignFinishedQuest')

    def __init__(self, campaignID, info):
        self.__id = campaignID
        self.__info = info
        self.__operations = {}
        self.__PM3CampaignFinishedQuest = None
        self.__isUnlocked = False
        return

    def getID(self):
        return self.__id

    def getName(self):
        return self.__info[b'name']

    def getUserName(self):
        return self.__info[b'userString']

    def getUserDescription(self):
        return self.__info[b'description']

    def getOperations(self):
        return self.__operations

    def getPM3CampaignFinishedQuest(self):
        return self.__PM3CampaignFinishedQuest

    def isUnlocked(self):
        return self.__isUnlocked

    def isStarted(self):
        return bool([operation for operation in self.__operations.itervalues() if operation.isStarted()])

    def isFullCompleted(self):
        return all([operation.isFullCompleted() for operation in self.__operations.itervalues()])

    def updateProgress(self, hiddenQuests):
        self.__PM3CampaignFinishedQuest = hiddenQuests.get(finders.PM3_CAMPAIGN_FINISHED_QUEST)
        for tile in self.__operations.itervalues():
            if tile.isUnlocked():
                self.__isUnlocked = True
                break

        return

    def addOperation(self, operation):
        if operation.getID() not in self.__operations:
            self.__operations[operation.getID()] = operation
        return


class PMOperation(object):
    __slots__ = (b'__id', b'__info', b'__quests', b'__initialQuests', b'__finalQuests', b'__isUnlocked', b'__isPaused', b'__hasRequiredVehicles', b'__achievements', b'__tokens', b'__bonuses', b'__isAwardAchieved', b'__freeTokensCount', b'__freeTokensTotalCount', b'__branch', b'__disabled', b'__pmPointsMaxCount', b'__pmPointsTotalCount', b'__requiredLevel', b'__vehDetails', b'__PM3RewardQuest', b'__PM3RewardHonorQuest')

    def __init__(self, tileID, info, branch=0):
        self.__id = tileID
        self.__info = info
        self.__quests = {}
        self.__initialQuests = {}
        self.__finalQuests = {}
        self.__isUnlocked = False
        self.__isPaused = False
        self.__hasRequiredVehicles = False
        self.__requiredLevel = 0
        self.__achievements = dict((chID, (ACHIEVEMENT_BLOCK.TOTAL, aName)) for chID, aName in self.__info[b'achievements'].iteritems())
        self.__tokens = {}
        self.__bonuses = {}
        self.__vehDetails = {}
        self.__isAwardAchieved = False
        self.__freeTokensCount = 0
        self.__freeTokensTotalCount = 0
        self.__pmPointsMaxCount = 0
        self.__pmPointsTotalCount = 0
        self.__PM3RewardQuest = None
        self.__PM3RewardHonorQuest = None
        self.__branch = branch
        self.__disabled = False
        return

    def getID(self):
        return self.__id

    def getBranch(self):
        return self.__branch

    def getNextOperationIDs(self):
        return self.__info[b'nextTileIDs']

    def getName(self):
        return self.__info[b'name']

    def getUserName(self):
        return self.__info[b'userString']

    def getTotalPmPointsCount(self):
        return self.__pmPointsTotalCount

    def getMaxPmPointsCount(self):
        return self.__pmPointsMaxCount

    def getShortUserName(self):
        return i18n.makeString(b'#personal_missions:operations/title%d' % self.getID())

    def getUserDescription(self):
        return self.__info[b'description']

    def getChainClassifier(self, chainID):
        firstQuest = first(self.__quests.get(chainID, {}).itervalues())
        if firstQuest is not None:
            return firstQuest.getQuestClassifier()
        else:
            return

    def getChainByClassifierAttr(self, classifier):
        return findFirst((lambda it: self.getChainClassifier(it[0]).classificationAttr == classifier), self.getQuests().iteritems(), (None, None))

    def getIterationChain(self):
        if self.__branch == PM_BRANCH.REGULAR:
            return VEHICLE_TYPES_ORDER
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_2:
            return nations.ALLIANCES_TAGS_ORDER
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_3:
            return constants.COMMON_ROLE.ALL_ORDER
        return ()

    def getChainName(self, chainID):
        classifier = self.getChainClassifier(chainID).classificationAttr
        if self.__branch == PM_BRANCH.REGULAR:
            return PERSONAL_MISSIONS.chainNameByVehicleType(classifier)
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_2:
            allianceId = nations.ALLIANCE_IDS[classifier]
            return PERSONAL_MISSIONS.getAllianceName(allianceId)
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_3:
            return PERSONAL_MISSIONS_30.chainNameByRole(classifier)
        return b''

    def getAllianceID(self, chainID):
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_2:
            classifier = self.getChainClassifier(chainID).classificationAttr
            return nations.ALLIANCE_IDS[classifier]
        return

    def getChainDescription(self, chainID):
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_2:
            classifier = self.getChainClassifier(chainID).classificationAttr
            allianceId = nations.ALLIANCE_IDS[classifier]
            return PERSONAL_MISSIONS.getAllianceDetails(allianceId)
        return b''

    def getChainIcon(self, chainID):
        classifier = self.getChainClassifier(chainID).classificationAttr
        if self.__branch == PM_BRANCH.REGULAR:
            return Vehicle.getTypeBigIconPath(classifier)
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_2:
            allianceId = nations.ALLIANCE_IDS[classifier]
            return RES_ICONS.getAllianceIcon(allianceId)
        return b''

    def getSmallChainIcon(self, chainID):
        classifier = self.getChainClassifier(chainID).classificationAttr
        if self.__branch == PM_BRANCH.REGULAR:
            return Vehicle.getTypeSmallIconPath(classifier, False)
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_2:
            return RES_ICONS.getAlliance17x19Icon(classifier)
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_3:
            return self.__getOperationMissionCategoryIconPath(size=b'16x16', classifier=classifier)
        return b''

    def getChainMajorTag(self, chainID):
        firstQuest = first(self.__quests.get(chainID, {}).itervalues())
        if firstQuest is not None:
            return firstQuest.getMajorTag()
        else:
            return

    def getChainSortKey(self, chainID):
        return self.getChainMajorTag(chainID)

    def getChainTotalTokensCount(self, chainID, isMainBonuses=None):
        result = 0
        for tokenID in self.__info[b'tokens']:
            for q in self.__quests[chainID].itervalues():
                for tokenBonus in q.getBonuses(b'tokens', isMainBonuses):
                    tokens = tokenBonus.getTokens()
                    if tokenID in tokens:
                        result += tokens[tokenID].count

        return result

    def getIconID(self):
        return self.__info[b'iconID']

    def getCampaignID(self):
        return self.__info[b'seasonID']

    def getChainSize(self):
        return self.__info[b'questsInChain']

    def getQuestsCount(self):
        return self.__info[b'chainsCount'] * self.getChainSize()

    def getPrice(self):
        return self.__info[b'price']

    def getChainsCount(self):
        return self.__info[b'chainsCount']

    def getQuests(self):
        return self.__quests

    def getQuestsInChainByFilter(self, chainID, filterFunc=(lambda v: True)):
        result = {}
        for qID, q in self.__quests[chainID].iteritems():
            if filterFunc(q):
                result[qID] = q

        return result

    def getQuestsByFilter(self, filterFunc=(lambda v: True)):
        result = {}
        for _, quests in self.__quests.iteritems():
            for qID, q in quests.iteritems():
                if filterFunc(q):
                    result[qID] = q

        return result

    def getInProgressQuests(self):
        return self.getQuestsByFilter((lambda quest: quest.isInProgress()))

    def getCompletedQuests(self, isRewardReceived=None):
        return self.getQuestsByFilter((lambda quest: quest.isCompleted(isRewardReceived=isRewardReceived)))

    def getFullCompletedQuests(self, isRewardReceived=None):
        return self.getQuestsByFilter((lambda quest: quest.isFullCompleted(isRewardReceived=isRewardReceived)))

    def getPawnedQuests(self):
        return self.getQuestsByFilter(operator.methodcaller(b'areTokensPawned'))

    def isCompleted(self, isRewardReceived=None):
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_3:
            return self.__isAwardAchieved
        return len(self.getCompletedQuests(isRewardReceived)) == self.getQuestsCount()

    def isActive(self):
        return len(self.getInProgressQuests()) > 0

    def isInProgress(self):
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_3:
            return self.isActive() or not self.isCompleted() and (bool(self.getCompletedQuests()) or bool(self.getTotalPmPointsCount()))
        return self.isActive()

    def isFullCompleted(self, isQuestRewardReceived=None, isFinalRewardReceived=True):
        if self.__branch == PM_BRANCH.PERSONAL_MISSION_3:
            return (self.__isAwardAchieved or not isFinalRewardReceived) and len(self.getCompletedQuests(isQuestRewardReceived)) == self.getQuestsCount()
        return len(self.getFullCompletedQuests(isQuestRewardReceived)) == self.getQuestsCount()

    def isAwardAchieved(self):
        return self.__isAwardAchieved

    def getCompletedFinalQuests(self, isRewardReceived=None):
        return self.getQuestsByFilter((lambda quest: quest.isCompleted(isRewardReceived=isRewardReceived) and quest.isFinal()))

    def getInitialQuests(self):
        return self.__initialQuests

    def getFinalQuests(self):
        return self.__finalQuests

    def isAvailable(self):
        if self.isDisabled():
            return ValidationResult(False, b'disabled')
        if not self.isUnlocked():
            return ValidationResult(False, b'isLocked')
        if not self.hasRequiredVehicles():
            return ValidationResult(False, b'noVehicle')
        return ValidationResult(True, b'')

    def isUnlocked(self):
        return self.__isUnlocked

    def isPaused(self):
        return self.__isPaused

    def setDisabledState(self, value):
        self.__disabled = value
        for _, questsInChain in self.__quests.iteritems():
            for _, q in questsInChain.iteritems():
                q.setDisabledState(value)

        return

    def isDisabled(self):
        return self.__disabled

    def setRequiredVehicleLevel(self, level):
        self.__requiredLevel = level
        return

    def getRequiredVehicleLevel(self):
        return self.__requiredLevel

    def hasRequiredVehicles(self):
        return bool(self.getQuestsByFilter(operator.methodcaller(b'hasRequiredVehicles')))

    def hasCollectedAllPoints(self):
        return self.__pmPointsTotalCount >= self.__pmPointsMaxCount

    def getAchievements(self):
        return self.__achievements

    def getTokens(self):
        return self.__tokens

    def isStarted(self):
        return self.isInProgress() or self.isCompleted()

    def getTokensCount(self):
        return tuple([sum(tokensCount) for tokensCount in zip(*self.__tokens.values())])

    def getTotalTokensCount(self):
        result = 0
        for chainID in self.__quests.iterkeys():
            result += self.getChainTotalTokensCount(chainID)

        return result

    def getTokensPawnedCount(self):
        result = 0
        for quest in self.getPawnedQuests().itervalues():
            result += quest.getPawnCost()

        return result

    def getFreeTokensCount(self):
        return self.__freeTokensCount

    def getFreeTokensTotalCount(self):
        return self.__freeTokensTotalCount

    def getBonuses(self):
        return self.__bonuses

    def getVehDetails(self):
        return self.__vehDetails

    def getPM3RewardQuest(self):
        return self.__PM3RewardQuest

    def getPM3RewardHonorQuest(self):
        return self.__PM3RewardHonorQuest

    def getPM3VehicleBonus(self):
        for bonus in self.__PM3RewardQuest.getBonuses():
            if bonus.getName() == b'vehicles':
                for vehicle, _ in bonus.getVehicles():
                    return vehicle

        return

    def getVehicleBonus(self):
        for bonuses in self.getBonuses().itervalues():
            for bonus in bonuses:
                if bonus.getName() == b'vehicles':
                    for vehicle, _ in bonus.getVehicles():
                        return vehicle

        return

    def updateProgress(self, eventsCache, hiddenQuests=None):
        qp = eventsCache.questsProgress
        self.__isUnlocked = False
        for quest in self.__initialQuests.itervalues():
            if quest.isUnlocked():
                self.__isUnlocked = True
                break

        if hiddenQuests is None:
            hiddenQuests = eventsCache.getHiddenQuests()
        self.__tokens, self.__bonuses, self.__vehDetails = {}, {}, {}
        if self.getBranch() == PM_BRANCH.PERSONAL_MISSION_3:
            self.__vehDetails = self.__getVehDetailsFromTokens(hiddenQuests)
            self.__PM3RewardQuest = hiddenQuests.get(finders.PM3_OPERATION_REWARD_QUEST % self.getID())
            self.__PM3RewardHonorQuest = hiddenQuests.get(finders.PM3_OPERATION_FINISHED_HONOR_QUEST % (self.getCampaignID(), self.getID()))
            if self.__PM3RewardQuest:
                for token in self.__PM3RewardQuest.accountReqs.getTokens():
                    if token.getID() == finders.PM_POINTS % (self.getCampaignID(), self.getID()):
                        self.__pmPointsTotalCount = qp.getTokenCount(token.getID())
                        self.__pmPointsMaxCount = token.getNeededCount()

        operationTokensFinder = finders.multipleTokenFinder(self.__info[b'tokens'])
        quest = finders.getQuestByTokenAndBonus(hiddenQuests, operationTokensFinder, finders.operationCompletionBonusFinder(self))
        if quest is not None:
            for token in quest.accountReqs.getTokens():
                if token.getID() in self.__info[b'tokens']:
                    self.__tokens[token.getID()] = (
                     qp.getTokenCount(token.getID()), token.getNeededCount())
                    self.__bonuses.setdefault(token.getID(), []).extend(quest.getBonuses())

        else:
            LOG_ERROR(b'Main token quest was not found for Personal missions operation!', self.getID())
        self.__hasRequiredVehicles = False
        self.__freeTokensCount = 0
        self.__freeTokensTotalCount = 0
        for quests in self.__quests.itervalues():
            for quest in quests.itervalues():
                tokenBonuses = quest.getBonuses(b'tokens')
                for bonus in tokenBonuses:
                    if bonus.getName() == b'freeTokens':
                        bonusCount = bonus.getCount()
                        self.__freeTokensTotalCount += bonusCount
                        if quest.isFullCompleted():
                            self.__freeTokensCount += bonusCount

        if self.getBranch() != PM_BRANCH.PERSONAL_MISSION_3:
            self.__isAwardAchieved = bool(qp.getTokenCount(finders.getOperationCompleteToken(self)))
        else:
            self.__isAwardAchieved = any((
             qp.getTokenCount(finders.PM3_PERSONAL_MISSION_REWARD_CLAIMED) % self.getID(),
             qp.getTokenCount(finders.PM3_PERSONAL_MISSION_BASE_TOKEN % (self.getCampaignID(),
              self.getID())),
             qp.getTokenCount(finders.PM3_FINISHED_CAMPAIGN_TOKEN)))
        self.__isPaused = not eventsCache.getPersonalMissions().isCampaignActive(PM_BRANCH.TYPE_TO_NAME[self.__branch]) and self.isStarted()
        return

    def addQuest(self, quest):
        questID = quest.getID()
        chain = self.__quests.setdefault(quest.getChainID(), {})
        if questID not in chain:
            chain[questID] = quest
            if quest.isInitial():
                self.__initialQuests[questID] = quest
            elif quest.isFinal():
                self.__finalQuests[quest.getChainID()] = quest
        return

    @staticmethod
    def __getOperationMissionCategoryIconPath(size, classifier):
        category = PM3_ROLE_TO_ICON_NAME[classifier]
        return backport.image(R.images.gui.maps.icons.personal_missions_30.category.num(size).dyn(category)())

    def __getVehDetailsFromTokens(self, hiddenQuests):
        vehDetails = {}
        pm3Milestones = finders.getPM3Milestones(hiddenQuests, self.getID())
        for milestoneQuest in pm3Milestones.values():
            detailName = b''
            vehDetailGap = 0
            for bonus in milestoneQuest.getBonuses():
                if bonus.getName() == b'battleToken':
                    for tokenName in bonus.getValue():
                        if tokenName.startswith(finders.PM3_VEHICLE_DETAIL_TOKEN % self.getID()):
                            detailName = tokenName

            for token in milestoneQuest.accountReqs.getTokens():
                if token.getID() == finders.PM_POINTS % (self.getCampaignID(), self.getID()):
                    vehDetailGap = token.getNeededCount()

            vehDetails[detailName] = vehDetailGap

        return vehDetails


class PersonalMission(ServerEventAbstract):
    __slots__ = ServerEventAbstract.__slots__ + (b'__pmType', b'__pqProgress', b'__campaignID', b'__hasRequiredVehicles', b'__canBePawned', b'__conditionsProgress', b'__disabled', b'__conditionsConfig', b'__missionConditionState')
    ONE_BATTLE_OPERATIONS_IDS = (1, 2, 3, 4, 6)
    _TankmanBonus = namedtuple(b'_TankmanBonus', (b'tankman', b'isMain'))

    def __init__(self, qID, pmType, progress=None, campaignID=None):
        super(PersonalMission, self).__init__(qID, pmType.mainQuestInfo)
        self.__pmType = pmType
        self.__pqProgress = progress
        self.__campaignID = campaignID
        self.__hasRequiredVehicles = False
        self.__canBePawned = False
        self.__conditionsProgress = None
        self.__disabled = False
        self.__conditionsConfig = getQuestConfig(self.__pmType.generalQuestID)
        self.__missionConditionState = {}
        return

    def isAvailable(self):
        if self.isDisabled():
            return ValidationResult(False, b'disabled')
        if not self.isUnlocked():
            return ValidationResult(False, b'isLocked')
        if not self.hasRequiredVehicles():
            return ValidationResult(False, b'noVehicle')
        return ValidationResult(True, b'')

    def getDummyHeaderType(self):
        if self.getOperationID() in self.ONE_BATTLE_OPERATIONS_IDS:
            return DISPLAY_TYPE.NONE
        return DISPLAY_TYPE.SIMPLE

    def isOneBattleQuest(self):
        return self.getOperationID() in self.ONE_BATTLE_OPERATIONS_IDS

    def getConditionsProgress(self):
        return self.__conditionsProgress

    def getConditionsConfig(self):
        return self.__conditionsConfig or {}

    def setRequiredVehiclesPresence(self, hasRequiredVehicles):
        self.__hasRequiredVehicles = hasRequiredVehicles
        return

    def setCanBePawned(self, canBePawned):
        self.__canBePawned = canBePawned
        return

    def setMissionConditionState(self, vehID, progressID, state):
        if self.__missionConditionState.get(vehID, None):
            self.__missionConditionState[vehID].update({progressID: state})
        else:
            self.__missionConditionState.update({vehID: {progressID: state}})
        return

    def clearConditionState(self):
        self.__missionConditionState = {}
        return

    def hasRequiredVehicles(self):
        return self.__hasRequiredVehicles

    def getPMType(self):
        return self.__pmType

    def getMainQuestID(self):
        return self.__pmType.mainQuestInfo[b'id']

    def getAddQuestID(self):
        return self.__pmType.addQuestInfo[b'id']

    def getInternalID(self):
        return self.__pmType.internalID

    def getChainID(self):
        return self.__pmType.chainID

    def getOperationID(self):
        return self.__pmType.tileID

    def getCampaignID(self):
        return self.__campaignID

    def getUserType(self):
        return i18n.makeString(QUESTS.ITEM_TYPE_PERSONALMISSION)

    def getUserName(self):
        return self.__pmType.userString

    def getShortUserName(self):
        return self.__pmType.shortUserString

    def getUserDescription(self):
        return self.__pmType.description

    def getUserAdvice(self):
        return self.__pmType.advice

    def getGeneralQuestID(self):
        return self.__pmType.generalQuestID

    def getVehMinLevel(self):
        return self.__pmType.minLevel

    def getVehMaxLevel(self):
        return self.__pmType.maxLevel

    def getQuestBranch(self):
        return self.__pmType.branch

    def getQuestBranchName(self):
        return PM_BRANCH.TYPE_TO_NAME[self.getQuestBranch()]

    def setDisabledState(self, value):
        self.__disabled = value
        return

    def isDisabled(self):
        return self.__disabled

    def isUnlocked(self):
        return self.__pqProgress is not None and self.__pqProgress.unlocked

    def isInProgress(self):
        return self.__pqProgress is not None and self.__pqProgress.selected

    def isAvailableToPerform(self):
        return self.__pqProgress is not None and self.__pqProgress.unlocked and self.__pqProgress.state <= _PMS.UNLOCKED and not self.isDisabled()

    def isAmongUsedQuestVehicle(self, vehCD):
        if self.getConditionsProgress():
            return vehCD in self.getConditionsProgress().get(b'battlesUniqueVehicles', set())
        return False

    def hasCompletedUniqueBattleConditions(self, vehCD):
        requiredBattles = -1
        previousBattleCnt = 0
        for _, configData in self.__conditionsConfig.iteritems():
            requiredBattles = configData[b'config'].get(b'uniqueVehicle', 0)

        if self.getConditionsProgress():
            previousBattleCnt = len(sorted(self.getConditionsProgress().get(b'battlesUniqueVehicles', set())))
        if requiredBattles == 0 or previousBattleCnt + 1 == requiredBattles:
            return self.hasCompletedAllMissionConditions(vehCD)
        return False

    def hasCompletedAllMissionConditions(self, vehCD):
        missionState = self.__missionConditionState.get(vehCD, None)
        if missionState:
            completedConditions = 0
            isInOrGroup = False
            for conditionKey, configData in self.__conditionsConfig.iteritems():
                currentConditionState = missionState.get(conditionKey)
                isInOrGroup = configData[b'description'].isInOrGroup
                if currentConditionState in QUEST_PROGRESS_STATE.COMPLETED_STATES:
                    completedConditions += 1
                elif currentConditionState == QUEST_PROGRESS_STATE.FAILED and not isInOrGroup:
                    return False

            if completedConditions >= len(self.__conditionsConfig) or isInOrGroup and completedConditions:
                return True
        return False

    def hasAdditionalConditions(self):
        for _, configData in self.__conditionsConfig.iteritems():
            if not configData[b'config'].get(b'isMain', False):
                return True

        return False

    def hasProgress(self):
        return self.__pqProgress.state > _PMS.NONE

    def isInitial(self):
        return self.__pmType.isInitial

    def isFinal(self):
        return self.__pmType.isFinal

    @property
    def isOnPause(self):
        return self.__checkForFlags(PM_FLAG.PAUSE)

    def getQuestClassifier(self):
        return self.__pmType.classifier

    def getMajorTag(self):
        return self.__pmType.getMajorTag()

    def isMainCompleted(self, isRewardReceived=None):
        if isRewardReceived is True:
            states = (
             _PMS.MAIN_REWARD_GOTTEN, _PMS.ALL_REWARDS_GOTTEN)
        elif isRewardReceived is False:
            states = (
             _PMS.NEED_GET_MAIN_REWARD, _PMS.NEED_GET_ALL_REWARDS)
        else:
            states = (
             _PMS.MAIN_REWARD_GOTTEN, _PMS.ALL_REWARDS_GOTTEN,
             _PMS.NEED_GET_MAIN_REWARD, _PMS.NEED_GET_ALL_REWARDS)
        return self.__checkForStates(*states)

    def isFullCompleted(self, isRewardReceived=None):
        if isRewardReceived is True:
            states = (
             _PMS.ALL_REWARDS_GOTTEN,)
        elif isRewardReceived is False:
            states = (
             _PMS.NEED_GET_ALL_REWARDS,)
        else:
            states = _PMS.COMPLETED
        return self.__checkForStates(*states)

    def isCompleted(self, progress=None, isRewardReceived=None):
        return self.isMainCompleted(isRewardReceived) or self.isFullCompleted(isRewardReceived)

    def areTokensPawned(self):
        return self.isMainCompleted() and self.__pqProgress is not None and self.__pqProgress.pawned

    def getPawnCost(self):
        if self.isFinal():
            pawnCost = PM_BRANCH_TO_FINAL_PAWN_COST[self.getQuestBranch()]
        else:
            pawnCost = constants.PERSONAL_MISSION_PAWN_COST
        return pawnCost

    def canBeSelected(self):
        return self.isUnlocked() and not self.isFullCompleted() and not self.isInProgress()

    def canBePawned(self):
        return self.__canBePawned and not self.isMainCompleted()

    def isDone(self):
        return self.__checkForStates(_PMS.NEED_GET_ALL_REWARDS, _PMS.ALL_REWARDS_GOTTEN)

    def needToGetMainReward(self):
        return self.__checkForStates(_PMS.NEED_GET_ALL_REWARDS, _PMS.NEED_GET_MAIN_REWARD)

    def needToGetAddReward(self):
        return self.__checkForStates(_PMS.NEED_GET_ALL_REWARDS, _PMS.NEED_GET_ADD_REWARD)

    def needToGetAllReward(self):
        return self.__checkForStates(_PMS.NEED_GET_ALL_REWARDS)

    def needToGetReward(self):
        return self.__checkForStates(*_PMS.NEED_GET_REWARD)

    def updateProgress(self, questsProgress):
        self.__pqProgress = questsProgress.getPersonalMissionProgress(self.__pmType, self._id)
        progressName = b'pm3_progress' if self.getQuestBranch() == PM_BRANCH.PERSONAL_MISSION_3 else b'pm2_progress'
        self.__conditionsProgress = questsProgress.getConditionsProgress(self.__pmType.generalQuestID, progressName)
        return

    def updatePqStateInBattle(self, pqState):
        if self.__pqProgress:
            self.__pqProgress = PersonalMissionsProgressRequester.PersonalMissionProgress(state=pqState, flags=self.__pqProgress.flags, selected=self.__pqProgress.selected, unlocked=self.__pqProgress.unlocked, pawned=self.__pqProgress.pawned)
        else:
            self.__pqProgress = PersonalMissionsProgressRequester.PersonalMissionProgress(state=pqState, flags=PM_FLAG.NONE, selected=(), unlocked=0, pawned=False)
        return

    def getBonuses(self, bonusName=None, filterFunc=None, isMain=None, returnAwardList=False, isDelayed=False, ctx=None):
        if isMain is None:
            data = (
             self.__pmType.mainQuestInfo, self.__pmType.addQuestInfo)
        elif isMain:
            data = (
             self.__pmType.mainQuestInfo,)
        else:
            data = (
             self.__pmType.addQuestInfo,)
        if returnAwardList:
            data = (
             self.__pmType.addAwardListQuestInfo,)
        result = []
        for d in data:
            if isDelayed:
                bonuses = d.get(b'bonusDelayed', {}).iteritems()
            else:
                bonuses = d.get(b'bonus', {}).iteritems()
            for n, v in bonuses:
                if bonusName is not None and n != bonusName:
                    continue
                if filterFunc is not None and not filterFunc(n, v):
                    continue
                result.extend(getBonuses(self, n, v, ctx=ctx))

        return sorted(result, cmp=compareBonuses, key=operator.methodcaller(b'getName'))

    def getTankmanBonus(self):
        for isMainBonus in (True, False):
            for bonus in self.getBonuses(isMain=isMainBonus, isDelayed=True):
                if bonus.getName() == b'tankwomanBonus':
                    return self._TankmanBonus(bonus, isMainBonus)

        return self._TankmanBonus(None, None)

    @staticmethod
    def needToGetTankWoman(quest):
        bonus = quest.getTankmanBonus()
        return bonus.tankman and (quest.needToGetAddReward() and not bonus.isMain or quest.needToGetMainReward() and bonus.isMain)

    def __checkForStates(self, *statesToCheck):
        return self.__pqProgress is not None and self.__pqProgress.state in statesToCheck

    def __checkForFlags(self, flagsToCheck):
        return self.__pqProgress is not None and self.__pqProgress.flags & flagsToCheck == flagsToCheck

    def __repr__(self):
        return b'PQuest<id=%d; state=%s; flags=%s unlocked=%s>' % (
         self._id, self.__pqProgress.state, self.__pqProgress.flags, self.isUnlocked())


class MotiveQuest(Quest):

    def getUserName(self):
        return i18n.makeString(Quest.getUserName(self))

    def getGroupID(self):
        return DEFAULTS_GROUPS.MOTIVE_QUESTS

    def getDescription(self):
        return i18n.makeString(Quest.getDescription(self))

    def getParents(self):
        return {}

    def getTips(self):
        return getLocalizedData(self._data, b'advice')

    def getAwardMsg(self):
        return getLocalizedData(self._data, b'congratulation')

    def getRequirementsStr(self):
        return getLocalizedData(self._data, b'requirements')


class MapsTrainingQuest(Quest):

    def __init__(self, qID, data, progress=None):
        super(MapsTrainingQuest, self).__init__(qID, data, progress)
        conds = dict(data[b'conditions'])
        self.postBattleCond = MapsTrainingPostBattleConditions(conds[b'postBattle'], self.preBattleCond, self.getID())
        return

    def getUserName(self):
        return backport.text(R.strings.static_quests.mt_battle_quests.dyn(self.getID()).name())


def _getTileIconPath(tileIconID, prefix, state):
    return b'../maps/icons/quests/tiles/%s_%s_%s.png' % (tileIconID, prefix, state)


def getTileNormalUpIconPath(tileIconID):
    return _getTileIconPath(tileIconID, b'color', b'up')


def getTileNormalOverIconPath(tileIconID):
    return _getTileIconPath(tileIconID, b'color', b'over')


def getTileGrayUpIconPath(tileIconID):
    return _getTileIconPath(tileIconID, b'gray', b'up')


def getTileGrayOverIconPath(tileIconID):
    return _getTileIconPath(tileIconID, b'gray', b'over')


class IQuestBuilder(object):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        raise NotImplementedError
        return

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        raise NotImplementedError
        return


class PersonalQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return questType == constants.EVENT_TYPE.PERSONAL_QUEST

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return PersonalQuest(qID, data, progress, expiryTime)


class GroupQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return questType == constants.EVENT_TYPE.GROUP

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return Group(qID, data)


class MotiveQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return questType == constants.EVENT_TYPE.MOTIVE_QUEST

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return MotiveQuest(qID, data, progress)


class RankedQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return questType == constants.EVENT_TYPE.RANKED_QUEST

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return RankedQuest(qID, data, progress)


class BattleMattersTokenQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        if questType != constants.EVENT_TYPE.TOKEN_QUEST:
            return False
        return qID.startswith(BATTLE_MATTERS_QUEST_ID) or qID.startswith(BATTLE_MATTERS_INTERMEDIATE_QUEST_ID) or qID.startswith(BATTLE_MATTERS_COMPENSATION_QUEST_ID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return BattleMattersTokenQuest(qID, data, progress)


class DailyTokenQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return questType == constants.EVENT_TYPE.TOKEN_QUEST and isDailyQuest(qID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return DailyEpicTokenQuest(qID, data, progress)


class TokenQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return questType == constants.EVENT_TYPE.TOKEN_QUEST

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return TokenQuest(qID, data, progress)


class BattleMattersQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return qID.startswith(BATTLE_MATTERS_QUEST_ID) or qID.startswith(BATTLE_MATTERS_COMPENSATION_QUEST_ID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return BattleMattersQuest(qID, data, progress)


class PremiumQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return isPremium(qID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return PremiumQuest(qID, data, progress)


class DailyQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return isDailyQuest(qID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return DailyQuest(qID, data, progress)


class WeeklyQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return isWeeklyQuest(qID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return WeeklyQuest(qID, data, progress)


class MapsTrainingQuestBuilder(IQuestBuilder):

    @classmethod
    def isSuitableQuest(cls, questType, qID):
        return events_helpers.isMapsTrainingQuest(qID)

    @classmethod
    def buildQuest(cls, questType, qID, data, progress=None, expiryTime=None):
        return MapsTrainingQuest(qID, data, progress)


registerQuestBuilders((
 PersonalQuestBuilder, GroupQuestBuilder, MotiveQuestBuilder, RankedQuestBuilder, BattleMattersTokenQuestBuilder,
 DailyTokenQuestBuilder, TokenQuestBuilder, BattleMattersQuestBuilder, PremiumQuestBuilder, DailyQuestBuilder,
 WeeklyQuestBuilder, MapsTrainingQuestBuilder))

def createQuest(builders, questType, qID, data, progress=None, expiryTime=None):
    for builder in builders:
        if builder.isSuitableQuest(questType, qID):
            return builder.buildQuest(questType, qID, data, progress, expiryTime)

    return Quest(qID, data, progress)


def createAction(eventType, aID, data):
    if eventType == constants.EVENT_TYPE.GROUP:
        return Group(aID, data)
    return Action(aID, data)


def _isBattleMattersQuestAvailable(quest):
    if quest.isCompleted():
        return True
    else:
        if isinstance(quest, BattleMattersTokenQuest):
            if super(BattleMattersTokenQuest, quest).isCompleted():
                return True
        for item in quest.accountReqs.getConditions().items:
            if item.getName() == b'token' and item.getID() == (b'{}_unlock').format(quest.getID()):
                return item.getReceivedCount() >= item.getNeededCount()

        return
