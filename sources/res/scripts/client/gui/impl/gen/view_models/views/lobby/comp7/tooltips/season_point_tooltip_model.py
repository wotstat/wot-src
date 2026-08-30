from enum import Enum
from frameworks.wulf import ViewModel

class SeasonPointState(Enum):
    ACHIEVED = b'achieved'
    POSSIBLE = b'possible'
    NOTACHIEVED = b'notAchieved'


class SeasonPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SeasonPointTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return SeasonPointState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getSeasonPointExchangeRate(self):
        return self._getNumber(1)

    def setSeasonPointExchangeRate(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(SeasonPointTooltipModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'seasonPointExchangeRate', 0)
        return
