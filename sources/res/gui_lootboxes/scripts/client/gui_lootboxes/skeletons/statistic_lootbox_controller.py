from skeletons.gui.game_control import IGameController

class IStatisticLootBoxController(IGameController):
    onStatusChanged = None

    @property
    def onBaseStatCollect(self):
        raise NotImplementedError
        return

    def getFullStatistic(self):
        raise NotImplementedError
        return

    def getMergeStatByLootboxIDs(self, lootboxIDs):
        raise NotImplementedError
        return

    def getLootboxesExpireInfo(self):
        raise NotImplementedError
        return

    def isNeedShowHint(self):
        raise NotImplementedError
        return

    def getLootBoxesVersionInfo(self, lootboxID=None):
        raise NotImplementedError
        return

    def isShowStatistic(self):
        raise NotImplementedError
        return
