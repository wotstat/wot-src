from frameworks.wulf import ViewModel
from gui.impl.gen import R

class StyleUnlockedViewModel(ViewModel):
    __slots__ = (b'onOkClick', b'onSecondaryClick', b'onAnimationSound')

    def __init__(self, properties=5, commands=3):
        super(StyleUnlockedViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankLevel(self):
        return self._getString(0)

    def setTankLevel(self, value):
        self._setString(0, value)
        return

    def getTankTypeIcon(self):
        return self._getResource(1)

    def setTankTypeIcon(self, value):
        self._setResource(1, value)
        return

    def getTankName(self):
        return self._getString(2)

    def setTankName(self, value):
        self._setString(2, value)
        return

    def getSecondaryButtonTooltip(self):
        return self._getString(3)

    def setSecondaryButtonTooltip(self, value):
        self._setString(3, value)
        return

    def getSecondaryButtonEnabled(self):
        return self._getBool(4)

    def setSecondaryButtonEnabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(StyleUnlockedViewModel, self)._initialize()
        self._addStringProperty(b'tankLevel', b'')
        self._addResourceProperty(b'tankTypeIcon', R.invalid())
        self._addStringProperty(b'tankName', b'')
        self._addStringProperty(b'secondaryButtonTooltip', b'')
        self._addBoolProperty(b'secondaryButtonEnabled', False)
        self.onOkClick = self._addCommand(b'onOkClick')
        self.onSecondaryClick = self._addCommand(b'onSecondaryClick')
        self.onAnimationSound = self._addCommand(b'onAnimationSound')
        return
