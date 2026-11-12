from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NyPetDecorationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(NyPetDecorationTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getResource(0)

    def setName(self, value):
        self._setResource(0, value)
        return

    def getDecorationType(self):
        return self._getString(1)

    def setDecorationType(self, value):
        self._setString(1, value)
        return

    def getDecorationTypeIcon(self):
        return self._getResource(2)

    def setDecorationTypeIcon(self, value):
        self._setResource(2, value)
        return

    def getDescription(self):
        return self._getResource(3)

    def setDescription(self, value):
        self._setResource(3, value)
        return

    def getIcon(self):
        return self._getResource(4)

    def setIcon(self, value):
        self._setResource(4, value)
        return

    def getIsLocked(self):
        return self._getBool(5)

    def setIsLocked(self, value):
        self._setBool(5, value)
        return

    def getPrice(self):
        return self._getNumber(6)

    def setPrice(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(NyPetDecorationTooltipModel, self)._initialize()
        self._addResourceProperty(b'name', R.invalid())
        self._addStringProperty(b'decorationType', b'')
        self._addResourceProperty(b'decorationTypeIcon', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        self._addBoolProperty(b'isLocked', True)
        self._addNumberProperty(b'price', 0)
        return
