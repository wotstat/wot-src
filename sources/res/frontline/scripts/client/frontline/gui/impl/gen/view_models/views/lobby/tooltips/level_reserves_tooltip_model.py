from frameworks.wulf import Array, ViewModel

class LevelReservesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LevelReservesTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevels(self):
        return self._getArray(0)

    def setLevels(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getLevelsType():
        return unicode

    def getHasOptionalReserves(self):
        return self._getBool(1)

    def setHasOptionalReserves(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(LevelReservesTooltipModel, self)._initialize()
        self._addArrayProperty(b'levels', Array())
        self._addBoolProperty(b'hasOptionalReserves', False)
        return
