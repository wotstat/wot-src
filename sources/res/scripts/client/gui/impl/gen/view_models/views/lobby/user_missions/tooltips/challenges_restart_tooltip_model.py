from frameworks.wulf import ViewModel

class ChallengesRestartTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ChallengesRestartTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getRestartCost(self):
        return self._getNumber(0)

    def setRestartCost(self, value):
        self._setNumber(0, value)
        return

    def getCurrency(self):
        return self._getString(1)

    def setCurrency(self, value):
        self._setString(1, value)
        return

    def getFreeRestarts(self):
        return self._getNumber(2)

    def setFreeRestarts(self, value):
        self._setNumber(2, value)
        return

    def getUsedFreeRestarts(self):
        return self._getNumber(3)

    def setUsedFreeRestarts(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(ChallengesRestartTooltipModel, self)._initialize()
        self._addNumberProperty(b'restartCost', 0)
        self._addStringProperty(b'currency', b'')
        self._addNumberProperty(b'freeRestarts', 0)
        self._addNumberProperty(b'usedFreeRestarts', 0)
        return
