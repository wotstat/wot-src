import locale, logging, time, typing, weakref
from collections import namedtuple, defaultdict, OrderedDict
from CurrentVehicle import g_currentVehicle
from Event import EventManager, Event
from constants import EVENT_TYPE, PREMIUM_TYPE
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import EventInfo, EventHeader
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import MarathonAwardComposer
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getMissionInfoData
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.MOTIVATION_QUESTS import MOTIVATION_QUESTS
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.event_boards.settings import isGroupMinimized, expandGroup
from gui.impl import backport
from gui.impl.gen.resources import R
from gui.server_events import settings
from gui.server_events.awards_formatters import AWARDS_SIZES
from gui.server_events.cond_formatters.tokens import TokensMarathonFormatter
from gui.server_events.event_items import DEFAULTS_GROUPS
from gui.server_events.events_constants import RANKED_DAILY_GROUP_ID, RANKED_PLATFORM_GROUP_ID, BATTLE_ROYALE_GROUPS_ID, EPIC_BATTLE_GROUPS_ID, FUN_RANDOM_GROUP_ID
from gui.server_events.events_helpers import isBattleMattersQuestID, isPremium, dailyQuestsSortFunc, isPremiumQuestsEnable, getPremiumGroup, getDailyEpicGroup, getRankedDailyGroup, getRankedPlatformGroup, getDailyBattleRoyaleGroup, getFunRandomDailyGroup, isDebutBoxesGroup, isVersusAIQuest, isSummerSaleGroup
from gui.server_events.events_helpers import missionsSortFunc
from gui.server_events.formatters import DECORATION_SIZES
from gui.shared.formatters import text_styles
from gui.shared.formatters.icons import makeImageTag
from helpers import dependency, time_utils, getLanguageCode
from helpers.i18n import makeString as _ms
from skeletons.gui.game_control import IRankedBattlesController, IBattleRoyaleController, IEpicBattleMetaGameController, IFunRandomController, IDebutBoxesController, IWinbackController, IUnseenEventsCounter, ISummerSaleController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from gui.server_events.event_items import Quest
_EventsBlockData = namedtuple(b'EventsBlockData', b'filteredCount totalCount blockData')
_MAIN_QUEST_AWARDS_COUNT = 6
_BIG_TOKENS_TRESHOLD = 2
awardsFormatters = MarathonAwardComposer(_MAIN_QUEST_AWARDS_COUNT)
tokenMarathonsCondFormatter = TokensMarathonFormatter()
_logger = logging.getLogger(__name__)

class GuiGroupBlockID(object):
    BASE = b'base'
    UNGROUPED_BLOCK = b'ungroupedBlock'
    REGULAR_GROUPED_BLOCK = b'regularGroupedBlock'
    MOTIVE_QUESTS_BLOCK = b'motiveQuestsBlock'
    MARATHON_GROUPED_BLOCK = b'marathonGroupedBlock'
    ELEN_QUEST_BLOCK = b'elenQuest'
    PREMIUM_QUESTS_BLOCK = b'premiumQuests'
    ORDER = (
     BASE,
     PREMIUM_QUESTS_BLOCK,
     UNGROUPED_BLOCK,
     REGULAR_GROUPED_BLOCK,
     MOTIVE_QUESTS_BLOCK,
     MARATHON_GROUPED_BLOCK,
     ELEN_QUEST_BLOCK)
    ORDER_INDICES = dict((n, i) for i, n in enumerate(ORDER))

    @classmethod
    def getBlockPriority(cls, blockID):
        return cls.ORDER_INDICES.get(blockID, 0)


def getGroupPackerByContextID(contextID, proxy):
    if contextID == DEFAULTS_GROUPS.UNGROUPED_QUESTS:
        return _UngroupedQuestsBlockInfo()
    else:
        if contextID == DEFAULTS_GROUPS.MOTIVE_QUESTS:
            return _MotiveQuestsBlockInfo()
        if contextID is not None and contextID != DEFAULTS_GROUPS.FOR_CURRENT_VEHICLE:
            groups = proxy.getGroups()
            group = groups.get(contextID)
            if group:
                groupID = group.getID()
                if group.isMarathon():
                    return _MissionsGroupQuestsBlockInfo(group)
                if group.isPremium():
                    return _PremiumGroupedQuestsBlockInfo()
                if isVersusAIQuest(groupID):
                    return _VersusAIGroupedQuestsBlockInfo(group)
                return _GroupedEventsBlockInfo(group)
        return


def _getMissionsCountLabel(completed, total):
    completed = text_styles.stats(completed)
    total = text_styles.standard(total)
    return text_styles.concatStylesToSingleLine(text_styles.standard(QUESTS.MISSIONS_TAB_CATEGORY_HEADER_PERFORMEDTASKS), text_styles.disabled(b'  %s / %s' % (completed, total)))


