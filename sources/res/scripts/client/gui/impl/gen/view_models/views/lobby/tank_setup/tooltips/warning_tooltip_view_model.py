from enum import Enum
from frameworks.wulf import ViewModel

class WarningDescription(Enum):
    SIMILARDEVICEALREADYINSTALLED = b'similar_device_already_installed'
    USELESSBATTLEBOOSTER = b'useless_battle_booster'
    USELESSCREWSKILLBATTLEBOOSTER = b'useless_crew_skill_battle_booster'


class WarningTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
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

    def _initialize(self):
        super(WarningTooltipViewModel, self)._initialize()
        self._addStringProperty(b'reason')
        self._addBoolProperty(b'isCritical', False)
        return
