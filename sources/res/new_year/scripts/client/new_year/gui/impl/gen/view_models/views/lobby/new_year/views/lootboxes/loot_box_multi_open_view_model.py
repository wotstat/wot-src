from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.lootboxes.loot_box_reward_row_model import LootBoxRewardRowModel

class LootBoxMultiOpenViewModel(ViewModel):
    __slots__ = (b'onCloseBtnClick', b'onShowAnimationBtnClick', b'showSpecialReward', b'onOpenBox', b'onReadyToRestart', b'onContinueOpening', b'onPauseOpening')
    USUAL_BOX_TYPE = b'newYear_usual'
    PREMIUM_BOX_TYPE = b'newYear_premium'

    def __init__(self, properties=18, commands=7):
        super(LootBoxMultiOpenViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewardRows(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardRowsType():
        return LootBoxRewardRowModel

    def getOpenedCount(self):
        return self._getNumber(1)

    def setOpenedCount(self, value):
        self._setNumber(1, value)
        return

    def getBoxesCounter(self):
        return self._getNumber(2)

    def setBoxesCounter(self, value):
        self._setNumber(2, value)
        return

    def getLimitToOpen(self):
        return self._getNumber(3)

    def setLimitToOpen(self, value):
        self._setNumber(3, value)
        return

    def getLootboxType(self):
        return self._getString(4)

    def setLootboxType(self, value):
        self._setString(4, value)
        return

    def getLootboxIcon(self):
        return self._getResource(5)

    def setLootboxIcon(self, value):
        self._setResource(5, value)
        return

    def getBoxCategory(self):
        return self._getString(6)

    def setBoxCategory(self, value):
        self._setString(6, value)
        return

    def getRestart(self):
        return self._getBool(7)

    def setRestart(self, value):
        self._setBool(7, value)
        return

    def getIsFreeBox(self):
        return self._getBool(8)

    def setIsFreeBox(self, value):
        self._setBool(8, value)
        return

    def getIsLootboxesEnabled(self):
        return self._getBool(9)

    def setIsLootboxesEnabled(self, value):
        self._setBool(9, value)
        return

    def getHardReset(self):
        return self._getBool(10)

    def setHardReset(self, value):
        self._setBool(10, value)
        return

    def getIsPausedForSpecial(self):
        return self._getBool(11)

    def setIsPausedForSpecial(self, value):
        self._setBool(11, value)
        return

    def getIsOnPause(self):
        return self._getBool(12)

    def setIsOnPause(self, value):
        self._setBool(12, value)
        return

    def getStartShowIndex(self):
        return self._getNumber(13)

    def setStartShowIndex(self, value):
        self._setNumber(13, value)
        return

    def getLeftToOpenCount(self):
        return self._getNumber(14)

    def setLeftToOpenCount(self, value):
        self._setNumber(14, value)
        return

    def getCurrentPage(self):
        return self._getNumber(15)

    def setCurrentPage(self, value):
        self._setNumber(15, value)
        return

    def getIsServerError(self):
        return self._getBool(16)

    def setIsServerError(self, value):
        self._setBool(16, value)
        return

    def getIsAnimationEnabled(self):
        return self._getBool(17)

    def setIsAnimationEnabled(self, value):
        self._setBool(17, value)
        return

    def _initialize(self):
        super(LootBoxMultiOpenViewModel, self)._initialize()
        self._addViewModelProperty(b'rewardRows', UserListModel())
        self._addNumberProperty(b'openedCount', 0)
        self._addNumberProperty(b'boxesCounter', 0)
        self._addNumberProperty(b'limitToOpen', 0)
        self._addStringProperty(b'lootboxType', b'')
        self._addResourceProperty(b'lootboxIcon', R.invalid())
        self._addStringProperty(b'boxCategory', b'')
        self._addBoolProperty(b'restart', False)
        self._addBoolProperty(b'isFreeBox', False)
        self._addBoolProperty(b'isLootboxesEnabled', True)
        self._addBoolProperty(b'hardReset', False)
        self._addBoolProperty(b'isPausedForSpecial', False)
        self._addBoolProperty(b'isOnPause', False)
        self._addNumberProperty(b'startShowIndex', 0)
        self._addNumberProperty(b'leftToOpenCount', 0)
        self._addNumberProperty(b'currentPage', 0)
        self._addBoolProperty(b'isServerError', False)
        self._addBoolProperty(b'isAnimationEnabled', False)
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onShowAnimationBtnClick = self._addCommand(b'onShowAnimationBtnClick')
        self.showSpecialReward = self._addCommand(b'showSpecialReward')
        self.onOpenBox = self._addCommand(b'onOpenBox')
        self.onReadyToRestart = self._addCommand(b'onReadyToRestart')
        self.onContinueOpening = self._addCommand(b'onContinueOpening')
        self.onPauseOpening = self._addCommand(b'onPauseOpening')
        return
