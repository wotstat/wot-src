import weakref
from VSPlanEvents import OnVehicleEquipmentActivated, OnInnerDeviceWasCrit, OnVehicleTotalDamageDealtIncrease, OnVehicleAssistIncrease, OnVehicleInRange, OnVehicleShotDamagedEnemyVehicle, OnVehicleRadioDistanceChange, OnWitnessEnemyDamaged, OnTankmanStatusChanged
from items.components.perks_constants import PerkState, CrewPerkLevelCollectors
from visual_script.slot_types import SLOT_TYPE
from visual_script.context import VScriptContext, vse_get_property, vse_func_call, vse_forward_event, vse_context_effect_forward_event
from visual_script.type import VScriptEnum
from visual_script.misc import ASPECT

class PerkNotifyState(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return b'state'

    @classmethod
    def vs_enum(cls):
        return PerkState


class CrewPerkLevelCollector(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return b'levelCollector'

    @classmethod
    def vs_enum(cls):
        return CrewPerkLevelCollectors

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.SERVER]


class PerkContext(VScriptContext):
    OnVehicleStartMoving = vse_forward_event(b'OnVehicleStartMoving', (), display_name=b'OnVehicleStartMoving', description=b'On vehicle start moving')
    OnVehicleStopMoving = vse_forward_event(b'OnVehicleStopMoving', (), display_name=b'OnVehicleStopMoving', description=b'On vehicle stop moving')
    OnVehicleStartFwdMoving = vse_forward_event(b'OnVehicleStartFwdMoving', (), display_name=b'OnVehicleStartFwdMoving', description=b'On vehicle start forward moving')
    OnVehicleStopFwdMoving = vse_forward_event(b'OnVehicleStopFwdMoving', (), display_name=b'OnVehicleStopFwdMoving', description=b'On vehicle stop forward moving')
    OnVehicleShoot = vse_forward_event(b'OnVehicleShoot', (), display_name=b'OnVehicleShoot', description=b'On vehicle shoot')
    OnVehicleStun = vse_forward_event(b'OnVehicleStun', (), display_name=b'OnVehicleStun', description=b'On vehicle stun')
    OnVehicleStunOff = vse_forward_event(b'OnVehicleStunOff', (), display_name=b'OnVehicleStunOff', description=b'On vehicle stun off')
    OnVehicleFireStarted = vse_forward_event(b'OnVehicleFireStarted', (), display_name=b'OnVehicleFireStarted', description=b'On vehicle fire started')
    OnVehicleFireStopped = vse_forward_event(b'OnVehicleFireStopped', (), display_name=b'OnVehicleFireStopped', description=b'On vehicle fire stopped')
    OnVehicleEquipmentSwap = vse_forward_event(b'OnVehicleEquipmentSwap', (), display_name=b'OnVehicleEquipmentSwap', description=b'On vehicle equipment swap')
    OnVehicleBlockDamage = vse_forward_event(b'OnVehicleBlockDamage', (), display_name=b'OnVehicleBlockDamage', description=b'On vehicle block damage')
    OnVehicleChangeHealth = vse_forward_event(b'OnVehicleChangeHealth', (), display_name=b'OnVehicleChangeHealth', description=b'On vehicle change health')
    OnVehicleDeviceWasCrit = vse_forward_event(b'OnVehicleDeviceWasCrit', (), display_name=b'OnVehicleDeviceWasCrit', description=b'On vehicle device was crit')
    OnVehicleTankmanWasCrit = vse_forward_event(b'OnVehicleTankmanWasCrit', (), display_name=b'OnVehicleTankmanWasCrit', description=b'On vehicle tankman was crit')
    OnVehicleTankmanHealed = vse_forward_event(b'OnVehicleTankmanHealed', (), display_name=b'OnVehicleTankmanHealed', description=b'On vehicle tankman healed')
    OnVehicleDeviceHealed = vse_forward_event(b'OnVehicleDeviceHealed', (), display_name=b'OnVehicleDeviceHealed', description=b'On vehicle device healed')
    OnVehicleGunReloadFinished = vse_forward_event(b'OnVehicleGunReloadFinished', (), display_name=b'OnVehicleGunReloadFinished', description=b'On vehicle gun reload finished')
    OnEnemyDetected = vse_forward_event(b'OnEnemyDetected', (), display_name=b'OnEnemyDetected', description=b'On enemy detected')
    OnVehicleSixthSenseActivate = vse_forward_event(b'OnVehicleSixthSenseActivate', (), display_name=b'OnVehicleSixthSenseActivate', description=b'On vehicle sixth sense activate')
    OnVehicleChangeShellsByClient = vse_forward_event(b'OnVehicleChangeShellsByClient', (), display_name=b'OnVehicleChangeShellsByClient', description=b'On vehicle change shells by client')
    OnVehicleOnTargetKilled = vse_forward_event(b'OnVehicleOnTargetKilled', (), display_name=b'OnVehicleOnTargetKilled', description=b'On vehicle on target killed')
    OnVehicleOnTargetCrit = vse_forward_event(b'OnVehicleOnTargetCrit', (), display_name=b'OnVehicleOnTargetCrit', description=b'On vehicle on target crit')
    OnArenaOnBattleStart = vse_forward_event(b'OnArenaOnBattleStart', (), display_name=b'OnArenaOnBattleStart', description=b'On battle start')
    OnInnerDeviceWasCrit = vse_forward_event(OnInnerDeviceWasCrit.__name__, zip(OnInnerDeviceWasCrit._fields, (SLOT_TYPE.INT,)), display_name=b'OnInnerDeviceWasCrit', description=b'On inner device was crit')
    OnVehicleEquipmentActivated = vse_forward_event(OnVehicleEquipmentActivated.__name__, zip(OnVehicleEquipmentActivated._fields, (SLOT_TYPE.INT, SLOT_TYPE.STR)), display_name=b'OnEquipmentActivated', description=b'On equipment activated')
    OnVehicleTotalDamageDealtIncrease = vse_forward_event(OnVehicleTotalDamageDealtIncrease.__name__, zip(OnVehicleTotalDamageDealtIncrease._fields, (SLOT_TYPE.INT,)), display_name=b'OnVehicleTotalDamageDealtIncrease', description=b'On vehicle total damage dealt increase')
    OnVehicleAssistIncrease = vse_forward_event(OnVehicleAssistIncrease.__name__, zip(OnVehicleAssistIncrease._fields, (SLOT_TYPE.INT,)), display_name=b'OnVehicleAssistIncrease', description=b'On vehicle assist increase')
    OnVehicleInRange = vse_forward_event(OnVehicleInRange.__name__, zip(OnVehicleInRange._fields, (SLOT_TYPE.INT, SLOT_TYPE.STR, SLOT_TYPE.BOOL)), display_name=b'OnVehicleInRange', description=b'On vehicle in range')
    OnVehicleShotDamagedEnemyVehicle = vse_forward_event(OnVehicleShotDamagedEnemyVehicle.__name__, zip(OnVehicleShotDamagedEnemyVehicle._fields, (SLOT_TYPE.INT,)), display_name=b'OnVehicleShotDamagedEnemyVehicle', description=b'On vehicle shot damaged enemy vehicle')
    OnWitnessEnemyDamaged = vse_forward_event(OnWitnessEnemyDamaged.__name__, zip(OnWitnessEnemyDamaged._fields, (SLOT_TYPE.INT,)), display_name=b'OnWitnessEnemyDamaged', description=b'Vehicle has been damage in our vision')
    OnVehicleRadioDistanceChange = vse_forward_event(OnVehicleRadioDistanceChange.__name__, zip(OnVehicleRadioDistanceChange._fields, (SLOT_TYPE.FLOAT,)), display_name=b'OnVehicleRadioDistanceChange', description=b'On vehicle radio distance change', display_group=b'Aura')
    OnPerkRestarted = vse_forward_event(b'OnPerkRestarted', (), display_name=b'onPerkRestarted', description=b'On perk restarted', display_group=b'Perk')

    def __init__(self, aspectImplClass, perksControllerWeakRef, perkID, perkLevel, scopeID):
        super(PerkContext, self).__init__(aspectImplClass.ASPECT)
        self._aspectImpl = aspectImplClass(perksControllerWeakRef, perkID, perkLevel, scopeID)
        return

    @property
    def perkID(self):
        return self._aspectImpl.perkID

    @property
    def perkLevel(self):
        return self._aspectImpl.perkLevel

    @property
    def scopeID(self):
        return self._aspectImpl.scopeID

    @property
    def vehicleID(self):
        return self._aspectImpl.vehicleID

    @vse_get_property(SLOT_TYPE.PERK, display_name=b'Self', description=b'Perk reference', display_group=b'Perk')
    def getSelf(self):
        return weakref.proxy(self)

    @vse_get_property(SLOT_TYPE.VEHICLE, display_name=b'Vehicle', description=b'Vehicle entity', display_group=b'Perk')
    def getVehicle(self):
        return self._aspectImpl.vehicle

    @vse_get_property(SLOT_TYPE.INT, display_name=b'PerkID', description=b'Perk ID', display_group=b'Perk/Support')
    def getPerkID(self):
        return self._aspectImpl.perkID

    @vse_get_property(SLOT_TYPE.INT, display_name=b'Level', description=b'Perk level', display_group=b'Perk/Support')
    def getLevel(self):
        return self._aspectImpl.perkLevel

    @vse_get_property(SLOT_TYPE.INT, display_name=b'VehicleID', description=b'Vehicle ID', display_group=b'Perk/Support')
    def getVehicleID(self):
        return self._aspectImpl.vehicleID

    @vse_func_call(None, (
     SLOT_TYPE.STR, SLOT_TYPE.FLOAT), display_name=b'AddFactorModifier', description=b'Adds a modifier for a specified factor', display_group=b'Perk')
    def addFactorModifier(self, factor, value):
        self._aspectImpl.addFactorModifier(factor, value)
        return

    @vse_func_call(None, (
     SLOT_TYPE.STR, SLOT_TYPE.FLOAT), display_name=b'AddAuraModifier', description=b'Adds a modifier to aura scope', display_group=b'Aura')
    def addAuraModifier(self, factor, value):
        self._aspectImpl.addAuraModifier(factor, value)
        return

    @vse_func_call(None, (), display_name=b'DropAuraModifiers', description=b'Reset aura modifiers', display_group=b'Aura')
    def dropAuraModifiers(self):
        self._aspectImpl.dropAuraModifiers()
        return

    @vse_func_call(None, (
     SLOT_TYPE.INT, SLOT_TYPE.FLOAT, SLOT_TYPE.FLOAT), display_name=b'StartAura', descrption=b'Starts aura loop', display_group=b'Aura')
    def startAura(self, targetTeam, startRadius, interval):
        self._aspectImpl.startAura(targetTeam, startRadius, interval)
        return

    @vse_func_call(None, (
     SLOT_TYPE.FLOAT,), display_name=b'SetAuraRange', description=b'Set range for aura', display_group=b'Aura')
    def setAuraRange(self, radius):
        self._aspectImpl.setAuraRange(radius)
        return

    @vse_func_call(None, (
     SLOT_TYPE.STR, SLOT_TYPE.INT), display_name=b'RemoveFactorModifiers', description=b'Remove modifier by count', display_group=b'Perk')
    def removeFactorModifiers(self, factor, numMods):
        self._aspectImpl.removeFactorModifiers(factor, numMods)
        return

    @vse_func_call(None, (), display_name=b'DropAllPerkModifiers', description=b'Reset all perk modifiers', display_group=b'Perk')
    def dropAllPerkModifiers(self):
        self._aspectImpl.dropAllPerkModifiers()
        return

    def setPerkLevel(self, level):
        self._aspectImpl.perkLevel = level
        return

    @vse_func_call(None, (
     PerkNotifyState.slotType(), SLOT_TYPE.FLOAT), display_name=b'NotifyOnClient', description=b'Notify client on perk state change to perks panel', display_group=b'Perk')
    def notifyOnClient(self, state, lifeTime):
        self._aspectImpl.notifyOnClient(state, lifeTime)
        return

    @vse_func_call(None, (), display_name=b'NotifyOnClientRibbon', description=b'Notify client on perk to ribbon panel', display_group=b'Perk')
    def notifyOnClientRibbon(self):
        self._aspectImpl.notifyOnClientRibbon()
        return


class CrewContext(PerkContext):

    @vse_context_effect_forward_event(OnTankmanStatusChanged.__name__, zip(OnTankmanStatusChanged._fields, (SLOT_TYPE.INT,)), display_name=b'OnTankmanStatusChanged', description=b'Tankman has been deactivated or healed. This event should only be used to track perk activity and not for internal perk logic.', display_group=b'Crew')
    def tankmanStatusChangedEffect(self, *args):
        self._aspectImpl.tankmanStatusChanged(*args)
        return

    @vse_get_property(SLOT_TYPE.BOOL, display_name=b'IsActive', description=b'is the current perk active (tankman activity determined)', display_group=b'Crew')
    def getIsActive(self):
        return self._aspectImpl.isActive

    @vse_get_property(SLOT_TYPE.BOOL, display_name=b'NeedTankmanUpdate', description=b'returns True only if something related to tankmen, which enabled this perk, has changed', display_group=b'Crew')
    def needTankmanUpdate(self):
        return self._aspectImpl.needTankmanUpdate

    @vse_func_call(None, (
     SLOT_TYPE.FLOAT,), display_name=b'SetAmmoChangeFactorForVehicle', description=b'Set ammo change factor for vehicle (information only, does not change TTC)', display_group=b'Perk_403')
    def setAmmoChangeFactorForVehicle(self, factor):
        self._aspectImpl.setAmmoChangeFactorForVehicle(factor)
        return

    @vse_func_call(None, (
     CrewPerkLevelCollector.slotType(),), display_name=b'SetLevelCollector', description=b'Update level of crew based on selected collector', display_group=b'Crew')
    def setLevelCollector(self, levelCollector):
        self._aspectImpl.setLevelCollector(levelCollector)
        return

    def __init__(self, aspectImplClass, perksControllerWeakRef, perkID, perkLevel, scopeID, skillData):
        super(PerkContext, self).__init__(aspectImplClass.ASPECT)
        self._aspectImpl = aspectImplClass(perksControllerWeakRef, perkID, perkLevel, scopeID, skillData)
        return
