from frameworks.wulf import Array
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import NyIndicatorType
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.pet_shop.price_range import PriceRange

class ShopCard(NyIndicatorType):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(ShopCard, self).__init__(properties=properties, commands=commands)
        return

    def getIsProgressionPrices(self):
        return self._getBool(1)

    def setIsProgressionPrices(self, value):
        self._setBool(1, value)
        return

    def getLoyaltyPoints(self):
        return self._getNumber(2)

    def setLoyaltyPoints(self, value):
        self._setNumber(2, value)
        return

    def getVitalityPoints(self):
        return self._getNumber(3)

    def setVitalityPoints(self, value):
        self._setNumber(3, value)
        return

    def getItemsInInventory(self):
        return self._getNumber(4)

    def setItemsInInventory(self, value):
        self._setNumber(4, value)
        return

    def getIsWaiting(self):
        return self._getBool(5)

    def setIsWaiting(self, value):
        self._setBool(5, value)
        return

    def getIsLocked(self):
        return self._getBool(6)

    def setIsLocked(self, value):
        self._setBool(6, value)
        return

    def getAtmosphereLevelToUnlock(self):
        return self._getNumber(7)

    def setAtmosphereLevelToUnlock(self, value):
        self._setNumber(7, value)
        return

    def getPriceRanges(self):
        return self._getArray(8)

    def setPriceRanges(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getPriceRangesType():
        return PriceRange

    def getCount(self):
        return self._getNumber(9)

    def setCount(self, value):
        self._setNumber(9, value)
        return

    def getId(self):
        return self._getNumber(10)

    def setId(self, value):
        self._setNumber(10, value)
        return

    def getCurrentPointPrice(self):
        return self._getNumber(11)

    def setCurrentPointPrice(self, value):
        self._setNumber(11, value)
        return

    def getCurrentPrice(self):
        return self._getNumber(12)

    def setCurrentPrice(self, value):
        self._setNumber(12, value)
        return

    def _initialize(self):
        super(ShopCard, self)._initialize()
        self._addBoolProperty(b'isProgressionPrices', True)
        self._addNumberProperty(b'loyaltyPoints', 0)
        self._addNumberProperty(b'vitalityPoints', 0)
        self._addNumberProperty(b'itemsInInventory', 0)
        self._addBoolProperty(b'isWaiting', False)
        self._addBoolProperty(b'isLocked', False)
        self._addNumberProperty(b'atmosphereLevelToUnlock', 0)
        self._addArrayProperty(b'priceRanges', Array())
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'currentPointPrice', 0)
        self._addNumberProperty(b'currentPrice', 0)
        return
