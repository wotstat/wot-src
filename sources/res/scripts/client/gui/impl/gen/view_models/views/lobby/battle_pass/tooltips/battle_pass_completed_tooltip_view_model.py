from frameworks.wulf import ViewModel

class BattlePassCompletedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BattlePassCompletedTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsBattlePassPurchased(self):
        return self._getBool(0)

    def setIsBattlePassPurchased(self, value):
        self._setBool(0, value)
        return

    def getNotChosenRewardCount(self):
        return self._getNumber(1)

    def setNotChosenRewardCount(self, value):
        self._setNumber(1, value)
        return

    def getIsBpPointsShopEntryPointActive(self):
        return self._getBool(2)

    def setIsBpPointsShopEntryPointActive(self, value):
        self._setBool(2, value)
        return

    def getIsSingleChapter(self):
        return self._getBool(3)

    def setIsSingleChapter(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(BattlePassCompletedTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isBattlePassPurchased', False)
        self._addNumberProperty(b'notChosenRewardCount', 0)
        self._addBoolProperty(b'isBpPointsShopEntryPointActive', False)
        self._addBoolProperty(b'isSingleChapter', False)
        return
