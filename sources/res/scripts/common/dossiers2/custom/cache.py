import nations
from items import vehicles
from collector_vehicle import CollectorVehicleConsts

def getCache():
    global _g_cache
    return _g_cache


def buildCache():
    vehiclesByLevel = {}
    vehiclesByTag = {b'beast': (set()), b'sinai': (set()), b'patton': (set()), b'supply': (set())}
    vehiclesInTreeByNation = {}
    vehiclesInTree = set()
    nationsWithVehiclesInTree = []
    collectorVehiclesByNations = {}
    collectorVehiclesLevelsByNations = {}
    unlocksSources = vehicles.getUnlocksSources()
    for nationIdx in xrange(len(nations.NAMES)):
        nationList = vehicles.g_list.getList(nationIdx)
        vehiclesInNationTree = set()
        for vehDescr in nationList.itervalues():
            if b'supply' in vehDescr.tags:
                vehiclesByTag[b'supply'].add(vehDescr.compactDescr)
            if b'bob' in vehDescr.tags:
                continue
            elif b'battle_royale' in vehDescr.tags:
                continue
            elif b'maps_training' in vehDescr.tags:
                continue
            elif b'event_battles' in vehDescr.tags:
                continue
            elif b'secret' in vehDescr.tags:
                continue
            vehiclesByLevel.setdefault(vehDescr.level, set()).add(vehDescr.compactDescr)
            for tag in (b'beast', b'sinai', b'patton'):
                if tag in vehDescr.tags:
                    vehiclesByTag[tag].add(vehDescr.compactDescr)

            if CollectorVehicleConsts.COLLECTOR_VEHICLES_TAG in vehDescr.tags:
                collectorVehiclesByNations.setdefault(nationIdx, set()).add(vehDescr.compactDescr)
                collectorVehiclesLevelsByNations.setdefault(nationIdx, set()).add(vehDescr.level)
                continue
            vehType = vehicles.g_cache.vehicle(nationIdx, vehDescr.id)
            if not vehType.isPremium:
                if len(unlocksSources.get(vehDescr.compactDescr, set())) > 0 or len(vehType.unlocksDescrs) > 0:
                    vehiclesInNationTree.add(vehDescr.compactDescr)

        vehiclesInTree.update(vehiclesInNationTree)
        vehiclesInTreeByNation[nationIdx] = vehiclesInNationTree
        if bool(vehiclesInNationTree):
            nationsWithVehiclesInTree.append(nationIdx)

    vehicles8p = vehiclesByLevel[8] | vehiclesByLevel[9] | vehiclesByLevel[10]
    _g_cache.update({b'vehiclesByLevel': vehiclesByLevel, 
       b'vehicles8+': vehicles8p, 
       b'vehiclesInTreesWithout1Lvl': (vehiclesInTree - vehiclesByLevel[1]), 
       b'vehiclesByTag': vehiclesByTag, 
       b'mausTypeCompDescr': (vehicles.makeVehicleTypeCompDescrByName(b'germany:G42_Maus')), 
       b'vehiclesInTreesByNation': vehiclesInTreeByNation, 
       b'vehiclesInTrees': vehiclesInTree, 
       b'nationsWithVehiclesInTree': nationsWithVehiclesInTree, 
       b'collectorVehiclesByNations': collectorVehiclesByNations, 
       b'collectorVehiclesLevelsByNations': collectorVehiclesLevelsByNations})
    return


_g_cache = {}
