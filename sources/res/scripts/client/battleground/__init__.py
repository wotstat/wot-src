from __future__ import absolute_import
from items import vehicles
__author__ = b'a_jorov'

def getKamikazeEquipmentDescr():
    return vehicles.g_cache.equipments()[vehicles.g_cache.equipmentIDs()[b'spawn_kamikaze']]
