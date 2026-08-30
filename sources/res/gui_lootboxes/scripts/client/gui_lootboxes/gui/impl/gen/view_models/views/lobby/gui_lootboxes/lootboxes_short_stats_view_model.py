from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.statistic_reward_model import StatisticRewardModel

class TabState(IntEnum):
    SINGLE = 0
    ALL = 1


class LootboxesShortStatsViewModel(ViewModel):
    __slots__ = (b'onCloseStat', b'onOpenFullStats', b'onTabSwitch', b'onVehiclePreview')

    def __init__(self, properties=8, commands=4):
        super(LootboxesShortStatsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentTab(self):
        return TabState(self._getNumber(0))

    def setCurrentTab(self, value):
        self._setNumber(0, value.value)
        return

    def getCurrentRewards(self):
        return self._getArray(1)

    def setCurrentRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCurrentRewardsType():
        return StatisticRewardModel

    def getAllRewards(self):
        return self._getArray(2)

    def setAllRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getAllRewardsType():
        return StatisticRewardModel

    def getIsLoading(self):
        return self._getBool(3)

    def setIsLoading(self, value):
        self._setBool(3, value)
        return

    def getLootBoxName(self):
        return self._getString(4)

    def setLootBoxName(self, value):
        self._setString(4, value)
        return

    def getIsShown(self):
        return self._getBool(5)

    def setIsShown(self, value):
        self._setBool(5, value)
        return

    def getHasVisibleLootBoxes(self):
        return self._getBool(6)

    def setHasVisibleLootBoxes(self, value):
        self._setBool(6, value)
        return

    def getIsOptDeviceRestored(self):
        return self._getBool(7)

    def setIsOptDeviceRestored(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(LootboxesShortStatsViewModel, self)._initialize()
        self._addNumberProperty(b'currentTab')
        self._addArrayProperty(b'currentRewards', Array())
        self._addArrayProperty(b'allRewards', Array())
        self._addBoolProperty(b'isLoading', True)
        self._addStringProperty(b'lootBoxName', b'')
        self._addBoolProperty(b'isShown', False)
        self._addBoolProperty(b'hasVisibleLootBoxes', False)
        self._addBoolProperty(b'isOptDeviceRestored', True)
        self.onCloseStat = self._addCommand(b'onCloseStat')
        self.onOpenFullStats = self._addCommand(b'onOpenFullStats')
        self.onTabSwitch = self._addCommand(b'onTabSwitch')
        self.onVehiclePreview = self._addCommand(b'onVehiclePreview')
        return
