from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.battle_royale_reward_points import BattleRoyaleRewardPoints
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_model import RewardPointsModel

class ChapterType(Enum):
    DEFAULT = b'default'
    MARATHON = b'marathon'
    RESOURCE = b'resource'


class BattlePassInProgressTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(BattlePassInProgressTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewardPoints(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardPointsType():
        return RewardPointsModel

    @property
    def battleRoyaleRewardPoints(self):
        return self._getViewModel(1)

    @staticmethod
    def getBattleRoyaleRewardPointsType():
        return BattleRoyaleRewardPoints

    @property
    def rewardsCommon(self):
        return self._getViewModel(2)

    @staticmethod
    def getRewardsCommonType():
        return BonusModel

    @property
    def rewardsElite(self):
        return self._getViewModel(3)

    @staticmethod
    def getRewardsEliteType():
        return BonusModel

    def getLevel(self):
        return self._getNumber(4)

    def setLevel(self, value):
        self._setNumber(4, value)
        return

    def getChapter(self):
        return self._getNumber(5)

    def setChapter(self, value):
        self._setNumber(5, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(6)

    def setCurrentPoints(self, value):
        self._setNumber(6, value)
        return

    def getMaxPoints(self):
        return self._getNumber(7)

    def setMaxPoints(self, value):
        self._setNumber(7, value)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(8)

    def setIsBattlePassPurchased(self, value):
        self._setBool(8, value)
        return

    def getTimeTillEnd(self):
        return self._getString(9)

    def setTimeTillEnd(self, value):
        self._setString(9, value)
        return

    def getBattleType(self):
        return self._getString(10)

    def setBattleType(self, value):
        self._setString(10, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(11)

    def setNotChosenRewardCount(self, value):
        self._setNumber(11, value)
        return

    def getChapterType(self):
        return ChapterType(self._getString(12))

    def setChapterType(self, value):
        self._setString(12, value.value)
        return

    def getExpireTime(self):
        return self._getNumber(13)

    def setExpireTime(self, value):
        self._setNumber(13, value)
        return

    def _initialize(self):
        super(BattlePassInProgressTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'rewardPoints', UserListModel())
        self._addViewModelProperty(b'battleRoyaleRewardPoints', BattleRoyaleRewardPoints())
        self._addViewModelProperty(b'rewardsCommon', UserListModel())
        self._addViewModelProperty(b'rewardsElite', UserListModel())
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'chapter', 0)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'maxPoints', 0)
        self._addBoolProperty(b'isBattlePassPurchased', False)
        self._addStringProperty(b'timeTillEnd', b'')
        self._addStringProperty(b'battleType', b'')
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addStringProperty(b'chapterType')
        self._addNumberProperty(b'expireTime', 0)
        return
