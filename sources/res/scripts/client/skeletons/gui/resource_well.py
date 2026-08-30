from __future__ import absolute_import
from typing import Dict, Optional, Set, List
from Event import Event
from skeletons.gui.game_control import IGameController

class IResourceWellController(IGameController):
    onEventUpdated = None
    onSettingsChanged = None
    onNumberRequesterUpdated = None

    @property
    def config(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    def isStarted(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isPaused(self):
        raise NotImplementedError
        return

    def isNotStarted(self):
        raise NotImplementedError
        return

    def isForbiddenAccount(self):
        raise NotImplementedError
        return

    def isSeasonNumberDefault(self):
        raise NotImplementedError
        return

    def getRewardLimit(self, rewardID):
        raise NotImplementedError
        return

    def getCurrentPoints(self):
        raise NotImplementedError
        return

    def isRewardReceived(self, rewardID):
        raise NotImplementedError
        return

    def getReceivedRewardIDs(self):
        raise NotImplementedError
        return

    def getBalance(self):
        raise NotImplementedError
        return

    def getPurchaseMode(self):
        raise NotImplementedError
        return

    def getRewardVehicle(self, rewardID):
        raise NotImplementedError
        return

    def getRewardStyleID(self, rewardID):
        raise NotImplementedError
        return

    def getCurrentRewardID(self):
        raise NotImplementedError
        return

    def getRewardSequence(self, rewardID):
        raise NotImplementedError
        return

    def getRewardLeftCount(self, rewardID):
        raise NotImplementedError
        return

    def isParentRewardAvailable(self, rewardID):
        raise NotImplementedError
        return

    def isRewardAvailable(self, rewardID):
        raise NotImplementedError
        return

    def isRewardCountAvailable(self, rewardID):
        raise NotImplementedError
        return

    def getAvailableRewards(self):
        raise NotImplementedError
        return

    def isRewardsOver(self):
        raise NotImplementedError
        return

    def isRewardVehicle(self, vehicleCD):
        raise NotImplementedError
        return

    def startNumberRequesters(self):
        raise NotImplementedError
        return

    def stopNumberRequesters(self):
        raise NotImplementedError
        return
