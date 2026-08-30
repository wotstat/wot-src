from __future__ import absolute_import
import typing
from Event import Event
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl

class IBattleResultsService(object):
    __slots__ = ()
    onResultPosted = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def requestResults(self, ctx, callback=None):
        raise NotImplementedError
        return

    def requestEmblem(self, ctx, callback=None):
        raise NotImplementedError
        return

    def postResult(self, result, needToShowUI=True):
        raise NotImplementedError
        return

    def areResultsPosted(self, arenaUniqueID):
        raise NotImplementedError
        return

    def getResultsVO(self, arenaUniqueID):
        raise NotImplementedError
        return

    def getStatsCtrl(self, arenaUniqueID):
        raise NotImplementedError
        return

    def saveStatsSorting(self, bonusType, iconType, sortDirection):
        raise NotImplementedError
        return

    def applyAdditionalBonus(self, arenaUniqueID):
        raise NotImplementedError
        return

    def isAddXPBonusApplied(self, arenaUniqueID):
        raise NotImplementedError
        return

    def isAddXPBonusEnabled(self, arenaUniqueID):
        raise NotImplementedError
        return

    def getAdditionalXPValue(self, arenaUniqueID):
        raise NotImplementedError
        return

    def submitPlayerSatisfactionRating(self, areneUniqueID, rating):
        raise NotImplementedError
        return

    def getPlayerSatisfactionRating(self, arenaUniqueID):
        raise NotImplementedError
        return

    def isCrewSameForArena(self, arenaUniqueID):
        raise NotImplementedError
        return

    def isXPToTManSameForArena(self, arenaUniqueID):
        raise NotImplementedError
        return

    def getVehicleForArena(self, arenaUniqueID):
        raise NotImplementedError
        return

    def notifyBattleResultsPosted(self, arenaUniqueID, needToShowUI=False):
        raise NotImplementedError
        return
