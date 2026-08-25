from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__ = (b'confirm', b'cancel')

    def __init__(self, properties=7, commands=2):
        super(ConfirmationModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getChallengeID(self):
        return self._getNumber(1)

    def setChallengeID(self, value):
        self._setNumber(1, value)
        return

    def getChallengeName(self):
        return self._getString(2)

    def setChallengeName(self, value):
        self._setString(2, value)
        return

    def getConfirmationType(self):
        return self._getString(3)

    def setConfirmationType(self, value):
        self._setString(3, value)
        return

    def getIsFreeRestart(self):
        return self._getBool(4)

    def setIsFreeRestart(self, value):
        self._setBool(4, value)
        return

    def getBalance(self):
        return self._getArray(5)

    def setBalance(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getBalanceType():
        return PriceItemModel

    def getIsWalletAvailable(self):
        return self._getBool(6)

    def setIsWalletAvailable(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(ConfirmationModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceItemModel())
        self._addNumberProperty(b'challengeID', 0)
        self._addStringProperty(b'challengeName', b'')
        self._addStringProperty(b'confirmationType', b'')
        self._addBoolProperty(b'isFreeRestart', False)
        self._addArrayProperty(b'balance', Array())
        self._addBoolProperty(b'isWalletAvailable', True)
        self.confirm = self._addCommand(b'confirm')
        self.cancel = self._addCommand(b'cancel')
        return
