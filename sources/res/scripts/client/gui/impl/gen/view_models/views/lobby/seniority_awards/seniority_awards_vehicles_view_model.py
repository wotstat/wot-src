from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_vehicle_model import SeniorityAwardsVehicleModel

class ViewState(Enum):
    SELECTION = b'selection'
    VIEW_REWARD_AFTER_SELECTION = b'viewRewardAfterSelection'
    VIEW_REWARD = b'viewReward'


class SeniorityAwardsVehiclesViewModel(ViewModel):
    __slots__ = (b'onMoreRewards', b'onGoToHangar', b'onClose', b'onSelectVehicleReward')

    def __init__(self, properties=6, commands=4):
        super(SeniorityAwardsVehiclesViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def getMaxCategory(self):
        return self._getString(1)

    def setMaxCategory(self, value):
        self._setString(1, value)
        return

    def getFromEntryPoint(self):
        return self._getBool(2)

    def setFromEntryPoint(self, value):
        self._setBool(2, value)
        return

    def getVehicles(self):
        return self._getArray(3)

    def setVehicles(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getVehiclesType():
        return SeniorityAwardsVehicleModel

    def getViewState(self):
        return ViewState(self._getString(4))

    def setViewState(self, value):
        self._setString(4, value.value)
        return

    def getAvailableRewardsCount(self):
        return self._getNumber(5)

    def setAvailableRewardsCount(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(SeniorityAwardsVehiclesViewModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        self._addStringProperty(b'maxCategory', b'')
        self._addBoolProperty(b'fromEntryPoint', False)
        self._addArrayProperty(b'vehicles', Array())
        self._addStringProperty(b'viewState', ViewState.VIEW_REWARD.value)
        self._addNumberProperty(b'availableRewardsCount', 0)
        self.onMoreRewards = self._addCommand(b'onMoreRewards')
        self.onGoToHangar = self._addCommand(b'onGoToHangar')
        self.onClose = self._addCommand(b'onClose')
        self.onSelectVehicleReward = self._addCommand(b'onSelectVehicleReward')
        return
