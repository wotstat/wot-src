from enum import Enum
from frameworks.wulf import Array
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.common_view_model import CommonViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class RewardReason(Enum):
    BUY_BATTLE_PASS = b'buyBattlePassReason'
    BUY_BATTLE_PASS_LEVELS = b'buyBattlePassLevelsReason'
    BUY_MULTIPLE_BATTLE_PASS = b'buyMultipleBattlePassReason'
    BUY_BATTLE_PASS_WITH_LEVELS = b'buyBattlePassWithLevelsReason'
    STYLE_UPGRADE = b'styleUpgradeReason'
    DEFAULT = b'defaultReason'


class BattlePassAwardsViewModel(CommonViewModel):
    __slots__ = (b'onBuyClick', b'onClose', b'onShowPostProgression')

    def __init__(self, properties=18, commands=4):
        super(BattlePassAwardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainRewards(self):
        return self._getViewModel(4)

    @staticmethod
    def getMainRewardsType():
        return RewardItemModel

    @property
    def additionalRewards(self):
        return self._getViewModel(5)

    @staticmethod
    def getAdditionalRewardsType():
        return RewardItemModel

    @property
    def packageRewards(self):
        return self._getViewModel(6)

    @staticmethod
    def getPackageRewardsType():
        return RewardItemModel

    @property
    def starterPackRewards(self):
        return self._getViewModel(7)

    @staticmethod
    def getStarterPackRewardsType():
        return RewardItemModel

    def getChapterID(self):
        return self._getNumber(8)

    def setChapterID(self, value):
        self._setNumber(8, value)
        return

    def getReason(self):
        return RewardReason(self._getString(9))

    def setReason(self, value):
        self._setString(9, value.value)
        return

    def getIsFinalReward(self):
        return self._getBool(10)

    def setIsFinalReward(self, value):
        self._setBool(10, value)
        return

    def getIsBaseStyleLevel(self):
        return self._getBool(11)

    def setIsBaseStyleLevel(self, value):
        self._setBool(11, value)
        return

    def getIsNeedToShowOffer(self):
        return self._getBool(12)

    def setIsNeedToShowOffer(self, value):
        self._setBool(12, value)
        return

    def getSeasonStopped(self):
        return self._getBool(13)

    def setSeasonStopped(self, value):
        self._setBool(13, value)
        return

    def getWideRewardsIDs(self):
        return self._getArray(14)

    def setWideRewardsIDs(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getWideRewardsIDsType():
        return int

    def getIsExtra(self):
        return self._getBool(15)

    def setIsExtra(self, value):
        self._setBool(15, value)
        return

    def getIsPostProgressionUnlocked(self):
        return self._getBool(16)

    def setIsPostProgressionUnlocked(self, value):
        self._setBool(16, value)
        return

    def getIsStarterPack(self):
        return self._getBool(17)

    def setIsStarterPack(self, value):
        self._setBool(17, value)
        return

    def _initialize(self):
        super(BattlePassAwardsViewModel, self)._initialize()
        self._addViewModelProperty(b'mainRewards', UserListModel())
        self._addViewModelProperty(b'additionalRewards', UserListModel())
        self._addViewModelProperty(b'packageRewards', UserListModel())
        self._addViewModelProperty(b'starterPackRewards', UserListModel())
        self._addNumberProperty(b'chapterID', 0)
        self._addStringProperty(b'reason')
        self._addBoolProperty(b'isFinalReward', False)
        self._addBoolProperty(b'isBaseStyleLevel', False)
        self._addBoolProperty(b'isNeedToShowOffer', False)
        self._addBoolProperty(b'seasonStopped', False)
        self._addArrayProperty(b'wideRewardsIDs', Array())
        self._addBoolProperty(b'isExtra', False)
        self._addBoolProperty(b'isPostProgressionUnlocked', False)
        self._addBoolProperty(b'isStarterPack', False)
        self.onBuyClick = self._addCommand(b'onBuyClick')
        self.onClose = self._addCommand(b'onClose')
        self.onShowPostProgression = self._addCommand(b'onShowPostProgression')
        return
