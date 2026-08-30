from enum import Enum
from frameworks.wulf import ViewModel

class TabState(Enum):
    DISABLED = b'disabled'
    ISAVAILABLE = b'isAvailable'
    COMPLETEWITHHONOR = b'completeWithHonor'
    COMPLETED = b'completed'


class Pm3QuestsPageTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(Pm3QuestsPageTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def getMaxValue(self):
        return self._getNumber(2)

    def setMaxValue(self, value):
        self._setNumber(2, value)
        return

    def getMinVehicleLevel(self):
        return self._getNumber(3)

    def setMinVehicleLevel(self, value):
        self._setNumber(3, value)
        return

    def getMaxVehicleLevel(self):
        return self._getNumber(4)

    def setMaxVehicleLevel(self, value):
        self._setNumber(4, value)
        return

    def getSelected(self):
        return self._getBool(5)

    def setSelected(self, value):
        self._setBool(5, value)
        return

    def getState(self):
        return TabState(self._getString(6))

    def setState(self, value):
        self._setString(6, value.value)
        return

    def getBranchName(self):
        return self._getString(7)

    def setBranchName(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(Pm3QuestsPageTabModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'value', 0)
        self._addNumberProperty(b'maxValue', 0)
        self._addNumberProperty(b'minVehicleLevel', 0)
        self._addNumberProperty(b'maxVehicleLevel', 0)
        self._addBoolProperty(b'selected', False)
        self._addStringProperty(b'state')
        self._addStringProperty(b'branchName', b'')
        return
