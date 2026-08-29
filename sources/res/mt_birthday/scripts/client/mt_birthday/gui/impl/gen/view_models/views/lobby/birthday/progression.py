from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.token_bonus_model import TokenBonusModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.progression_level import ProgressionLevel

class Progression(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(Progression, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentLevel(self):
        return self._getNumber(0)

    def setCurrentLevel(self, value):
        self._setNumber(0, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(1)

    def setCurrentPoints(self, value):
        self._setNumber(1, value)
        return

    def getPointsDeltaFrom(self):
        return self._getNumber(2)

    def setPointsDeltaFrom(self, value):
        self._setNumber(2, value)
        return

    def getInfinityLevelCompleteCount(self):
        return self._getNumber(3)

    def setInfinityLevelCompleteCount(self, value):
        self._setNumber(3, value)
        return

    def getInfinityStartPoints(self):
        return self._getNumber(4)

    def setInfinityStartPoints(self, value):
        self._setNumber(4, value)
        return

    def getInfinityMaxPoints(self):
        return self._getNumber(5)

    def setInfinityMaxPoints(self, value):
        self._setNumber(5, value)
        return

    def getInfinitySubstagesCount(self):
        return self._getNumber(6)

    def setInfinitySubstagesCount(self, value):
        self._setNumber(6, value)
        return

    def getInfinityDeltaFrom(self):
        return self._getNumber(7)

    def setInfinityDeltaFrom(self, value):
        self._setNumber(7, value)
        return

    def getLevels(self):
        return self._getArray(8)

    def setLevels(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getLevelsType():
        return ProgressionLevel

    def getInfinityRewards(self):
        return self._getArray(9)

    def setInfinityRewards(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getInfinityRewardsType():
        return TokenBonusModel

    def _initialize(self):
        super(Progression, self)._initialize()
        self._addNumberProperty(b'currentLevel', 1)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'pointsDeltaFrom', 0)
        self._addNumberProperty(b'infinityLevelCompleteCount', 0)
        self._addNumberProperty(b'infinityStartPoints', 0)
        self._addNumberProperty(b'infinityMaxPoints', 0)
        self._addNumberProperty(b'infinitySubstagesCount', 0)
        self._addNumberProperty(b'infinityDeltaFrom', 0)
        self._addArrayProperty(b'levels', Array())
        self._addArrayProperty(b'infinityRewards', Array())
        return
