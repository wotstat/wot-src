from frameworks.wulf import Array, ViewModel

class MissionProgressTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MissionProgressTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTotalMissionsAmount(self):
        return self._getNumber(0)

    def setTotalMissionsAmount(self, value):
        self._setNumber(0, value)
        return

    def getCompletedMissionsAmount(self):
        return self._getNumber(1)

    def setCompletedMissionsAmount(self, value):
        self._setNumber(1, value)
        return

    def getVehicles(self):
        return self._getArray(2)

    def setVehicles(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getVehiclesType():
        return unicode

    def _initialize(self):
        super(MissionProgressTooltipModel, self)._initialize()
        self._addNumberProperty(b'totalMissionsAmount', 0)
        self._addNumberProperty(b'completedMissionsAmount', 0)
        self._addArrayProperty(b'vehicles', Array())
        return