class _EventsBlockBuilder(object):

    def __init__(self):
        self._cache = defaultdict(dict)
        self.__initDefaultBlocks()
        return

    def init(self):
        self.invalidateBlocks()
        return

    def clear(self):
        self.__clearDefaultBlocks()
        self._cache.clear()
        return

    def getBlocksData(self, srvEvents, filterFunc):
        result = []
        for groupInfo in self.__getBlocksInfos():
            blockData = groupInfo.buildEventsBlockData(srvEvents, filterFunc)
            if blockData is not None:
                result.append(blockData)

        return result

    def getSuitableEvents(self):
        result = []
        for groupInfo in self.__getBlocksInfos():
            result.extend(groupInfo.getSuitableEvents())

        return result

    def markVisited(self):
        for groupInfo in self.__getBlocksInfos():
            groupInfo.markVisited()

        return

    def getBlocksAdvisableEvents(self, events):
        result = []
        for groupInfo in self.__getBlocksInfos():
            result.extend(groupInfo.getBlockAdvisableEvents(events))

        return result

    def invalidateBlocks(self):
        for groupInfo in self.__getBlocksInfos():
            groupInfo.invalidate()

        return

    def _getDefaultBlocks(self):
        return []

    def __initDefaultBlocks(self):
        defaults = self._cache[b'defaults']
        for blockInfo in self._getDefaultBlocks():
            defaults[blockInfo.getEventsBlockID()] = blockInfo

        return

    def __clearDefaultBlocks(self):
        defaults = self._cache[b'defaults']
        for gInfo in defaults.itervalues():
            gInfo.clear()

        defaults.clear()
        return

    def __getBlocksInfos(self):
        result = []
        resultExtend = result.extend
        for group in self._cache.itervalues():
            resultExtend(group.values())

        return sorted(result, key=(lambda blockInfo: blockInfo.getSortPriority()), reverse=True)


class VehicleGroupBuilder(_EventsBlockBuilder):

    def __init__(self):
        super(VehicleGroupBuilder, self).__init__()
        self.__em = EventManager()
        self.onBlocksDataChanged = Event(self.__em)
        return

    def init(self):
        super(VehicleGroupBuilder, self).init()
        g_currentVehicle.onChanged += self.__onVehicleChanged
        return

    def clear(self):
        super(VehicleGroupBuilder, self).clear()
        g_currentVehicle.onChanged -= self.__onVehicleChanged
        self.__em.clear()
        return

    def _getDefaultBlocks(self):
        return [_VehicleQuestsBlockInfo()]

    def __onVehicleChanged(self):
        self.onBlocksDataChanged()
        return


class GroupedEventsBlocksBuilder(_EventsBlockBuilder):
    eventsCache = dependency.descriptor(IEventsCache)

    def clear(self):
        cachedGroups = self._cache[b'groupedEvents']
        for blockInfo in cachedGroups.itervalues():
            blockInfo.clear()

        cachedGroups.clear()
        super(GroupedEventsBlocksBuilder, self).clear()
        return

    def invalidateBlocks(self):
        super(GroupedEventsBlocksBuilder, self).invalidateBlocks()
        newEventsGroups = self._getEventsGroups()
        cachedGroups = self._cache[b'groupedEvents']
        newGroupsKeys = set(newEventsGroups.keys())
        oldGroupsKeys = set(cachedGroups.keys())
        invalidGroupsIds = oldGroupsKeys.intersection(newGroupsKeys)
        newGroupsIds = newGroupsKeys.difference(invalidGroupsIds)
        lostGroupsIds = oldGroupsKeys.difference(invalidGroupsIds)
        for gID in lostGroupsIds:
            cachedGroups.pop(gID).clear()

        for gID in invalidGroupsIds:
            cachedGroups[gID].clear()
            cachedGroups[gID] = self._createGroupedEventsBlock(newEventsGroups[gID])

        for gID in newGroupsIds:
            cachedGroups[gID] = self._createGroupedEventsBlock(newEventsGroups[gID])

        return

    def _createGroupedEventsBlock(self, group):
        raise NotImplementedError
        return

    def _getEventsGroups(self):
        raise NotImplementedError
        return


class MissionsGroupsBuilder(GroupedEventsBlocksBuilder):
    __debutBoxesController = dependency.descriptor(IDebutBoxesController)

    def _createGroupedEventsBlock(self, group):
        if isDebutBoxesGroup(group.getID(), debutBoxesController=self.__debutBoxesController):
            return _DebutBoxesQuestsBlockInfo(group)
        return _MissionsGroupQuestsBlockInfo(group)

    def _getEventsGroups(self):
        return self.eventsCache.getGroups(filterFunc=(lambda g: g.isMarathon() or isDebutBoxesGroup(g.getID(), debutBoxesController=self.__debutBoxesController)))


class MarathonsDumbBuilder(GroupedEventsBlocksBuilder):

    def _createGroupedEventsBlock(self, group):
        return []

    def _getEventsGroups(self):
        return {}


