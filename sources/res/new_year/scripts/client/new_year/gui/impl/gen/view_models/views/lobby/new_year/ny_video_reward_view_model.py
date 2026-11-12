from frameworks.wulf import Array
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_reward_item_model import Pm3RewardItemModel

class NyVideoRewardViewModel(VehicleInfoModel):
    __slots__ = (b'onClose', b'onError', b'onShowVehicle', b'onVideoStarted')

    def __init__(self, properties=17, commands=4):
        super(NyVideoRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWindowAccessible(self):
        return self._getBool(10)

    def setIsWindowAccessible(self, value):
        self._setBool(10, value)
        return

    def getIsFocused(self):
        return self._getBool(11)

    def setIsFocused(self, value):
        self._setBool(11, value)
        return

    def getStage(self):
        return self._getNumber(12)

    def setStage(self, value):
        self._setNumber(12, value)
        return

    def getPosition(self):
        return self._getNumber(13)

    def setPosition(self, value):
        self._setNumber(13, value)
        return

    def getHasExtraRewards(self):
        return self._getBool(14)

    def setHasExtraRewards(self, value):
        self._setBool(14, value)
        return

    def getBadgeTop(self):
        return self._getNumber(15)

    def setBadgeTop(self, value):
        self._setNumber(15, value)
        return

    def getRewards(self):
        return self._getArray(16)

    def setRewards(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getRewardsType():
        return Pm3RewardItemModel

    def _initialize(self):
        super(NyVideoRewardViewModel, self)._initialize()
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addBoolProperty(b'isFocused', True)
        self._addNumberProperty(b'stage', 0)
        self._addNumberProperty(b'position', 0)
        self._addBoolProperty(b'hasExtraRewards', False)
        self._addNumberProperty(b'badgeTop', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onError = self._addCommand(b'onError')
        self.onShowVehicle = self._addCommand(b'onShowVehicle')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        return
