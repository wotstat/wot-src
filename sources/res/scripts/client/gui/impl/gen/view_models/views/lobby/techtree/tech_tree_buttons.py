from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class ButtonType(Enum):
    EARLYACCESS = b'earlyAccess'
    PARAGONS = b'paragons'


class State(Enum):
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    FIRST_BRANCH_RESET = b'firstBranchReset'
    DROPPED_BRANCH = b'droppedBranch'


class TechTreeButtons(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TechTreeButtons, self).__init__(properties=properties, commands=commands)
        return

    def getBranchID(self):
        return self._getNumber(0)

    def setBranchID(self, value):
        self._setNumber(0, value)
        return

    def getButtonRow(self):
        return self._getNumber(1)

    def setButtonRow(self, value):
        self._setNumber(1, value)
        return

    def getButtonType(self):
        return ButtonType(self._getString(2))

    def setButtonType(self, value):
        self._setString(2, value.value)
        return

    def getButtonState(self):
        return State(self._getString(3))

    def setButtonState(self, value):
        self._setString(3, value.value)
        return

    def getVehiclesCDs(self):
        return self._getArray(4)

    def setVehiclesCDs(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getVehiclesCDsType():
        return int

    def _initialize(self):
        super(TechTreeButtons, self)._initialize()
        self._addNumberProperty(b'branchID', 0)
        self._addNumberProperty(b'buttonRow', 0)
        self._addStringProperty(b'buttonType')
        self._addStringProperty(b'buttonState')
        self._addArrayProperty(b'vehiclesCDs', Array())
        return
