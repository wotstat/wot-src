from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from last_stand.gui.game_control.ls_difficulty_missions_controller import DifficultyMission
    from gui.server_events.bonuses import SimpleBonus

class ILSDifficultyMissionsController(IGameController):
    onDifficultyMissionsStatusUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def missionsSorted(self, difficulty):
        raise NotImplementedError
        return

    def isProgressCompleted(self):
        raise NotImplementedError
        return

    def getMission(self, missionID):
        raise NotImplementedError
        return

    def getMissionsCount(self, difficulty):
        raise NotImplementedError
        return

    def getCompletedMissionsIndexByDifficulty(self, difficulty):
        raise NotImplementedError
        return

    def getIndexes(self, missionID):
        raise NotImplementedError
        return

    def getMissionByIndex(self, difficulty, index):
        raise NotImplementedError
        return

    def getMissionIDByIndex(self, difficulty, index):
        raise NotImplementedError
        return

    def getAggregatedMissionRewards(self, difficulty):
        raise NotImplementedError
        return

    def addArenaIDToCache(self, arenaID):
        raise NotImplementedError
        return

    def isArenaIDInCache(self, arenaID):
        raise NotImplementedError
        return
