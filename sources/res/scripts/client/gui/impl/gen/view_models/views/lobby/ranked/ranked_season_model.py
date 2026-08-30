from frameworks.wulf import ViewModel

class RankedSeasonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(RankedSeasonModel, self).__init__(properties=properties, commands=commands)
        return

    def getSeasonNumber(self):
        return self._getNumber(0)

    def setSeasonNumber(self, value):
        self._setNumber(0, value)
        return

    def getStartDate(self):
        return self._getNumber(1)

    def setStartDate(self, value):
        self._setNumber(1, value)
        return

    def getEndDate(self):
        return self._getNumber(2)

    def setEndDate(self, value):
        self._setNumber(2, value)
        return

    def getIsValid(self):
        return self._getBool(3)

    def setIsValid(self, value):
        self._setBool(3, value)
        return

    def getIsSpecialSeason(self):
        return self._getBool(4)

    def setIsSpecialSeason(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(RankedSeasonModel, self)._initialize()
        self._addNumberProperty(b'seasonNumber', -1)
        self._addNumberProperty(b'startDate', -1)
        self._addNumberProperty(b'endDate', -1)
        self._addBoolProperty(b'isValid', False)
        self._addBoolProperty(b'isSpecialSeason', False)
        return
