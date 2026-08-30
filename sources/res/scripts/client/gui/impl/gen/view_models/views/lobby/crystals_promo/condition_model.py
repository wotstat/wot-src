from frameworks.wulf import ViewModel

class ConditionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ConditionModel, self).__init__(properties=properties, commands=commands)
        return

    def getPosition(self):
        return self._getNumber(0)

    def setPosition(self, value):
        self._setNumber(0, value)
        return

    def getForWin(self):
        return self._getNumber(1)

    def setForWin(self, value):
        self._setNumber(1, value)
        return

    def getForDefeat(self):
        return self._getNumber(2)

    def setForDefeat(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(ConditionModel, self)._initialize()
        self._addNumberProperty(b'position', 0)
        self._addNumberProperty(b'forWin', 0)
        self._addNumberProperty(b'forDefeat', 0)
        return
