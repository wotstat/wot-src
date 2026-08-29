from items import vehicles

def getEquipmentById(equipmentId):
    return vehicles.g_cache.equipments()[equipmentId]


def getSmokeDataByPredicate(smokeInfo, teamPredicate, postEffectPredicate):
    if smokeInfo is None or not teamPredicate or not postEffectPredicate:
        return (None, None)
    if teamPredicate(smokeInfo[b'team']) and postEffectPredicate(smokeInfo[b'expiring']):
        return (smokeInfo[b'endTime'], getEquipmentById(smokeInfo[b'equipmentID']))
    else:
        return (None, None)
