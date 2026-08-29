from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class FrontlineConfirmMultipleNamesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FrontlineConfirmMultipleNamesModel, self).__init__(properties=properties, commands=commands)
        return

    def getNames(self):
        return self._getArray(0)

    def setNames(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getNamesType():
        return unicode

    def _initialize(self):
        super(FrontlineConfirmMultipleNamesModel, self)._initialize()
        self._addArrayProperty(b'names', Array())
        return
