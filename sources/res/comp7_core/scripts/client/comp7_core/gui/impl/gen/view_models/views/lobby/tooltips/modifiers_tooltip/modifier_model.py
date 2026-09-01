from enum import Enum
from frameworks.wulf import Array, ViewModel
from comp7_core.gui.impl.gen.view_models.views.lobby.tooltips.modifiers_tooltip.limit_model import LimitModel

class ModType(Enum):
    FAKE_MODIFIER = b'fakeModifier'
    VEHICLE_HEALTH = b'vehicleHealth'
    GRAVITY_FACTOR = b'gravityFactor'
    DISP_FACTOR_CHASSIS_MOVEMENT = b'dispFactorChassisMovement'
    DISP_FACTOR_CHASSIS_ROTATION = b'dispFactorChassisRotation'
    TURRET_ROTATION_SPEED = b'turretRotationSpeed'
    GUN_ROTATION_SPEED = b'gunRotationSpeed'
    RELOAD_TIME = b'reloadTime'
    TWIN_GUN_RELOAD_TIME = b'twinGunReloadTime'
    CLIP_INTERVAL = b'clipInterval'
    BURST_INTERVAL = b'burstInterval'
    AUTORELOAD_TIME = b'autoreloadTime'
    AIMING_TIME = b'aimingTime'
    SHOT_DISPERSION_RADIUS = b'shotDispersionRadius'
    DISP_FACTOR_TURRET_ROTATION = b'dispFactorTurretRotation'
    DISP_FACTOR_AFTER_SHOT = b'dispFactorAfterShot'
    DISP_FACTOR_WHILE_GUN_DAMAGED = b'dispFactorWhileGunDamaged'
    SHELL_GRAVITY = b'shellGravity'
    SHELL_SPEED = b'shellSpeed'
    DAMAGE_RANDOMIZATION = b'damageRandomization'
    PIERCING_POWER_RANDOMIZATION = b'piercingPowerRandomization'
    NORMALIZATION_ANGLE = b'normalizationAngle'
    RICOCHET_ANGLE = b'ricochetAngle'
    ENGINE_POWER = b'enginePower'
    ENGINE_FIRE_FACTOR = b'engineFireFactor'
    FW_MAX_SPEED = b'fwMaxSpeed'
    BK_MAX_SPEED = b'bkMaxSpeed'
    ROTATION_SPEED_ON_STILL = b'rotationSpeedOnStill'
    ROTATION_SPEED_ON_MOVE = b'rotationSpeedOnMove'
    INVISIBILITY_ON_STILL = b'invisibilityOnStill'
    INVISIBILITY_ON_MOVE = b'invisibilityOnMove'
    VISION_RADIUS = b'visionRadius'
    RADIO_DISTANCE = b'radioDistance'
    BATTLE_LENGTH = b'battleLength'
    VEHICLE_RAMMING_DAMAGE = b'vehicleRammingDamage'
    VEHICLE_PRESSURE_DAMAGE = b'vehiclePressureDamage'
    TURRET_RAMMING_DAMAGE = b'turretRammingDamage'
    TURRET_PRESSURE_DAMAGE = b'turretPressureDamage'
    ENV_HULL_DAMAGE = b'envHullDamage'
    ENV_CHASSIS_DAMAGE = b'envChassisDamage'
    ENV_TANKMAN_DAMAGE_CHANCE = b'envTankmanDamageChance'
    ENV_MODULE_DAMAGE_CHANCE = b'envModuleDamageChance'
    REPAIR_SPEED = b'repairSpeed'
    VISION_MIN_RADIUS = b'visionMinRadius'
    VISION_MAX_RADIUS = b'visionMaxRadius'
    VISION_TIME = b'visionTime'
    EQUIPMENT_COOLDOWN = b'equipmentCooldown'
    INVISIBILITY_FACTOR_AT_SHOT = b'invisibilityFactorAtShot'
    VEHICLE_AOI_RADIUS = b'vehicleAoIRadius'
    DEVICE_DAMAGE_FIRST = b'deviceDamageFirst'
    AMMO_BAY_HEALTH = b'ammoBayHealth'
    ENGINE_HEALTH = b'engineHealth'
    FUEL_TANK_HEALTH = b'fuelTankHealth'
    TURRET_ROTATOR_HEALTH = b'turretRotatorHealth'
    SURVEYING_DEVICE_HEALTH = b'surveyingDeviceHealth'
    CHASSIS_HEALTH = b'chassisHealth'
    GUN_HEALTH = b'gunHealth'


class ModPhysType(Enum):
    UNDEFINED = b'undefined'
    METERS_PER_SECOND = b'metersPerSecond'
    KILOMETERS_PER_HOUR = b'km_per_hour'
    RADIANS = b'radians'
    DEGREES = b'degrees'
    DEGREES_PER_SECOND = b'degrees_per_second'
    HIT_POINTS = b'hitPoints'
    MILLIMETERS = b'millimeters'
    METERS = b'meters'
    SECONDS = b'seconds'
    MINUTES = b'minutes'
    RADIANS_PER_SECOND = b'radians_per_second'
    METER_PER_SECOND_SQUARED = b'meter_per_second_squared'
    PROBABILITY = b'probability'
    DEVIATION = b'deviation'
    LOGIC = b'logic'
    HORSEPOWER = b'horsepower'


class ModUseType(Enum):
    UNDEFINED = b'undefined'
    VAL = b'val'
    MUL = b'mul'
    ADD = b'add'


class ModGameplayImpact(Enum):
    UNDEFINED = b'undefined'
    POSITIVE = b'positive'
    NEGATIVE = b'negative'


class ModifierModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ModifierModel, self).__init__(properties=properties, commands=commands)
        return

    def getModificationType(self):
        return ModType(self._getString(0))

    def setModificationType(self, value):
        self._setString(0, value.value)
        return

    def getResName(self):
        return self._getString(1)

    def setResName(self, value):
        self._setString(1, value)
        return

    def getValue(self):
        return self._getReal(2)

    def setValue(self, value):
        self._setReal(2, value)
        return

    def getPhysicalType(self):
        return ModPhysType(self._getString(3))

    def setPhysicalType(self, value):
        self._setString(3, value.value)
        return

    def getUseType(self):
        return ModUseType(self._getString(4))

    def setUseType(self, value):
        self._setString(4, value.value)
        return

    def getGameplayImpact(self):
        return ModGameplayImpact(self._getString(5))

    def setGameplayImpact(self, value):
        self._setString(5, value.value)
        return

    def getLimits(self):
        return self._getArray(6)

    def setLimits(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getLimitsType():
        return LimitModel

    def _initialize(self):
        super(ModifierModel, self)._initialize()
        self._addStringProperty(b'modificationType')
        self._addStringProperty(b'resName', b'')
        self._addRealProperty(b'value', 0.0)
        self._addStringProperty(b'physicalType')
        self._addStringProperty(b'useType')
        self._addStringProperty(b'gameplayImpact')
        self._addArrayProperty(b'limits', Array())
        return
