from frameworks.wulf import ViewModel

class GameModeCellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(GameModeCellModel, self).__init__(properties=properties, commands=commands)
        return

    def getText(self):
        return self._getString(0)

    def setText(self, value):
        self._setString(0, value)
        return

    def getPoints(self):
        return self._getNumber(1)

    def setPoints(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(GameModeCellModel, self)._initialize()
        self._addStringProperty(b'text', b'')
        self._addNumberProperty(b'points', 0)
        return
