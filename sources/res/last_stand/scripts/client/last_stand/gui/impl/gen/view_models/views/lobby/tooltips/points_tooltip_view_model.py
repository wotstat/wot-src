from frameworks.wulf import ViewModel

class PointsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(PointsTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)
        return

    def getEffective(self):
        return self._getNumber(1)

    def setEffective(self, value):
        self._setNumber(1, value)
        return

    def getObelisk(self):
        return self._getNumber(2)

    def setObelisk(self, value):
        self._setNumber(2, value)
        return

    def getMissionDaily(self):
        return self._getNumber(3)

    def setMissionDaily(self, value):
        self._setNumber(3, value)
        return

    def getVehicleDaily(self):
        return self._getNumber(4)

    def setVehicleDaily(self, value):
        self._setNumber(4, value)
        return

    def getBundleKey(self):
        return self._getString(5)

    def setBundleKey(self, value):
        self._setString(5, value)
        return

    def getIsPostBattle(self):
        return self._getBool(6)

    def setIsPostBattle(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(PointsTooltipViewModel, self)._initialize()
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'effective', 0)
        self._addNumberProperty(b'obelisk', 0)
        self._addNumberProperty(b'missionDaily', 0)
        self._addNumberProperty(b'vehicleDaily', 0)
        self._addStringProperty(b'bundleKey', b'')
        self._addBoolProperty(b'isPostBattle', False)
        return
