from __future__ import absolute_import
from skeletons.gui.game_control import IGameController, ISeasonProvider
from Event import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterator
    from gui.server_events.bonuses import SimpleBonus

class IEconomicsController(IGameController, ISeasonProvider):
    onProgressUpdated = None
    onRewardsUpdated = None
    onProgressSeenByUser = None

    def getConfig(self):
        raise NotImplementedError
        return

    def getStampsCountPerLevel(self):
        raise NotImplementedError
        return

    def getProgressionMaxLevel(self):
        raise NotImplementedError
        return

    def getStampsCount(self):
        raise NotImplementedError
        return

    def getMaxRequiredStampsCount(self):
        raise NotImplementedError
        return

    def getFinishedLevelsCount(self):
        raise NotImplementedError
        return

    def getCurrentLevel(self):
        raise NotImplementedError
        return

    def getTicketCount(self):
        raise NotImplementedError
        return

    def getQuickTicketCount(self):
        raise NotImplementedError
        return

    def getQuickBossTicketExpiryTime(self):
        raise NotImplementedError
        return

    def getQuickHunterTicketCount(self):
        raise NotImplementedError
        return

    def getQuickHunterTicketExpiryTime(self):
        raise NotImplementedError
        return

    def getTicketTokenName(self):
        raise NotImplementedError
        return

    def getStampTokenName(self):
        raise NotImplementedError
        return

    def getQuickTicketTokenName(self):
        raise NotImplementedError
        return

    def getQuickHunterTicketTokenName(self):
        raise NotImplementedError
        return

    def hasEnoughTickets(self):
        raise NotImplementedError
        return

    def getProgressionRewards(self):
        raise NotImplementedError
        return

    def notifyProgressSeen(self):
        raise NotImplementedError
        return
