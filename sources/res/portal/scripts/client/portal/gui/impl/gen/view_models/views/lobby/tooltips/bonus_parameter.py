from frameworks.wulf import ViewModel

class BonusParameter(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BonusParameter, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(BonusParameter, self)._initialize()
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'description', b'')
        return
