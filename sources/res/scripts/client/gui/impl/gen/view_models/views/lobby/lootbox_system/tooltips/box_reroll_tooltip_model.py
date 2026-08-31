from frameworks.wulf import Array, ViewModel

class BoxRerollTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BoxRerollTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrency(self):
        return self._getString(0)

    def setCurrency(self, value):
        self._setString(0, value)
        return

    def getPrices(self):
        return self._getArray(1)

    def setPrices(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getPricesType():
        return int

    def getRerollAttempts(self):
        return self._getNumber(2)

    def setRerollAttempts(self, value):
        self._setNumber(2, value)
        return

    def getEventName(self):
        return self._getString(3)

    def setEventName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(BoxRerollTooltipModel, self)._initialize()
        self._addStringProperty(b'currency', b'')
        self._addArrayProperty(b'prices', Array())
        self._addNumberProperty(b'rerollAttempts', 0)
        self._addStringProperty(b'eventName', b'')
        return
