from frameworks.wulf import ViewModel

class QuickTrainingDiscountTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QuickTrainingDiscountTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getOldFreeXpBaseValue(self):
        return self._getNumber(0)

    def setOldFreeXpBaseValue(self, value):
        self._setNumber(0, value)
        return

    def getNewFreeXpBaseValue(self):
        return self._getNumber(1)

    def setNewFreeXpBaseValue(self, value):
        self._setNumber(1, value)
        return

    def getOldXpExchangeValue(self):
        return self._getNumber(2)

    def setOldXpExchangeValue(self, value):
        self._setNumber(2, value)
        return

    def getNewXpExchangeValue(self):
        return self._getNumber(3)

    def setNewXpExchangeValue(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(QuickTrainingDiscountTooltipModel, self)._initialize()
        self._addNumberProperty(b'oldFreeXpBaseValue', 1)
        self._addNumberProperty(b'newFreeXpBaseValue', 1)
        self._addNumberProperty(b'oldXpExchangeValue', 1)
        self._addNumberProperty(b'newXpExchangeValue', 1)
        return
