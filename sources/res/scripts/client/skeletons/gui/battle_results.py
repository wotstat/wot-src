from Event import Event

class IBattleResultsService(object):
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

    def composers(self):
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

    def popResultsAnimation(self, arenaUniqueID):
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

    def isCrewSameForArena(self, arenaUniqueID):
        raise NotImplementedError
        return

    def isXPToTManSameForArena(self, arenaUniqueID):
        raise NotImplementedError
        return

    def getVehicleForArena(self, arenaUniqueID):
        raise NotImplementedError
        return
