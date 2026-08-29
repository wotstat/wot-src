from enum import Enum
from frameworks.wulf import ViewModel

class ArmoryYardCurrencies(Enum):
    ARMORYCOIN = b'armory_coin'
    PROGRESSIONTOKEN = b'progression_token'


class ArmoryYardCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ArmoryYardCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getReceivedTokens(self):
        return self._getNumber(0)

    def setReceivedTokens(self, value):
        self._setNumber(0, value)
        return

    def getTotalTokens(self):
        return self._getNumber(1)

    def setTotalTokens(self, value):
        self._setNumber(1, value)
        return

    def getQuestsForToken(self):
        return self._getNumber(2)

    def setQuestsForToken(self, value):
        self._setNumber(2, value)
        return

    def getStartTimestamp(self):
        return self._getNumber(3)

    def setStartTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(4)

    def setEndTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getCurrency(self):
        return ArmoryYardCurrencies(self._getString(5))

    def setCurrency(self, value):
        self._setString(5, value.value)
        return

    def _initialize(self):
        super(ArmoryYardCurrencyTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'receivedTokens', 0)
        self._addNumberProperty(b'totalTokens', 0)
        self._addNumberProperty(b'questsForToken', 0)
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addStringProperty(b'currency', ArmoryYardCurrencies.PROGRESSIONTOKEN.value)
        return
