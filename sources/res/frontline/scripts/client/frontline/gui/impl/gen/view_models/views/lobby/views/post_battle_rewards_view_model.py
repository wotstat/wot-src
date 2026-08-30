from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_reward_model import FrontlineRewardModel

class PostBattleRewardsViewModel(ViewModel):
    __slots__ = (b'onClaimRewards', b'onContinue', b'onClose', b'onIntroStartsPlaying', b'onRibbonStartsPlaying', b'onProgressBarAnimationStart', b'onProgressBarAnimationComplete')

    def __init__(self, properties=8, commands=7):
        super(PostBattleRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRank(self):
        return self._getNumber(0)

    def setRank(self, value):
        self._setNumber(0, value)
        return

    def getPrevProgress(self):
        return self._getReal(1)

    def setPrevProgress(self, value):
        self._setReal(1, value)
        return

    def getCurrProgress(self):
        return self._getReal(2)

    def setCurrProgress(self, value):
        self._setReal(2, value)
        return

    def getAchievedPoints(self):
        return self._getNumber(3)

    def setAchievedPoints(self, value):
        self._setNumber(3, value)
        return

    def getAmountRewardsToClaim(self):
        return self._getNumber(4)

    def setAmountRewardsToClaim(self, value):
        self._setNumber(4, value)
        return

    def getMaxLevel(self):
        return self._getNumber(5)

    def setMaxLevel(self, value):
        self._setNumber(5, value)
        return

    def getIsMaxLevel(self):
        return self._getBool(6)

    def setIsMaxLevel(self, value):
        self._setBool(6, value)
        return

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return FrontlineRewardModel

    def _initialize(self):
        super(PostBattleRewardsViewModel, self)._initialize()
        self._addNumberProperty(b'rank', 0)
        self._addRealProperty(b'prevProgress', 0.0)
        self._addRealProperty(b'currProgress', 0.0)
        self._addNumberProperty(b'achievedPoints', 0)
        self._addNumberProperty(b'amountRewardsToClaim', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addBoolProperty(b'isMaxLevel', False)
        self._addArrayProperty(b'rewards', Array())
        self.onClaimRewards = self._addCommand(b'onClaimRewards')
        self.onContinue = self._addCommand(b'onContinue')
        self.onClose = self._addCommand(b'onClose')
        self.onIntroStartsPlaying = self._addCommand(b'onIntroStartsPlaying')
        self.onRibbonStartsPlaying = self._addCommand(b'onRibbonStartsPlaying')
        self.onProgressBarAnimationStart = self._addCommand(b'onProgressBarAnimationStart')
        self.onProgressBarAnimationComplete = self._addCommand(b'onProgressBarAnimationComplete')
        return
