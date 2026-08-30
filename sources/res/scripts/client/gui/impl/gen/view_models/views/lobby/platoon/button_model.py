from frameworks.wulf import ViewModel

class ButtonModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=6, commands=1):
        super(ButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getCaption(self):
        return self._getString(0)

    def setCaption(self, value):
        self._setString(0, value)
        return

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getHasTooltip(self):
        return self._getBool(3)

    def setHasTooltip(self, value):
        self._setBool(3, value)
        return

    def getText(self):
        return self._getString(4)

    def setText(self, value):
        self._setString(4, value)
        return

    def getTooltipCaption(self):
        return self._getString(5)

    def setTooltipCaption(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(ButtonModel, self)._initialize()
        self._addStringProperty(b'caption', b'')
        self._addBoolProperty(b'isEnabled', True)
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'hasTooltip', True)
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'tooltipCaption', b'')
        self.onClick = self._addCommand(b'onClick')
        return
