from frameworks.wulf import ViewModel

class ReservesAwardViewModel(ViewModel):
    __slots__ = (b'onClose', b'onPremiumAccountExtend', b'onSubscriptionExtend')

    def __init__(self, properties=4, commands=3):
        super(ReservesAwardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCreditAmount(self):
        return self._getNumber(0)

    def setCreditAmount(self, value):
        self._setNumber(0, value)
        return

    def getGoldAmount(self):
        return self._getNumber(1)

    def setGoldAmount(self, value):
        self._setNumber(1, value)
        return

    def getShowCreditWarning(self):
        return self._getBool(2)

    def setShowCreditWarning(self, value):
        self._setBool(2, value)
        return

    def getShowGoldWarning(self):
        return self._getBool(3)

    def setShowGoldWarning(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ReservesAwardViewModel, self)._initialize()
        self._addNumberProperty(b'creditAmount', 0)
        self._addNumberProperty(b'goldAmount', 0)
        self._addBoolProperty(b'showCreditWarning', False)
        self._addBoolProperty(b'showGoldWarning', False)
        self.onClose = self._addCommand(b'onClose')
        self.onPremiumAccountExtend = self._addCommand(b'onPremiumAccountExtend')
        self.onSubscriptionExtend = self._addCommand(b'onSubscriptionExtend')
        return
