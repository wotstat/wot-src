from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class StyleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(StyleInfoModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getStyleName(self):
        return self._getString(1)

    def setStyleName(self, value):
        self._setString(1, value)
        return

    def getStyleId(self):
        return self._getNumber(2)

    def setStyleId(self, value):
        self._setNumber(2, value)
        return

    def getIsVehicleInHangar(self):
        return self._getBool(3)

    def setIsVehicleInHangar(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(StyleInfoModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addStringProperty(b'styleName', b'')
        self._addNumberProperty(b'styleId', 0)
        self._addBoolProperty(b'isVehicleInHangar', False)
        return
