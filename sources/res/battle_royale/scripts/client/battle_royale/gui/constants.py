import enum
ROYALE_POSTBATTLE_REWARDS_COUNT = 8

class BattleRoyaleEquipments(object):
    LARGE_REPAIRKIT = b'large_repairkit_battle_royale'
    AFTER_BURNING = b'afterburning_battle_royale'
    REGENERATION_KIT = b'regenerationKit'
    SELF_BUFF = b'selfBuff'
    TRAP_POINT = b'trappoint'
    REPAIR_POINT = b'repairpoint'
    HEAL_POINT = b'healPoint'
    SMOKE = b'smoke_battle_royale'
    BOMBER = b'arcade_bomber_with_own_damage_battle_royale'
    KAMIKAZE = b'spawn_kamikaze'
    BERSERKER = b'berserker'
    MINE_FIELD = b'arcade_minefield_battle_royale'
    SMOKE_WITH_DAMAGE = b'arcade_smoke_battle_royale_with_damage'
    ARCADE_SMOKE = b'arcade_smoke_battle_royale'
    FIRE_CIRCLE = b'fireCircle'
    CORRODING_SHOT = b'corrodingShot'
    CLING_BRANDER = b'clingBrander'
    ADAPTATION_HEALTH_RESTORE = b'adaptationHealthRestore'
    THUNDER_STRIKE = b'thunderStrike'
    SHOT_PASSION = b'shotPassion'


class BattleRoyaleComponents(object):
    SHOT_PASSION = b'shotPassionComponent'
    FIRE_CIRCLE = b'vehicleFireCircleEffectComponent'


BR_EQUIPMENTS_WITH_MESSAGES = frozenset([
 BattleRoyaleEquipments.TRAP_POINT, BattleRoyaleEquipments.AFTER_BURNING,
 BattleRoyaleEquipments.REGENERATION_KIT, BattleRoyaleEquipments.SELF_BUFF,
 BattleRoyaleEquipments.HEAL_POINT, BattleRoyaleEquipments.LARGE_REPAIRKIT,
 BattleRoyaleEquipments.BERSERKER, BattleRoyaleEquipments.MINE_FIELD,
 BattleRoyaleEquipments.REPAIR_POINT, BattleRoyaleEquipments.BOMBER,
 BattleRoyaleEquipments.KAMIKAZE, BattleRoyaleEquipments.SMOKE,
 BattleRoyaleEquipments.SMOKE_WITH_DAMAGE, BattleRoyaleEquipments.ARCADE_SMOKE,
 BattleRoyaleEquipments.FIRE_CIRCLE,
 BattleRoyaleEquipments.CORRODING_SHOT, BattleRoyaleEquipments.CLING_BRANDER,
 BattleRoyaleEquipments.ADAPTATION_HEALTH_RESTORE, BattleRoyaleEquipments.THUNDER_STRIKE,
 BattleRoyaleEquipments.SHOT_PASSION])

class AmmoTypes(object):
    BASIC_SHELL = b'bshell'
    PREMIUM_SHELL = b'pshell'
    ITEM = b'item'
    CHARGE1 = b'charge1'
    CHARGE2 = b'charge2'
    CHARGE3 = b'charge3'
    CHARGE4 = b'charge4'
    CHARGES = (
     CHARGE1, CHARGE2, CHARGE3, CHARGE4)
    SHELLS = (BASIC_SHELL, PREMIUM_SHELL)


class BattleRoyalePerfProblems(object):
    HIGH_RISK = 1
    MEDIUM_RISK = 2
    LOW_RISK = 3


class ParamTypes(object):
    DELTA = b'delta'
    CONST = b'const'
    SIMPLE = b'simple'


BR_QUEST_ID_PREFIX = b'token:br:title'
BATTLE_ROYALE_VEHICLES_INVOICE = b'battle_royale_vehicles_invoice'
BR_COIN = b'brcoin'
STP_COIN = b'stpcoin'
SUB_MODE_ID_KEY = b'SubModeId'

class BattleRoyaleSubMode(object):
    SOLO_MODE_ID = 1
    SOLO_DYNAMIC_MODE_ID = 2
    SQUAD_MODE_ID = 3
    ALL_RANGE = (
     SOLO_MODE_ID, SOLO_DYNAMIC_MODE_ID, SQUAD_MODE_ID)


class BattleRoyaleModeState(enum.Enum):
    Regular = 0
    CeasefireCurrentServer = 1
    CeasefireAllServers = 2
    Unavailable = 3
    Finished = 4
