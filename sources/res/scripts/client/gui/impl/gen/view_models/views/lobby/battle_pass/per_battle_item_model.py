from frameworks.wulf import ViewModel

class PerBattleItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PerBattleItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)
        return

    def getWinPoint(self):
        return self._getNumber(1)

    def setWinPoint(self, value):
        self._setNumber(1, value)
        return

    def getLosePoint(self):
        return self._getNumber(2)

    def setLosePoint(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(PerBattleItemModel, self)._initialize()
        self._addStringProperty(b'label', b'')
        self._addNumberProperty(b'winPoint', 0)
        self._addNumberProperty(b'losePoint', 0)
        return
