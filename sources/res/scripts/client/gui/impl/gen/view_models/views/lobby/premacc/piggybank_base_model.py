from frameworks.wulf import ViewModel

class PiggybankBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(PiggybankBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getMaxAmount(self):
        return self._getNumber(0)

    def setMaxAmount(self, value):
        self._setNumber(0, value)
        return

    def getMaxAmountStr(self):
        return self._getString(1)

    def setMaxAmountStr(self, value):
        self._setString(1, value)
        return

    def getCurrentAmount(self):
        return self._getNumber(2)

    def setCurrentAmount(self, value):
        self._setNumber(2, value)
        return

    def getCurrentAmountStr(self):
        return self._getString(3)

    def setCurrentAmountStr(self, value):
        self._setString(3, value)
        return

    def getIsTankPremiumActive(self):
        return self._getBool(4)

    def setIsTankPremiumActive(self, value):
        self._setBool(4, value)
        return

    def getTimeleft(self):
        return self._getNumber(5)

    def setTimeleft(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(PiggybankBaseModel, self)._initialize()
        self._addNumberProperty(b'maxAmount', 1)
        self._addStringProperty(b'maxAmountStr', b'0')
        self._addNumberProperty(b'currentAmount', 0)
        self._addStringProperty(b'currentAmountStr', b'0')
        self._addBoolProperty(b'isTankPremiumActive', False)
        self._addNumberProperty(b'timeleft', 0)
        return
