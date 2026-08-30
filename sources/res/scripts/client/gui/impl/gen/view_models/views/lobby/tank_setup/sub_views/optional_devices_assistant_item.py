from frameworks.wulf import Array, ViewModel

class OptionalDevicesAssistantItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(OptionalDevicesAssistantItem, self).__init__(properties=properties, commands=commands)
        return

    def getPopularity(self):
        return self._getReal(0)

    def setPopularity(self, value):
        self._setReal(0, value)
        return

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getItemsType():
        return unicode

    def _initialize(self):
        super(OptionalDevicesAssistantItem, self)._initialize()
        self._addRealProperty(b'popularity', 0.0)
        self._addArrayProperty(b'items', Array())
        return
