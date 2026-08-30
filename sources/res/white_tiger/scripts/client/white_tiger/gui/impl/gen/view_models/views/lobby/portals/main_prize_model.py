from frameworks.wulf import ViewModel

class MainPrizeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MainPrizeModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankName(self):
        return self._getString(0)

    def setTankName(self, value):
        self._setString(0, value)
        return

    def getTankLevel(self):
        return self._getNumber(1)

    def setTankLevel(self, value):
        self._setNumber(1, value)
        return

    def getTankNation(self):
        return self._getString(2)

    def setTankNation(self, value):
        self._setString(2, value)
        return

    def getTankType(self):
        return self._getString(3)

    def setTankType(self, value):
        self._setString(3, value)
        return

    def getTankRoleName(self):
        return self._getString(4)

    def setTankRoleName(self, value):
        self._setString(4, value)
        return

    def getDiscountPerToken(self):
        return self._getNumber(5)

    def setDiscountPerToken(self, value):
        self._setNumber(5, value)
        return

    def getDiscountTokenCount(self):
        return self._getNumber(6)

    def setDiscountTokenCount(self, value):
        self._setNumber(6, value)
        return

    def getMaxDiscountTokenCount(self):
        return self._getNumber(7)

    def setMaxDiscountTokenCount(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(MainPrizeModel, self)._initialize()
        self._addStringProperty(b'tankName', b'')
        self._addNumberProperty(b'tankLevel', 0)
        self._addStringProperty(b'tankNation', b'')
        self._addStringProperty(b'tankType', b'')
        self._addStringProperty(b'tankRoleName', b'')
        self._addNumberProperty(b'discountPerToken', 0)
        self._addNumberProperty(b'discountTokenCount', 0)
        self._addNumberProperty(b'maxDiscountTokenCount', 0)
        return
