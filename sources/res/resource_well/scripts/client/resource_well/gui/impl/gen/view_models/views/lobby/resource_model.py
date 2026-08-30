from frameworks.wulf import ViewModel

class ResourceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ResourceModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getInventoryCount(self):
        return self._getNumber(1)

    def setInventoryCount(self, value):
        self._setNumber(1, value)
        return

    def getLimit(self):
        return self._getNumber(2)

    def setLimit(self, value):
        self._setNumber(2, value)
        return

    def getBalance(self):
        return self._getNumber(3)

    def setBalance(self, value):
        self._setNumber(3, value)
        return

    def getRate(self):
        return self._getReal(4)

    def setRate(self, value):
        self._setReal(4, value)
        return

    def getTooltipId(self):
        return self._getString(5)

    def setTooltipId(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(ResourceModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'inventoryCount', 0)
        self._addNumberProperty(b'limit', 0)
        self._addNumberProperty(b'balance', 0)
        self._addRealProperty(b'rate', 0.0)
        self._addStringProperty(b'tooltipId', b'')
        return
