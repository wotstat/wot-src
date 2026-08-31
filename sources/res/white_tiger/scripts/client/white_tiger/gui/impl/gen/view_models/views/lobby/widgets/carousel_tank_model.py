from frameworks.wulf import ViewModel
from gui.impl.gen import R

class CarouselTankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(CarouselTankModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getIconSmall(self):
        return self._getResource(2)

    def setIconSmall(self, value):
        self._setResource(2, value)
        return

    def getId(self):
        return self._getNumber(3)

    def setId(self, value):
        self._setNumber(3, value)
        return

    def getQuantity(self):
        return self._getNumber(4)

    def setQuantity(self, value):
        self._setNumber(4, value)
        return

    def getIsHunter(self):
        return self._getBool(5)

    def setIsHunter(self, value):
        self._setBool(5, value)
        return

    def getIsSpecial(self):
        return self._getBool(6)

    def setIsSpecial(self, value):
        self._setBool(6, value)
        return

    def getSelected(self):
        return self._getBool(7)

    def setSelected(self, value):
        self._setBool(7, value)
        return

    def getInBattle(self):
        return self._getBool(8)

    def setInBattle(self, value):
        self._setBool(8, value)
        return

    def getInPlatoon(self):
        return self._getBool(9)

    def setInPlatoon(self, value):
        self._setBool(9, value)
        return

    def getUnsuitable(self):
        return self._getBool(10)

    def setUnsuitable(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(CarouselTankModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addResourceProperty(b'iconSmall', R.invalid())
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'quantity', 0)
        self._addBoolProperty(b'isHunter', False)
        self._addBoolProperty(b'isSpecial', False)
        self._addBoolProperty(b'selected', False)
        self._addBoolProperty(b'inBattle', False)
        self._addBoolProperty(b'inPlatoon', False)
        self._addBoolProperty(b'unsuitable', False)
        return
