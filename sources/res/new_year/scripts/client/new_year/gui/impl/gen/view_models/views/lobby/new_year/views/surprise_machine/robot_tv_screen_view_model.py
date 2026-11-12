from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RobotTvScreenState(Enum):
    IDLE = b'idle'
    ACTIVE = b'active'
    CHOOSEAMOUNT = b'chooseAmount'
    REWARDING = b'rewarding'
    VEHICLEREWARDING = b'vehicleRewarding'
    ERROR = b'error'


class RobotTvButtons(Enum):
    ONE = b'one'
    NOT_ONE = b'notOne'
    CHANGE = b'change'
    NOT_SELECTED = b'notSelected'


class RobotTvScreenViewModel(ViewModel):
    __slots__ = (b'onButtonClick', b'rewardingFinished', b'goToRewardVehicle', b'onCoinApplied')

    def __init__(self, properties=4, commands=4):
        super(RobotTvScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedButton(self):
        return RobotTvButtons(self._getString(0))

    def setSelectedButton(self, value):
        self._setString(0, value.value)
        return

    def getTokensCount(self):
        return self._getNumber(1)

    def setTokensCount(self, value):
        self._setNumber(1, value)
        return

    def getScreenState(self):
        return RobotTvScreenState(self._getString(2))

    def setScreenState(self, value):
        self._setString(2, value.value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(RobotTvScreenViewModel, self)._initialize()
        self._addStringProperty(b'selectedButton')
        self._addNumberProperty(b'tokensCount', 0)
        self._addStringProperty(b'screenState')
        self._addArrayProperty(b'rewards', Array())
        self.onButtonClick = self._addCommand(b'onButtonClick')
        self.rewardingFinished = self._addCommand(b'rewardingFinished')
        self.goToRewardVehicle = self._addCommand(b'goToRewardVehicle')
        self.onCoinApplied = self._addCommand(b'onCoinApplied')
        return