class QuestsGroupsBuilder(GroupedEventsBlocksBuilder):
    lobbyContext = dependency.descriptor(ILobbyContext)
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    __rankedController = dependency.descriptor(IRankedBattlesController)
    __funRandomController = dependency.descriptor(IFunRandomController)
    __summerSaleController = dependency.descriptor(ISummerSaleController)

    def invalidateBlocks(self):
        super(QuestsGroupsBuilder, self).invalidateBlocks()
        group = getDailyEpicGroup()
        epicBattleQuestsAvailable = self.__epicController.isEnabled() and self.__epicController.isCurrentCycleActive()
        if group and epicBattleQuestsAvailable and EPIC_BATTLE_GROUPS_ID not in self._cache[b'groupedEvents']:
            self._cache[b'groupedEvents'][EPIC_BATTLE_GROUPS_ID] = self._createGroupedEventsBlock(group)
        _, isCycleActive = self.__battleRoyaleController.getCurrentCycleInfo()
        battleRoyaleQuestsAvailable = isCycleActive and (self.__battleRoyaleController.isInPrimeTime() or self.__battleRoyaleController.hasPrimeTimesLeftForCurrentCycle())
        group = getDailyBattleRoyaleGroup()
        if group and battleRoyaleQuestsAvailable and BATTLE_ROYALE_GROUPS_ID not in self._cache[b'groupedEvents']:
            self._cache[b'groupedEvents'][BATTLE_ROYALE_GROUPS_ID] = self._createGroupedEventsBlock(group)
        if self.__rankedController.getCurrentSeason() is not None:
            rankedDaily = getRankedDailyGroup()
            if rankedDaily and RANKED_DAILY_GROUP_ID not in self._cache[b'groupedEvents']:
                self._cache[b'groupedEvents'][RANKED_DAILY_GROUP_ID] = self._createGroupedEventsBlock(rankedDaily)
            rankedPlatform = getRankedPlatformGroup()
            if rankedPlatform and RANKED_PLATFORM_GROUP_ID not in self._cache[b'groupedEvents']:
                self._cache[b'groupedEvents'][RANKED_PLATFORM_GROUP_ID] = self._createGroupedEventsBlock(rankedPlatform)
        if self.__funRandomController.subModesInfo.isAvailable():
            funRandomGroup = getFunRandomDailyGroup()
            if funRandomGroup and FUN_RANDOM_GROUP_ID not in self._cache[b'groupedEvents']:
                self._cache[b'groupedEvents'][FUN_RANDOM_GROUP_ID] = self._createGroupedEventsBlock(funRandomGroup)
        elif FUN_RANDOM_GROUP_ID in self._cache[b'groupedEvents']:
            self._cache[b'groupedEvents'].pop(FUN_RANDOM_GROUP_ID)
        group = getPremiumGroup()
        if isPremiumQuestsEnable() and b'premium' not in self._cache[b'groupedEvents'].iterkeys() and group:
            self._cache[b'groupedEvents'][b'premium'] = _PremiumGroupedQuestsBlockInfo()
        return

    def _getDefaultBlocks(self):
        return [_MotiveQuestsBlockInfo(),
         _UngroupedQuestsBlockInfo()]

    def _createGroupedEventsBlock(self, group):
        groupID = group.getID()
        if isVersusAIQuest(groupID):
            return _VersusAIGroupedQuestsBlockInfo(group)
        if isSummerSaleGroup(group.getID(), summerSaleController=self.__summerSaleController):
            return _SummerSaleQuestsBlockInfo(group)
        return _GroupedQuestsBlockInfo(group)

    def _getEventsGroups(self):
        return self.eventsCache.getGroups(filterFunc=(lambda g: g.isRegularQuest()))


class ElenGroupsBuilder(_EventsBlockBuilder):

    def __init__(self):
        super(ElenGroupsBuilder, self).__init__()
        self._eventsData = None
        self._playerData = None
        self._myEventsTop = None
        self._currentEventID = None
        return

    def invalidateBlocks(self):
        super(ElenGroupsBuilder, self).invalidateBlocks()
        cachedGroups = OrderedDict()
        self._cache[b'elenEvents'] = cachedGroups
        events = self._eventsData.getEvents() if self._eventsData is not None else None
        if events is None:
            return
        else:
            for event in events:
                isChosen = self._currentEventID == event.getEventID()
                cachedGroups[event.getEventID()] = _ElenBlockInfo(event, self._myEventsTop, self._playerData, isChosen)

            return

    def setEventsData(self, eventsData, playerData, myEventsTop, currentEventID):
        self._eventsData = weakref.proxy(eventsData)
        self._playerData = weakref.proxy(playerData)
        self._myEventsTop = weakref.proxy(myEventsTop)
        self._currentEventID = currentEventID
        self.invalidateBlocks()
        return


