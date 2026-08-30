from frameworks.wulf import ViewModel

class CartRentModel(ViewModel):
    __slots__ = (b'onSelectAutoRent',)

    def __init__(self, properties=4, commands=1):
        super(CartRentModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsRentable(self):
        return self._getBool(0)

    def setIsRentable(self, value):
        self._setBool(0, value)
        return

    def getRentCount(self):
        return self._getNumber(1)

    def setRentCount(self, value):
        self._setNumber(1, value)
        return

    def getHasAutoRent(self):
        return self._getBool(2)

    def setHasAutoRent(self, value):
        self._setBool(2, value)
        return

    def getIsAutoRentSelected(self):
        return self._getBool(3)

    def setIsAutoRentSelected(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(CartRentModel, self)._initialize()
        self._addBoolProperty(b'isRentable', False)
        self._addNumberProperty(b'rentCount', 0)
        self._addBoolProperty(b'hasAutoRent', False)
        self._addBoolProperty(b'isAutoRentSelected', False)
        self.onSelectAutoRent = self._addCommand(b'onSelectAutoRent')
        return
