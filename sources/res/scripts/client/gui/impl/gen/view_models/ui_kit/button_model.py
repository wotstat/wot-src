from gui.impl.gen import R
from frameworks.wulf import ViewModel

class ButtonModel(ViewModel):
    __slots__ = (b'onClicked',)

    def __init__(self, properties=5, commands=1):
        super(ButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getRawLabel(self):
        return self._getString(0)

    def setRawLabel(self, value):
        self._setString(0, value)
        return

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)
        return

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def getIconAfterText(self):
        return self._getBool(4)

    def setIconAfterText(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(ButtonModel, self)._initialize()
        self._addStringProperty(b'rawLabel', b'')
        self._addResourceProperty(b'label', R.invalid())
        self._addBoolProperty(b'isEnabled', True)
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'iconAfterText', True)
        self.onClicked = self._addCommand(b'onClicked')
        return
