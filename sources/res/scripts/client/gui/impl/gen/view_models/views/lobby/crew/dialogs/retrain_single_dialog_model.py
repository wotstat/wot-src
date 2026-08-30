from gui.impl.gen import R
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.role_change_model import RoleChangeModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.tankman_skills_change_base_dialog_model import TankmanSkillsChangeBaseDialogModel

class RetrainSingleDialogModel(TankmanSkillsChangeBaseDialogModel):
    __slots__ = (b'onRoleCheckChanged', b'onRoleSelected')

    def __init__(self, properties=14, commands=4):
        super(RetrainSingleDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def targetVehicle(self):
        return self._getViewModel(8)

    @staticmethod
    def getTargetVehicleType():
        return VehicleInfoModel

    @property
    def roleChange(self):
        return self._getViewModel(9)

    @staticmethod
    def getRoleChangeType():
        return RoleChangeModel

    def getTitle(self):
        return self._getResource(10)

    def setTitle(self, value):
        self._setResource(10, value)
        return

    def getWarning(self):
        return self._getResource(11)

    def setWarning(self, value):
        self._setResource(11, value)
        return

    def getIsPriceSelected(self):
        return self._getBool(12)

    def setIsPriceSelected(self, value):
        self._setBool(12, value)
        return

    def getHasRetrainDiscount(self):
        return self._getBool(13)

    def setHasRetrainDiscount(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(RetrainSingleDialogModel, self)._initialize()
        self._addViewModelProperty(b'targetVehicle', VehicleInfoModel())
        self._addViewModelProperty(b'roleChange', RoleChangeModel())
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'warning', R.invalid())
        self._addBoolProperty(b'isPriceSelected', False)
        self._addBoolProperty(b'hasRetrainDiscount', False)
        self.onRoleCheckChanged = self._addCommand(b'onRoleCheckChanged')
        self.onRoleSelected = self._addCommand(b'onRoleSelected')
        return
