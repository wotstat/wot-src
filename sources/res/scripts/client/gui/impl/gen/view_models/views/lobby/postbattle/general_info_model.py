from gui.impl.gen import R
from frameworks.wulf import ViewModel

class GeneralInfoModel(ViewModel):
    __slots__ = ()
    WIN_STATUS_TIE = 0
    WIN_STATUS_WIN = 1
    WIN_STATUS_LOSE = 2

    def __init__(self, properties=10, commands=0):
        super(GeneralInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getWinStatus(self):
        return self._getNumber(0)

    def setWinStatus(self, value):
        self._setNumber(0, value)
        return

    def getBattleType(self):
        return self._getResource(1)

    def setBattleType(self, value):
        self._setResource(1, value)
        return

    def getVehicleIconName(self):
        return self._getString(2)

    def setVehicleIconName(self, value):
        self._setString(2, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(3)

    def setVehicleLevel(self, value):
        self._setNumber(3, value)
        return

    def getArenaName(self):
        return self._getString(4)

    def setArenaName(self, value):
        self._setString(4, value)
        return

    def getBattleFinishTime(self):
        return self._getNumber(5)

    def setBattleFinishTime(self, value):
        self._setNumber(5, value)
        return

    def getServerTime(self):
        return self._getNumber(6)

    def setServerTime(self, value):
        self._setNumber(6, value)
        return

    def getVehicleType(self):
        return self._getString(7)

    def setVehicleType(self, value):
        self._setString(7, value)
        return

    def getLocalizedVehicleName(self):
        return self._getString(8)

    def setLocalizedVehicleName(self, value):
        self._setString(8, value)
        return

    def getIsBoss(self):
        return self._getBool(9)

    def setIsBoss(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(GeneralInfoModel, self)._initialize()
        self._addNumberProperty(b'winStatus', 0)
        self._addResourceProperty(b'battleType', R.invalid())
        self._addStringProperty(b'vehicleIconName', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addStringProperty(b'arenaName', b'')
        self._addNumberProperty(b'battleFinishTime', 0)
        self._addNumberProperty(b'serverTime', 0)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'localizedVehicleName', b'')
        self._addBoolProperty(b'isBoss', False)
        return
