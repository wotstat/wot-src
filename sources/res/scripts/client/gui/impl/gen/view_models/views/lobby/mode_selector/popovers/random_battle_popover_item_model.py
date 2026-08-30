from gui.impl.gen import R
from frameworks.wulf import ViewModel

class RandomBattlePopoverItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(RandomBattlePopoverItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getTooltipHeader(self):
        return self._getResource(1)

    def setTooltipHeader(self, value):
        self._setResource(1, value)
        return

    def getTooltipBody(self):
        return self._getResource(2)

    def setTooltipBody(self, value):
        self._setResource(2, value)
        return

    def getTooltipAlert(self):
        return self._getString(3)

    def setTooltipAlert(self, value):
        self._setString(3, value)
        return

    def getType(self):
        return self._getString(4)

    def setType(self, value):
        self._setString(4, value)
        return

    def getIsChecked(self):
        return self._getBool(5)

    def setIsChecked(self, value):
        self._setBool(5, value)
        return

    def getIsEnabled(self):
        return self._getBool(6)

    def setIsEnabled(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(RandomBattlePopoverItemModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'tooltipHeader', R.invalid())
        self._addResourceProperty(b'tooltipBody', R.invalid())
        self._addStringProperty(b'tooltipAlert', b'')
        self._addStringProperty(b'type', b'')
        self._addBoolProperty(b'isChecked', False)
        self._addBoolProperty(b'isEnabled', False)
        return
