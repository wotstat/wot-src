from frameworks.wulf import ViewModel

class EfficiencyItemModel(ViewModel):
    __slots__ = ()
    DAMAGE_ASSISTED_STUN = b'damageAssistedStun'
    SPOTTED = b'spotted'
    DAMAGE_ASSISTED = b'damageAssisted'
    DAMAGE_BLOCKED_BY_ARMOR = b'damageBlockedByArmor'
    CRITS_COUNT = b'critsCount'
    DAMAGE_DEALT = b'damageDealt'
    KILLS = b'kills'

    def __init__(self, properties=4, commands=0):
        super(EfficiencyItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamName(self):
        return self._getString(0)

    def setParamName(self, value):
        self._setString(0, value)
        return

    def getSimpleValue(self):
        return self._getNumber(1)

    def setSimpleValue(self, value):
        self._setNumber(1, value)
        return

    def getDetailedValue(self):
        return self._getNumber(2)

    def setDetailedValue(self, value):
        self._setNumber(2, value)
        return

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(EfficiencyItemModel, self)._initialize()
        self._addStringProperty(b'paramName', b'')
        self._addNumberProperty(b'simpleValue', 0)
        self._addNumberProperty(b'detailedValue', 0)
        self._addBoolProperty(b'isVisible', True)
        return
