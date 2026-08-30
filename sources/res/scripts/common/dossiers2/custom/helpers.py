import typing
from dossiers2.custom.cache import getCache
from dossiers2.custom.records import RECORDS, RECORD_INDICES, RECORD_DB_IDS, DB_ID_TO_RECORD
from nations import ALL_NATIONS_INDEX
from paragons_common import getResetVehicles

def getTankExpertRequirements(vehTypeFrags, nationID=ALL_NATIONS_INDEX):
    cache = getCache()
    killedVehTypes = set(vehTypeFrags.iterkeys())
    res = {b'tankExpert': (cache[b'vehiclesInTrees'] - killedVehTypes)}
    if nationID == ALL_NATIONS_INDEX:
        nationIDs = cache[b'nationsWithVehiclesInTree']
    else:
        nationIDs = [
         nationID]
    vehiclesInTreesByNation = cache[b'vehiclesInTreesByNation']
    for nationIdx in nationIDs:
        res[(b'').join([b'tankExpert', str(nationIdx)])] = vehiclesInTreesByNation[nationIdx] - killedVehTypes

    return res


def getMechanicEngineerRequirements(defaultUnlocks, unlocks, nationID=ALL_NATIONS_INDEX):
    cache = getCache()
    vehiclesInTreesByNation = cache[b'vehiclesInTreesByNation']
    res = {b'mechanicEngineer': (cache[b'vehiclesInTrees'] - defaultUnlocks - unlocks)}
    if nationID == ALL_NATIONS_INDEX:
        nationIDs = cache[b'nationsWithVehiclesInTree']
    else:
        nationIDs = [
         nationID]
    for nationIdx in nationIDs:
        res[(b'').join([b'mechanicEngineer', str(nationIdx)])] = vehiclesInTreesByNation[nationIdx] - defaultUnlocks - unlocks

    return res


def getVehicleCollectorRequirements(inventoryVehicles, nationID=ALL_NATIONS_INDEX):
    cache = getCache()
    collectorVehicles = getAllCollectorVehicles()
    res = {b'collectorVehicle': (collectorVehicles - inventoryVehicles)}
    collectorVehiclesByNations = cache[b'collectorVehiclesByNations']
    nationIDs = collectorVehiclesByNations.keys() if nationID == ALL_NATIONS_INDEX else [nationID]
    for nationIdx in nationIDs:
        achievementName = (b'').join([b'collectorVehicle', str(nationIdx)])
        collectorVehiclesByNation = collectorVehiclesByNations.get(nationIdx, set())
        if collectorVehiclesByNation:
            res[achievementName] = collectorVehiclesByNation - inventoryVehicles

    return res


def getAllCollectorVehicles(nationID=ALL_NATIONS_INDEX):
    cache = getCache()
    collectorVehicles = set()
    collectorVehiclesByNations = cache[b'collectorVehiclesByNations']
    if nationID == ALL_NATIONS_INDEX:
        for collectorVehiclesInNation in collectorVehiclesByNations.itervalues():
            collectorVehicles.update(collectorVehiclesInNation)

    else:
        collectorVehicles.update(collectorVehiclesByNations.get(nationID, set()))
    return collectorVehicles


def getRecordMaxValue(block, record):
    recordPacking = RECORDS[RECORD_INDICES[block, record]]
    if recordPacking[2] == b'b' or recordPacking[2] == b'bs':
        return 1
    return recordPacking[4]


def updateTankExpert(dossierDescr, vehTypeFrags, nationID):
    res = getTankExpertRequirements(vehTypeFrags, nationID)
    for record, value in res.iteritems():
        if len(value) == 0:
            if not dossierDescr[b'achievements'][record]:
                dossierDescr[b'achievements'][record] = True
                dossierDescr.addPopUp(b'achievements', record, True)

    return


def updateMechanicEngineer(dossierDescr, defaultUnlocks, unlocks, nationID=ALL_NATIONS_INDEX):
    res = getMechanicEngineerRequirements(defaultUnlocks, unlocks, nationID=nationID)
    for record, value in res.iteritems():
        if len(value) == 0:
            if not dossierDescr[b'achievements'][record]:
                dossierDescr[b'achievements'][record] = True
                dossierDescr.addPopUp(b'achievements', record, True)

    return


def updateVehicleCollector(dossierDescr, inventoryVehicles, nationID):
    res = getVehicleCollectorRequirements(inventoryVehicles, nationID)
    for record, value in res.iteritems():
        if len(value) == 0:
            if not dossierDescr[b'achievements'][record]:
                dossierDescr[b'achievements'][record] = True
                dossierDescr.addPopUp(b'achievements', record, True)

    return


def updateVehicleBoughtListAchievements(dossierDescr, vehDescr):
    if vehDescr.type.isCollectorVehicle or vehDescr.type.isPremium:
        return
    level = vehDescr.level
    if 5 <= level <= 10:
        medalName = (b'steamGetTankLevel{0}Medal').format(level)
        if not dossierDescr[b'steamAchievements'][medalName]:
            dossierDescr[b'steamAchievements'][medalName] = True
    return


def updateRareAchievements(dossierDescr, achievements):
    block = dossierDescr[b'rareAchievements']
    for achievement in achievements:
        if achievement > 0:
            block.append(achievement)
        elif achievement < 0:
            try:
                block.remove(abs(achievement))
            except:
                pass

    return


def convertDossierPathToDBId(path):
    return RECORD_DB_IDS[path]


def convertDBIdToDossierPath(value):
    return DB_ID_TO_RECORD[value]
