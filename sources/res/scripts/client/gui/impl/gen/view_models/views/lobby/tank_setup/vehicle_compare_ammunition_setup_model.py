from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.main_tank_setup_model import MainTankSetupModel

class VehicleCompareAmmunitionSetupModel(ViewModel):
    __slots__ = (b'onClose', b'onResized', b'onViewRendered', b'onAnimationEnd')

    def __init__(self, properties=4, commands=4):
        super(VehicleCompareAmmunitionSetupModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tankSetup(self):
        return self._getViewModel(0)

    @staticmethod
    def getTankSetupType():
        return MainTankSetupModel

    @property
    def vehicleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getShow(self):
        return self._getBool(2)

    def setShow(self, value):
        self._setBool(2, value)
        return

    def getSelectedSlot(self):
        return self._getNumber(3)

    def setSelectedSlot(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(VehicleCompareAmmunitionSetupModel, self)._initialize()
        self._addViewModelProperty(b'tankSetup', MainTankSetupModel())
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addBoolProperty(b'show', False)
        self._addNumberProperty(b'selectedSlot', -1)
        self.onClose = self._addCommand(b'onClose')
        self.onResized = self._addCommand(b'onResized')
        self.onViewRendered = self._addCommand(b'onViewRendered')
        self.onAnimationEnd = self._addCommand(b'onAnimationEnd')
        return
