def getTankPortalActualPrice(tankPortalPrice, discountPerToken, discountTokenCount):
    totalDiscount = discountTokenCount * discountPerToken
    return tankPortalPrice - totalDiscount


def isHunterVehicle(vehicleCD, eventVehicles):
    return vehicleCD in eventVehicles.get(b'hunters', {})


def isBossVehicle(vehicleCD, eventVehicles):
    return vehicleCD in eventVehicles.get(b'bosses', {})


def isSpecialBossVehicle(vehicleCD, eventVehicles):
    return vehicleCD in eventVehicles.get(b'specialBosses', {})


def isAnyTypeBoss(vehicleCD, eventVehicles):
    return vehicleCD in eventVehicles.get(b'bosses', {}) or vehicleCD in eventVehicles.get(b'specialBosses', {})


def getBossVehicles(eventVehicles):
    return eventVehicles.get(b'bosses', {})


def getSpecialBossVehicleCDs(eventVehicles):
    return eventVehicles.get(b'specialBosses', {}).keys()


def getHunterVehicles(eventVehicles):
    return eventVehicles.get(b'hunters', {})


def isEventVehicle(config, vehCD):
    return vehCD in config[b'allEventVehicleCDs']


def getVehicleData(config, vehCD):
    if vehCD in config[b'allEventVehicleCDs']:
        hunters = config[b'eventVehicles'].get(b'hunters', {})
        if vehCD in hunters:
            return hunters[vehCD]
        bosses = config[b'eventVehicles'].get(b'bosses', {})
        if vehCD in bosses:
            return bosses[vehCD]
        specialBosses = config[b'eventVehicles'].get(b'specialBosses', {})
        if vehCD in specialBosses:
            return specialBosses[vehCD]
    return
