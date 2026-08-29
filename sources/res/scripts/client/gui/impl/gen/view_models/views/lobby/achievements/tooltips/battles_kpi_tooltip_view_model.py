from frameworks.wulf import ViewModel

class BattlesKpiTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(BattlesKpiTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCountOfBattles(self):
        return self._getString(0)

    def setCountOfBattles(self, value):
        self._setString(0, value)
        return

    def getWins(self):
        return self._getString(1)

    def setWins(self, value):
        self._setString(1, value)
        return

    def getDefeat(self):
        return self._getString(2)

    def setDefeat(self, value):
        self._setString(2, value)
        return

    def getDraws(self):
        return self._getString(3)

    def setDraws(self, value):
        self._setString(3, value)
        return

    def getWinsPercent(self):
        return self._getString(4)

    def setWinsPercent(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(BattlesKpiTooltipViewModel, self)._initialize()
        self._addStringProperty(b'countOfBattles', b'')
        self._addStringProperty(b'wins', b'')
        self._addStringProperty(b'defeat', b'')
        self._addStringProperty(b'draws', b'')
        self._addStringProperty(b'winsPercent', b'')
        return
