from frameworks.wulf import ViewModel

class CurrencyRecordsItemDetailsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CurrencyRecordsItemDetailsModel, self).__init__(properties=properties, commands=commands)
        return

    def getItemName(self):
        return self._getString(0)

    def setItemName(self, value):
        self._setString(0, value)
        return

    def getItemValue(self):
        return self._getString(1)

    def setItemValue(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(CurrencyRecordsItemDetailsModel, self)._initialize()
        self._addStringProperty(b'itemName', b'')
        self._addStringProperty(b'itemValue', b'')
        return
