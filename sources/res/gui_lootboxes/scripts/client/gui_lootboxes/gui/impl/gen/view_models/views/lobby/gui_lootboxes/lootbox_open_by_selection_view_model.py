from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.reward_video_model import RewardVideoModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.vehicle_bonus_model import VehicleBonusModel

class LootboxOpenBySelectionViewModel(ViewModel):
    __slots__ = (b'onCardSelect', b'onSkip', b'onAnimationFinished', b'onClose', b'onVideoStarted', b'onVideoEnded', b'onPreview')

    def __init__(self, properties=8, commands=7):
        super(LootboxOpenBySelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCards(self):
        return self._getArray(0)

    def setCards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCardsType():
        return int

    def getIsLoading(self):
        return self._getBool(1)

    def setIsLoading(self, value):
        self._setBool(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return VehicleBonusModel

    def getRewardVideos(self):
        return self._getArray(3)

    def setRewardVideos(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardVideosType():
        return RewardVideoModel

    def getIsWindowAccessible(self):
        return self._getBool(4)

    def setIsWindowAccessible(self, value):
        self._setBool(4, value)
        return

    def getIsGuaranteedReward(self):
        return self._getBool(5)

    def setIsGuaranteedReward(self, value):
        self._setBool(5, value)
        return

    def getHasVideoFooter(self):
        return self._getBool(6)

    def setHasVideoFooter(self, value):
        self._setBool(6, value)
        return

    def getLootBoxIconName(self):
        return self._getString(7)

    def setLootBoxIconName(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(LootboxOpenBySelectionViewModel, self)._initialize()
        self._addArrayProperty(b'cards', Array())
        self._addBoolProperty(b'isLoading', False)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'rewardVideos', Array())
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addBoolProperty(b'isGuaranteedReward', False)
        self._addBoolProperty(b'hasVideoFooter', False)
        self._addStringProperty(b'lootBoxIconName', b'')
        self.onCardSelect = self._addCommand(b'onCardSelect')
        self.onSkip = self._addCommand(b'onSkip')
        self.onAnimationFinished = self._addCommand(b'onAnimationFinished')
        self.onClose = self._addCommand(b'onClose')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        self.onVideoEnded = self._addCommand(b'onVideoEnded')
        self.onPreview = self._addCommand(b'onPreview')
        return
