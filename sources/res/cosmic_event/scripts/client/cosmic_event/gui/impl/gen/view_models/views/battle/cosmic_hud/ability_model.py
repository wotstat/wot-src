from enum import Enum
from frameworks.wulf import ViewModel

class Ability(Enum):
    NONE = b'none'
    SHELL = b'shell'
    ACCELERATION = b'acceleration'
    TELEPORT = b'teleport'
    SHIELD = b'shield'
    BLACK_HOLE = b'black_hole'
    OVERCHARGE = b'overcharge'
    RAPID_SHELLING = b'rapid_shelling'
    POWER_SHOT = b'power_shot'
    WAVE = b'wave'
    STUN_SHOT = b'stun_shot'
    REPULSION_MINE = b'repulsion_mine'


class AbilityModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(AbilityModel, self).__init__(properties=properties, commands=commands)
        return

    def getAbility(self):
        return Ability(self._getString(0))

    def setAbility(self, value):
        self._setString(0, value.value)
        return

    def getReloadTimeLeft(self):
        return self._getReal(1)

    def setReloadTimeLeft(self, value):
        self._setReal(1, value)
        return

    def getReloadTime(self):
        return self._getReal(2)

    def setReloadTime(self, value):
        self._setReal(2, value)
        return

    def getIsActive(self):
        return self._getBool(3)

    def setIsActive(self, value):
        self._setBool(3, value)
        return

    def getIsTargeting(self):
        return self._getBool(4)

    def setIsTargeting(self, value):
        self._setBool(4, value)
        return

    def getIsEnabled(self):
        return self._getBool(5)

    def setIsEnabled(self, value):
        self._setBool(5, value)
        return

    def getKeyBind(self):
        return self._getString(6)

    def setKeyBind(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(AbilityModel, self)._initialize()
        self._addStringProperty(b'ability', Ability.NONE.value)
        self._addRealProperty(b'reloadTimeLeft', 0.0)
        self._addRealProperty(b'reloadTime', 0.0)
        self._addBoolProperty(b'isActive', False)
        self._addBoolProperty(b'isTargeting', False)
        self._addBoolProperty(b'isEnabled', True)
        self._addStringProperty(b'keyBind', b'')
        return
