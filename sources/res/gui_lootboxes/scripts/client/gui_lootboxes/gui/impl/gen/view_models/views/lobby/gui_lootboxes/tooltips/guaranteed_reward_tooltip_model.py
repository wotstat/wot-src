from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class GuaranteedRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(GuaranteedRewardTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevelsRange(self):
        return self._getArray(0)

    def setLevelsRange(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getLevelsRangeType():
        return int

    def getGuaranteedFrequencies(self):
        return self._getArray(1)

    def setGuaranteedFrequencies(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getGuaranteedFrequenciesType():
        return int

    def getGuaranteedBoxNameKeys(self):
        return self._getArray(2)

    def setGuaranteedBoxNameKeys(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getGuaranteedBoxNameKeysType():
        return unicode

    def getVehiclesOnly(self):
        return self._getBool(3)

    def setVehiclesOnly(self, value):
        self._setBool(3, value)
        return

    def getMultipleStages(self):
        return self._getBool(4)

    def setMultipleStages(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(GuaranteedRewardTooltipModel, self)._initialize()
        self._addArrayProperty(b'levelsRange', Array())
        self._addArrayProperty(b'guaranteedFrequencies', Array())
        self._addArrayProperty(b'guaranteedBoxNameKeys', Array())
        self._addBoolProperty(b'vehiclesOnly', True)
        self._addBoolProperty(b'multipleStages', False)
        return
