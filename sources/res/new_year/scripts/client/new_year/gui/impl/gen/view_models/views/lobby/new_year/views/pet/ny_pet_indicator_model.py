from frameworks.wulf import Array
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import NyIndicatorType
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_item_leaderboard_point import NyPetItemLeaderboardPoint

class NyPetIndicatorModel(NyIndicatorType):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(NyPetIndicatorModel, self).__init__(properties=properties, commands=commands)
        return

    def getMaxPoint(self):
        return self._getNumber(1)

    def setMaxPoint(self, value):
        self._setNumber(1, value)
        return

    def getCurPoint(self):
        return self._getNumber(2)

    def setCurPoint(self, value):
        self._setNumber(2, value)
        return

    def getPotentialCurPoint(self):
        return self._getNumber(3)

    def setPotentialCurPoint(self, value):
        self._setNumber(3, value)
        return

    def getScaleLevels(self):
        return self._getArray(4)

    def setScaleLevels(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getScaleLevelsType():
        return int

    def getItemCount(self):
        return self._getNumber(5)

    def setItemCount(self, value):
        self._setNumber(5, value)
        return

    def getItemScalePoint(self):
        return self._getNumber(6)

    def setItemScalePoint(self, value):
        self._setNumber(6, value)
        return

    def getItemLeaderboardPoint(self):
        return self._getArray(7)

    def setItemLeaderboardPoint(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getItemLeaderboardPointType():
        return NyPetItemLeaderboardPoint

    def getScaleDowngradeTime(self):
        return self._getReal(8)

    def setScaleDowngradeTime(self, value):
        self._setReal(8, value)
        return

    def getScaleEmptyTime(self):
        return self._getReal(9)

    def setScaleEmptyTime(self, value):
        self._setReal(9, value)
        return

    def getIsLocked(self):
        return self._getBool(10)

    def setIsLocked(self, value):
        self._setBool(10, value)
        return

    def getAtmosphereLevelToUnlock(self):
        return self._getNumber(11)

    def setAtmosphereLevelToUnlock(self, value):
        self._setNumber(11, value)
        return

    def getIsLoading(self):
        return self._getBool(12)

    def setIsLoading(self, value):
        self._setBool(12, value)
        return

    def getBonus(self):
        return self._getNumber(13)

    def setBonus(self, value):
        self._setNumber(13, value)
        return

    def getWasOverflowed(self):
        return self._getBool(14)

    def setWasOverflowed(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(NyPetIndicatorModel, self)._initialize()
        self._addNumberProperty(b'maxPoint', 0)
        self._addNumberProperty(b'curPoint', 0)
        self._addNumberProperty(b'potentialCurPoint', 0)
        self._addArrayProperty(b'scaleLevels', Array())
        self._addNumberProperty(b'itemCount', 0)
        self._addNumberProperty(b'itemScalePoint', 0)
        self._addArrayProperty(b'itemLeaderboardPoint', Array())
        self._addRealProperty(b'scaleDowngradeTime', 0.0)
        self._addRealProperty(b'scaleEmptyTime', 0.0)
        self._addBoolProperty(b'isLocked', False)
        self._addNumberProperty(b'atmosphereLevelToUnlock', 0)
        self._addBoolProperty(b'isLoading', False)
        self._addNumberProperty(b'bonus', 0)
        self._addBoolProperty(b'wasOverflowed', False)
        return
