from frameworks.wulf import ViewModel

class ComparisonModel(ViewModel):
    __slots__ = (b'onAddToComparison',)
    ENABLED = b'enabled'
    DISABLED_FULL_BASKET = b'disabledFullBasket'
    DISABLED_ON_SERVER = b'disabledOnServer'
    CAN_NOT_COMPARE = b'canNotCompare'

    def __init__(self, properties=1, commands=1):
        super(ComparisonModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return self._getString(0)

    def setStatus(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(ComparisonModel, self)._initialize()
        self._addStringProperty(b'status', b'')
        self.onAddToComparison = self._addCommand(b'onAddToComparison')
        return
