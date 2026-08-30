from frameworks.wulf import ViewModel

class ShopSalesEntryPointViewModel(ViewModel):
    __slots__ = (b'onActionClick',)

    def __init__(self, properties=3, commands=1):
        super(ShopSalesEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStartDate(self):
        return self._getNumber(0)

    def setStartDate(self, value):
        self._setNumber(0, value)
        return

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)
        return

    def getTimestamp(self):
        return self._getNumber(2)

    def setTimestamp(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(ShopSalesEntryPointViewModel, self)._initialize()
        self._addNumberProperty(b'startDate', -1)
        self._addNumberProperty(b'endDate', -1)
        self._addNumberProperty(b'timestamp', -1)
        self.onActionClick = self._addCommand(b'onActionClick')
        return
