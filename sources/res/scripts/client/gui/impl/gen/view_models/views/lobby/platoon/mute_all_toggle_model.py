from frameworks.wulf import ViewModel

class MuteAllToggleModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(MuteAllToggleModel, self).__init__(properties=properties, commands=commands)
        return

    def getTooltipHeader(self):
        return self._getString(0)

    def setTooltipHeader(self, value):
        self._setString(0, value)
        return

    def getTooltipBody(self):
        return self._getString(1)

    def setTooltipBody(self, value):
        self._setString(1, value)
        return

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)
        return

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(MuteAllToggleModel, self)._initialize()
        self._addStringProperty(b'tooltipHeader', b'')
        self._addStringProperty(b'tooltipBody', b'')
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isVisible', True)
        self.onClick = self._addCommand(b'onClick')
        return
