from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_item_model import SelectableRewardItemModel
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_tab_model import SelectableRewardTabModel

class SelectableRewardModel(ViewModel):
    __slots__ = (b'onOkClick', b'onCloseClick', b'onTabClick', b'onRewardAdd', b'onRewardReduce')

    def __init__(self, properties=4, commands=5):
        super(SelectableRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getTabs(self):
        return self._getArray(0)

    def setTabs(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getTabsType():
        return SelectableRewardTabModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getRewardsType():
        return SelectableRewardItemModel

    def getTotalRewardCount(self):
        return self._getNumber(2)

    def setTotalRewardCount(self, value):
        self._setNumber(2, value)
        return

    def getSelectedTab(self):
        return self._getString(3)

    def setSelectedTab(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(SelectableRewardModel, self)._initialize()
        self._addArrayProperty(b'tabs', Array())
        self._addArrayProperty(b'rewards', Array())
        self._addNumberProperty(b'totalRewardCount', 0)
        self._addStringProperty(b'selectedTab', b'')
        self.onOkClick = self._addCommand(b'onOkClick')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onTabClick = self._addCommand(b'onTabClick')
        self.onRewardAdd = self._addCommand(b'onRewardAdd')
        self.onRewardReduce = self._addCommand(b'onRewardReduce')
        return
