from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class MapsTrainingScenarioModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MapsTrainingScenarioModel, self).__init__(properties=properties, commands=commands)
        return

    def getTeam(self):
        return self._getNumber(0)

    def setTeam(self, value):
        self._setNumber(0, value)
        return

    def getScenarioNum(self):
        return self._getNumber(1)

    def setScenarioNum(self, value):
        self._setNumber(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getIsComplete(self):
        return self._getBool(3)

    def setIsComplete(self, value):
        self._setBool(3, value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(MapsTrainingScenarioModel, self)._initialize()
        self._addNumberProperty(b'team', 0)
        self._addNumberProperty(b'scenarioNum', 0)
        self._addStringProperty(b'vehicleType', b'')
        self._addBoolProperty(b'isComplete', False)
        self._addArrayProperty(b'rewards', Array())
        return
