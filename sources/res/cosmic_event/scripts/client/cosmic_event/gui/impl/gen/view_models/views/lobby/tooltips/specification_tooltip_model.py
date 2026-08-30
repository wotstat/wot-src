from frameworks.wulf import ViewModel

class SpecificationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SpecificationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(SpecificationTooltipModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        return
