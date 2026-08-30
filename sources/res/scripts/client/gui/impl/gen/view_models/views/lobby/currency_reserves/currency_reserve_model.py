from enum import Enum
from frameworks.wulf import ViewModel

class CurrencyEnum(Enum):
    CREDITS = b'Credits'
    GOLD = b'Gold'


class CurrencyReserveModel(ViewModel):
    __slots__ = (b'onInfoButtonClick', b'onActionButtonClick')

    def __init__(self, properties=5, commands=2):
        super(CurrencyReserveModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrency(self):
        return CurrencyEnum(self._getString(0))

    def setCurrency(self, value):
        self._setString(0, value.value)
        return

    def getMaxCapacity(self):
        return self._getNumber(1)

    def setMaxCapacity(self, value):
        self._setNumber(1, value)
        return

    def getAmount(self):
        return self._getNumber(2)

    def setAmount(self, value):
        self._setNumber(2, value)
        return

    def getIsActive(self):
        return self._getBool(3)

    def setIsActive(self, value):
        self._setBool(3, value)
        return

    def getIsEnabled(self):
        return self._getBool(4)

    def setIsEnabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(CurrencyReserveModel, self)._initialize()
        self._addStringProperty(b'currency')
        self._addNumberProperty(b'maxCapacity', 0)
        self._addNumberProperty(b'amount', 0)
        self._addBoolProperty(b'isActive', False)
        self._addBoolProperty(b'isEnabled', True)
        self.onInfoButtonClick = self._addCommand(b'onInfoButtonClick')
        self.onActionButtonClick = self._addCommand(b'onActionButtonClick')
        return
