from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class WeeklyQuestProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(WeeklyQuestProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIsCompleted(self):
        return self._getBool(1)

    def setIsCompleted(self, value):
        self._setBool(1, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)
        return

    def getTotalProgress(self):
        return self._getNumber(3)

    def setTotalProgress(self, value):
        self._setNumber(3, value)
        return

    def getEarned(self):
        return self._getNumber(4)

    def setEarned(self, value):
        self._setNumber(4, value)
        return

    def getNavigationEnabled(self):
        return self._getBool(5)

    def setNavigationEnabled(self, value):
        self._setBool(5, value)
        return

    def getCommonConditionId(self):
        return self._getNumber(6)

    def setCommonConditionId(self, value):
        self._setNumber(6, value)
        return

    def getBonuses(self):
        return self._getArray(7)

    def setBonuses(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(WeeklyQuestProgressModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'earned', 0)
        self._addBoolProperty(b'navigationEnabled', False)
        self._addNumberProperty(b'commonConditionId', 0)
        self._addArrayProperty(b'bonuses', Array())
        return
