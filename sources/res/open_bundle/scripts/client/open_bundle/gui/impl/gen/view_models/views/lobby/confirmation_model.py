from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__ = (b'confirm', b'cancel')

    def __init__(self, properties=4, commands=2):
        super(ConfirmationModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getBundleType(self):
        return self._getString(1)

    def setBundleType(self, value):
        self._setString(1, value)
        return

    def getBalance(self):
        return self._getArray(2)

    def setBalance(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getBalanceType():
        return PriceItemModel

    def getIsWalletAvailable(self):
        return self._getBool(3)

    def setIsWalletAvailable(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ConfirmationModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceItemModel())
        self._addStringProperty(b'bundleType', b'')
        self._addArrayProperty(b'balance', Array())
        self._addBoolProperty(b'isWalletAvailable', True)
        self.confirm = self._addCommand(b'confirm')
        self.cancel = self._addCommand(b'cancel')
        return
