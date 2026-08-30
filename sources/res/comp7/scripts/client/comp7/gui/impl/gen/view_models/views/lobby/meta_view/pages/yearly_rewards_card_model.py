from enum import Enum
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.comp7_bonus_model import Comp7BonusModel
from comp7.gui.impl.gen.view_models.views.lobby.season_point_model import SeasonPointModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class RewardsState(Enum):
    GUARANTEED = b'guaranteed'
    POSSIBLE = b'possible'
    NOTAVAILABLE = b'notAvailable'
    CLAIMED = b'claimed'


class YearlyRewardsCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(YearlyRewardsCardModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return Comp7BonusModel

    def getSeasonPoints(self):
        return self._getArray(2)

    def setSeasonPoints(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSeasonPointsType():
        return SeasonPointModel

    def getRewardsState(self):
        return RewardsState(self._getString(3))

    def setRewardsState(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(YearlyRewardsCardModel, self)._initialize()
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'seasonPoints', Array())
        self._addStringProperty(b'rewardsState')
        return
