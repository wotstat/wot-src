from enum import Enum
from frameworks.wulf import ViewModel

class WarningDescription(Enum):
    SIMILARDEVICEALREADYINSTALLED = b'similar_device_already_installed'
    TOOHEAVY = b'too_heavy'
    USELESSBATTLEBOOSTER = b'useless_battle_booster'
    NOTWITHINSTALLEDEQUIPMENT = b'not_with_installed_equipment'
    UNSUITABLEBATTLEMOD = b'unsuitable_battlemode'
    COMPARE = b'compare'


class WarningTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(WarningTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getReason(self):
        return WarningDescription(self._getString(0))

    def setReason(self, value):
        self._setString(0, value.value)
        return

    def getIsCritical(self):
        return self._getBool(1)

    def setIsCritical(self, value):
        self._setBool(1, value)
        return

    def getLockedByDevice(self):
        return self._getString(2)

    def setLockedByDevice(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(WarningTooltipViewModel, self)._initialize()
        self._addStringProperty(b'reason')
        self._addBoolProperty(b'isCritical', False)
        self._addStringProperty(b'lockedByDevice', b'')
        return
