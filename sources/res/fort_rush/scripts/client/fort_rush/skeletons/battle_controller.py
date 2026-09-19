from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from gui.prb_control.items import ValidationResult
    from gui.shared.gui_items.Vehicle import Vehicle
    from typing import List, Optional
    from Event import Event

class IFortRushBattleController(IGameController):
    onConfigUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isWithinActiveTimeframe(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def isInAnnouncement(self):
        raise NotImplementedError
        return

    def getTimeLeft(self):
        raise NotImplementedError
        return

    def isEventPrbActive(self):
        raise NotImplementedError
        return

    def isFrozen(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def selectBattle(self):
        raise NotImplementedError
        return

    def selectRandomBattle(self):
        raise NotImplementedError
        return

    def isInfoPageEnabled(self):
        raise NotImplementedError
        return

    def getNewDailyMissionsTimestamp(self):
        raise NotImplementedError
        return

    def getFortRushDailyQuests(self):
        raise NotImplementedError
        return

    def getTotalProgressionPoints(self):
        raise NotImplementedError
        return

    def getCurrentStageIndex(self):
        raise NotImplementedError
        return

    def getCurrentStagePoints(self):
        raise NotImplementedError
        return

    def isProgressionCompleted(self):
        raise NotImplementedError
        return

    def getCurrentProgressionStageRewards(self):
        raise NotImplementedError
        return

    def getProgressionRewards(self, questId):
        raise NotImplementedError
        return

    def getEligibleVehicleTiers(self):
        raise NotImplementedError
        return

    def getForbiddenVehClasses(self):
        raise NotImplementedError
        return

    def isSuitableVehicle(self, vehicle):
        raise NotImplementedError
        return

    def hasSuitableVehicles(self):
        raise NotImplementedError
        return

    def getLastStageThreshold(self):
        raise NotImplementedError
        return
