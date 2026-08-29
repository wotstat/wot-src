from gui.impl.gen import R
from frameworks.wulf import ViewModel

class GiftModel(ViewModel):
    __slots__ = ()
    RENT_TYPE_NO = b'no_rent'
    RENT_TYPE_TIME = b'time'
    RENT_TYPE_BATTLES = b'battles'
    RENT_TYPE_WINS = b'wins'

    def __init__(self, properties=15, commands=0):
        super(GiftModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)
        return

    def getCount(self):
        return self._getNumber(4)

    def setCount(self, value):
        self._setNumber(4, value)
        return

    def getNationFlag(self):
        return self._getString(5)

    def setNationFlag(self, value):
        self._setString(5, value)
        return

    def getHighlight(self):
        return self._getString(6)

    def setHighlight(self, value):
        self._setString(6, value)
        return

    def getRentType(self):
        return self._getString(7)

    def setRentType(self, value):
        self._setString(7, value)
        return

    def getRentValue(self):
        return self._getNumber(8)

    def setRentValue(self, value):
        self._setNumber(8, value)
        return

    def getInventoryCount(self):
        return self._getNumber(9)

    def setInventoryCount(self, value):
        self._setNumber(9, value)
        return

    def getIsDisabled(self):
        return self._getBool(10)

    def setIsDisabled(self, value):
        self._setBool(10, value)
        return

    def getButtonLabel(self):
        return self._getResource(11)

    def setButtonLabel(self, value):
        self._setResource(11, value)
        return

    def getPrice(self):
        return self._getNumber(12)

    def setPrice(self, value):
        self._setNumber(12, value)
        return

    def getIsNotEnoughMoney(self):
        return self._getBool(13)

    def setIsNotEnoughMoney(self, value):
        self._setBool(13, value)
        return

    def getAvailableCount(self):
        return self._getNumber(14)

    def setAvailableCount(self, value):
        self._setNumber(14, value)
        return

    def _initialize(self):
        super(GiftModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'nationFlag', b'')
        self._addStringProperty(b'highlight', b'')
        self._addStringProperty(b'rentType', b'')
        self._addNumberProperty(b'rentValue', 0)
        self._addNumberProperty(b'inventoryCount', 0)
        self._addBoolProperty(b'isDisabled', False)
        self._addResourceProperty(b'buttonLabel', R.invalid())
        self._addNumberProperty(b'price', 0)
        self._addBoolProperty(b'isNotEnoughMoney', False)
        self._addNumberProperty(b'availableCount', 0)
        return
