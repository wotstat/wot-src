from frameworks.wulf import ViewModel

class WtCarouselTankModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(WtCarouselTankModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getId(self):
        return self._getNumber(2)

    def setId(self, value):
        self._setNumber(2, value)
        return

    def getQuantity(self):
        return self._getNumber(3)

    def setQuantity(self, value):
        self._setNumber(3, value)
        return

    def getSelected(self):
        return self._getBool(4)

    def setSelected(self, value):
        self._setBool(4, value)
        return

    def getInBattle(self):
        return self._getBool(5)

    def setInBattle(self, value):
        self._setBool(5, value)
        return

    def getInPlatoon(self):
        return self._getBool(6)

    def setInPlatoon(self, value):
        self._setBool(6, value)
        return

    def getUnsuitable(self):
        return self._getBool(7)

    def setUnsuitable(self, value):
        self._setBool(7, value)
        return

    def getWtVehicleType(self):
        return self._getString(8)

    def setWtVehicleType(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(WtCarouselTankModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'quantity', 0)
        self._addBoolProperty(b'selected', False)
        self._addBoolProperty(b'inBattle', False)
        self._addBoolProperty(b'inPlatoon', False)
        self._addBoolProperty(b'unsuitable', False)
        self._addStringProperty(b'wtVehicleType', b'boss')
        return
