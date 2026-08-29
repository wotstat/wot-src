import typing
from collections import OrderedDict
import Event
from constants import EVENT_CLIENT_DATA
from gui.ClientUpdateManager import g_clientUpdateManager
from shared_utils import first, _logger
from helpers import dependency
from mt_birthday.skeletons.sub_controllers import ITanksBirthdayProgressionSubController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from mt_birthday_common.constants import MT_BIRTHDAY_QUEST_PROGRESSION_ID, MT_BIRTHDAY_QUEST_PROGRESSION_ID_FORMAT, MT_BIRTHDAY_PROGRESSION_TOKEN, MT_BIRTHDAY_INFINITY_COMPLETE_TOKEN, MT_BIRTHDAY_INFINITY_PROGRESSION_TOKEN
if typing.TYPE_CHECKING:
    from gui.server_events.event_items import Quest
    from typing import Dict, Tuple, List

class TanksBirthdayProgressionSubController(ITanksBirthdayProgressionSubController):
    __eventsCache = dependency.descriptor(IEventsCache)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, eManager):
        self.onProgressionUpdated = Event.Event(eManager)
        self.__progressionConfig = None
        return

    def start(self):
        g_clientUpdateManager.addCallback(b'tokens', self.__onTokensUpdate)
        g_clientUpdateManager.addCallback(b'eventsData', self.__onEventsDataUpdated)
        return

    def stop(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__progressionConfig = None
        return

    def parseQuests(self):
        progressionConfig = self.__parseEventData(self.__eventsCache.getHiddenQuests(filterFunc=(lambda quest: self.isBirthdayProgressionQuest(quest.getID()))))
        return progressionConfig

    @property
    def progressionConfig(self):
        if self.__progressionConfig is None:
            self.__progressionConfig = self.parseQuests()
        return self.__progressionConfig

    def __parseEventData(self, eventData):
        levels = OrderedDict()
        lastRequiredProgressionPoints = 0
        maxLevelIdx = len(eventData)
        for levelIdx in range(1, maxLevelIdx + 1):
            if levelIdx < maxLevelIdx:
                isInfinity = False
            else:
                isInfinity = True
            if levelIdx <= len(eventData):
                quest = eventData.get(MT_BIRTHDAY_QUEST_PROGRESSION_ID_FORMAT.format(levelIdx), None)
                if quest is None:
                    _logger.error(b'Wrong MT_BIRTHDAY progression level quest format!')
                    return {}
                requiredProgressionPoints = self.getProgressionPointsRequiredFromQuest(quest)
            else:
                quest = None
                requiredProgressionPoints = float(b'inf')
            if requiredProgressionPoints < 1:
                _logger.error(b'Wrong MT_BIRTHDAY progression level quest format!')
                return {}
            if quest is not None:
                bonuses = quest.getBonuses()
            else:
                bonuses = None
            levels[levelIdx] = {b'minProgressionPoints': lastRequiredProgressionPoints, 
               b'maxProgressionPoints': requiredProgressionPoints, 
               b'bonuses': bonuses, 
               b'isInfinity': isInfinity}
            lastRequiredProgressionPoints = requiredProgressionPoints

        return levels

    @staticmethod
    def isBirthdayProgressionQuest(qID):
        return qID.startswith(MT_BIRTHDAY_QUEST_PROGRESSION_ID)

    @staticmethod
    def getProgressionPointsRequiredFromQuest(questData):
        return first((t.getNeededCount() for t in questData.accountReqs.getTokens() if t.getID() == MT_BIRTHDAY_PROGRESSION_TOKEN), default=0)

    def __onEventsDataUpdated(self, diff):
        if EVENT_CLIENT_DATA.QUEST in diff:
            self.__progressionConfig = None
            self.onProgressionUpdated()
        return

    def __onTokensUpdate(self, diff):
        if MT_BIRTHDAY_PROGRESSION_TOKEN in diff or MT_BIRTHDAY_INFINITY_PROGRESSION_TOKEN in diff:
            self.onProgressionUpdated()
        return

    def getProgressionTokensCount(self):
        return self.__itemsCache.items.tokens.getTokenCount(MT_BIRTHDAY_PROGRESSION_TOKEN)

    def getInfinityProgressionTokensCount(self):
        return self.__itemsCache.items.tokens.getTokenCount(MT_BIRTHDAY_INFINITY_COMPLETE_TOKEN)

    def isInfinityLevel(self):
        return bool(self.__itemsCache.items.tokens.getTokenCount(MT_BIRTHDAY_INFINITY_PROGRESSION_TOKEN))

    def getCurrentProgressionLevel(self):
        progressionTokenCount = self.getProgressionTokensCount()
        for level, value in self.progressionConfig.iteritems():
            if value[b'minProgressionPoints'] <= progressionTokenCount < value[b'maxProgressionPoints']:
                return (level, self.progressionConfig[level])

        infLevelIdx, infLevelQuest = self.getInfinityLevel()
        if progressionTokenCount >= infLevelQuest[b'maxProgressionPoints']:
            return (infLevelIdx, infLevelQuest)
        else:
            return (None, None)

    def getLevelByPoints(self, points):
        for level, value in self.progressionConfig.iteritems():
            if value[b'minProgressionPoints'] <= points < value[b'maxProgressionPoints']:
                return (level, self.progressionConfig[level])

        return (None, None)

    def getInfinityLevel(self):
        for levelIdx, levelQuest in self.progressionConfig.iteritems():
            if levelQuest[b'isInfinity']:
                return (levelIdx, levelQuest)

        return

    def getSimpleLevels(self):
        levels = []
        for levelIdx, levelQuest in self.progressionConfig.iteritems():
            if not levelQuest[b'isInfinity']:
                levels.append((levelIdx, levelQuest))

        return levels
