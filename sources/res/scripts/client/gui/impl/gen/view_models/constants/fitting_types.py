from frameworks.wulf import ViewModel

class FittingTypes(ViewModel):
    __slots__ = ()
    OPTIONAL_DEVICE = b'optionalDevice'
    EQUIPMENT = b'equipment'
    SHELL = b'shell'
    VEHICLE = b'vehicle'
    MODULE = b'module'
    ORDER = b'order'
    BOOSTER = b'battleBooster'
    CREW_BOOKS = b'crewBooks'
    CUSTOMIZATION = b'customization'
    BATTLE_ABILITY = b'battleAbility'
    VEHICLE_GUN = b'vehicleGun'
    VEHICLE_DUAL_GUN = b'vehicleDualGun'
    VEHICLE_TURRET = b'vehicleTurret'
    VEHICLE_CHASSIS = b'vehicleChassis'
    VEHICLE_WHEELED_CHASSIS = b'vehicleWheeledChassis'
    VEHICLE_ENGINE = b'vehicleEngine'
    VEHICLE_RADIO = b'vehicleRadio'
    POST_PROGRESSION_MODIFICATION = b'postProgressionModification'
    POST_PROGRESSION_PAIR_MODIFICATION = b'postProgressionPairModification'

    def __init__(self, properties=0, commands=0):
        super(FittingTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(FittingTypes, self)._initialize()
        return
