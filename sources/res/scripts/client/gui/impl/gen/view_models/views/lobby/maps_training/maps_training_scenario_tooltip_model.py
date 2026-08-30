from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class MapsTrainingScenarioTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MapsTrainingScenarioTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleType(self):
        return self._getString(0)

    def setVehicleType(self, value):
        self._setString(0, value)
        return

    def getTeam(self):
        return self._getNumber(1)

    def setTeam(self, value):
        self._setNumber(1, value)
        return

    def getScenarioNum(self):
        return self._getNumber(2)

    def setScenarioNum(self, value):
        self._setNumber(2, value)
        return

    def getMapId(self):
        return self._getString(3)

    def setMapId(self, value):
        self._setString(3, value)
        return

    def getTargets(self):
        return self._getArray(4)

    def setTargets(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getTargetsType():
        return unicode

    def getVehicleName(self):
        return self._getString(5)

    def setVehicleName(self, value):
        self._setString(5, value)
        return

    def getIsComplete(self):
        return self._getBool(6)

    def setIsComplete(self, value):
        self._setBool(6, value)
        return

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(MapsTrainingScenarioTooltipModel, self)._initialize()
        self._addStringProperty(b'vehicleType', b'')
        self._addNumberProperty(b'team', 0)
        self._addNumberProperty(b'scenarioNum', 0)
        self._addStringProperty(b'mapId', b'')
        self._addArrayProperty(b'targets', Array())
        self._addStringProperty(b'vehicleName', b'')
        self._addBoolProperty(b'isComplete', False)
        self._addArrayProperty(b'rewards', Array())
        return
