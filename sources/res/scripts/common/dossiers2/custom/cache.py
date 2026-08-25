from __future__ import absolute_import
from future.utils import viewvalues
from past.builtins import xrange
import nations
from items import vehicles
from collector_vehicle import CollectorVehicleConsts
PRESTIGE_ALLOWED_TAGS = {
 7, 8, 9, 10, 
 11, 12, 13, 14, 15, 
 16, 17, 18, 19, 
 20, 21, 
 22, 23, 24, 25, 
 26, 27, 28, 29, 30, 31, 
 32, 33, 34, 35, 36, 
 37, 38, 
 39, 40, 41}
EXCLUDE_VEHICLE_BY_TAGS = {
 42, 43, 44, 45, 27}

def getCache():
    global _g_cache
    return _g_cache


def buildCache():
    vehiclesByLevel = {}
    TAGS_TO_COLLECT = {
     b'beast', b'sinai', b'patton'}.union(PRESTIGE_ALLOWED_TAGS)
    vehiclesByTag = {tag: set() for tag in TAGS_TO_COLLECT}
    vehiclesInTreeByNation = {}
    vehiclesInTree = set()
    nationsWithVehiclesInTree = []
    collectorVehiclesByNations = {}
    collectorVehiclesLevelsByNations = {}
    vehiclesNameToDescr = {}
    vehicleEliteStatusXp = {}
    vehiclesByClass = {tag: set() for tag in vehicles.VEHICLE_CLASS_TAGS}
    unlocksSources = vehicles.getUnlocksSources()
    for nationIdx in xrange(len(nations.NAMES)):
        nationList = vehicles.g_list.getList(nationIdx)
        vehiclesInNationTree = set()
        for vehDescr in viewvalues(nationList):
            if EXCLUDE_VEHICLE_BY_TAGS.intersection(vehDescr.tags):
                continue
            vehiclesNameToDescr[vehDescr.name] = vehDescr.compactDescr
            vehicleEliteStatusXp[vehDescr.compactDescr] = __getVehicleEliteStatusXp(vehDescr.compactDescr)
            vehiclesByLevel.setdefault(vehDescr.level, set()).add(vehDescr.compactDescr)
            for tag in TAGS_TO_COLLECT:
                if tag in vehDescr.tags:
                    vehiclesByTag[tag].add(vehDescr.compactDescr)

            for tag in vehicles.VEHICLE_CLASS_TAGS:
                if tag in vehDescr.tags:
                    vehiclesByClass[tag].add(vehDescr.compactDescr)

            if CollectorVehicleConsts.COLLECTOR_VEHICLES_TAG in vehDescr.tags:
                collectorVehiclesByNations.setdefault(nationIdx, set()).add(vehDescr.compactDescr)
                collectorVehiclesLevelsByNations.setdefault(nationIdx, set()).add(vehDescr.level)
                continue
            if len(unlocksSources.get(vehDescr.compactDescr, set())) > 0 or len(vehicles.g_cache.vehicle(nationIdx, vehDescr.id).unlocksDescrs) > 0:
                vehiclesInNationTree.add(vehDescr.compactDescr)

        vehiclesInTree.update(vehiclesInNationTree)
        vehiclesInTreeByNation[nationIdx] = vehiclesInNationTree
        if bool(vehiclesInNationTree):
            nationsWithVehiclesInTree.append(nationIdx)

    vehicles8p = vehiclesByLevel[8] | vehiclesByLevel[9] | vehiclesByLevel[10] | vehiclesByLevel[11]
    _g_cache.update({b'vehiclesByLevel': vehiclesByLevel, 
       b'vehicles8+': vehicles8p, 
       b'vehiclesByTag': vehiclesByTag, 
       b'mausTypeCompDescr': (vehicles.makeVehicleTypeCompDescrByName(b'germany:G42_Maus')), 
       b'vehiclesInTreesByNation': vehiclesInTreeByNation, 
       b'vehiclesInTrees': vehiclesInTree, 
       b'nationsWithVehiclesInTree': nationsWithVehiclesInTree, 
       b'collectorVehiclesByNations': collectorVehiclesByNations, 
       b'collectorVehiclesLevelsByNations': collectorVehiclesLevelsByNations, 
       b'vehiclesNameToDescr': vehiclesNameToDescr, 
       b'vehicleEliteStatusXp': vehicleEliteStatusXp, 
       b'vehiclesByClass': vehiclesByClass})
    return


_g_cache = {}

def __getVehicleEliteStatusXp(vehicleCompDescr):
    eliteXpCost = 0
    vehType = vehicles.getVehicleType(vehicleCompDescr)
    for unlockDescr in vehType.unlocksDescrs:
        eliteXpCost += unlockDescr[0]

    return eliteXpCost
