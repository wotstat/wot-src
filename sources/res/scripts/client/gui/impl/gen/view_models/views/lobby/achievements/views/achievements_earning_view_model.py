from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel

class AchievementsEarningViewModel(ViewModel):
    __slots__ = (b'onShown', b'onGoToAchievement')

    def __init__(self, properties=2, commands=2):
        super(AchievementsEarningViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAnimationPlaying(self):
        return self._getBool(0)

    def setIsAnimationPlaying(self, value):
        self._setBool(0, value)
        return

    def getAchievements(self):
        return self._getArray(1)

    def setAchievements(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getAchievementsType():
        return AdvancedAchievementModel

    def _initialize(self):
        super(AchievementsEarningViewModel, self)._initialize()
        self._addBoolProperty(b'isAnimationPlaying', False)
        self._addArrayProperty(b'achievements', Array())
        self.onShown = self._addCommand(b'onShown')
        self.onGoToAchievement = self._addCommand(b'onGoToAchievement')
        return
