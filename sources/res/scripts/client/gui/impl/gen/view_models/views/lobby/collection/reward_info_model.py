from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.collection.reward_model import RewardModel

class RewardState(Enum):
    JUSTRECEIVED = b'justReceived'
    RECEIVED = b'received'
    UNRECEIVED = b'unreceived'


class RewardInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RewardInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getRequiredItemsCount(self):
        return self._getNumber(0)

    def setRequiredItemsCount(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return RewardState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardModel

    def _initialize(self):
        super(RewardInfoModel, self)._initialize()
        self._addNumberProperty(b'requiredItemsCount', 0)
        self._addStringProperty(b'state')
        self._addArrayProperty(b'rewards', Array())
        return
