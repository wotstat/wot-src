from frameworks.wulf import ViewModel

class SquadBonusItemRendererModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SquadBonusItemRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getString(0)

    def setLevel(self, value):
        self._setString(0, value)
        return

    def getDefeatValue(self):
        return self._getNumber(1)

    def setDefeatValue(self, value):
        self._setNumber(1, value)
        return

    def getWinValue(self):
        return self._getNumber(2)

    def setWinValue(self, value):
        self._setNumber(2, value)
        return

    def getIsCurrentLevel(self):
        return self._getBool(3)

    def setIsCurrentLevel(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SquadBonusItemRendererModel, self)._initialize()
        self._addStringProperty(b'level', b'')
        self._addNumberProperty(b'defeatValue', 0)
        self._addNumberProperty(b'winValue', 0)
        self._addBoolProperty(b'isCurrentLevel', False)
        return
