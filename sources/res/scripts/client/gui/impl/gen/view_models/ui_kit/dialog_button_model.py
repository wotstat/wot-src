from frameworks.wulf import ViewModel
from gui.impl.gen import R

class DialogButtonModel(ViewModel):
    __slots__ = (b'onClicked',)
    BTN_SUBMIT = b'submit'
    BTN_CANCEL = b'cancel'
    BTN_RESEARCH = b'research'
    BTN_PURCHASE = b'purchase'

    def __init__(self, properties=10, commands=1):
        super(DialogButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getRawLabel(self):
        return self._getString(1)

    def setRawLabel(self, value):
        self._setString(1, value)
        return

    def getLabel(self):
        return self._getResource(2)

    def setLabel(self, value):
        self._setResource(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def getDoSetFocus(self):
        return self._getBool(4)

    def setDoSetFocus(self, value):
        self._setBool(4, value)
        return

    def getIcon(self):
        return self._getResource(5)

    def setIcon(self, value):
        self._setResource(5, value)
        return

    def getIconAfterText(self):
        return self._getBool(6)

    def setIconAfterText(self, value):
        self._setBool(6, value)
        return

    def getSoundDown(self):
        return self._getResource(7)

    def setSoundDown(self, value):
        self._setResource(7, value)
        return

    def getTooltipHeader(self):
        return self._getResource(8)

    def setTooltipHeader(self, value):
        self._setResource(8, value)
        return

    def getTooltipBody(self):
        return self._getResource(9)

    def setTooltipBody(self, value):
        self._setResource(9, value)
        return

    def _initialize(self):
        super(DialogButtonModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'rawLabel', b'')
        self._addResourceProperty(b'label', R.invalid())
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'doSetFocus', False)
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'iconAfterText', True)
        self._addResourceProperty(b'soundDown', R.invalid())
        self._addResourceProperty(b'tooltipHeader', R.invalid())
        self._addResourceProperty(b'tooltipBody', R.invalid())
        self.onClicked = self._addCommand(b'onClicked')
        return
