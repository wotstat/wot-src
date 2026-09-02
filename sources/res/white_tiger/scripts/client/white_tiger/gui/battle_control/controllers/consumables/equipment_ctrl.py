import Event
from gui.battle_control.controllers.consumables.equipment_ctrl import EquipmentsReplayPlayer, EquipmentsController
from gui.shared.utils.MethodsRules import MethodsRules
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from constants import ARENA_PERIOD
from white_tiger.gui.battle_control.controllers.consumables.equipment_items import WTRepairKit, WTMedKitItem, WTPassiveHeal, WTUnionStrength, WTInvisibilityModA, WTInvisibilityModB, WTHyperionModA, WTHyperionModB, WTTeleportModA, WTTeleportModB, WTStunArea, WTChargedShot, WTBarrier, WTNitro, WTDamageShield, WTExplosiveShot, WTImpulseModA, WTVampirism, WTDecreaseReloadTime, WTGroupRepair, WTCloneItem, WTMissile, WTSmokeScreen, WTPlasmaRetention, WTStunAreaModA, WTIncreaseDamage, WTExtractorShot, WTExplosiveDamageShield, WTDome
_EQ_TYPES = {b'wt_repairkit': WTRepairKit, 
   b'wt_medkit': WTMedKitItem, 
   b'wt_passive_heal': WTPassiveHeal, 
   b'wt_union_strength': WTUnionStrength, 
   b'wt_invisibility_mod_a': WTInvisibilityModA, 
   b'wt_invisibility_mod_b': WTInvisibilityModB, 
   b'wt_hyperion_mod_a': WTHyperionModA, 
   b'wt_hyperion_mod_b': WTHyperionModB, 
   b'wt_teleport_mod_a': WTTeleportModA, 
   b'wt_teleport_mod_b': WTTeleportModB, 
   b'wt_stun_area': WTStunArea, 
   b'wt_charged_shot': WTChargedShot, 
   b'wt_nitro': WTNitro, 
   b'wt_barrier': WTBarrier, 
   b'wt_damage_shield': WTDamageShield, 
   b'wt_explosive_shot': WTExplosiveShot, 
   b'wt_impulse_mod_a': WTImpulseModA, 
   b'wt_vampirism': WTVampirism, 
   b'wt_decrease_reload_time': WTDecreaseReloadTime, 
   b'wt_group_repair': WTGroupRepair, 
   b'wt_clone': WTCloneItem, 
   b'wt_missile': WTMissile, 
   b'wt_smoke_screen': WTSmokeScreen, 
   b'wt_plasma_retention': WTPlasmaRetention, 
   b'wt_stun_area_mod_a': WTStunAreaModA, 
   b'wt_increase_damage': WTIncreaseDamage, 
   b'wt_extractor_shot': WTExtractorShot, 
   b'wt_explosive_damage_shield': WTExplosiveDamageShield, 
   b'wt_dome': WTDome}

class WhiteTigerEquipmentController(EquipmentsController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, setup):
        super(WhiteTigerEquipmentController, self).__init__(setup)
        self.onDebuffEquipmentChanged = Event.Event(self._eManager)
        return

    @classmethod
    def createItem(cls, descriptor, quantity, stage, timeRemaining, totalTime):
        clazz = _EQ_TYPES.get(descriptor.name)
        if not clazz:
            return None
        else:
            item = clazz(descriptor, quantity, stage, timeRemaining, totalTime, descriptor.tags)
            return item

    @MethodsRules.delayable(b'notifyPlayerVehicleSet')
    def setEquipment(self, intCD, quantity, stage, timeRemaining, totalTime):
        super(WhiteTigerEquipmentController, self).setEquipment(intCD, quantity, stage, timeRemaining, totalTime)
        item = self.getEquipment(intCD)
        if item is None:
            return
        else:
            return

    def getEquipment(self, intCD):
        periodCtrl = self.__sessionProvider.shared.arenaPeriod
        if periodCtrl and periodCtrl.getPeriod() <= ARENA_PERIOD.WAITING:
            return
        else:
            try:
                item = self._equipments[intCD]
            except KeyError:
                item = None

            return item

    def getItemIDx(self, intCD):
        return self._order.index(intCD) + 1


class WhiteTigerReplayConsumablesPanelMeta(EquipmentsReplayPlayer, WhiteTigerEquipmentController):
    pass
