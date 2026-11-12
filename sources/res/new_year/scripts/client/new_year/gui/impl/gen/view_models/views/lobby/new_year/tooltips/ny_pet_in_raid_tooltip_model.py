from frameworks.wulf import ViewModel

class NyPetInRaidTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NyPetInRaidTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getBoostAmount(self):
        return self._getNumber(0)

    def setBoostAmount(self, value):
        self._setNumber(0, value)
        return

    def getMaxBoostLimit(self):
        return self._getNumber(1)

    def setMaxBoostLimit(self, value):
        self._setNumber(1, value)
        return

    def getRaidRemainingTime(self):
        return self._getNumber(2)

    def setRaidRemainingTime(self, value):
        self._setNumber(2, value)
        return

    def getBoostTime(self):
        return self._getNumber(3)

    def setBoostTime(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(NyPetInRaidTooltipModel, self)._initialize()
        self._addNumberProperty(b'boostAmount', 0)
        self._addNumberProperty(b'maxBoostLimit', 0)
        self._addNumberProperty(b'raidRemainingTime', 0)
        self._addNumberProperty(b'boostTime', 0)
        return
