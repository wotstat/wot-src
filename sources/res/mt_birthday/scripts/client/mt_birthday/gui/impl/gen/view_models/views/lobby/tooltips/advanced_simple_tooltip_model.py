from frameworks.wulf import ViewModel

class AdvancedSimpleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(AdvancedSimpleTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getHeader(self):
        return self._getString(0)

    def setHeader(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getAdditionalDescription(self):
        return self._getString(2)

    def setAdditionalDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(AdvancedSimpleTooltipModel, self)._initialize()
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'additionalDescription', b'')
        return
