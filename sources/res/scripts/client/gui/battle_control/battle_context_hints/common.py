from shared_utils import CONST_CONTAINER

class HintId(CONST_CONTAINER):
    PLAYER_VEHICLE_OBSERVED = b'PlayerVehicleObserved'
    KILLED_WHILE_OBSERVED = b'KilledWhileObserved'
    IN_SAFETY_WHILE_NOT_OBSERVED = b'InSafetyWhileNotObserved'
    ENGINE_DAMAGE_REPAIR_KIT = b'EngineDamageRepairKit'
    AMMUNITION_DAMAGE_REPAIR_KIT = b'AmmunitionDamageRepairKit'
    FUELTANK_DAMAGE_REPAIR_KIT = b'FueltankDamageRepairKit'
    GUN_ROTATOR_DAMAGE_REPAIR_KIT = b'GunRotatorDamageRepairKit'
    GUN_DAMAGE_REPAIR_KIT = b'GunDamageRepairKit'
    AMMUNITION_CRIT = b'AmmunitionCrit'
    FUELTANK_CRIT = b'FueltankCrit'
    GUN_ROTATOR_DESTROY_REPAIR_KIT = b'GunRotatorDestroyRepairKit'
    ENGINE_DESTROY_REPAIR_KIT = b'EngineDestroyRepairKit'
    GUN_DESTROY_REPAIR_KIT = b'GunDestroyRepairKit'
    TRACK_DESTROY_REPAIR_KIT = b'TrackDestroyRepairKit'
    MODULE_DAMAGE = b'ModuleDamage'
    COMMANDER_DAMAGE_MED_KIT = b'CommanderDamageMedKit'
    DRIVER_DAMAGE_MED_KIT = b'DriverDamageMedKit'
    GUNNER_DAMAGE_MED_KIT = b'GunnerDamageMedKit'
    LOADER_DAMAGE_MED_KIT = b'LoaderDamageMedKit'
    RADIOMAN_DAMAGE_MED_KIT = b'RadiomanDamageMedKit'


class ContextHintsSoundEvents(CONST_CONTAINER):
    PLAYER_VEHICLE_OBSERVED = b'vo_contextHints_04_00'
    KILLED_WHILE_OBSERVED = b'vo_contextHints_04_01'
    IN_SAFETY_WHILE_NOT_OBSERVED = b'vo_contextHints_04_02'
    MODULE_REPAIR_KIT = b'vo_contextHints_04_03'
    AMMUNITION_CRIT = b'vo_contextHints_04_08'
    FUELTANK_CRIT = b'vo_contextHints_04_09'
    MODULE_DAMAGE = b'vo_contextHints_04_14'
    TANKMAN_DAMAGE = b'vo_contextHints_04_15'
