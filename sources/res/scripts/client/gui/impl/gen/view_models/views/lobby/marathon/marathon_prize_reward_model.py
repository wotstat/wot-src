from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.marathon.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.marathon.marathon_prize_vehicle_model import MarathonPrizeVehicleModel

class MarathonPrizeRewardModel(ViewModel):
    __slots__ = (b'onAcceptClicked', b'onSecondaryClicked', b'onCancelClicked')

    def __init__(self, properties=11, commands=3):
        super(MarathonPrizeRewardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return MarathonPrizeVehicleModel

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def getSupTitle(self):
        return self._getResource(2)

    def setSupTitle(self, value):
        self._setResource(2, value)
        return

    def getSubTitle(self):
        return self._getResource(3)

    def setSubTitle(self, value):
        self._setResource(3, value)
        return

    def getStage(self):
        return self._getNumber(4)

    def setStage(self, value):
        self._setNumber(4, value)
        return

    def getImage(self):
        return self._getResource(5)

    def setImage(self, value):
        self._setResource(5, value)
        return

    def getIconReward(self):
        return self._getResource(6)

    def setIconReward(self, value):
        self._setResource(6, value)
        return

    def getHasVehicle(self):
        return self._getBool(7)

    def setHasVehicle(self, value):
        self._setBool(7, value)
        return

    def getRewards(self):
        return self._getArray(8)

    def setRewards(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def getRestRewards(self):
        return self._getArray(9)

    def setRestRewards(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getRestRewardsType():
        return BonusModel

    def getRestRewardsCount(self):
        return self._getNumber(10)

    def setRestRewardsCount(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(MarathonPrizeRewardModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', MarathonPrizeVehicleModel())
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'supTitle', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        self._addNumberProperty(b'stage', 0)
        self._addResourceProperty(b'image', R.invalid())
        self._addResourceProperty(b'iconReward', R.invalid())
        self._addBoolProperty(b'hasVehicle', False)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'restRewards', Array())
        self._addNumberProperty(b'restRewardsCount', 0)
        self.onAcceptClicked = self._addCommand(b'onAcceptClicked')
        self.onSecondaryClicked = self._addCommand(b'onSecondaryClicked')
        self.onCancelClicked = self._addCommand(b'onCancelClicked')
        return
