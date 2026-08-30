from collections import namedtuple

class PcVSPlanSimpleEvent(object):
    CLIENT_ACTIVATION_EVENT = b'OnClientActivation'
    VEHICLE_START_MOVING = b'OnVehicleStartMoving'
    VEHICLE_STOP_MOVING = b'OnVehicleStopMoving'
    VEHICLE_START_FWD_MOVING = b'OnVehicleStartFwdMoving'
    VEHICLE_STOP_FWD_MOVING = b'OnVehicleStopFwdMoving'
    VEHICLE_SHOOT = b'OnVehicleShoot'
    VEHICLE_STUN = b'OnVehicleStun'
    VEHICLE_STUN_OFF = b'OnVehicleStunOff'
    VEHICLE_FIRE_STARTED = b'OnVehicleFireStarted'
    VEHICLE_FIRE_STOPPED = b'OnVehicleFireStopped'
    VEHICLE_EQUIPMENT_SWAP = b'OnVehicleEquipmentSwap'
    VEHICLE_BLOCK_DAMAGE = b'OnVehicleBlockDamage'
    VEHICLE_CHANGE_HEALTH = b'OnVehicleChangeHealth'
    VEHICLE_DEVICE_WAS_CRIT = b'OnVehicleDeviceWasCrit'
    VEHICLE_TANKMAN_WAS_CRIT = b'OnVehicleTankmanWasCrit'
    VEHICLE_TANKMAN_HEALED = b'OnVehicleTankmanHealed'
    VEHICLE_DEVICE_HEALED = b'OnVehicleDeviceHealed'
    VEHICLE_GUN_REALOAD_FINISHED = b'OnVehicleGunReloadFinished'
    ENEMY_DETECTED = b'OnEnemyDetected'
    VEHICLE_SIXTH_SENSE_ACTIVATE = b'OnVehicleSixthSenseActivate'
    VEHICLE_CHANGE_SHELLS_BY_CLIENT = b'OnVehicleChangeShellsByClient'
    VEHICLE_ON_TARGET_KILLED = b'OnVehicleOnTargetKilled'
    VEHICLE_ON_TARGET_CRIT = b'OnVehicleOnTargetCrit'
    ARENA_ON_BATTLE_START = b'OnArenaOnBattleStart'


OnInnerDeviceWasCrit = namedtuple(b'OnInnerDeviceWasCrit', b'modulesCount')
OnVehicleEquipmentActivated = namedtuple(b'OnVehicleEquipmentActivated', b'cooldownEquipmentIndex, cooldownEquipmentName')
OnVehicleTotalDamageDealtIncrease = namedtuple(b'OnVehicleTotalDamageDealtIncrease', b'totalDamageDealt')
OnVehicleAssistIncrease = namedtuple(b'OnVehicleAssistIncrease', b'assistPoints')
OnVehicleInRange = namedtuple(b'OnVehicleInRange', b'targetTeam, targetClass, enabled')
OnVehicleShotDamagedEnemyVehicle = namedtuple(b'OnVehicleShotDamagedEnemyVehicle', b'targetId')
OnVehicleRadioDistanceChange = namedtuple(b'OnVehicleRadioDistanceChange', b'radioDistance')
OnWitnessEnemyDamaged = namedtuple(b'OnWitnessEnemyDamaged', b'targetID')
OnTankmanStatusChanged = namedtuple(b'tankmanStatusChangedEffect', b'tmanIdx')
