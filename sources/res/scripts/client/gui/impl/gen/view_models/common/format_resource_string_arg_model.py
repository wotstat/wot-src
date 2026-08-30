from frameworks.wulf import ViewModel

class FormatResourceStringArgModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FormatResourceStringArgModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(FormatResourceStringArgModel, self)._initialize()
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'name', b'')
        return
