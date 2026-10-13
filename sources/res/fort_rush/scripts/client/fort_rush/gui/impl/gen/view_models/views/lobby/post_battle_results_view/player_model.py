from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.account_model import AccountModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.fort_rush_stats_efficiency_model import FortRushStatsEfficiencyModel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.vehicle_stats_model import VehicleStatsModel

class PlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
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
        return FortRushStatsEfficiencyModel

    def getIsPersonal(self):
        return self._getBool(2)

    def setIsPersonal(self, value):
        self._setBool(2, value)
        return

    def getPlayerIndex(self):
        return self._getNumber(3)

    def setPlayerIndex(self, value):
        self._setNumber(3, value)
        return

    def getDatabaseID(self):
        return self._getNumber(4)

    def setDatabaseID(self, value):
        self._setNumber(4, value)
        return

    def getSquadIndex(self):
        return self._getNumber(5)

    def setSquadIndex(self, value):
        self._setNumber(5, value)
        return

    def getVehiclesStats(self):
        return self._getArray(6)

    def setVehiclesStats(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getVehiclesStatsType():
        return VehicleStatsModel

    def _initialize(self):
        super(PlayerModel, self)._initialize()
        self._addViewModelProperty(b'userNames', AccountModel())
        self._addViewModelProperty(b'efficiencyValues', FortRushStatsEfficiencyModel())
        self._addBoolProperty(b'isPersonal', False)
        self._addNumberProperty(b'playerIndex', 0)
        self._addNumberProperty(b'databaseID', 0)
        self._addNumberProperty(b'squadIndex', 0)
        self._addArrayProperty(b'vehiclesStats', Array())
        return
