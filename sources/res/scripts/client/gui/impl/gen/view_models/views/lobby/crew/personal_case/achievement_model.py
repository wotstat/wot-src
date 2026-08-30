from frameworks.wulf import ViewModel

class AchievementModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(AchievementModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)
        return

    def getBlock(self):
        return self._getString(2)

    def setBlock(self, value):
        self._setString(2, value)
        return

    def getIsRare(self):
        return self._getBool(3)

    def setIsRare(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(AchievementModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'amount', 0)
        self._addStringProperty(b'block', b'')
        self._addBoolProperty(b'isRare', False)
        return
