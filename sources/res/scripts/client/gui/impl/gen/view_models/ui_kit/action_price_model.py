from frameworks.wulf import ViewModel

class ActionPriceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(ActionPriceModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getIsEnough(self):
        return self._getBool(1)

    def setIsEnough(self, value):
        self._setBool(1, value)
        return

    def getIsWithAction(self):
        return self._getBool(2)

    def setIsWithAction(self, value):
        self._setBool(2, value)
        return

    def getAction(self):
        return self._getNumber(3)

    def setAction(self, value):
        self._setNumber(3, value)
        return

    def getDefPrice(self):
        return self._getString(4)

    def setDefPrice(self, value):
        self._setString(4, value)
        return

    def getPrice(self):
        return self._getString(5)

    def setPrice(self, value):
        self._setString(5, value)
        return

    def getIsFree(self):
        return self._getBool(6)

    def setIsFree(self, value):
        self._setBool(6, value)
        return

    def getFontNotEnoughIsEnabled(self):
        return self._getBool(7)

    def setFontNotEnoughIsEnabled(self, value):
        self._setBool(7, value)
        return

    def getTooltipType(self):
        return self._getString(8)

    def setTooltipType(self, value):
        self._setString(8, value)
        return

    def getKey(self):
        return self._getString(9)

    def setKey(self, value):
        self._setString(9, value)
        return

    def getNewCredits(self):
        return self._getNumber(10)

    def setNewCredits(self, value):
        self._setNumber(10, value)
        return

    def getNewGold(self):
        return self._getNumber(11)

    def setNewGold(self, value):
        self._setNumber(11, value)
        return

    def getNewCrystal(self):
        return self._getNumber(12)

    def setNewCrystal(self, value):
        self._setNumber(12, value)
        return

    def getOldCredits(self):
        return self._getNumber(13)

    def setOldCredits(self, value):
        self._setNumber(13, value)
        return

    def getOldGold(self):
        return self._getNumber(14)

    def setOldGold(self, value):
        self._setNumber(14, value)
        return

    def getOldCrystal(self):
        return self._getNumber(15)

    def setOldCrystal(self, value):
        self._setNumber(15, value)
        return

    def getIsBuying(self):
        return self._getBool(16)

    def setIsBuying(self, value):
        self._setBool(16, value)
        return

    def getShowOldValue(self):
        return self._getBool(17)

    def setShowOldValue(self, value):
        self._setBool(17, value)
        return

    def _initialize(self):
        super(ActionPriceModel, self)._initialize()
        self._addStringProperty(b'type', b'gold')
        self._addBoolProperty(b'isEnough', False)
        self._addBoolProperty(b'isWithAction', False)
        self._addNumberProperty(b'action', 0)
        self._addStringProperty(b'defPrice', b'')
        self._addStringProperty(b'price', b'')
        self._addBoolProperty(b'isFree', False)
        self._addBoolProperty(b'fontNotEnoughIsEnabled', True)
        self._addStringProperty(b'tooltipType', b'economics')
        self._addStringProperty(b'key', b'')
        self._addNumberProperty(b'newCredits', 0)
        self._addNumberProperty(b'newGold', 0)
        self._addNumberProperty(b'newCrystal', 0)
        self._addNumberProperty(b'oldCredits', 0)
        self._addNumberProperty(b'oldGold', 0)
        self._addNumberProperty(b'oldCrystal', 0)
        self._addBoolProperty(b'isBuying', True)
        self._addBoolProperty(b'showOldValue', False)
        return
