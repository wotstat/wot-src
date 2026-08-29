from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.comp7_bonus_model import Comp7BonusModel

class RewardsState(Enum):
    GUARANTEED = b'guaranteed'
    POSSIBLE = b'possible'
    NOTAVAILABLE = b'notAvailable'
    CLAIMED = b'claimed'


class SeasonPointState(Enum):
    ACHIEVED = b'achieved'
    POSSIBLE = b'possible'
    NOTACHIEVED = b'notAchieved'


class YearlyRewardsCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(YearlyRewardsCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return Comp7BonusModel

    def getSeasonPoints(self):
        return self._getArray(1)

    def setSeasonPoints(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSeasonPointsType():
        return SeasonPointState

    def getRewardsState(self):
        return RewardsState(self._getString(2))

    def setRewardsState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(YearlyRewardsCardModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'seasonPoints', Array())
        self._addStringProperty(b'rewardsState')
        return
