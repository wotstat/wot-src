import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    import Event
    from typing import Dict, Tuple, List, Union
    from gui.server_events.event_items import Quest
    from gui.server_events.bonuses import SimpleBonus

class ICosmicEventProgressionController(IGameController):
    onProgressPointsUpdated = None

    def getQuests(self):
        raise NotImplementedError
        return

    def getDailyQuests(self):
        raise NotImplementedError
        return

    def getAchievementsQuests(self):
        raise NotImplementedError
        return

    def getCurrentPoints(self):
        raise NotImplementedError
        return

    def getMaxProgressionPoints(self):
        raise NotImplementedError
        return

    def getProgression(self):
        raise NotImplementedError
        return

    def isCosmicProgressionQuest(self, questID):
        raise NotImplementedError
        return

    def getBonuses(self):
        raise NotImplementedError
        return

    def getCurrentStage(self):
        raise NotImplementedError
        return

    def setQuestProgressAsViewed(self, quest):
        raise NotImplementedError
        return

    def getQuestCompletionChanged(self, quest):
        raise NotImplementedError
        return

    def getLastSeenPoints(self):
        raise NotImplementedError
        return

    def updateLastSeenPoints(self, points=None):
        raise NotImplementedError
        return

    def isProgressionFinished(self):
        raise NotImplementedError
        return

    def collectSortedDailyQuests(self):
        raise NotImplementedError
        return

    def collectSortedRelevantDailyQuests(self):
        raise NotImplementedError
        return
