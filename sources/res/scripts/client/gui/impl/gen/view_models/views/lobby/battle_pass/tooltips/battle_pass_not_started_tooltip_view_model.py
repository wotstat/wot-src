from frameworks.wulf import ViewModel

class BattlePassNotStartedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattlePassNotStartedTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDate(self):
        return self._getString(0)

    def setDate(self, value):
        self._setString(0, value)
        return

    def getSeasonNum(self):
        return self._getNumber(1)

    def setSeasonNum(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(BattlePassNotStartedTooltipViewModel, self)._initialize()
        self._addStringProperty(b'date', b'')
        self._addNumberProperty(b'seasonNum', 0)
        return