class _EventsBlockInfo(object):
    blockType = GuiGroupBlockID.BASE
    __unseenEventsManager = dependency.descriptor(IUnseenEventsCounter)

    def __init__(self, headerLinkage=b'', bodyLinkage=b''):
        self._headerLinkage = headerLinkage
        self._bodyLinkage = bodyLinkage
        self._events = ()
        self._suitableEvents = ()
        self._cachedInfo = {}
        return

    def getSuitableEvents(self):
        return self._suitableEvents

    def invalidate(self):
        self._cachedInfo.clear()
        return

    def getSortPriority(self):
        return (self._getGuiBlockPriority(), self._getAdvancePriority())

    def buildEventsBlockData(self, srvEvents, filterFunc):
        self._suitableEvents = self.findEvents(srvEvents)
        self._events = filter(filterFunc, self._suitableEvents)
        return _EventsBlockData(len(self._events), len(self._suitableEvents), self._getVO())

    def getBlockAdvisableEvents(self, srvEvents):
        return self.findEvents(srvEvents)

    def markVisited(self):
        self.__unseenEventsManager.seenEvents({e.getID(): 1 for e in self._suitableEvents})
        return

    def clear(self):
        self._events = ()
        self._suitableEvents = ()
        self._cachedInfo.clear()
        return

    def getEventsBlockID(self):
        raise NotImplementedError
        return

    def findEvents(self, srvEvents):
        return sorted(self._findEvents(srvEvents), key=missionsSortFunc, reverse=True)

    def _getGuiBlockPriority(self):
        return GuiGroupBlockID.getBlockPriority(self.blockType)

    def _getAdvancePriority(self):
        return 0

    def _findEvents(self, srvEvents):
        raise NotImplementedError
        return

    def _getVO(self):
        vo = self._getGuiLinkages()
        vo.update({b'blockId': (self.getEventsBlockID()), 
           b'headerData': (self._getHeaderData()), 
           b'bodyData': (self._getBodyData())})
        return vo

    def _getMainQuest(self):
        return

    def _getGuiLinkages(self):
        return {b'headerLinkage': (self._headerLinkage), 
           b'bodyLinkage': (self._bodyLinkage)}

    def _getBodyData(self):
        cardsList = []
        for e in self._events:
            eventID = e.getID()
            if eventID in self._cachedInfo:
                missionData = self._cachedInfo[eventID]
            else:
                missionData = getMissionInfoData(e)
                self._cachedInfo[eventID] = missionData
            if missionData is not None:
                cardsList.append(missionData.getInfo())

        if not cardsList and self._suitableEvents:
            return {b'missions': cardsList, 
               b'dummy': {b'iconSource': (RES_ICONS.MAPS_ICONS_LIBRARY_ALERTBIGICON), 
                          b'htmlText': (text_styles.alert(_ms(QUESTS.MISSIONS_NOTASKSBODY_DUMMY_TEXT))), 
                          b'alignCenter': False, 
                          b'btnVisible': True, 
                          b'btnLabel': (QUESTS.MISSIONS_NOTASKSBODY_DUMMY_BTNLABEL), 
                          b'btnTooltip': b'', 
                          b'btnEvent': b'ResetFilterEvent', 
                          b'btnLinkage': (BUTTON_LINKAGES.BUTTON_BLACK)}}
        else:
            return {b'missions': cardsList}

    def _getHeaderData(self):
        raise NotImplementedError
        return


class _CollapsableEventsBlockInfo(_EventsBlockInfo):

    def _getVO(self):
        data = super(_CollapsableEventsBlockInfo, self)._getVO()
        data.update({b'isCollapsed': (settings.isGroupMinimized(self.getEventsBlockID()))})
        return data


class _GroupedEventsBlockInfo(_CollapsableEventsBlockInfo):
    eventsCache = dependency.descriptor(IEventsCache)
    blockType = GuiGroupBlockID.REGULAR_GROUPED_BLOCK

    def __init__(self, group, headerLinkage=b'', bodyLinkage=b''):
        super(_GroupedEventsBlockInfo, self).__init__(headerLinkage, bodyLinkage)
        self._group = group
        self._filterEnable = True
        return

    def buildEventsBlockData(self, srvEvents, filterFunc):
        self._suitableEvents = self.findEvents(srvEvents)
        self._events = filter(filterFunc, self._suitableEvents) if self._filterEnable else self._suitableEvents
        if not self._suitableEvents:
            return None
        else:
            return _EventsBlockData(len(self._events), len(self._suitableEvents), self._getVO())

    def clear(self):
        self._group = None
        return

    def getEventsBlockID(self):
        return self._group.getID()

    def getTitle(self):
        return text_styles.promoTitle(self._group.getUserName())

    def getTitleBlock(self):
        linkedActionID = self._group.getLinkedAction(self.eventsCache.getActions())
        return {b'title': (self.getTitle()), 
           b'action': {b'actionID': linkedActionID, 
                       b'label': (text_styles.tutorial(QUESTS.MISSIONS_TAB_MARATHONS_HEADER_TITLE_ACTION)), 
                       b'visible': (linkedActionID is not None)}}

    def _findEvents(self, srvEvents):
        return self._group.getGroupContent(srvEvents)

    def _getAdvancePriority(self):
        if not self._group:
            return 0
        return self._group.getPriority()

    def _getDescrBlock(self):
        minStartTime = min([q.getStartTime() for q in self._suitableEvents])
        maxFinishTime = max([q.getFinishTime() for q in self._suitableEvents])
        return {b'period': (text_styles.middleTitle(_ms(QUESTS.MISSIONS_TAB_MARATHONS_HEADER_PERIOD, startDate=backport.getLongDateFormat(minStartTime), endDate=backport.getLongDateFormat(maxFinishTime)))), 
           b'isMultiline': True, 
           b'hasCalendarIcon': True}

    def _getHeaderData(self):
        return {b'titleBlock': (self.getTitleBlock()), 
           b'descBlock': (self._getDescrBlock())}


