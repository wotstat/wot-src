from __future__ import absolute_import
import re, nations
from items import vehicles
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from items import vehicle_items
_FORMAT_REXP = re.compile(b'{([a-zA-Z]+)}?')
_VEH_INFO_ARGS = {b'level': (lambda descr: str(descr.type.level)), 
   b'class': (lambda descr: descr.type.getVehicleClass()), 
   b'vehName': (lambda descr: descr.type.name.split(b':')[1]), 
   b'clip': (lambda descr: b'hasClip' if b'clip' in descr.gun.tags else b'noClip'), 
   b'autoreload': (lambda descr: b'hasAutoReload' if b'autoreload' in descr.gun.tags else b'noAutoreload'), 
   b'wheels': (lambda descr: b'hasWheels' if descr.isWheeledVehicle else b'noWheels'), 
   b'burst': (lambda descr: b'hasBurst' if descr.hasBurst else b'noBurst'), 
   b'dualGun': (lambda descr: b'hasDualGun' if descr.isDualgunVehicle else b'noDualGun'), 
   b'hydraulicChassis': (lambda descr: b'hasHydraulicChassis' if descr.type.hasSiegeMode and descr.type.hasHydraulicChassis else b'noHydraulicChassis')}

def formatVehicleInfoString(fmtStr, descr):

    def replaceMatch(match):
        specifier = match.group(1)
        handler = _VEH_INFO_ARGS.get(specifier)
        if specifier and handler:
            return handler(descr)
        return specifier

    return _FORMAT_REXP.sub(replaceMatch, fmtStr)


def getShellDescrByName(name):
    shellNation, shellName = name.split(b':')
    nationID = nations.INDICES[shellNation]
    shellID = vehicles.g_cache.shellIDs(nationID)[shellName]
    return vehicles.g_cache.shells(nationID)[shellID]


def getArtefactsIndex(artefactID):
    _, index, __ = artefactID.split(b':')
    return int(index)
