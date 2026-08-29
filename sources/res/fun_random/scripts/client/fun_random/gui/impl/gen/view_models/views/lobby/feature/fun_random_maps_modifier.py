from frameworks.wulf import ViewModel

class FunRandomMapsModifier(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(FunRandomMapsModifier, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getPositionX(self):
        return self._getNumber(2)

    def setPositionX(self, value):
        self._setNumber(2, value)
        return

    def getPositionY(self):
        return self._getNumber(3)

    def setPositionY(self, value):
        self._setNumber(3, value)
        return

    def getTitle(self):
        return self._getString(4)

    def setTitle(self, value):
        self._setString(4, value)
        return

    def getDescription(self):
        return self._getString(5)

    def setDescription(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(FunRandomMapsModifier, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'positionX', 0)
        self._addNumberProperty(b'positionY', 0)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        return