class _GroupedQuestsBlockInfo(_GroupedEventsBlockInfo):
    blockType = GuiGroupBlockID.REGULAR_GROUPED_BLOCK
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def __init__(self, group, headerLinkage=QUESTS_ALIASES.MISSION_PACK_CATEGORY_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE):
        super(_GroupedQuestsBlockInfo, self).__init__(group, headerLinkage, bodyLinkage)
        self._totalQuestsCount = 0
        self._completedQuestsCount = 0
        return

    def _findEvents(self, srvEvents):
        groupId = self.getEventsBlockID()
        if groupId == BATTLE_ROYALE_GROUPS_ID:
            currentSeason = self.__battleRoyaleController.getCurrentSeason()
            isSeasonActive = currentSeason is not None and self.__battleRoyaleController.getCurrentCycleInfo()[1]
            if self.__battleRoyaleController.isEnabled() and isSeasonActive:
                result = self.__battleRoyaleController.getQuests().values()
            else:
                result = []
        else:
            result = self._group.getGroupContent(srvEvents)
        self._completedQuestsCount = 0
        for quest in result:
            if quest.isCompleted():
                self._completedQuestsCount += 1

        self._totalQuestsCount = len(result)
        return result

    def _getDescrBlock(self):
        data = super(_GroupedQuestsBlockInfo, self)._getDescrBlock()
        data.update({b'isMultiline': False})
        data.update({b'descr': (_getMissionsCountLabel(self._completedQuestsCount, self._totalQuestsCount))})
        return data


class _MissionsGroupQuestsBlockInfo(_GroupedEventsBlockInfo):
    blockType = GuiGroupBlockID.MARATHON_GROUPED_BLOCK

    def __init__(self, group):
        super(_MissionsGroupQuestsBlockInfo, self).__init__(group, headerLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE)
        self._mainQuest = None
        return

    def clear(self):
        self._mainQuest = None
        super(_MissionsGroupQuestsBlockInfo, self).clear()
        return

    def _findEvents(self, srvEvents):
        suitableEvents = self._group.getGroupContent(srvEvents)
        self._mainQuest = self._group.getMainQuest(suitableEvents)
        if self._mainQuest:
            suitableEvents.remove(self._mainQuest)
        return suitableEvents

    def _getMainQuest(self):
        return self._mainQuest

    def _getDescrBlock(self):
        data = super(_MissionsGroupQuestsBlockInfo, self)._getDescrBlock()
        if self._mainQuest:
            data.update({b'descr': (text_styles.main(self._mainQuest.getDescription()))})
        return data

    def _getHeaderData(self):
        tokensData = []
        awardsData = []
        awardImgTooltip = None
        awardImgSource = b''
        prefetcher = self.eventsCache.prefetcher
        if self._mainQuest:
            tokensData = tokenMarathonsCondFormatter.format(self._mainQuest)
            uiDecoration = self._mainQuest.getIconID()
            if uiDecoration:
                awardImgSource = prefetcher.getMissionDecoration(uiDecoration, DECORATION_SIZES.BONUS)
                awardImgTooltip = {b'isSpecial': True, 
                   b'specialAlias': (TOOLTIPS_CONSTANTS.ADDITIONAL_AWARDS), 
                   b'specialArgs': (awardsFormatters.getShortBonusesData(self._mainQuest.getBonuses()))}
            else:
                awardsData = awardsFormatters.getFormattedBonuses(self._mainQuest.getBonuses(), AWARDS_SIZES.BIG)
        return {b'uiDecoration': (prefetcher.getMissionDecoration(self._group.getIconID(), DECORATION_SIZES.MARATHON)), b'titleBlock': (self.getTitleBlock()), 
           b'descBlock': (self._getDescrBlock()), 
           b'conditionBlock': {b'title': (text_styles.middleTitle(QUESTS.MISSIONS_TAB_MARATHONS_HEADER_CONDITION)), 
                               b'tokensData': tokensData}, 
           b'awardBlock': {b'title': (text_styles.middleTitle(QUESTS.MISSIONS_TAB_MARATHONS_HEADER_AWARD)), 
                           b'awardsData': awardsData, 
                           b'awardImgSource': awardImgSource, 
                           b'awardImgTooltip': awardImgTooltip}}


