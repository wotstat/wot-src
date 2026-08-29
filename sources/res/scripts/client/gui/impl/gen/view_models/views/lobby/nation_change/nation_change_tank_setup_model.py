from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_instruction_model import NationChangeInstructionModel

class NationChangeTankSetupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NationChangeTankSetupModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def instructionSlot(self):
        return self._getViewModel(0)

    @staticmethod
    def getInstructionSlotType():
        return NationChangeInstructionModel

    def getEquipmentList(self):
        return self._getArray(1)

    def setEquipmentList(self, value):
        self._setArray(1, value)
        return

    def getShellList(self):
        return self._getArray(2)

    def setShellList(self, value):
        self._setArray(2, value)
        return

    def getSupplyList(self):
        return self._getArray(3)

    def setSupplyList(self, value):
        self._setArray(3, value)
        return

    def _initialize(self):
        super(NationChangeTankSetupModel, self)._initialize()
        self._addViewModelProperty(b'instructionSlot', NationChangeInstructionModel())
        self._addArrayProperty(b'equipmentList', Array())
        self._addArrayProperty(b'shellList', Array())
        self._addArrayProperty(b'supplyList', Array())
        return
