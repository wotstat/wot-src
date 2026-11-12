from frameworks.wulf import ViewModel

class NyPetRaidBoostTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NyPetRaidBoostTooltipModel, self).__init__(properties=properties, commands=commands)
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

    def getBoostTime(self):
        return self._getNumber(2)

    def setBoostTime(self, value):
        self._setNumber(2, value)
        return

    def getBoostsToAdd(self):
        return self._getNumber(3)

    def setBoostsToAdd(self, value):
        self._setNumber(3, value)
        return

    def getBoostAccrualTime(self):
        return self._getNumber(4)

    def setBoostAccrualTime(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(NyPetRaidBoostTooltipModel, self)._initialize()
        self._addNumberProperty(b'boostAmount', 0)
        self._addNumberProperty(b'maxBoostLimit', 0)
        self._addNumberProperty(b'boostTime', 0)
        self._addNumberProperty(b'boostsToAdd', 0)
        self._addNumberProperty(b'boostAccrualTime', 0)
        return