class _DebutBoxesQuestsBlockInfo(_GroupedEventsBlockInfo):
    blockType = GuiGroupBlockID.MARATHON_GROUPED_BLOCK
    __debutBoxesController = dependency.descriptor(IDebutBoxesController)

    def __init__(self, group):
        super(_DebutBoxesQuestsBlockInfo, self).__init__(group, headerLinkage=QUESTS_ALIASES.MISSION_PACK_DEBUT_BOXES_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE)
        return

    def _getVO(self):
        data = super(_DebutBoxesQuestsBlockInfo, self)._getVO()
        if not self.__debutBoxesController.isEnabled():
            data.update({b'isCollapsed': True})
        return data

    def _getHeaderData(self):
        data = super(_DebutBoxesQuestsBlockInfo, self)._getHeaderData()
        data.update({b'isEnabled': (self.__debutBoxesController.isEnabled())})
        return data

    def _getBodyData(self):
        if not self.__debutBoxesController.isEnabled():
            return {b'missions': []}
        return super(_DebutBoxesQuestsBlockInfo, self)._getBodyData()


class _SummerSaleQuestsBlockInfo(_GroupedEventsBlockInfo):
    blockType = GuiGroupBlockID.MARATHON_GROUPED_BLOCK
    __summerSaleController = dependency.descriptor(ISummerSaleController)

    def __init__(self, group):
        super(_SummerSaleQuestsBlockInfo, self).__init__(group, headerLinkage=QUESTS_ALIASES.MISSION_PACK_SUMMER_SALE_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE)
        return

    def _getVO(self):
        data = super(_SummerSaleQuestsBlockInfo, self)._getVO()
        if not self.__summerSaleController.isEnabled():
            data.update({b'isCollapsed': True})
        return data

    def _getHeaderData(self):
        data = super(_SummerSaleQuestsBlockInfo, self)._getHeaderData()
        data.update({b'isEnabled': (self.__summerSaleController.isEnabled())})
        return data

    def _getDescrBlock(self):
        data = super(_SummerSaleQuestsBlockInfo, self)._getDescrBlock()
        data.update({b'isMultiline': False})
        return data

    def _getBodyData(self):
        if not self.__summerSaleController.isEnabled():
            return {b'missions': []}
        return super(_SummerSaleQuestsBlockInfo, self)._getBodyData()


class _UngroupedQuestsBlockInfo(_CollapsableEventsBlockInfo):
    blockType = GuiGroupBlockID.UNGROUPED_BLOCK

    def __init__(self):
        super(_UngroupedQuestsBlockInfo, self).__init__(headerLinkage=QUESTS_ALIASES.MISSION_PACK_CATEGORY_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE)
        self.__totalQuestsCount = 0
        self.__completedQuestsCount = 0
        return

    def buildEventsBlockData(self, srvEvents, filterFunc):
        self._suitableEvents = self.findEvents(srvEvents)
        self._events = filter(filterFunc, self._suitableEvents)
        if not self._suitableEvents:
            return None
        else:
            return _EventsBlockData(len(self._events), len(self._suitableEvents), self._getVO())

    def getEventsBlockID(self):
        return DEFAULTS_GROUPS.UNGROUPED_QUESTS

    def getTitle(self):
        return text_styles.promoTitle(QUESTS.QUESTS_TITLE_UNGOUPEDQUESTS)

    def getTitleBlock(self):
        return {b'title': (self.getTitle())}

    def getDetailedTitle(self):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _findEvents(self, srvEvents):
        suitabaleQuests = [q for q in srvEvents.itervalues() if q.getGroupID() == DEFAULTS_GROUPS.UNGROUPED_QUESTS and q.getType() != EVENT_TYPE.MOTIVE_QUEST]
        self.__totalQuestsCount = len(suitabaleQuests)
        self.__completedQuestsCount = len([q for q in suitabaleQuests if q.isCompleted()])
        return suitabaleQuests

    def _getHeaderData(self):
        return {b'titleBlock': (self.getTitleBlock()), 
           b'descBlock': (self._getDescrBlock())}

    def _getDescrBlock(self):
        return {b'descr': (_getMissionsCountLabel(self.__completedQuestsCount, self.__totalQuestsCount)), 
           b'period': (text_styles.middleTitle(QUESTS.MISSIONS_GROUP_OTHERS_LABEL)), 
           b'hasCalendarIcon': False, 
           b'isMultiline': False}


