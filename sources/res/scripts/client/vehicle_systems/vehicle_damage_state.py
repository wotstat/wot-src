import constants

class VehicleDamageState(object):
    MODEL_STATE_NAMES = (b'undamaged', b'destroyed', b'exploded')
    __healthToStateMap = {0: b'destruction', 
       (constants.SPECIAL_VEHICLE_HEALTH.AMMO_BAY_DESTROYED): b'ammoBayBurnOff', 
       (constants.SPECIAL_VEHICLE_HEALTH.TURRET_DETACHED): b'ammoBayExplosion', 
       (constants.SPECIAL_VEHICLE_HEALTH.FUEL_EXPLODED): b'fuelExplosion', 
       (constants.SPECIAL_VEHICLE_HEALTH.DESTR_BY_FALL_RAMMING): b'rammingDestruction'}

    @staticmethod
    def getState(health, isCrewActive, isUnderWater):
        if health > 0:
            if not isCrewActive:
                if isUnderWater:
                    return b'submersionDeath'
                return b'crewDeath'
            return b'alive'
        return VehicleDamageState.__healthToStateMap[health]

    __stateToModelEffectsMap = {b'ammoBayExplosion': (b'exploded', None), 
       b'ammoBayBurnOff': (b'destroyed', None), 
       b'fuelExplosion': (b'destroyed', b'fuelExplosion'), 
       b'destruction': (b'destroyed', b'destruction'), 
       b'crewDeath': (b'undamaged', b'crewDeath'), 
       b'rammingDestruction': (b'destroyed', b'rammingDestruction'), 
       b'submersionDeath': (b'undamaged', b'submersionDeath'), 
       b'alive': (b'undamaged', b'empty')}

    @staticmethod
    def getStateParams(state):
        return VehicleDamageState.__stateToModelEffectsMap[state]

    state = property((lambda self: self.__state))
    modelState = property((lambda self: self.__model))
    isCurrentModelDamaged = property((lambda self: VehicleDamageState.isDamagedModel(self.modelState)))
    isCurrentModelUndamaged = property((lambda self: VehicleDamageState.isUndamagedModel(self.modelState)))
    isCurrentModelExploded = property((lambda self: VehicleDamageState.isExplodedModel(self.modelState)))
    effect = property((lambda self: self.__effect))

    @staticmethod
    def isDamagedModel(model):
        return model != b'undamaged'

    @staticmethod
    def isUndamagedModel(model):
        return model == b'undamaged'

    @staticmethod
    def isExplodedModel(model):
        return model == b'exploded'

    def __init__(self):
        self.__state = None
        self.__model = None
        self.__effect = None
        return

    def update(self, health, isCrewActive, isUnderWater):
        self.__state = VehicleDamageState.getState(health, isCrewActive, isUnderWater)
        params = VehicleDamageState.getStateParams(self.__state)
        self.__model, self.__effect = params
        return
