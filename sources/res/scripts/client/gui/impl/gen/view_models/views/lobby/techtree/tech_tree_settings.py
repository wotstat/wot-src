from frameworks.wulf import ViewModel

class TechTreeSettings(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TechTreeSettings, self).__init__(properties=properties, commands=commands)
        return

    def getRowsNumber(self):
        return self._getNumber(0)

    def setRowsNumber(self, value):
        self._setNumber(0, value)
        return

    def getColumnsNumber(self):
        return self._getNumber(1)

    def setColumnsNumber(self, value):
        self._setNumber(1, value)
        return

    def getPremiumRowsNumber(self):
        return self._getNumber(2)

    def setPremiumRowsNumber(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(TechTreeSettings, self)._initialize()
        self._addNumberProperty(b'rowsNumber', 0)
        self._addNumberProperty(b'columnsNumber', 0)
        self._addNumberProperty(b'premiumRowsNumber', 0)
        return
