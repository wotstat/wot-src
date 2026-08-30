from enum import IntEnum
from frameworks.wulf import ViewModel

class ResultEnum(IntEnum):
    DEFEAT = -1
    DRAW = 0
    VICTORY = 1


class BattleNotifierViewModel(ViewModel):
    __slots__ = (b'onResultShown',)

    def __init__(self, properties=9, commands=1):
        super(BattleNotifierViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattleResult(self):
        return ResultEnum(self._getNumber(0))

    def setBattleResult(self, value):
        self._setNumber(0, value.value)
        return

    def getBattleStartTime(self):
        return self._getNumber(1)

    def setBattleStartTime(self, value):
        self._setNumber(1, value)
        return

    def getMapName(self):
        return self._getString(2)

    def setMapName(self, value):
        self._setString(2, value)
        return

    def getVehicleName(self):
        return self._getString(3)

    def setVehicleName(self, value):
        self._setString(3, value)
        return

    def getVehicleTier(self):
        return self._getNumber(4)

    def setVehicleTier(self, value):
        self._setNumber(4, value)
        return

    def getVehicleClass(self):
        return self._getString(5)

    def setVehicleClass(self, value):
        self._setString(5, value)
        return

    def getCreditsAmount(self):
        return self._getNumber(6)

    def setCreditsAmount(self, value):
        self._setNumber(6, value)
        return

    def getExperienceAmount(self):
        return self._getNumber(7)

    def setExperienceAmount(self, value):
        self._setNumber(7, value)
        return

    def getCrystalAmount(self):
        return self._getNumber(8)

    def setCrystalAmount(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(BattleNotifierViewModel, self)._initialize()
        self._addNumberProperty(b'battleResult')
        self._addNumberProperty(b'battleStartTime', 667004400)
        self._addStringProperty(b'mapName', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'vehicleTier', 0)
        self._addStringProperty(b'vehicleClass', b'')
        self._addNumberProperty(b'creditsAmount', 0)
        self._addNumberProperty(b'experienceAmount', 0)
        self._addNumberProperty(b'crystalAmount', 0)
        self.onResultShown = self._addCommand(b'onResultShown')
        return
