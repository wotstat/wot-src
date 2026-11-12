from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.raid_item_model import RaidItemModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipts_panel import ReceiptsPanel

class NyTamagotchiRaidViewModel(ViewModel):
    __slots__ = (b'onOnboardingRestart', b'onRaidStart', b'onUpdateSelected', b'onClose', b'onReceiveReward', b'onAccelerationRaid', b'onOpenReceiptsTabs', b'onCloseReceiptsTabs', b'onSetOnboardingEnd', b'onRecipiePreview')

    def __init__(self, properties=16, commands=10):
        super(NyTamagotchiRaidViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def receiptsPanel(self):
        return self._getViewModel(0)

    @staticmethod
    def getReceiptsPanelType():
        return ReceiptsPanel

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getItemsType():
        return RaidItemModel

    def getSelectedItems(self):
        return self._getArray(2)

    def setSelectedItems(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSelectedItemsType():
        return RaidItemModel

    def getTimeLeft(self):
        return self._getNumber(3)

    def setTimeLeft(self, value):
        self._setNumber(3, value)
        return

    def getRemainingTime(self):
        return self._getNumber(4)

    def setRemainingTime(self, value):
        self._setNumber(4, value)
        return

    def getPreviewTime(self):
        return self._getNumber(5)

    def setPreviewTime(self, value):
        self._setNumber(5, value)
        return

    def getIsTamagotchiForRaidReady(self):
        return self._getBool(6)

    def setIsTamagotchiForRaidReady(self, value):
        self._setBool(6, value)
        return

    def getIsHasUnreceivedReward(self):
        return self._getBool(7)

    def setIsHasUnreceivedReward(self, value):
        self._setBool(7, value)
        return

    def getIsBoostMode(self):
        return self._getBool(8)

    def setIsBoostMode(self, value):
        self._setBool(8, value)
        return

    def getIsFirstOnboardingEnter(self):
        return self._getBool(9)

    def setIsFirstOnboardingEnter(self, value):
        self._setBool(9, value)
        return

    def getBoostAmount(self):
        return self._getNumber(10)

    def setBoostAmount(self, value):
        self._setNumber(10, value)
        return

    def getMaxBoostLimit(self):
        return self._getNumber(11)

    def setMaxBoostLimit(self, value):
        self._setNumber(11, value)
        return

    def getBoostTime(self):
        return self._getNumber(12)

    def setBoostTime(self, value):
        self._setNumber(12, value)
        return

    def getIsReceiptsTabsOpened(self):
        return self._getBool(13)

    def setIsReceiptsTabsOpened(self, value):
        self._setBool(13, value)
        return

    def getBoostAccrualTime(self):
        return self._getNumber(14)

    def setBoostAccrualTime(self, value):
        self._setNumber(14, value)
        return

    def getBoostsToAdd(self):
        return self._getNumber(15)

    def setBoostsToAdd(self, value):
        self._setNumber(15, value)
        return

    def _initialize(self):
        super(NyTamagotchiRaidViewModel, self)._initialize()
        self._addViewModelProperty(b'receiptsPanel', ReceiptsPanel())
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'selectedItems', Array())
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'remainingTime', 0)
        self._addNumberProperty(b'previewTime', 0)
        self._addBoolProperty(b'isTamagotchiForRaidReady', False)
        self._addBoolProperty(b'isHasUnreceivedReward', False)
        self._addBoolProperty(b'isBoostMode', False)
        self._addBoolProperty(b'isFirstOnboardingEnter', False)
        self._addNumberProperty(b'boostAmount', 0)
        self._addNumberProperty(b'maxBoostLimit', 0)
        self._addNumberProperty(b'boostTime', 0)
        self._addBoolProperty(b'isReceiptsTabsOpened', False)
        self._addNumberProperty(b'boostAccrualTime', 0)
        self._addNumberProperty(b'boostsToAdd', 0)
        self.onOnboardingRestart = self._addCommand(b'onOnboardingRestart')
        self.onRaidStart = self._addCommand(b'onRaidStart')
        self.onUpdateSelected = self._addCommand(b'onUpdateSelected')
        self.onClose = self._addCommand(b'onClose')
        self.onReceiveReward = self._addCommand(b'onReceiveReward')
        self.onAccelerationRaid = self._addCommand(b'onAccelerationRaid')
        self.onOpenReceiptsTabs = self._addCommand(b'onOpenReceiptsTabs')
        self.onCloseReceiptsTabs = self._addCommand(b'onCloseReceiptsTabs')
        self.onSetOnboardingEnd = self._addCommand(b'onSetOnboardingEnd')
        self.onRecipiePreview = self._addCommand(b'onRecipiePreview')
        return
