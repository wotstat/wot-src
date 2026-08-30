from frameworks.wulf import ViewModel

class StatisticItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(StatisticItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getMainValue(self):
        return self._getString(1)

    def setMainValue(self, value):
        self._setString(1, value)
        return

    def getAdditionalValue(self):
        return self._getString(2)

    def setAdditionalValue(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(StatisticItemModel, self)._initialize()
        self._addStringProperty(b'type', b'battles')
        self._addStringProperty(b'mainValue', b'')
        self._addStringProperty(b'additionalValue', b'')
        return
