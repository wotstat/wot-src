from frameworks.wulf import ViewModel

class CommonViewModel(ViewModel):
    __slots__ = (b'onClosed',)

    def __init__(self, properties=4, commands=1):
        super(CommonViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(1)

    def setCurrentLevel(self, value):
        self._setNumber(1, value)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(2)

    def setIsBattlePassPurchased(self, value):
        self._setBool(2, value)
        return

    def getCanBuy(self):
        return self._getBool(3)

    def setCanBuy(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(CommonViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addNumberProperty(b'currentLevel', 0)
        self._addBoolProperty(b'isBattlePassPurchased', False)
        self._addBoolProperty(b'canBuy', False)
        self.onClosed = self._addCommand(b'onClosed')
        return
