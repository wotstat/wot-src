from frameworks.wulf import ViewModel

class TeamLogosModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TeamLogosModel, self).__init__(properties=properties, commands=commands)
        return

    def getX48(self):
        return self._getString(0)

    def setX48(self, value):
        self._setString(0, value)
        return

    def getX86(self):
        return self._getString(1)

    def setX86(self, value):
        self._setString(1, value)
        return

    def getX260(self):
        return self._getString(2)

    def setX260(self, value):
        self._setString(2, value)
        return

    def getX522(self):
        return self._getString(3)

    def setX522(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(TeamLogosModel, self)._initialize()
        self._addStringProperty(b'x48', b'')
        self._addStringProperty(b'x86', b'')
        self._addStringProperty(b'x260', b'')
        self._addStringProperty(b'x522', b'')
        return
