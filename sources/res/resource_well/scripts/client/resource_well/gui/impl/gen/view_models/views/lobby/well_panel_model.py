from resource_well.gui.impl.gen.view_models.views.lobby.enums import EventMode
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class WellPanelModel(ViewModel):
    __slots__ = (b'onAction',)

    def __init__(self, properties=5, commands=1):
        super(WellPanelModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getTopRewardsCount(self):
        return self._getNumber(1)

    def setTopRewardsCount(self, value):
        self._setNumber(1, value)
        return

    def getRegularRewardsCount(self):
        return self._getNumber(2)

    def setRegularRewardsCount(self, value):
        self._setNumber(2, value)
        return

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)
        return

    def getEventMode(self):
        return EventMode(self._getString(4))

    def setEventMode(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(WellPanelModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addNumberProperty(b'topRewardsCount', 0)
        self._addNumberProperty(b'regularRewardsCount', 0)
        self._addBoolProperty(b'isVisible', False)
        self._addStringProperty(b'eventMode')
        self.onAction = self._addCommand(b'onAction')
        return
