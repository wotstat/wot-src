from enum import Enum
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_stats_parameter_model import DetailedStatsParameterModel

class Comp7LightParamType(Enum):
    SHOTS = b'shots'
    HITS = b'hits'
    EXPLOSIONHITS = b'explosionHits'
    DAMAGEDEALT = b'damageDealt'
    SNIPERDAMAGEDEALT = b'sniperDamageDealt'
    DAMAGEDEALTBYSKILLS = b'damageDealtBySkills'
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
    HEALED = b'healed'
    CAPTUREDPOINTSOFINTEREST = b'capturedPointsOfInterest'
    ROLESKILLUSED = b'roleSkillUsed'


class Comp7LightDetailedStatsParameterModel(DetailedStatsParameterModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(Comp7LightDetailedStatsParameterModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(Comp7LightDetailedStatsParameterModel, self)._initialize()
        return
