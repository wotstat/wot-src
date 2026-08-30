from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class TriggersModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TriggersModel, self).__init__(properties=properties, commands=commands)
        return

    def getComponentId(self):
        return self._getString(0)

    def setComponentId(self, value):
        self._setString(0, value)
        return

    def getTriggers(self):
        return self._getArray(1)

    def setTriggers(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTriggersType():
        return unicode

    def _initialize(self):
        super(TriggersModel, self)._initialize()
        self._addStringProperty(b'componentId', b'')
        self._addArrayProperty(b'triggers', Array())
        return