class _MotiveQuestsBlockInfo(_CollapsableEventsBlockInfo):
    blockType = GuiGroupBlockID.MOTIVE_QUESTS_BLOCK

    def __init__(self):
        super(_MotiveQuestsBlockInfo, self).__init__(headerLinkage=QUESTS_ALIASES.MISSION_PACK_CATEGORY_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE)
        return

    def buildEventsBlockData(self, srvEvents, filterFunc):
        self._suitableEvents = self.findEvents(srvEvents)
        self._events = filter(filterFunc, self._suitableEvents)
        if not self._suitableEvents:
            return None
        else:
            return _EventsBlockData(len(self._events), len(self._suitableEvents), self._getVO())

    def getEventsBlockID(self):
        return DEFAULTS_GROUPS.MOTIVE_QUESTS

    def getTitle(self):
        return text_styles.promoTitle(MOTIVATION_QUESTS.GROUP)

    def getTitleBlock(self):
        return {b'title': (self.getTitle())}

    def _findEvents(self, srvEvents):
        suitabaleQuests = [q for q in srvEvents.itervalues() if q.getType() == EVENT_TYPE.MOTIVE_QUEST and not q.isCompleted() and q.isAvailable()[0]]
        return suitabaleQuests

    def _getHeaderData(self):
        return {b'titleBlock': (self.getTitleBlock()), 
           b'descBlock': (self._getDescrBlock())}

    def _getDescrBlock(self):
        return {b'descr': b'', 
           b'period': (text_styles.middleTitle(QUESTS.MISSIONS_GROUP_MOTIVE_LABEL)), 
           b'hasCalendarIcon': False, 
           b'isMultiline': False}


class _VehicleQuestsBlockInfo(_EventsBlockInfo):

    def __init__(self):
        super(_VehicleQuestsBlockInfo, self).__init__(headerLinkage=QUESTS_ALIASES.MISSION_PACK_CURRENT_VEHICLE_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSION_PACK_MARATHON_BODY_LINKAGE)
        return

    def getEventsBlockID(self):
        return DEFAULTS_GROUPS.FOR_CURRENT_VEHICLE

    def getTitleBlock(self):
        tankInfo = b''
        tankType = b''
        if g_currentVehicle.isPresent():
            item = g_currentVehicle.item
            tankInfo = text_styles.concatStylesToMultiLine(text_styles.promoSubTitle(item.userName), text_styles.stats(MENU.levels_roman(item.level)))
            tankType = b'../maps/icons/vehicleTypes/big/%s.png' % item.type
        return {b'title': (self.getTitle()), b'tankType': tankType, 
           b'tankInfo': tankInfo}

    def _findEvents(self, srvEvents):
        return filter(self.__applyFilter, srvEvents.itervalues())

    def getTitle(self):
        return text_styles.promoTitle(QUESTS.QUESTS_TITLE_CURRENTLYAVAILABLE)

    def _getHeaderData(self):
        return {b'titleBlock': (self.getTitleBlock())}

    def __applyFilter(self, quest):
        forbiddenQuestConditions = [
         (lambda q: q.getType() in (EVENT_TYPE.TOKEN_QUEST,)),
         (lambda q: not q.getFinishTimeLeft()),
         (lambda q: isBattleMattersQuestID(q.getGroupID()) or isPremium(q.getGroupID()))]
        if any(isForbidden(quest) for isForbidden in forbiddenQuestConditions):
            return False
        if not g_currentVehicle.isPresent():
            return False
        if quest.getType() != EVENT_TYPE.MOTIVE_QUEST:
            return quest.isValidVehicleCondition(g_currentVehicle.item)
        return quest.isValidVehicleCondition(g_currentVehicle.item) and not quest.isCompleted() and quest.isAvailable()[0]


class _ElenBlockInfo(_EventsBlockInfo):
    blockType = GuiGroupBlockID.ELEN_QUEST_BLOCK

    def __init__(self, event, eventsTop, playerData, isChosen):
        super(_ElenBlockInfo, self).__init__(headerLinkage=QUESTS_ALIASES.MISSIONS_EVENT_BOARDS_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSIONS_EVENT_BOARDS_BODY_LINKAGE)
        self._event = event
        self._eventsTop = eventsTop
        self._playerData = playerData
        self._isChosen = isChosen
        return

    def getEventsBlockID(self):
        return self._event.getEventID()

    def getTitleBlock(self):
        return {b'title': (self._event.getName())}

    def buildEventsBlockData(self, srvEvents, filterFunc):
        return _EventsBlockData(1, 1, self._getVO())

    def _findEvents(self, srvEvents):
        raise SoftException(b'This method should not be reached in this context')
        return

    def _getHeaderData(self):
        eventInfo = EventHeader(self._event, self._playerData)
        data = {b'titleBlock': (self.getTitleBlock())}
        data.update(eventInfo.getInfo())
        return data

    def _getVO(self):
        data = super(_ElenBlockInfo, self)._getVO()
        minimized = isGroupMinimized(self._event)
        if self._isChosen and minimized:
            expandGroup(self._event, True)
            minimized = False
        data.update({b'isCollapsed': minimized})
        data[b'bgAlpha'] = 1
        return data

    def _getBodyData(self):
        event = EventInfo(self._event, self._playerData, self._eventsTop)
        top = event.getTopInfo()
        result = {b'missions': top, 
           b'taskBlock': (event.getTaskInfo()), 
           b'conditionBlock': (event.getConditionInfo()), 
           b'awardBlock': (event.getAwardInfo()), 
           b'isEventBegan': (self._event.isStarted()), 
           b'uiDecoration': (self._event.getKeyArtBig()), 
           b'popoverAlias': (event.getPopoverAlias()), 
           b'eventID': (self._event.getEventID())}
        result.update(event.getServerData())
        result.update(event.getStatusData())
        if top:
            result.update({b'taskBlock': (event.getTaskInfo()), 
               b'conditionBlock': (event.getConditionInfo()), 
               b'awardBlock': (event.getAwardInfo())})
        return result


