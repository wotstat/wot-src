from enum import IntEnum
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class DoneValueEnum(IntEnum):
    UNDONE = 0
    PARTIALDONE = 1
    DONE = 2


class MapsTrainingResultModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=12, commands=1):
        super(MapsTrainingResultModel, self).__init__(properties=properties, commands=commands)
        return

    def getDoneValue(self):
        return DoneValueEnum(self._getNumber(0))

    def setDoneValue(self, value):
        self._setNumber(0, value.value)
        return

    def getMapID(self):
        return self._getString(1)

    def setMapID(self, value):
        self._setString(1, value)
        return

    def getMapName(self):
        return self._getResource(2)

    def setMapName(self, value):
        self._setResource(2, value)
        return

    def getSelectedScenario(self):
        return self._getString(3)

    def setSelectedScenario(self, value):
        self._setString(3, value)
        return

    def getSelectedVehicleType(self):
        return self._getResource(4)

    def setSelectedVehicleType(self, value):
        self._setResource(4, value)
        return

    def getKills(self):
        return self._getNumber(5)

    def setKills(self, value):
        self._setNumber(5, value)
        return

    def getAllTargets(self):
        return self._getNumber(6)

    def setAllTargets(self, value):
        self._setNumber(6, value)
        return

    def getTime(self):
        return self._getString(7)

    def setTime(self, value):
        self._setString(7, value)
        return

    def getVehicleImage(self):
        return self._getResource(8)

    def setVehicleImage(self, value):
        self._setResource(8, value)
        return

    def getWasDone(self):
        return self._getBool(9)

    def setWasDone(self, value):
        self._setBool(9, value)
        return

    def getHangarReady(self):
        return self._getBool(10)

    def setHangarReady(self, value):
        self._setBool(10, value)
        return

    def getRewards(self):
        return self._getArray(11)

    def setRewards(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(MapsTrainingResultModel, self)._initialize()
        self._addNumberProperty(b'doneValue')
        self._addStringProperty(b'mapID', b'')
        self._addResourceProperty(b'mapName', R.invalid())
        self._addStringProperty(b'selectedScenario', b'')
        self._addResourceProperty(b'selectedVehicleType', R.invalid())
        self._addNumberProperty(b'kills', 0)
        self._addNumberProperty(b'allTargets', 0)
        self._addStringProperty(b'time', b'')
        self._addResourceProperty(b'vehicleImage', R.invalid())
        self._addBoolProperty(b'wasDone', False)
        self._addBoolProperty(b'hangarReady', False)
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        return
