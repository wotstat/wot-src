from frameworks.wulf import ViewModel

class CompensationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CompensationModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getLabel(self):
        return self._getString(3)

    def setLabel(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(CompensationModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'label', b'')
        return
