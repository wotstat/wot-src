from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from winback.gui.impl.gen.view_models.views.lobby.views.selectable_reward_category_model import SelectableRewardCategoryModel

class SelectableRewardName(Enum):
    VEHICLE = b'vehicle'
    COMPENSATION = b'compensation'


class WinbackSelectableRewardViewModel(ViewModel):
    __slots__ = (b'onCategorySelect', b'onFilterReset', b'onSelectReward', b'onClose', b'onConfirm')
    VEHICLE_LEVEL = b'vehicleLevel'
    REWARD_INDEX = b'rewardIndex'

    def __init__(self, properties=5, commands=5):
        super(WinbackSelectableRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategories(self):
        return self._getArray(0)

    def setCategories(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCategoriesType():
        return SelectableRewardCategoryModel

    def getProgressionName(self):
        return self._getString(1)

    def setProgressionName(self, value):
        self._setString(1, value)
        return

    def getTotalRewardsCount(self):
        return self._getNumber(2)

    def setTotalRewardsCount(self, value):
        self._setNumber(2, value)
        return

    def getSelectedRewardsCount(self):
        return self._getNumber(3)

    def setSelectedRewardsCount(self, value):
        self._setNumber(3, value)
        return

    def getSelectableRewards(self):
        return self._getArray(4)

    def setSelectableRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSelectableRewardsType():
        return BonusModel

    def _initialize(self):
        super(WinbackSelectableRewardViewModel, self)._initialize()
        self._addArrayProperty(b'categories', Array())
        self._addStringProperty(b'progressionName', b'')
        self._addNumberProperty(b'totalRewardsCount', 0)
        self._addNumberProperty(b'selectedRewardsCount', 0)
        self._addArrayProperty(b'selectableRewards', Array())
        self.onCategorySelect = self._addCommand(b'onCategorySelect')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        self.onSelectReward = self._addCommand(b'onSelectReward')
        self.onClose = self._addCommand(b'onClose')
        self.onConfirm = self._addCommand(b'onConfirm')
        return
