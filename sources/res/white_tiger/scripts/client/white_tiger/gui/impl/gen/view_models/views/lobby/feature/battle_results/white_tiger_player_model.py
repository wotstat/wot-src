from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from white_tiger.gui.impl.gen.view_models.views.lobby.feature.battle_results.white_tiger_stats_efficiency_model import WhiteTigerStatsEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel
from gui.impl.gen.view_models.views.lobby.battle_results.user_status_model import UserStatusModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class WhiteTigerPlayerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(WhiteTigerPlayerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def userNames(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserNamesType():
        return UserNameModel

    @property
    def vehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    @property
    def userStatus(self):
        return self._getViewModel(2)

    @staticmethod
    def getUserStatusType():
        return UserStatusModel

    @property
    def efficiencyValues(self):
        return self._getViewModel(3)

    @staticmethod
    def getEfficiencyValuesType():
        return WhiteTigerStatsEfficiencyModel

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

    def getIsPersonal(self):
        return self._getBool(7)

    def setIsPersonal(self, value):
        self._setBool(7, value)
        return

    def getDetailedStatistics(self):
        return self._getArray(8)

    def setDetailedStatistics(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getDetailedStatisticsType():
        return DetailedStatsParameterModel

    def _initialize(self):
        super(WhiteTigerPlayerModel, self)._initialize()
        self._addViewModelProperty(b'userNames', UserNameModel())
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addViewModelProperty(b'userStatus', UserStatusModel())
        self._addViewModelProperty(b'efficiencyValues', WhiteTigerStatsEfficiencyModel())
        self._addNumberProperty(b'playerIndex', 0)
        self._addNumberProperty(b'databaseID', 0)
        self._addNumberProperty(b'squadIndex', 0)
        self._addBoolProperty(b'isPersonal', False)
        self._addArrayProperty(b'detailedStatistics', Array())
        return
