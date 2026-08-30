from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.early_access.early_access_vehicle_model import EarlyAccessVehicleModel

class BuyResult(IntEnum):
    NONE = 0
    SUCCESS = 1
    FAIL = 2


class EarlyAccessBuyViewModel(ViewModel):
    __slots__ = (b'onAboutEvent', b'onBuyTokens', b'onBackToPrevScreen')
    ARG_BUY_TOKENS_AMOUNT = b'tokens'

    def __init__(self, properties=11, commands=3):
        super(EarlyAccessBuyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getBuyResult(self):
        return BuyResult(self._getNumber(1))

    def setBuyResult(self, value):
        self._setNumber(1, value.value)
        return

    def getFromTimestamp(self):
        return self._getNumber(2)

    def setFromTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getToTimestamp(self):
        return self._getNumber(3)

    def setToTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getTotalTokensCount(self):
        return self._getNumber(4)

    def setTotalTokensCount(self, value):
        self._setNumber(4, value)
        return

    def getRecievedTokensCount(self):
        return self._getNumber(5)

    def setRecievedTokensCount(self, value):
        self._setNumber(5, value)
        return

    def getInitialTokensCount(self):
        return self._getNumber(6)

    def setInitialTokensCount(self, value):
        self._setNumber(6, value)
        return

    def getCurrentTokensBalance(self):
        return self._getNumber(7)

    def setCurrentTokensBalance(self, value):
        self._setNumber(7, value)
        return

    def getTokenPriceInGold(self):
        return self._getNumber(8)

    def setTokenPriceInGold(self, value):
        self._setNumber(8, value)
        return

    def getGoldBalance(self):
        return self._getNumber(9)

    def setGoldBalance(self, value):
        self._setNumber(9, value)
        return

    def getVehicles(self):
        return self._getArray(10)

    def setVehicles(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getVehiclesType():
        return EarlyAccessVehicleModel

    def _initialize(self):
        super(EarlyAccessBuyViewModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addNumberProperty(b'buyResult', BuyResult.NONE.value)
        self._addNumberProperty(b'fromTimestamp', 0)
        self._addNumberProperty(b'toTimestamp', 0)
        self._addNumberProperty(b'totalTokensCount', 0)
        self._addNumberProperty(b'recievedTokensCount', 0)
        self._addNumberProperty(b'initialTokensCount', 0)
        self._addNumberProperty(b'currentTokensBalance', 0)
        self._addNumberProperty(b'tokenPriceInGold', 0)
        self._addNumberProperty(b'goldBalance', 0)
        self._addArrayProperty(b'vehicles', Array())
        self.onAboutEvent = self._addCommand(b'onAboutEvent')
        self.onBuyTokens = self._addCommand(b'onBuyTokens')
        self.onBackToPrevScreen = self._addCommand(b'onBackToPrevScreen')
        return
