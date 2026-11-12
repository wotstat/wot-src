from enum import Enum
from frameworks.wulf import ViewModel

class PetNeed(Enum):
    FOOD = b'food'
    FUN = b'fun'
    ACTIVITY = b'activity'


class PetStatsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PetStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return PetNeed(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)
        return

    def getBonus(self):
        return self._getNumber(2)

    def setBonus(self, value):
        self._setNumber(2, value)
        return

    def getMaxBonus(self):
        return self._getNumber(3)

    def setMaxBonus(self, value):
        self._setNumber(3, value)
        return

    def getNextStage(self):
        return self._getNumber(4)

    def setNextStage(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(PetStatsModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addNumberProperty(b'timeLeft', 0)
        self._addNumberProperty(b'bonus', 0)
        self._addNumberProperty(b'maxBonus', 0)
        self._addNumberProperty(b'nextStage', 0)
        return
