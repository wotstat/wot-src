from frameworks.wulf import ViewModel

class RespawnPointViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RespawnPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPointID(self):
        return self._getString(0)

    def setPointID(self, value):
        self._setString(0, value)
        return

    def getCoordX(self):
        return self._getNumber(1)

    def setCoordX(self, value):
        self._setNumber(1, value)
        return

    def getCoordY(self):
        return self._getNumber(2)

    def setCoordY(self, value):
        self._setNumber(2, value)
        return

    def getPlayerName1(self):
        return self._getString(3)

    def setPlayerName1(self, value):
        self._setString(3, value)
        return

    def getPlayerName2(self):
        return self._getString(4)

    def setPlayerName2(self, value):
        self._setString(4, value)
        return

    def getSelected(self):
        return self._getBool(5)

    def setSelected(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(RespawnPointViewModel, self)._initialize()
        self._addStringProperty(b'pointID', b'')
        self._addNumberProperty(b'coordX', 0)
        self._addNumberProperty(b'coordY', 0)
        self._addStringProperty(b'playerName1', b'')
        self._addStringProperty(b'playerName2', b'')
        self._addBoolProperty(b'selected', False)
        return
