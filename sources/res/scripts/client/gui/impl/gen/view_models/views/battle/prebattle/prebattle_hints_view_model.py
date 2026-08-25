from frameworks.wulf import ViewModel

class PrebattleHintsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PrebattleHintsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHintType(self):
        return self._getString(0)

    def setHintType(self, value):
        self._setString(0, value)
        return

    def getCanSkip(self):
        return self._getBool(1)

    def setCanSkip(self, value):
        self._setBool(1, value)
        return

    def getIsColorBlind(self):
        return self._getBool(2)

    def setIsColorBlind(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PrebattleHintsViewModel, self)._initialize()
        self._addStringProperty(b'hintType', b'')
        self._addBoolProperty(b'canSkip', False)
        self._addBoolProperty(b'isColorBlind', False)
        return
