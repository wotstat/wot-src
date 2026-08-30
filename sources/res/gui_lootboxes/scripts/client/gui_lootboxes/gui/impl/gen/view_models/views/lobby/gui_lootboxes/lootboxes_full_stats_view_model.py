from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.lootbox_view_model import LootboxViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.statistic_reward_model import StatisticRewardModel

class LootboxesFullStatsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSelectedLootBoxes', b'onVehiclePreview', b'onStylePreview')
    SELECT_LOOTBOXES_ARG_NAME = b'lootBoxesID'

    def __init__(self, properties=4, commands=4):
        super(LootboxesFullStatsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAllRewards(self):
        return self._getArray(0)

    def setAllRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getAllRewardsType():
        return StatisticRewardModel

    def getLootboxes(self):
        return self._getArray(1)

    def setLootboxes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getLootboxesType():
        return LootboxViewModel

    def getSelectedLootBoxes(self):
        return self._getArray(2)

    def setSelectedLootBoxes(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSelectedLootBoxesType():
        return int

    def getCategory(self):
        return self._getString(3)

    def setCategory(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(LootboxesFullStatsViewModel, self)._initialize()
        self._addArrayProperty(b'allRewards', Array())
        self._addArrayProperty(b'lootboxes', Array())
        self._addArrayProperty(b'selectedLootBoxes', Array())
        self._addStringProperty(b'category', b'')
        self.onClose = self._addCommand(b'onClose')
        self.onSelectedLootBoxes = self._addCommand(b'onSelectedLootBoxes')
        self.onVehiclePreview = self._addCommand(b'onVehiclePreview')
        self.onStylePreview = self._addCommand(b'onStylePreview')
        return
