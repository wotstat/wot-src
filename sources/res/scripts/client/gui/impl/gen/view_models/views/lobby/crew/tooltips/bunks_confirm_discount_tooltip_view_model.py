from frameworks.wulf import ViewModel

class BunksConfirmDiscountTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BunksConfirmDiscountTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBunksCount(self):
        return self._getNumber(0)

    def setBunksCount(self, value):
        self._setNumber(0, value)
        return

    def getOldCost(self):
        return self._getNumber(1)

    def setOldCost(self, value):
        self._setNumber(1, value)
        return

    def getNewCost(self):
        return self._getNumber(2)

    def setNewCost(self, value):
        self._setNumber(2, value)
        return

    def getIsEnough(self):
        return self._getBool(3)

    def setIsEnough(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(BunksConfirmDiscountTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'bunksCount', 1)
        self._addNumberProperty(b'oldCost', 1)
        self._addNumberProperty(b'newCost', 1)
        self._addBoolProperty(b'isEnough', False)
        return
