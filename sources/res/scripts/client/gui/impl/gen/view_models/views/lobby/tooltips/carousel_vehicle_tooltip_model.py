from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.tooltips.earnings_model import EarningsModel
from gui.impl.gen.view_models.views.lobby.tooltips.service_records_model import ServiceRecordsModel
from gui.impl.gen.view_models.views.lobby.tooltips.statistics_model import StatisticsModel

class CarouselVehicleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CarouselVehicleTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def statistics(self):
        return self._getViewModel(0)

    @staticmethod
    def getStatisticsType():
        return StatisticsModel

    @property
    def earnings(self):
        return self._getViewModel(1)

    @staticmethod
    def getEarningsType():
        return EarningsModel

    @property
    def serviceRecords(self):
        return self._getViewModel(2)

    @staticmethod
    def getServiceRecordsType():
        return ServiceRecordsModel

    def getStatus(self):
        return self._getString(3)

    def setStatus(self, value):
        self._setString(3, value)
        return

    def getStateLevel(self):
        return self._getString(4)

    def setStateLevel(self, value):
        self._setString(4, value)
        return

    def getBpEntityValid(self):
        return self._getBool(5)

    def setBpEntityValid(self, value):
        self._setBool(5, value)
        return

    def getMechanics(self):
        return self._getArray(6)

    def setMechanics(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getMechanicsType():
        return VehicleMechanicModel

    def _initialize(self):
        super(CarouselVehicleTooltipModel, self)._initialize()
        self._addViewModelProperty(b'statistics', StatisticsModel())
        self._addViewModelProperty(b'earnings', EarningsModel())
        self._addViewModelProperty(b'serviceRecords', ServiceRecordsModel())
        self._addStringProperty(b'status', b'none')
        self._addStringProperty(b'stateLevel', b'none')
        self._addBoolProperty(b'bpEntityValid', False)
        self._addArrayProperty(b'mechanics', Array())
        return
