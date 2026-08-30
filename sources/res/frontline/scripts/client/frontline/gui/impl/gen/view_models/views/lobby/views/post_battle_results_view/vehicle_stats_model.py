from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class FrontlineParamType(Enum):
    ATKOBJECTIVES = b'atkObjectives'
    DEFOBJECTIVES = b'defObjectives'


class VehicleStatsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehicleStatsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    def getIsGeneralInfo(self):
        return self._getBool(1)

    def setIsGeneralInfo(self, value):
        self._setBool(1, value)
        return

    def getObjectivesReached(self):
        return self._getBool(2)

    def setObjectivesReached(self, value):
        self._setBool(2, value)
        return

    def getObjectivesDestroyed(self):
        return self._getNumber(3)

    def setObjectivesDestroyed(self, value):
        self._setNumber(3, value)
        return

    def getZoneCaptured(self):
        return self._getNumber(4)

    def setZoneCaptured(self, value):
        self._setNumber(4, value)
        return

    def getDetailedStatistics(self):
        return self._getArray(5)

    def setDetailedStatistics(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getDetailedStatisticsType():
        return DetailedStatsParameterModel

    def _initialize(self):
        super(VehicleStatsModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addBoolProperty(b'isGeneralInfo', False)
        self._addBoolProperty(b'objectivesReached', False)
        self._addNumberProperty(b'objectivesDestroyed', 0)
        self._addNumberProperty(b'zoneCaptured', 0)
        self._addArrayProperty(b'detailedStatistics', Array())
        return
