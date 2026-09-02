from items.attributes_helpers import CommonFactorsHelper, MODIFIER_TYPE
ALLOWED_DYNAMIC_ATTRS = [
 b'additiveShotDispersionFactor',
 b'armorSpallsDamageFactor',
 b'deviceDamageFactor',
 b'armorDamageFactor',
 b'spallsDeviceDamageFactor',
 b'chassis/shotDispersionFactors/movement',
 b'chassis/shotDispersionFactors/rotation',
 b'circularVisionRadius',
 b'crewChanceToHitFactor',
 b'crewLevelIncrease',
 b'crewRolesFactor',
 (
  b'damageFactor', MODIFIER_TYPE.MUL),
 b'deathZones/sensitivityFactor',
 b'engine/fireStartingChance',
 b'engine/power',
 b'enginePowerFactor',
 b'gun/aimingTime',
 b'gun/changeShell/reloadFactor',
 b'gun/piercing',
 b'gun/maxDistanceFactor',
 b'gun/shellSpeedFactor',
 b'gun/reloadTime',
 b'gun/rotationSpeed',
 (
  b'gun/shotDispersionFactors/afterShot', MODIFIER_TYPE.MUL),
 b'gun/shotDispersionFactors/turretRotation',
 b'gun/temperature/heatingFactor',
 b'healthBurnPerSecLossFraction',
 b'healthFactor',
 b'multShotDispersionFactor',
 b'radio/distance',
 b'ramming',
 b'repairSpeed',
 b'repeatedStunDurationFactor',
 b'stunResistanceDuration',
 b'stunResistanceEffect',
 b'turret/rotationSpeed',
 b'vehicle/maxSpeed',
 b'vehicle/maxSpeed/forward',
 b'vehicle/maxSpeed/backward',
 b'vehicle/rotationSpeed',
 b'vehicle/bkMaxSpeedBonus',
 b'vehicle/fwMaxSpeedBonus',
 b'moduleDamageFactor',
 b'engineAndFuelTanksDamageFactor',
 b'gun/chargeTimeBonus',
 b'gun/reloadLockTimeBonus',
 b'gun/loadShellIntoDualGunBonus']

class DynamicFactorsHelper(CommonFactorsHelper):
    ALLOWED_ATTRS = ALLOWED_DYNAMIC_ATTRS
    PREFIX = b'dynAttrs/'


attributes_dynamic_factory = DynamicFactorsHelper()
