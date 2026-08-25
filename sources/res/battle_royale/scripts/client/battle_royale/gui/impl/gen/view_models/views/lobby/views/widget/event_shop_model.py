from frameworks.wulf import ViewModel

class EventShopModel(ViewModel):
    __slots__ = (b'openShop',)

    def __init__(self, properties=2, commands=1):
        super(EventShopModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWGMoneyAvailable(self):
        return self._getBool(0)

    def setIsWGMoneyAvailable(self, value):
        self._setBool(0, value)
        return

    def getBalance(self):
        return self._getNumber(1)

    def setBalance(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(EventShopModel, self)._initialize()
        self._addBoolProperty(b'isWGMoneyAvailable', False)
        self._addNumberProperty(b'balance', 0)
        self.openShop = self._addCommand(b'openShop')
        return
