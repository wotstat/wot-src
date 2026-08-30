import ResMgr
from items import vehicles
_CONFIG_FILE = b'scripts/item_defs/rage.xml'

class DamageSettings(object):

    def __init__(self, section):
        self.damageFactor = section[b'damageFactor'].asFloat
        self.pointsForKill = section[b'ragePointsForKill'].asFloat
        return


class RageTeamOrSoloSettings(object):

    def __init__(self, section):
        self.vehicleDamageSettings = DamageSettings(section[b'vehicle'])
        self.equipmentDamageSettings = DamageSettings(section[b'equipment'])
        self.pointsForFlagPickup = section[b'ragePointsForFlagPickup'].asFloat
        self.pointsForFlagCapture = section[b'ragePointsForFlagCapture'].asFloat
        self.pointsForOneResource = section[b'ragePointsForOneResource'].asFloat
        self.deathPenalty = section[b'deathPenalty'].asFloat
        return


RageTeamSettings = RageTeamOrSoloSettings
RageSoloSettings = RageTeamOrSoloSettings

class RageSettings(object):

    def __init__(self, section):
        self.pointsLimit = section[b'ragePointsLimit'].asFloat
        self.equipments = {}
        for subsection in section[b'equipments'].values():
            id = vehicles.g_cache.equipmentIDs()[subsection[b'name'].asString]
            equipment = vehicles.g_cache.equipments()[id]
            self.equipments[equipment.compactDescr] = subsection[b'costInRagePoints'].asFloat

        self.teamSettings = RageTeamSettings(section[b'team'])
        self.soloSettings = RageSoloSettings(section[b'solo'])
        return

    def damageFactor(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.damageFactor

    def pointsForKill(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.pointsForKill

    def __getattr__(self, item):
        if item in (b'pointsForFlagPickup', b'pointsForFlagCapture', b'pointsForOneResource', b'deathPenalty'):
            return (lambda isSolo: getattr(self.soloSettings, item) if isSolo else getattr(self.teamSettings, item))
        else:
            return super(RageSettings, self).__getattr__(item)

        return


g_cache = None

def init():
    global g_cache
    section = ResMgr.openSection(_CONFIG_FILE)
    g_cache = RageSettings(section)
    return
