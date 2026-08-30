from frameworks.wulf import ViewModel

class ConversionTooltipBookModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ConversionTooltipBookModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getNation(self):
        return self._getString(2)

    def setNation(self, value):
        self._setString(2, value)
        return

    def getValue(self):
        return self._getNumber(3)

    def setValue(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(ConversionTooltipBookModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'nation', b'')
        self._addNumberProperty(b'value', 0)
        return
