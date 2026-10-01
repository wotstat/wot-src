from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.portal_reward_item_model import PortalRewardItemModel

class PortalRewardType(Enum):
    PROGRESSION = b'progression'
    LAST_LEVEL_VICTORY = b'lastLevelVictory'
    ALL_VEHICLES_UPGRADED = b'allVehiclesUpgraded'


class PortalRewardsViewModel(ViewModel):
    __slots__ = (b'onApprove', b'onShopClick')

    def __init__(self, properties=4, commands=2):
        super(PortalRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewardType(self):
        return PortalRewardType(self._getString(0))

    def setRewardType(self, value):
        self._setString(0, value.value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getIsSpecial(self):
        return self._getBool(2)

    def setIsSpecial(self, value):
        self._setBool(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return PortalRewardItemModel

    def _initialize(self):
        super(PortalRewardsViewModel, self)._initialize()
        self._addStringProperty(b'rewardType')
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isSpecial', False)
        self._addArrayProperty(b'rewards', Array())
        self.onApprove = self._addCommand(b'onApprove')
        self.onShopClick = self._addCommand(b'onShopClick')
        return
