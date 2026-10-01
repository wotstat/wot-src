import sys
from Queue import PriorityQueue
from enum import IntEnum
from wotdecorators import singleton
from chat_shared import SYS_MESSAGE_TYPE
from helpers import dependency
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.game_control.AwardController import ServiceChannelHandler
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.notifications import NotificationPriorityLevel
from portal.gui.portal_event_helpers import isPortalProgressionQuest, PROGRESSION_QUEST_PREFIX, isPortalLastLevelQuest, isPortalAllVehicleUpgradesQuest
from portal.gui.shared.event_dispatcher import showAwardsView
from portal.gui.shared.events import PortalComplexity
from portal.messenger.formatters.portal_formatters import PortalQuestAchievesFormatter
from portal.skeletons.portal_event_controller import IPortalEventController
from skeletons.gui.server_events import IEventsCache

@singleton
class _AwardViewQueue(object):

    def __init__(self):
        self.__viewQueue = PriorityQueue()
        self.__hasActiveView = False
        self.__currentCallback = None
        return

    def show(self, priority, rewardsData, callback=None):
        if self.__hasActiveView:
            self.__viewQueue.put((priority, rewardsData, callback))
        else:
            self.__showAwardsView(rewardsData, callback)
        return

    def close(self):
        if self.__currentCallback:
            self.__currentCallback()
            self.__currentCallback = None
        if self.__viewQueue.empty():
            self.__hasActiveView = False
            return
        else:
            _, awardsData, callback = self.__viewQueue.get()
            self.__showAwardsView(awardsData, callback)
            return

    def __showAwardsView(self, rewardsData, callback):
        self.__hasActiveView = True
        self.__currentCallback = callback
        showAwardsView(rewardsData, self.close)
        return


class AwardType(IntEnum):
    PROGRESSION = 0
    LAST_LEVEL_VICTORY = 1
    ALL_VEHICLES_UPGRADED = 2


class PortalProgressionAwardHandler(ServiceChannelHandler):
    __portalController = dependency.descriptor(IPortalEventController)
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, awardsController):
        super(PortalProgressionAwardHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardsController)
        self._achievesFormatter = PortalQuestAchievesFormatter()
        return

    def _showAward(self, ctx):
        data = ctx[1].data
        for questID in data.get(b'completedQuestIDs', set()):
            formattedRewards = self._achievesFormatter.formatQuestAchieves(data.get(b'detailedRewards', {}).get(questID, {}), asBattleFormatter=False)
            if isPortalProgressionQuest(questID):
                self.__showProgressionAward(questID, data, formattedRewards)
            elif isPortalLastLevelQuest(questID):
                self.__showLastLevelVictoryAward(questID, data, formattedRewards)
            elif isPortalAllVehicleUpgradesQuest(questID):
                self.__showAllVehiclesUpgraded(questID, data, formattedRewards)

        return

    def __showProgressionAward(self, questID, data, formattedRewards):
        stage = int(questID[len(PROGRESSION_QUEST_PREFIX):])
        rewardsData = {b'type': (AwardType.PROGRESSION), 
           b'stage': stage, 
           b'rewards': (data.get(b'detailedRewards', {}).get(questID, {}))}
        _AwardViewQueue.show(stage, rewardsData)
        return

    def __getRewards(self, questID):
        quests = self.__eventsCache.getAllQuests((lambda quest: quest.getID() == questID))
        bonuses = quests[questID].getBonuses()
        formattedList = []
        for reward in bonuses:
            for item in reward.formattedList():
                formattedList.append(item)

        return (b'{0}').format((b'\n').join(formattedList))

    def __showLastLevelVictoryAward(self, questID, data, formattedRewards):
        rewardsData = {b'type': (AwardType.LAST_LEVEL_VICTORY), 
           b'rewards': (data.get(b'detailedRewards', {}).get(questID, {}))}
        _AwardViewQueue.show(sys.maxint, rewardsData, self.__portalController.showOutroVideo)
        return

    def __showAllVehiclesUpgraded(self, questID, data, formattedRewards):
        rewardsData = {b'type': (AwardType.ALL_VEHICLES_UPGRADED), 
           b'rewards': (data.get(b'detailedRewards', {}).get(questID, {}))}
        _AwardViewQueue.show(sys.maxint, rewardsData)
        return


class PortalUnlockedComplexityHandler(ServiceChannelHandler):

    def __init__(self, awardsController):
        super(PortalUnlockedComplexityHandler, self).__init__(SYS_MESSAGE_TYPE.portalBattleResults.index(), awardsController)
        return

    def _needToShowAward(self, ctx):
        if not super(PortalUnlockedComplexityHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        data = message.data
        return b'portalUnlockedComplexityLevel' in data

    def _showAward(self, ctx):
        _, message = ctx
        unlockedComplexityLevel = message.data.get(b'portalUnlockedComplexityLevel', None)
        if not unlockedComplexityLevel:
            return
        else:
            battleLevelName = backport.text(R.strings.portal_lobby.complexity.level.dyn((b'c_{}').format(unlockedComplexityLevel))())
            SystemMessages.pushMessage(text=backport.text(R.strings.portal_messenger.serviceChannelMessages.portalDifficultyLevel.body(), level=battleLevelName), type=SystemMessages.SM_TYPE.PortalDifficultyLevelChanged, priority=NotificationPriorityLevel.MEDIUM)
            g_eventBus.handleEvent(PortalComplexity(PortalComplexity.UNLOCKED, ctx={b'level': unlockedComplexityLevel}), EVENT_BUS_SCOPE.DEFAULT)
            return
