from frameworks.wulf import ViewModel

class CriterionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CriterionModel, self).__init__(properties=properties, commands=commands)
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

    def getComponentId(self):
        return self._getString(2)

    def setComponentId(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(CriterionModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'componentId', b'')
        return
