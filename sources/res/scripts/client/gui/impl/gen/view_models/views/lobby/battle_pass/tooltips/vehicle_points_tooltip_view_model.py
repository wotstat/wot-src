from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel

class VehiclePointsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(VehiclePointsTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewardPoints(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardPointsType():
        return RewardPointsModel

    def getVehicleLevel(self):
        return self._getNumber(1)

    def setVehicleLevel(self, value):
        self._setNumber(1, value)
        return

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)
        return

    def getVehicleType(self):
        return self._getString(3)

    def setVehicleType(self, value):
        self._setString(3, value)
        return

    def getPointsCurrent(self):
        return self._getNumber(4)

    def setPointsCurrent(self, value):
        self._setNumber(4, value)
        return

    def getPointsTotal(self):
        return self._getNumber(5)

    def setPointsTotal(self, value):
        self._setNumber(5, value)
        return

    def getPointsReward(self):
        return self._getNumber(6)

    def setPointsReward(self, value):
        self._setNumber(6, value)
        return

    def getIsSpecialVehicle(self):
        return self._getBool(7)

    def setIsSpecialVehicle(self, value):
        self._setBool(7, value)
        return

    def getIsElite(self):
        return self._getBool(8)

    def setIsElite(self, value):
        self._setBool(8, value)
        return

    def getBattleType(self):
        return self._getString(9)

    def setBattleType(self, value):
        self._setString(9, value)
        return

    def getIsWotPlusShown(self):
        return self._getBool(10)

    def setIsWotPlusShown(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(VehiclePointsTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'rewardPoints', UserListModel())
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'pointsCurrent', 0)
        self._addNumberProperty(b'pointsTotal', 0)
        self._addNumberProperty(b'pointsReward', 0)
        self._addBoolProperty(b'isSpecialVehicle', False)
        self._addBoolProperty(b'isElite', False)
        self._addStringProperty(b'battleType', b'')
        self._addBoolProperty(b'isWotPlusShown', False)
        return
