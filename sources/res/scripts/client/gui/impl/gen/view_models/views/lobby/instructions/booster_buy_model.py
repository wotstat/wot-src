from gui.impl.gen.view_models.views.lobby.common.buy_sell_items_dialog_model import BuySellItemsDialogModel

class BoosterBuyModel(BuySellItemsDialogModel):
    __slots__ = (b'onSetIsRearm',)

    def __init__(self, properties=27, commands=4):
        super(BoosterBuyModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsRearm(self):
        return self._getBool(24)

    def setIsRearm(self, value):
        self._setBool(24, value)
        return

    def getIsDiscount(self):
        return self._getBool(25)

    def setIsDiscount(self, value):
        self._setBool(25, value)
        return

    def getDiscountValue(self):
        return self._getNumber(26)

    def setDiscountValue(self, value):
        self._setNumber(26, value)
        return

    def _initialize(self):
        super(BoosterBuyModel, self)._initialize()
        self._addBoolProperty(b'isRearm', False)
        self._addBoolProperty(b'isDiscount', False)
        self._addNumberProperty(b'discountValue', 0)
        self.onSetIsRearm = self._addCommand(b'onSetIsRearm')
        return
