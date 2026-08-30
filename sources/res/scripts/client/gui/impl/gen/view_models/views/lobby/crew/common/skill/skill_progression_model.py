from frameworks.wulf import ViewModel

class SkillProgressionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(SkillProgressionModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentXpValue(self):
        return self._getNumber(0)

    def setCurrentXpValue(self, value):
        self._setNumber(0, value)
        return

    def getTotalXpValue(self):
        return self._getNumber(1)

    def setTotalXpValue(self, value):
        self._setNumber(1, value)
        return

    def getSkillProgress(self):
        return self._getNumber(2)

    def setSkillProgress(self, value):
        self._setNumber(2, value)
        return

    def getDiscountValue(self):
        return self._getNumber(3)

    def setDiscountValue(self, value):
        self._setNumber(3, value)
        return

    def getZeroSkillsCount(self):
        return self._getNumber(4)

    def setZeroSkillsCount(self, value):
        self._setNumber(4, value)
        return

    def getIsLocked(self):
        return self._getBool(5)

    def setIsLocked(self, value):
        self._setBool(5, value)
        return

    def getIsMaxSkillLevel(self):
        return self._getBool(6)

    def setIsMaxSkillLevel(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(SkillProgressionModel, self)._initialize()
        self._addNumberProperty(b'currentXpValue', 0)
        self._addNumberProperty(b'totalXpValue', 0)
        self._addNumberProperty(b'skillProgress', 0)
        self._addNumberProperty(b'discountValue', 0)
        self._addNumberProperty(b'zeroSkillsCount', 0)
        self._addBoolProperty(b'isLocked', False)
        self._addBoolProperty(b'isMaxSkillLevel', False)
        return
