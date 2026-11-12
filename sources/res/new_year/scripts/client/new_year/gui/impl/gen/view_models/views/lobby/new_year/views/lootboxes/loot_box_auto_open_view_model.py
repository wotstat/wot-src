from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.lootboxes.loot_box_reward_row_model import LootBoxRewardRowModel

class LootBoxAutoOpenViewModel(ViewModel):
    __slots__ = (b'onOkBtnClick', b'onCloseBtnClick')

    def __init__(self, properties=4, commands=2):
        super(LootBoxAutoOpenViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewardRows(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardRowsType():
        return LootBoxRewardRowModel

    def getSmallBoxesQuantity(self):
        return self._getNumber(1)

    def setSmallBoxesQuantity(self, value):
        self._setNumber(1, value)
        return

    def getBigBoxesQuantity(self):
        return self._getNumber(2)

    def setBigBoxesQuantity(self, value):
        self._setNumber(2, value)
        return

    def getGiftsQuantity(self):
        return self._getNumber(3)

    def setGiftsQuantity(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(LootBoxAutoOpenViewModel, self)._initialize()
        self._addViewModelProperty(b'rewardRows', UserListModel())
        self._addNumberProperty(b'smallBoxesQuantity', 0)
        self._addNumberProperty(b'bigBoxesQuantity', 0)
        self._addNumberProperty(b'giftsQuantity', 0)
        self.onOkBtnClick = self._addCommand(b'onOkBtnClick')
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        return
