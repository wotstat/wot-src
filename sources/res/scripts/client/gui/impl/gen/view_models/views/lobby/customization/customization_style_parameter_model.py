from frameworks.wulf import ViewModel

class CustomizationStyleParameterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CustomizationStyleParameterModel, self).__init__(properties=properties, commands=commands)
        return

    def getPoId(self):
        return self._getString(0)

    def setPoId(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getString(2)

    def setValue(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(CustomizationStyleParameterModel, self)._initialize()
        self._addStringProperty(b'poId', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'value', b'')
        return
