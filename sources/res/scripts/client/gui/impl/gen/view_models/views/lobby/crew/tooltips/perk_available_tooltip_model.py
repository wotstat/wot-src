from frameworks.wulf import ViewModel

class PerkAvailableTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PerkAvailableTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getPerkCount(self):
        return self._getNumber(0)

    def setPerkCount(self, value):
        self._setNumber(0, value)
        return

    def getZeroPerkCount(self):
        return self._getNumber(1)

    def setZeroPerkCount(self, value):
        self._setNumber(1, value)
        return

    def getLastPerkLevel(self):
        return self._getNumber(2)

    def setLastPerkLevel(self, value):
        self._setNumber(2, value)
        return

    def getIsAllSlotsTrained(self):
        return self._getBool(3)

    def setIsAllSlotsTrained(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(PerkAvailableTooltipModel, self)._initialize()
        self._addNumberProperty(b'perkCount', 0)
        self._addNumberProperty(b'zeroPerkCount', 0)
        self._addNumberProperty(b'lastPerkLevel', 0)
        self._addBoolProperty(b'isAllSlotsTrained', False)
        return
