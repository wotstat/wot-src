from frameworks.wulf import ViewModel

class BattlePassNoChapterTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattlePassNoChapterTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getPoints(self):
        return self._getNumber(0)

    def setPoints(self, value):
        self._setNumber(0, value)
        return

    def getChapterName(self):
        return self._getString(1)

    def setChapterName(self, value):
        self._setString(1, value)
        return

    def getIsResourceActive(self):
        return self._getBool(2)

    def setIsResourceActive(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BattlePassNoChapterTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'points', 0)
        self._addStringProperty(b'chapterName', b'')
        self._addBoolProperty(b'isResourceActive', False)
        return
