from __future__ import absolute_import
import ResMgr
from constants import FLAG_TYPES
from soft_exception import SoftException
_CONFIG_FILE = b'scripts/item_defs/win_points.xml'

class DamageSettings(object):

    def __init__(self, section):
        self.pointsForKill = section[b'winPointsForKill'].asInt
        self.pointsForDamage = (
         section[b'winPointsForDamage'][b'damageToDeal'].asInt,
         section[b'winPointsForDamage'][b'pointsToGrant'].asInt)
        return


class WinPointsTeamOrSoloSettings(object):

    def __init__(self, section):
        self.vehicleDamageSettings = DamageSettings(section[b'vehicle'])
        self.equipmentDamageSettings = DamageSettings(section[b'equipment'])
        self.pointsForFlag = [
         0] * len(FLAG_TYPES.RANGE)
        for name, subsection in section[b'winPointsForFlag'].items():
            name = name.upper()
            flagTypeId = getattr(FLAG_TYPES, name, None)
            if flagTypeId is None:
                raise SoftException(b'Unknown flag type name (%s)' % (name,))
            self.pointsForFlag[flagTypeId] = subsection.asInt

        self.pointsForOneResource = section[b'winPointsForOneResource'].asInt
        return


WinPointsTeamSettings = WinPointsTeamOrSoloSettings
WinPointsSoloSettings = WinPointsTeamOrSoloSettings

class WinPointsSettings(object):

    def __init__(self, section):
        self.pointsCAP = section[b'winPointsCAP'].asInt
        self.teamSettings = WinPointsTeamSettings(section[b'team'])
        self.soloSettings = WinPointsSoloSettings(section[b'solo'])
        return

    def pointsForKill(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.pointsForKill

    def pointsForDamage(self, isSolo, forVehicle):
        settings = self.soloSettings if isSolo else self.teamSettings
        damageSettings = settings.vehicleDamageSettings if forVehicle else settings.equipmentDamageSettings
        return damageSettings.pointsForDamage

    def __getattr__(self, item):
        if item in (b'pointsForFlag', b'pointsForOneResource'):
            return (lambda isSolo: getattr(self.soloSettings, item) if isSolo else getattr(self.teamSettings, item))
        else:
            return super(WinPointsSettings, self).__getattr__(item)

        return


g_cache = None

def init():
    global g_cache
    g_cache = settings = {}
    section = ResMgr.openSection(_CONFIG_FILE)
    for name, subsection in section.items():
        settings[name] = WinPointsSettings(subsection)

    return
