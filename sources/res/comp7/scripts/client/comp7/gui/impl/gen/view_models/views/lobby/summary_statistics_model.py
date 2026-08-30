from enum import Enum
from frameworks.wulf import ViewModel

class SummaryStatisticsType(Enum):
    BATTLES = b'battles'
    DAMAGE = b'damage'
    MAXPRESTIGEPOINTS = b'maxPrestigePoints'
    MAXFRAGS = b'maxFrags'
    WINSERIES = b'winSeries'


class SummaryStatisticsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SummaryStatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return SummaryStatisticsType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getMain(self):
        return self._getNumber(1)

    def setMain(self, value):
        self._setNumber(1, value)
        return

    def getAdditional(self):
        return self._getReal(2)

    def setAdditional(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(SummaryStatisticsModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addNumberProperty(b'main', 0)
        self._addRealProperty(b'additional', 0.0)
        return
