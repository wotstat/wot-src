from enum import IntEnum
from frameworks.wulf import ViewModel

class RoverEnum(IntEnum):
    OLD = 1
    NEW = 2


class PlayerRecordModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PlayerRecordModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getClanAbbrev(self):
        return self._getString(1)

    def setClanAbbrev(self, value):
        self._setString(1, value)
        return

    def getScore(self):
        return self._getNumber(2)

    def setScore(self, value):
        self._setNumber(2, value)
        return

    def getVehicle(self):
        return RoverEnum(self._getNumber(3))

    def setVehicle(self, value):
        self._setNumber(3, value.value)
        return

    def getLootResearching(self):
        return self._getBool(4)

    def setLootResearching(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(PlayerRecordModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'clanAbbrev', b'')
        self._addNumberProperty(b'score', 0)
        self._addNumberProperty(b'vehicle', RoverEnum.OLD.value)
        self._addBoolProperty(b'lootResearching', False)
        return
