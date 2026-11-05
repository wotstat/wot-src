from enum import Enum
from frameworks.wulf import ViewModel

class ProgressionState(Enum):
    REWARD_RECEIVED = b'rewardReceived'
    REWARD_IN_PROGRESS = b'rewardInProgress'
    REWARD_LOCKED = b'rewardLocked'


class RewardType(Enum):
    STYLE_2D = b'style2D'
    CREW_MEMBER = b'crewMember'
    BIG_LOOTBOX = b'lootBox'


class ProgressionRewardItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ProgressionRewardItemViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRequiredOpenedDoorsAmount(self):
        return self._getNumber(0)

    def setRequiredOpenedDoorsAmount(self, value):
        self._setNumber(0, value)
        return

    def getActualOpenedDoorsAmount(self):
        return self._getNumber(1)

    def setActualOpenedDoorsAmount(self, value):
        self._setNumber(1, value)
        return

    def getState(self):
        return ProgressionState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def getTooltipContentId(self):
        return self._getNumber(4)

    def setTooltipContentId(self, value):
        self._setNumber(4, value)
        return

    def getRewardType(self):
        return RewardType(self._getString(5))

    def setRewardType(self, value):
        self._setString(5, value.value)
        return

    def _initialize(self):
        super(ProgressionRewardItemViewModel, self)._initialize()
        self._addNumberProperty(b'requiredOpenedDoorsAmount', 0)
        self._addNumberProperty(b'actualOpenedDoorsAmount', 0)
        self._addStringProperty(b'state')
        self._addStringProperty(b'tooltipId', b'')
        self._addNumberProperty(b'tooltipContentId', 0)
        self._addStringProperty(b'rewardType')
        return
