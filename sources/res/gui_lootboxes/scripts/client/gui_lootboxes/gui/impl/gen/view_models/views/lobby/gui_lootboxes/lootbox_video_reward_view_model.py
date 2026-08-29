from frameworks.wulf import Array
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.reward_video_model import RewardVideoModel

class LootboxVideoRewardViewModel(VehicleInfoModel):
    __slots__ = (b'onClose', b'onVideoStarted')

    def __init__(self, properties=18, commands=2):
        super(LootboxVideoRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def reward(self):
        return self._getViewModel(10)

    @staticmethod
    def getRewardType():
        return BonusModel

    def getIsWindowAccessible(self):
        return self._getBool(11)

    def setIsWindowAccessible(self, value):
        self._setBool(11, value)
        return

    def getVideoRes(self):
        return self._getString(12)

    def setVideoRes(self, value):
        self._setString(12, value)
        return

    def getLootboxType(self):
        return self._getString(13)

    def setLootboxType(self, value):
        self._setString(13, value)
        return

    def getLootboxID(self):
        return self._getNumber(14)

    def setLootboxID(self, value):
        self._setNumber(14, value)
        return

    def getIsGuaranteedReward(self):
        return self._getBool(15)

    def setIsGuaranteedReward(self, value):
        self._setBool(15, value)
        return

    def getHasVideoFooter(self):
        return self._getBool(16)

    def setHasVideoFooter(self, value):
        self._setBool(16, value)
        return

    def getRewardVideos(self):
        return self._getArray(17)

    def setRewardVideos(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getRewardVideosType():
        return RewardVideoModel

    def _initialize(self):
        super(LootboxVideoRewardViewModel, self)._initialize()
        self._addViewModelProperty(b'reward', UserListModel())
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addStringProperty(b'videoRes', b'')
        self._addStringProperty(b'lootboxType', b'')
        self._addNumberProperty(b'lootboxID', 0)
        self._addBoolProperty(b'isGuaranteedReward', False)
        self._addBoolProperty(b'hasVideoFooter', False)
        self._addArrayProperty(b'rewardVideos', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        return
