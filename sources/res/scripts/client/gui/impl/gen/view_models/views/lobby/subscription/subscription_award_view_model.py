from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class SubscriptionState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1
    CANCELED = 2
    ERROR = 3
    TRIAL = 4


class SubscriptionAwardViewModel(ViewModel):
    __slots__ = (b'onCloseButtonClick', b'onInfoButtonClick')

    def __init__(self, properties=3, commands=2):
        super(SubscriptionAwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getNextCharge(self):
        return self._getNumber(0)

    def setNextCharge(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return SubscriptionState(self._getNumber(1))

    def setState(self, value):
        self._setNumber(1, value.value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(SubscriptionAwardViewModel, self)._initialize()
        self._addNumberProperty(b'nextCharge', 0)
        self._addNumberProperty(b'state')
        self._addArrayProperty(b'rewards', Array())
        self.onCloseButtonClick = self._addCommand(b'onCloseButtonClick')
        self.onInfoButtonClick = self._addCommand(b'onInfoButtonClick')
        return
