from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.skill_select_row_model import SkillSelectRowModel

class SkillSelectViewModel(ViewModel):
    __slots__ = (b'onRestore', b'onCancel', b'onClose', b'onConfirm', b'onClick')

    def __init__(self, properties=4, commands=5):
        super(SkillSelectViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getMajorSkillRows(self):
        return self._getArray(1)

    def setMajorSkillRows(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMajorSkillRowsType():
        return SkillSelectRowModel

    def getBonusSkillRows(self):
        return self._getArray(2)

    def setBonusSkillRows(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBonusSkillRowsType():
        return SkillSelectRowModel

    def getIsActionsDisable(self):
        return self._getBool(3)

    def setIsActionsDisable(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SkillSelectViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addArrayProperty(b'majorSkillRows', Array())
        self._addArrayProperty(b'bonusSkillRows', Array())
        self._addBoolProperty(b'isActionsDisable', False)
        self.onRestore = self._addCommand(b'onRestore')
        self.onCancel = self._addCommand(b'onCancel')
        self.onClose = self._addCommand(b'onClose')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onClick = self._addCommand(b'onClick')
        return
