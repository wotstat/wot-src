from frameworks.wulf import ViewModel

class StatsParameterModel(ViewModel):
    __slots__ = ()
    CURRENT_TANK_SESSION_BATTLES_COUNT = b'currentTankSessionBattlesCount'
    CURRENT_TANK_SESSION_MAX_FRAGS = b'currentTankSessionMaxFrags'
    CURRENT_TANK_SESSION_MAX_DAMAGE_BLOCKED_BY_ARMOR = b'currentTankSessionMaxDamageBlockedByArmor'
    CURRENT_TANK_SESSION_MAX_DAMAGE_DEALT = b'currentTankSessionMaxDamageDealt'
    CURRENT_TANK_SESSION_MAX_ASSISTED = b'currentTankSessionMaxAssisted'
    CURRENT_TANK_SESSION_MAX_SPOTTED = b'currentTankSessionMaxSpotted'
    CURRENT_TANK_SESSION_MAX_SURVIVED = b'currentTankSessionMaxSurvived'
    CURRENT_TANK_SESSION_WIN_STREAK = b'currentTankSessionWinStreak'
    ACCOUNT_SESSION_BATTLES_COUNT = b'accountSessionBattlesCount'
    ACCOUNT_SESSION_TOTAL_TANKS_USED = b'accountSessionTotalTanksUsed'
    ACCOUNT_SESSION_TOTAL_FRAGS = b'accountSessionTotalFrags'
    ACCOUNT_SESSION_TOTAL_WINS = b'accountSessionTotalWins'
    ACCOUNT_SESSION_TOTAL_DAMAGE_BLOCKED_BY_ARMOR = b'accountSessionTotalDamageBlockedByArmor'
    ACCOUNT_SESSION_TOTAL_DAMAGE_DEALT = b'accountSessionTotalDamageDealt'
    ACCOUNT_SESSION_TOTAL_ASSISTED = b'accountSessionTotalAssisted'
    ACCOUNT_SESSION_TOTAL_SPOTTED = b'accountSessionTotalSpotted'
    ACCOUNT_SESSION_WIN_STREAK = b'accountSessionWinStreak'
    CURRENT_TANK_BATTLES_COUNT = b'currentTankBattlesCount'
    CURRENT_TANK_FRAGS = b'currentTankFrags'
    CURRENT_TANK_SPOTTED = b'currentTankSpotted'
    CURRENT_TANK_DAMAGE_DEALT = b'currentTankDamageDealt'
    CURRENT_TANK_DAMAGE_BLOCKED_BY_ARMOR = b'currentTankDamageBlockedByArmor'
    CURRENT_TANK_ASSISTED = b'currentTankAssisted'
    CURRENT_TANK_WINS = b'currentTankWins'
    ACCOUNT_TOTAL_DAMAGE_DEALT = b'accountTotalDamageDealt'
    ACCOUNT_TOTAL_WINS = b'accountTotalWins'
    ACCOUNT_TOTAL_SPOTTED = b'accountTotalSpotted'
    ACCOUNT_BATTLES_COUNT = b'accountBattlesCount'
    ACCOUNT_FUN_AGE = b'accountFunAge'
    ACCOUNT_FUN_TREES_DESTROYED = b'accountFunTreesDestroyed'
    ACCOUNT_TOTAL_MILEAGE = b'accountTotalMileage'

    def __init__(self, properties=2, commands=0):
        super(StatsParameterModel, self).__init__(properties=properties, commands=commands)
        return

    def getParameter(self):
        return self._getString(0)

    def setParameter(self, value):
        self._setString(0, value)
        return

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(StatsParameterModel, self)._initialize()
        self._addStringProperty(b'parameter', b'')
        self._addNumberProperty(b'value', 0)
        return
