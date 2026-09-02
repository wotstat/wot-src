from frameworks.wulf import ViewModel

class BoxRerollModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BoxRerollModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAvailable(self):
        return self._getBool(0)

    def setIsAvailable(self, value):
        self._setBool(0, value)
        return

    def getIsEnoughMoney(self):
        return self._getBool(1)

    def setIsEnoughMoney(self, value):
        self._setBool(1, value)
        return

    def getCurrency(self):
        return self._getString(2)

    def setCurrency(self, value):
        self._setString(2, value)
        return

    def getPrice(self):
        return self._getNumber(3)

    def setPrice(self, value):
        self._setNumber(3, value)
        return

    def getAttemptsLeft(self):
        return self._getNumber(4)

    def setAttemptsLeft(self, value):
        self._setNumber(4, value)
        return

    def getHasSpecialReward(self):
        return self._getBool(5)

    def setHasSpecialReward(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(BoxRerollModel, self)._initialize()
        self._addBoolProperty(b'isAvailable', False)
        self._addBoolProperty(b'isEnoughMoney', False)
        self._addStringProperty(b'currency', b'')
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'attemptsLeft', 0)
        self._addBoolProperty(b'hasSpecialReward', False)
        return
