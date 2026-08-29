from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class BlueprintUniversalTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BlueprintUniversalTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleModel

    def getBlueprintFragments(self):
        return self._getNumber(1)

    def setBlueprintFragments(self, value):
        self._setNumber(1, value)
        return

    def getExperience(self):
        return self._getNumber(2)

    def setExperience(self, value):
        self._setNumber(2, value)
        return

    def getDiscount(self):
        return self._getNumber(3)

    def setDiscount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(BlueprintUniversalTooltipModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleModel())
        self._addNumberProperty(b'blueprintFragments', 0)
        self._addNumberProperty(b'experience', 0)
        self._addNumberProperty(b'discount', 0)
        return
