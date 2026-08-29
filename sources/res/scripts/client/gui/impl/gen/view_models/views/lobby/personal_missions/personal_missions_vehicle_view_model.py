from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_vehicle_model import Pm3VehicleModel

class PersonalMissionsVehicleViewModel(ViewModel):
    __slots__ = (b'onCompare', b'onShowVehiclePreview', b'onShowInHangar', b'onBackToHangar', b'onMoveSpace', b'onStartMoving', b'onRestoreVehicle')
    ARG_VEHICLE_CD = b'vehicleCD'

    def __init__(self, properties=4, commands=7):
        super(PersonalMissionsVehicleViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return Pm3VehicleModel

    def getIsFinalRewardsView(self):
        return self._getBool(1)

    def setIsFinalRewardsView(self, value):
        self._setBool(1, value)
        return

    def getCurrentVehicleCD(self):
        return self._getNumber(2)

    def setCurrentVehicleCD(self, value):
        self._setNumber(2, value)
        return

    def getOperationName(self):
        return self._getString(3)

    def setOperationName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(PersonalMissionsVehicleViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', Pm3VehicleModel())
        self._addBoolProperty(b'isFinalRewardsView', False)
        self._addNumberProperty(b'currentVehicleCD', 0)
        self._addStringProperty(b'operationName', b'')
        self.onCompare = self._addCommand(b'onCompare')
        self.onShowVehiclePreview = self._addCommand(b'onShowVehiclePreview')
        self.onShowInHangar = self._addCommand(b'onShowInHangar')
        self.onBackToHangar = self._addCommand(b'onBackToHangar')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onStartMoving = self._addCommand(b'onStartMoving')
        self.onRestoreVehicle = self._addCommand(b'onRestoreVehicle')
        return
