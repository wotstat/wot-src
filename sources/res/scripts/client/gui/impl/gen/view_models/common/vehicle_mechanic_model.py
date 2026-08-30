from enum import Enum
from frameworks.wulf import ViewModel

class MechanicsEnum(Enum):
    UNKNOWN = b'unknown'
    MAGAZINE_GUN = b'magazineGun'
    AUTO_LOADER_GUN = b'autoLoaderGun'
    AUTO_LOADER_GUN_BOOST = b'autoLoaderGunBoost'
    DAMAGE_MUTABLE = b'damageMutable'
    DUAL_GUN = b'dualGun'
    HYDRAULIC_CHASSIS = b'hydraulicChassis'
    TRACK_WITHIN_TRACK = b'trackWithinTrack'
    SIEGE_MODE = b'siegeMode'
    STUN = b'stun'
    HYDRAULIC_WHEELED_CHASSIS = b'hydraulicWheeledChassis'
    TURBOSHAFT_ENGINE = b'turboshaftEngine'
    ROCKET_ACCELERATION = b'rocketAcceleration'
    TARGET_DESIGNATOR = b'targetDesignator'
    DUAL_ACCURACY = b'dualAccuracy'
    AUTO_SHOOT_GUN = b'autoShootGun'
    TWIN_GUN = b'twinGun'
    IMPROVED_RAMMING = b'improvedRamming'
    CONCENTRATION_MODE = b'concentrationMode'
    BATTLE_FURY = b'battleFury'
    EXTRA_SHOT_CLIP = b'extraShotClip'
    POWER_MODE = b'powerMode'
    ACCURACY_STACKS = b'accuracyStacks'
    SUPPORT_WEAPON = b'supportWeapon'
    PILLBOX_SIEGE_MODE = b'pillboxSiegeMode'
    CHARGEABLE_BURST = b'chargeableBurst'
    RECHARGEABLE_NITRO = b'rechargeableNitro'
    CHARGE_SHOT = b'chargeShot'
    OVERHEAT_STACKS = b'overheatStacks'
    STANCE_DANCE = b'stanceDance'
    STATIONARY_RELOAD = b'stationaryReload'
    OVERHEAT_GUN = b'overheatGun'
    HEATING_ZONES_GUN = b'heatingZonesGun'
    LOW_CHARGE_SHOT = b'lowChargeShot'
    STAGED_JET_BOOSTERS = b'stagedJetBoosters'
    PROPELLANT_GUN = b'propellantAfterburnerGun'
    WHEELED_DASH = b'wheeledDash'


class MechanicsRank(Enum):
    UNDEFINED = b'undefined'
    SILVER = b'silver'
    GOLD = b'gold'


class VehicleMechanicModel(ViewModel):
    __slots__ = ()
    MIN_SPECIAL_PRIORITY = 1

    def __init__(self, properties=4, commands=0):
        super(VehicleMechanicModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return MechanicsEnum(self._getString(0))

    def setName(self, value):
        self._setString(0, value.value)
        return

    def getPriority(self):
        return self._getNumber(1)

    def setPriority(self, value):
        self._setNumber(1, value)
        return

    def getRank(self):
        return MechanicsRank(self._getString(2))

    def setRank(self, value):
        self._setString(2, value.value)
        return

    def getHasVideo(self):
        return self._getBool(3)

    def setHasVideo(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(VehicleMechanicModel, self)._initialize()
        self._addStringProperty(b'name')
        self._addNumberProperty(b'priority', 0)
        self._addStringProperty(b'rank', MechanicsRank.UNDEFINED.value)
        self._addBoolProperty(b'hasVideo', False)
        return
