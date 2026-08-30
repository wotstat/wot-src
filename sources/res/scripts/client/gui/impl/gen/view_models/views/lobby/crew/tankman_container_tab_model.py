from frameworks.wulf import ViewModel

class TankmanContainerTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TankmanContainerTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getCounter(self):
        return self._getNumber(2)

    def setCounter(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(TankmanContainerTabModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'title', b'')
        self._addNumberProperty(b'counter', 0)
        return
