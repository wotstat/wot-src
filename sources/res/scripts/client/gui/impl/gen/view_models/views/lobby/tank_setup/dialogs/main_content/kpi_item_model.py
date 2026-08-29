from frameworks.wulf import ViewModel

class KpiItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(KpiItemModel, self).__init__(properties=properties, commands=commands)
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

    def _initialize(self):
        super(KpiItemModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value', b'')
        return
