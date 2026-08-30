from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.reward_view_rewards_model import RewardViewRewardsModel

class RewardViewModel(ViewModel):
    __slots__ = (b'onGoToDogTag', b'onGoToAchievement', b'onOpenNextReward', b'onOpenAchievementsPage', b'onClose')

    def __init__(self, properties=4, commands=5):
        super(RewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFirstEntry(self):
        return self._getBool(0)

    def setIsFirstEntry(self, value):
        self._setBool(0, value)
        return

    def getRewardsBalance(self):
        return self._getNumber(1)

    def setRewardsBalance(self, value):
        self._setNumber(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return RewardViewRewardsModel

    def getAchievements(self):
        return self._getArray(3)

    def setAchievements(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getAchievementsType():
        return AdvancedAchievementModel

    def _initialize(self):
        super(RewardViewModel, self)._initialize()
        self._addBoolProperty(b'isFirstEntry', False)
        self._addNumberProperty(b'rewardsBalance', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'achievements', Array())
        self.onGoToDogTag = self._addCommand(b'onGoToDogTag')
        self.onGoToAchievement = self._addCommand(b'onGoToAchievement')
        self.onOpenNextReward = self._addCommand(b'onOpenNextReward')
        self.onOpenAchievementsPage = self._addCommand(b'onOpenAchievementsPage')
        self.onClose = self._addCommand(b'onClose')
        return
