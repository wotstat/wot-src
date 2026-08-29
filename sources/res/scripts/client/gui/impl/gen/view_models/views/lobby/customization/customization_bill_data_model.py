from gui.impl.gen.view_models.views.lobby.customization.customization_bill_base_model import CustomizationBillBaseModel

class CustomizationBillDataModel(CustomizationBillBaseModel):
    __slots__ = (b'onAutoRentHintClose', b'onAutoRentChange', b'onCancelChanges', b'onClearBasket', b'onShowBuyWindow')

    def __init__(self, properties=15, commands=5):
        super(CustomizationBillDataModel, self).__init__(properties=properties, commands=commands)
        return

    def getCancelButtonEnabled(self):
        return self._getBool(10)

    def setCancelButtonEnabled(self, value):
        self._setBool(10, value)
        return

    def getClearButtonEnabled(self):
        return self._getBool(11)

    def setClearButtonEnabled(self, value):
        self._setBool(11, value)
        return

    def getIsAutoRentSelected(self):
        return self._getBool(12)

    def setIsAutoRentSelected(self, value):
        self._setBool(12, value)
        return

    def getShowAutoRentHint(self):
        return self._getBool(13)

    def setShowAutoRentHint(self, value):
        self._setBool(13, value)
        return

    def getIsLockedItem(self):
        return self._getBool(14)

    def setIsLockedItem(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(CustomizationBillDataModel, self)._initialize()
        self._addBoolProperty(b'cancelButtonEnabled', False)
        self._addBoolProperty(b'clearButtonEnabled', False)
        self._addBoolProperty(b'isAutoRentSelected', False)
        self._addBoolProperty(b'showAutoRentHint', False)
        self._addBoolProperty(b'isLockedItem', False)
        self.onAutoRentHintClose = self._addCommand(b'onAutoRentHintClose')
        self.onAutoRentChange = self._addCommand(b'onAutoRentChange')
        self.onCancelChanges = self._addCommand(b'onCancelChanges')
        self.onClearBasket = self._addCommand(b'onClearBasket')
        self.onShowBuyWindow = self._addCommand(b'onShowBuyWindow')
        return
