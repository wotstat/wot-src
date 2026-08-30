from enum import Enum
from frameworks.wulf import Array, ViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.player_model import PlayerModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class MarksOfMastery(Enum):
    NONE = b''
    MASTER = b'master'
    FIRST = b'first'
    SECOND = b'second'
    THIRD = b'third'


class ReplayModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(ReplayModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleModel

    @property
    def playerInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getPlayerInfoType():
        return PlayerModel

    def getId(self):
        return self._getString(2)

    def setId(self, value):
        self._setString(2, value)
        return

    def getIsFavorite(self):
        return self._getBool(3)

    def setIsFavorite(self, value):
        self._setBool(3, value)
        return

    def getArenaName(self):
        return self._getString(4)

    def setArenaName(self, value):
        self._setString(4, value)
        return

    def getTimestamp(self):
        return self._getNumber(5)

    def setTimestamp(self, value):
        self._setNumber(5, value)
        return

    def getEarnedXp(self):
        return self._getNumber(6)

    def setEarnedXp(self, value):
        self._setNumber(6, value)
        return

    def getDamageDealt(self):
        return self._getNumber(7)

    def setDamageDealt(self, value):
        self._setNumber(7, value)
        return

    def getDamageAssisted(self):
        return self._getNumber(8)

    def setDamageAssisted(self, value):
        self._setNumber(8, value)
        return

    def getDamageBlockedByArmor(self):
        return self._getNumber(9)

    def setDamageBlockedByArmor(self, value):
        self._setNumber(9, value)
        return

    def getKills(self):
        return self._getNumber(10)

    def setKills(self, value):
        self._setNumber(10, value)
        return

    def getMarksOfMastery(self):
        return MarksOfMastery(self._getString(11))

    def setMarksOfMastery(self, value):
        self._setString(11, value.value)
        return

    def getEpicMedals(self):
        return self._getArray(12)

    def setEpicMedals(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getEpicMedalsType():
        return unicode

    def _initialize(self):
        super(ReplayModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleModel())
        self._addViewModelProperty(b'playerInfo', PlayerModel())
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isFavorite', False)
        self._addStringProperty(b'arenaName', b'')
        self._addNumberProperty(b'timestamp', 0)
        self._addNumberProperty(b'earnedXp', 0)
        self._addNumberProperty(b'damageDealt', 0)
        self._addNumberProperty(b'damageAssisted', 0)
        self._addNumberProperty(b'damageBlockedByArmor', 0)
        self._addNumberProperty(b'kills', 0)
        self._addStringProperty(b'marksOfMastery', MarksOfMastery.NONE.value)
        self._addArrayProperty(b'epicMedals', Array())
        return
