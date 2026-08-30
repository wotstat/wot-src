from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class WeeklyMissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(WeeklyMissionModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getCommonConditionId(self):
        return self._getNumber(1)

    def setCommonConditionId(self, value):
        self._setNumber(1, value)
        return

    def getSpecialConditionIds(self):
        return self._getArray(2)

    def setSpecialConditionIds(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSpecialConditionIdsType():
        return int

    def getCurrentProgress(self):
        return self._getNumber(3)

    def setCurrentProgress(self, value):
        self._setNumber(3, value)
        return

    def getTotalProgress(self):
        return self._getNumber(4)

    def setTotalProgress(self, value):
        self._setNumber(4, value)
        return

    def getPreviousProgress(self):
        return self._getNumber(5)

    def setPreviousProgress(self, value):
        self._setNumber(5, value)
        return

    def getIsRerollInProgress(self):
        return self._getBool(6)

    def setIsRerollInProgress(self, value):
        self._setBool(6, value)
        return

    def getTimeToNextReroll(self):
        return self._getNumber(7)

    def setTimeToNextReroll(self, value):
        self._setNumber(7, value)
        return

    def getRerollCooldown(self):
        return self._getNumber(8)

    def setRerollCooldown(self, value):
        self._setNumber(8, value)
        return

    def getBonuses(self):
        return self._getArray(9)

    def setBonuses(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(WeeklyMissionModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'commonConditionId', 0)
        self._addArrayProperty(b'specialConditionIds', Array())
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'previousProgress', 0)
        self._addBoolProperty(b'isRerollInProgress', False)
        self._addNumberProperty(b'timeToNextReroll', 0)
        self._addNumberProperty(b'rerollCooldown', 0)
        self._addArrayProperty(b'bonuses', Array())
        return
