from frameworks.wulf import ViewModel

class ClaimRewardsModel(ViewModel):
    __slots__ = (b'onGoToRewardSelection',)

    def __init__(self, properties=2, commands=1):
        super(ClaimRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewardsCount(self):
        return self._getNumber(0)

    def setRewardsCount(self, value):
        self._setNumber(0, value)
        return

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(ClaimRewardsModel, self)._initialize()
        self._addNumberProperty(b'rewardsCount', 0)
        self._addBoolProperty(b'isDisabled', False)
        self.onGoToRewardSelection = self._addCommand(b'onGoToRewardSelection')
        return
