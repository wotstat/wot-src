from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class RankedYearAwardModel(ViewModel):
    __slots__ = (b'onActionBtnClick', b'onDestroyEvent')

    def __init__(self, properties=9, commands=2):
        super(RankedYearAwardModel, self).__init__(properties=properties, commands=commands)
        return

    def getAwardType(self):
        return self._getString(0)

    def setAwardType(self, value):
        self._setString(0, value)
        return

    def getStartClose(self):
        return self._getBool(1)

    def setStartClose(self, value):
        self._setBool(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    def getActionButtonLabel(self):
        return self._getResource(3)

    def setActionButtonLabel(self, value):
        self._setResource(3, value)
        return

    def getPointsTotal(self):
        return self._getNumber(4)

    def setPointsTotal(self, value):
        self._setNumber(4, value)
        return

    def getPointsCompensated(self):
        return self._getNumber(5)

    def setPointsCompensated(self, value):
        self._setNumber(5, value)
        return

    def getCrystals(self):
        return self._getNumber(6)

    def setCrystals(self, value):
        self._setNumber(6, value)
        return

    def getIsRewardSelected(self):
        return self._getBool(7)

    def setIsRewardSelected(self, value):
        self._setBool(7, value)
        return

    def getRewardsToSelect(self):
        return self._getNumber(8)

    def setRewardsToSelect(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(RankedYearAwardModel, self)._initialize()
        self._addStringProperty(b'awardType', b'')
        self._addBoolProperty(b'startClose', False)
        self._addArrayProperty(b'rewards', Array())
        self._addResourceProperty(b'actionButtonLabel', R.invalid())
        self._addNumberProperty(b'pointsTotal', 0)
        self._addNumberProperty(b'pointsCompensated', 0)
        self._addNumberProperty(b'crystals', 0)
        self._addBoolProperty(b'isRewardSelected', False)
        self._addNumberProperty(b'rewardsToSelect', 0)
        self.onActionBtnClick = self._addCommand(b'onActionBtnClick')
        self.onDestroyEvent = self._addCommand(b'onDestroyEvent')
        return
