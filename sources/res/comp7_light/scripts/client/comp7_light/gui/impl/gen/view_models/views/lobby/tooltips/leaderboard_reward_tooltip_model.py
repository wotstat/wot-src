from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    INPROGRESS = b'inProgress'
    COMPLETED = b'completed'
    SIMPLIFIED = b'simplified'


class LeaderboardRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LeaderboardRewardTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getSeasonEndTimestamp(self):
        return self._getNumber(1)

    def setSeasonEndTimestamp(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(LeaderboardRewardTooltipModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'seasonEndTimestamp', 0)
        return
