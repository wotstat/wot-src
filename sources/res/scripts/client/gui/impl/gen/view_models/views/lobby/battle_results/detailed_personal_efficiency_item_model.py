from frameworks.wulf import ViewModel

class DetailedPersonalEfficiencyItemModel(ViewModel):
    __slots__ = ()
    KILLED = b'targetKills'
    SPOTTED = b'spotted'
    DAMAGE_DEALT = b'damageDealt'
    PIERCINGS = b'piercings'
    STUN = b'damageAssistedStun'
    STUN_COUNT = b'stunCount'
    DAMAGE_ASSISTED = b'damageAssisted'
    CRITICAL_DAMAGE = b'criticalDamage'
    DAMAGE_BLOCKED_BY_ARMOR = b'damageBlockedByArmor'
    RICKOCHETS_RECEIVED = b'rickochetsReceived'
    NO_DAMAGE_DIRECT_HITS_RECIEVEVD = b'noDamageDirectHitsReceived'

    def __init__(self, properties=2, commands=0):
        super(DetailedPersonalEfficiencyItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamType(self):
        return self._getString(0)

    def setParamType(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(DetailedPersonalEfficiencyItemModel, self)._initialize()
        self._addStringProperty(b'paramType', b'')
        self._addNumberProperty(b'value', 0)
        return
