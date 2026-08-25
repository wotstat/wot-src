from frameworks.wulf import ViewModel

class IconModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(IconModel, self).__init__(properties=properties, commands=commands)
        return

    def getSmall(self):
        return self._getString(0)

    def setSmall(self, value):
        self._setString(0, value)
        return

    def getBig(self):
        return self._getString(1)

    def setBig(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(IconModel, self)._initialize()
        self._addStringProperty(b'small', b'')
        self._addStringProperty(b'big', b'')
        return
