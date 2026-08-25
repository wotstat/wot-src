from enum import Enum
from frameworks.wulf import ViewModel

class TooltipType(Enum):
    DISABLED_LAYOUT = b'disabledLayout'
    NOT_ENOUGH_ACHIEVEMENTS = b'notEnoughAchievements'
    DISABLED = b'disabled'
    OTHER_PLAYER = b'otherPlayer'


class EditingTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EditingTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTooltipType(self):
        return TooltipType(self._getString(0))

    def setTooltipType(self, value):
        self._setString(0, value.value)
        return

    def getRequiredAchievementsCount(self):
        return self._getNumber(1)

    def setRequiredAchievementsCount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(EditingTooltipViewModel, self)._initialize()
        self._addStringProperty(b'tooltipType')
        self._addNumberProperty(b'requiredAchievementsCount', 0)
        return
