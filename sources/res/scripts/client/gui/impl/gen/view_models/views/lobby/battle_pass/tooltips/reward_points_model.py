from frameworks.wulf import ViewModel

class RewardPointsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardPointsModel, self).__init__(properties=properties, commands=commands)
        return

    def getTopCount(self):
        return self._getNumber(0)

    def setTopCount(self, value):
        self._setNumber(0, value)
        return

    def getPointsWin(self):
        return self._getNumber(1)

    def setPointsWin(self, value):
        self._setNumber(1, value)
        return

    def getPointsLose(self):
        return self._getNumber(2)

    def setPointsLose(self, value):
        self._setNumber(2, value)
        return

    def getExternalPointsWin(self):
        return self._getNumber(3)

    def setExternalPointsWin(self, value):
        self._setNumber(3, value)
        return

    def getExternalPointsLose(self):
        return self._getNumber(4)

    def setExternalPointsLose(self, value):
        self._setNumber(4, value)
        return

    def getIsSpecial(self):
        return self._getBool(5)

    def setIsSpecial(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(RewardPointsModel, self)._initialize()
        self._addNumberProperty(b'topCount', 0)
        self._addNumberProperty(b'pointsWin', 0)
        self._addNumberProperty(b'pointsLose', 0)
        self._addNumberProperty(b'externalPointsWin', 0)
        self._addNumberProperty(b'externalPointsLose', 0)
        self._addBoolProperty(b'isSpecial', False)
        return
