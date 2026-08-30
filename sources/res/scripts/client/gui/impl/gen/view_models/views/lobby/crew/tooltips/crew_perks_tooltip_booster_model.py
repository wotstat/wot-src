from enum import Enum
from frameworks.wulf import ViewModel

class PerkImpactType(Enum):
    POSITIVE = b'positive'
    NEUTRAL = b'neutral'


class CrewPerksTooltipBoosterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewPerksTooltipBoosterModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def getImpact(self):
        return self._getString(2)

    def setImpact(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(CrewPerksTooltipBoosterModel, self)._initialize()
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'impact', b'')
        return
