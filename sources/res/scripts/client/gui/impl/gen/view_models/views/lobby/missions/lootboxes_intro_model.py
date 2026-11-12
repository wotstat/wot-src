from frameworks.wulf import ViewModel

class LootboxesIntroModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LootboxesIntroModel, self).__init__(properties=properties, commands=commands)
        return

    def getBoxCount(self):
        return self._getNumber(0)

    def setBoxCount(self, value):
        self._setNumber(0, value)
        return

    def getBonusQuestBoxCount(self):
        return self._getNumber(1)

    def setBonusQuestBoxCount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(LootboxesIntroModel, self)._initialize()
        self._addNumberProperty(b'boxCount', 0)
        self._addNumberProperty(b'bonusQuestBoxCount', 0)
        return
