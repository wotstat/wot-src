from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R

class ValueType(IntEnum):
    INTEGER = 0
    FLOAT = 1
    TIME = 2


class RegularParamType(Enum):
    SHOTS = b'shots'
    HITS = b'hits'
    EXPLOSIONHITS = b'explosionHits'
    DAMAGEDEALT = b'damageDealt'
    SNIPERDAMAGEDEALT = b'sniperDamageDealt'
    ARTILLERYSTRIKE = b'artilleryStrike'
    DIRECTHITSRECEIVED = b'directHitsReceived'
    PIERCINGSRECEIVED = b'piercingsReceived'
    NODAMAGEDIRECTHITSRECEIVED = b'noDamageDirectHitsReceived'
    EXPLOSIONHITSRECEIVED = b'explosionHitsReceived'
    DAMAGEBLOCKEDBYARMOR = b'damageBlockedByArmor'
    TEAMHITSDAMAGE = b'teamHitsDamage'
    SPOTTED = b'spotted'
    DAMAGEDKILLED = b'damagedKilled'
    DAMAGEASSISTED = b'damageAssisted'
    DAMAGEASSISTEDSELF = b'damageAssistedSelf'
    STUNDURATION = b'stunDuration'
    DAMAGEASSISTEDSTUN = b'damageAssistedStun'
    DAMAGEASSISTEDSTUNSELF = b'damageAssistedStunSelf'
    STUNNUM = b'stunNum'
    CAPTUREPOINTSVAL = b'capturePointsVal'
    MILEAGE = b'mileage'


class SimpleStatsParameterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SimpleStatsParameterModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getResource(0)

    def setLabel(self, value):
        self._setResource(0, value)
        return

    def getLabelKey(self):
        return self._getString(1)

    def setLabelKey(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getArray(2)

    def setValue(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getValueType():
        return float

    def getParamValueType(self):
        return ValueType(self._getNumber(3))

    def setParamValueType(self, value):
        self._setNumber(3, value.value)
        return

    def _initialize(self):
        super(SimpleStatsParameterModel, self)._initialize()
        self._addResourceProperty(b'label', R.invalid())
        self._addStringProperty(b'labelKey', b'')
        self._addArrayProperty(b'value', Array())
        self._addNumberProperty(b'paramValueType')
        return
