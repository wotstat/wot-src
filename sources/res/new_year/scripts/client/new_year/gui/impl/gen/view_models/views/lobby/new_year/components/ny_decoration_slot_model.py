from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NyDecorationSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(NyDecorationSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getToyID(self):
        return self._getNumber(0)

    def setToyID(self, value):
        self._setNumber(0, value)
        return

    def getImageName(self):
        return self._getString(1)

    def setImageName(self, value):
        self._setString(1, value)
        return

    def getTitle(self):
        return self._getResource(2)

    def setTitle(self, value):
        self._setResource(2, value)
        return

    def getDescription(self):
        return self._getResource(3)

    def setDescription(self, value):
        self._setResource(3, value)
        return

    def getAtmosphereBonus(self):
        return self._getNumber(4)

    def setAtmosphereBonus(self, value):
        self._setNumber(4, value)
        return

    def getType(self):
        return self._getString(5)

    def setType(self, value):
        self._setString(5, value)
        return

    def getRank(self):
        return self._getNumber(6)

    def setRank(self, value):
        self._setNumber(6, value)
        return

    def getGoldPrice(self):
        return self._getNumber(7)

    def setGoldPrice(self, value):
        self._setNumber(7, value)
        return

    def getIsPremium(self):
        return self._getBool(8)

    def setIsPremium(self, value):
        self._setBool(8, value)
        return

    def getIsSelected(self):
        return self._getBool(9)

    def setIsSelected(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(NyDecorationSlotModel, self)._initialize()
        self._addNumberProperty(b'toyID', 0)
        self._addStringProperty(b'imageName', b'')
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addNumberProperty(b'atmosphereBonus', 0)
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'rank', 1)
        self._addNumberProperty(b'goldPrice', 0)
        self._addBoolProperty(b'isPremium', False)
        self._addBoolProperty(b'isSelected', False)
        return
