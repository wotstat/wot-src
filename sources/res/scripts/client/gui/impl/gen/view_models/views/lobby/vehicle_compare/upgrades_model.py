from enum import Enum
from frameworks.wulf import ViewModel

class UpgradesState(Enum):
    ZERO_UPGRADES = b'zeroUpgrades'
    PARTIAL_UPGRADES = b'partialUpgrades'
    FULL_UPGRADES = b'fullUpgrades'


class UpgradesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(UpgradesModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return UpgradesState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getIsSelected(self):
        return self._getBool(1)

    def setIsSelected(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(UpgradesModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isSelected', False)
        return