class _PremiumGroupedQuestsBlockInfo(_GroupedQuestsBlockInfo):
    blockType = GuiGroupBlockID.PREMIUM_QUESTS_BLOCK
    groupID = b'prem_acc_qroup'
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        group = getPremiumGroup()
        super(_PremiumGroupedQuestsBlockInfo, self).__init__(group, headerLinkage=QUESTS_ALIASES.MISSIONS_GOLD_HEADER_LINKAGE, bodyLinkage=QUESTS_ALIASES.MISSIONS_PREMIUM_BODY_LINKAGE)
        self._filterEnable = False
        return

    def findEvents(self, srvEvents):
        return sorted(self._findEvents(srvEvents), key=dailyQuestsSortFunc, reverse=False)

    def getTitle(self):
        title = backport.text(R.strings.quests.premiumQuests.header.default())
        return (b'{}{}').format(makeImageTag(backport.image(R.images.gui.maps.icons.premacc.icons.premium_40x40()), 40, 40, -12), title)

    def _getVO(self):
        vo = super(_PremiumGroupedQuestsBlockInfo, self)._getVO()
        vo[b'bodyDataPremium'] = vo.pop(b'bodyData')
        vo[b'isPremium'] = True
        return vo

    def _getBodyData(self):
        cardsList = []
        for e in self._events:
            eventID = e.getID()
            if eventID in self._cachedInfo:
                missionData = self._cachedInfo[eventID]
            else:
                missionData = getMissionInfoData(e)
                self._cachedInfo[eventID] = missionData
            cardsList.append(missionData.getInfo())

        isPremEnabled = self.__isPremiumEnabled()
        isAllCompleted = self._completedQuestsCount == self._totalQuestsCount
        timeStr = self.__getDailyResetStatus()
        completeTitle = text_styles.missionStatusAvailable(backport.text(R.strings.quests.premiumQuests.body.complete(), time=timeStr) if isAllCompleted else b'')
        return {b'missions': cardsList, 
           b'title': (text_styles.promoTitle(QUESTS.PREMIUMQUESTS_BODY_TITLE)), 
           b'description': (text_styles.highlightText(QUESTS.PREMIUMQUESTS_BODY_DESCRIPTION)), 
           b'buttonDetails': (QUESTS.PREMIUMQUESTS_BODY_BUTTONDETAILS), 
           b'icon': (backport.image(R.images.gui.maps.icons.premacc.icons.premium_256x242())), 
           b'hasPremium': isPremEnabled, 
           b'completeTitle': completeTitle, 
           b'uiDecoration': (backport.image(R.images.gui.maps.icons.premacc.quests.background()))}

    def _getHeaderData(self):
        info = _getMissionsCountLabel(self._completedQuestsCount, self._totalQuestsCount)
        return {b'titleBlock': (self.getTitleBlock()), 
           b'info': info}

    def __isPremiumEnabled(self):
        return self.__itemsCache.items.stats.isActivePremium(PREMIUM_TYPE.PLUS)

    @staticmethod
    def __getDailyResetStatus():
        timeLeft = time_utils.ONE_DAY - time_utils.getServerRegionalTimeCurrentDay()
        if timeLeft >= 0:
            timeFmt = backport.text(R.strings.quests.details.conditions.postBattle.deltaDailyReset.timeFmt())
            parts = time_utils.getTimeStructInUTC(timeLeft)
            try:
                return time.strftime(timeFmt, parts)
            except ValueError:
                _logger.error(b'Current time locale: %r', locale.getlocale(locale.LC_TIME))
                _logger.error(b'Selected language: %r', getLanguageCode())
                _logger.exception(b'Invalid formatting string %r to delta of time %r', timeFmt, parts)

        return b''


class _VersusAIGroupedQuestsBlockInfo(_GroupedQuestsBlockInfo):

    def _findEvents(self, srvEvents):
        result = self._getQuests(srvEvents)
        self._completedQuestsCount = 0
        for quest in result:
            if quest.isCompleted():
                self._completedQuestsCount += 1

        self._totalQuestsCount = len(result)
        return result

    def _getDescrBlock(self):
        descriptionBlockInfo = super(_VersusAIGroupedQuestsBlockInfo, self)._getDescrBlock()
        descriptionBlockInfo[b'period'] = b''
        descriptionBlockInfo.pop(b'descr', None)
        return descriptionBlockInfo

    def _getQuests(self, srvEvents):
        winbackController = dependency.getInstanceIfHas(IWinbackController)
        if winbackController is None or not winbackController.isProgressionEnabled():
            return []
        return [quest for quest in self._group.getGroupContent(srvEvents) if quest.isCompleted() or quest.accountReqs.isAvailable()]
