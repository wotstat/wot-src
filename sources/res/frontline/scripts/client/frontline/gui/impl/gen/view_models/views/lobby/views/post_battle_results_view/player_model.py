from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.account_model import AccountModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.achievement_model import AchievementModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.vehicle_stats_model import VehicleStatsModel
from gui.impl.gen.view_models.views.lobby.battle_results.stats_efficiency_model import StatsEfficiencyModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(PlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def userNames(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserNamesType():
        return AccountModel

    @property
    def efficiencyValues(self):
        return self._getViewModel(1)

    @staticmethod
    def getEfficiencyValuesType():
        return StatsEfficiencyModel

    def getPrebattleID(self):
        return self._getNumber(2)

    def setPrebattleID(self, value):
        self._setNumber(2, value)
        return

    def getIsPersonal(self):
        return self._getBool(3)

    def setIsPersonal(self, value):
        self._setBool(3, value)
        return

    def getPlayerIndex(self):
        return self._getNumber(4)

    def setPlayerIndex(self, value):
        self._setNumber(4, value)
        return

    def getDatabaseID(self):
        return self._getNumber(5)

    def setDatabaseID(self, value):
        self._setNumber(5, value)
        return

    def getSquadIndex(self):
        return self._getNumber(6)

    def setSquadIndex(self, value):
        self._setNumber(6, value)
        return

    def getRank(self):
        return self._getNumber(7)

    def setRank(self, value):
        self._setNumber(7, value)
        return

    def getRespawns(self):
        return self._getNumber(8)

    def setRespawns(self, value):
        self._setNumber(8, value)
        return

    def getAchievements(self):
        return self._getArray(9)

    def setAchievements(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getAchievementsType():
        return AchievementModel

    def getVehiclesStats(self):
        return self._getArray(10)

    def setVehiclesStats(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getVehiclesStatsType():
        return VehicleStatsModel

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'userNames', AccountModel())
        self._addViewModelProperty(b'efficiencyValues', StatsEfficiencyModel())
        self._addNumberProperty(b'prebattleID', 0)
        self._addBoolProperty(b'isPersonal', False)
        self._addNumberProperty(b'playerIndex', 0)
        self._addNumberProperty(b'databaseID', 0)
        self._addNumberProperty(b'squadIndex', 0)
        self._addNumberProperty(b'rank', 1)
        self._addNumberProperty(b'respawns', 0)
        self._addArrayProperty(b'achievements', Array())
        self._addArrayProperty(b'vehiclesStats', Array())
        return
