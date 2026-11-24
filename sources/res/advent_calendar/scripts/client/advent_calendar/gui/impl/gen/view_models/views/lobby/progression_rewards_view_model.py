from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionRewardItemViewModel

class ProgressionRewardsViewModel(ViewModel):
    __slots__ = (b'onProgressionRewardCompleted',)

    def __init__(self, properties=2, commands=1):
        super(ProgressionRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCompleted(self):
        return self._getBool(0)

    def setIsCompleted(self, value):
        self._setBool(0, value)
        return

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return ProgressionRewardItemViewModel

    def _initialize(self):
        super(ProgressionRewardsViewModel, self)._initialize()
        self._addBoolProperty(b'isCompleted', False)
        self._addArrayProperty(b'rewards', Array())
        self.onProgressionRewardCompleted = self._addCommand(b'onProgressionRewardCompleted')
        return
