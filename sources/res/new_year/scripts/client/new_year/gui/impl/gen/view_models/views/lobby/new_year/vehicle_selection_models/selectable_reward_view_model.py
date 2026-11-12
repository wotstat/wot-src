from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.vehicle_selection_models.discount_vehicle_bonus_model import DiscountVehicleBonusModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.vehicle_selection_models.selectable_reward_category_model import SelectableRewardCategoryModel

class SelectableRewardViewModel(ViewModel):
    __slots__ = (b'onCategorySelect', b'onFilterReset', b'onSelectReward', b'onClose', b'onConfirm')

    def __init__(self, properties=4, commands=5):
        super(SelectableRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategories(self):
        return self._getArray(0)

    def setCategories(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCategoriesType():
        return SelectableRewardCategoryModel

    def getTotalRewardsCount(self):
        return self._getNumber(1)

    def setTotalRewardsCount(self, value):
        self._setNumber(1, value)
        return

    def getSelectedRewardsCount(self):
        return self._getNumber(2)

    def setSelectedRewardsCount(self, value):
        self._setNumber(2, value)
        return

    def getSelectableRewards(self):
        return self._getArray(3)

    def setSelectableRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSelectableRewardsType():
        return DiscountVehicleBonusModel

    def _initialize(self):
        super(SelectableRewardViewModel, self)._initialize()
        self._addArrayProperty(b'categories', Array())
        self._addNumberProperty(b'totalRewardsCount', 0)
        self._addNumberProperty(b'selectedRewardsCount', 0)
        self._addArrayProperty(b'selectableRewards', Array())
        self.onCategorySelect = self._addCommand(b'onCategorySelect')
        self.onFilterReset = self._addCommand(b'onFilterReset')
        self.onSelectReward = self._addCommand(b'onSelectReward')
        self.onClose = self._addCommand(b'onClose')
        self.onConfirm = self._addCommand(b'onConfirm')
        return
