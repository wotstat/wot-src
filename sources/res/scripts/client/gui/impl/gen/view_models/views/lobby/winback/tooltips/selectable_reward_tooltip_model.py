from frameworks.wulf import ViewModel

class SelectableRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SelectableRewardTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getPurchaseDiscount(self):
        return self._getNumber(1)

    def setPurchaseDiscount(self, value):
        self._setNumber(1, value)
        return

    def getResearchDiscount(self):
        return self._getNumber(2)

    def setResearchDiscount(self, value):
        self._setNumber(2, value)
        return

    def getIsDiscount(self):
        return self._getBool(3)

    def setIsDiscount(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SelectableRewardTooltipModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'purchaseDiscount', 0)
        self._addNumberProperty(b'researchDiscount', 0)
        self._addBoolProperty(b'isDiscount', False)
        return
