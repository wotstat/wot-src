from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class TopVehicleStatisticsModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(TopVehicleStatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattles(self):
        return self._getNumber(10)

    def setBattles(self, value):
        self._setNumber(10, value)
        return

    def getWinSeries(self):
        return self._getReal(11)

    def setWinSeries(self, value):
        self._setReal(11, value)
        return

    def getDamage(self):
        return self._getNumber(12)

    def setDamage(self, value):
        self._setNumber(12, value)
        return

    def getAssist(self):
        return self._getNumber(13)

    def setAssist(self, value):
        self._setNumber(13, value)
        return

    def getPrestigePoints(self):
        return self._getNumber(14)

    def setPrestigePoints(self, value):
        self._setNumber(14, value)
        return

    def getMaxFrags(self):
        return self._getReal(15)

    def setMaxFrags(self, value):
        self._setReal(15, value)
        return

    def getDestruction(self):
        return self._getReal(16)

    def setDestruction(self, value):
        self._setReal(16, value)
        return

    def _initialize(self):
        super(TopVehicleStatisticsModel, self)._initialize()
        self._addNumberProperty(b'battles', 0)
        self._addRealProperty(b'winSeries', 0.0)
        self._addNumberProperty(b'damage', 0)
        self._addNumberProperty(b'assist', 0)
        self._addNumberProperty(b'prestigePoints', 0)
        self._addRealProperty(b'maxFrags', 0.0)
        self._addRealProperty(b'destruction', 0.0)
        return
