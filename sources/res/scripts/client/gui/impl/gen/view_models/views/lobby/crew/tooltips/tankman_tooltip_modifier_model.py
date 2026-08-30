from frameworks.wulf import ViewModel
from gui.impl.gen import R

class TankmanTooltipModifierModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TankmanTooltipModifierModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getReal(0)

    def setValue(self, value):
        self._setReal(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getTitle(self):
        return self._getString(2)

    def setTitle(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(TankmanTooltipModifierModel, self)._initialize()
        self._addRealProperty(b'value', 0.0)
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        return
