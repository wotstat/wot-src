from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class TaskConditionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TaskConditionTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevels(self):
        return self._getString(0)

    def setLevels(self, value):
        self._setString(0, value)
        return

    def getVehicleTypes(self):
        return self._getArray(1)

    def setVehicleTypes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getVehicleTypesType():
        return unicode

    def getVehicleNations(self):
        return self._getArray(2)

    def setVehicleNations(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehicleNationsType():
        return unicode

    def getBattleTypes(self):
        return self._getArray(3)

    def setBattleTypes(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getBattleTypesType():
        return int

    def _initialize(self):
        super(TaskConditionTooltipViewModel, self)._initialize()
        self._addStringProperty(b'levels', b'')
        self._addArrayProperty(b'vehicleTypes', Array())
        self._addArrayProperty(b'vehicleNations', Array())
        self._addArrayProperty(b'battleTypes', Array())
        return
