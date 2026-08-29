from enum import IntEnum
from frameworks.wulf import ViewModel

class StyleBuyingStatus(IntEnum):
    AVAILABLE = 0
    NOTENOUGHMONEY = 1
    BPNOTPASSED = 2


class StyleBuyingPanelModel(ViewModel):
    __slots__ = (b'onBuy',)

    def __init__(self, properties=5, commands=1):
        super(StyleBuyingPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getPrice(self):
        return self._getNumber(1)

    def setPrice(self, value):
        self._setNumber(1, value)
        return

    def getCurrency(self):
        return self._getString(2)

    def setCurrency(self, value):
        self._setString(2, value)
        return

    def getUserCurrency(self):
        return self._getNumber(3)

    def setUserCurrency(self, value):
        self._setNumber(3, value)
        return

    def getStatus(self):
        return StyleBuyingStatus(self._getNumber(4))

    def setStatus(self, value):
        self._setNumber(4, value.value)
        return

    def _initialize(self):
        super(StyleBuyingPanelModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'price', 0)
        self._addStringProperty(b'currency', b'')
        self._addNumberProperty(b'userCurrency', 0)
        self._addNumberProperty(b'status')
        self.onBuy = self._addCommand(b'onBuy')
        return
