from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class AwardDayState(Enum):
    REGULARDAY = b'regularDay'
    SPECIALDAY = b'specialDay'
    PROGRESSIONQUEST = b'progressionQuest'


class OpenDoorStatus(Enum):
    OPEN_DOOR_SUCCESS = b'openDoorSuccess'
    OPEN_DOOR_FAILED = b'openDoorFailed'
    OPEN_DOOR_UNDEFINED = b'openDoorUndefined'


class RewardViewModel(ViewModel):
    __slots__ = (b'onCloseBtnClick', b'onGoToBoxesBtnClick', b'onRewardsShown', b'onSetBlur')

    def __init__(self, properties=9, commands=4):
        super(RewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDayId(self):
        return self._getNumber(0)

    def setDayId(self, value):
        self._setNumber(0, value)
        return

    def getDoorsOpenedAm(self):
        return self._getNumber(1)

    def setDoorsOpenedAm(self, value):
        self._setNumber(1, value)
        return

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getAwardDayState(self):
        return AwardDayState(self._getString(3))

    def setAwardDayState(self, value):
        self._setString(3, value.value)
        return

    def getShowBoxesButton(self):
        return self._getBool(4)

    def setShowBoxesButton(self, value):
        self._setBool(4, value)
        return

    def getOpenDoorStatus(self):
        return OpenDoorStatus(self._getString(5))

    def setOpenDoorStatus(self, value):
        self._setString(5, value.value)
        return

    def getIsAnimationEnabled(self):
        return self._getBool(6)

    def setIsAnimationEnabled(self, value):
        self._setBool(6, value)
        return

    def getRewardPlugin(self):
        return self._getString(7)

    def setRewardPlugin(self, value):
        self._setString(7, value)
        return

    def getRewardInfoPlugin(self):
        return self._getString(8)

    def setRewardInfoPlugin(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(RewardViewModel, self)._initialize()
        self._addNumberProperty(b'dayId', 0)
        self._addNumberProperty(b'doorsOpenedAm', 0)
        self._addArrayProperty(b'bonuses', Array())
        self._addStringProperty(b'awardDayState')
        self._addBoolProperty(b'showBoxesButton', False)
        self._addStringProperty(b'openDoorStatus')
        self._addBoolProperty(b'isAnimationEnabled', False)
        self._addStringProperty(b'rewardPlugin', b'')
        self._addStringProperty(b'rewardInfoPlugin', b'')
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onGoToBoxesBtnClick = self._addCommand(b'onGoToBoxesBtnClick')
        self.onRewardsShown = self._addCommand(b'onRewardsShown')
        self.onSetBlur = self._addCommand(b'onSetBlur')
        return
