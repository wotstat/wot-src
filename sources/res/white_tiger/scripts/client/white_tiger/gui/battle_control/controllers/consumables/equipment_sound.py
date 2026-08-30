import SoundGroups
from items import vehicles
from cgf_components import sound_helpers
from constants import EQUIPMENT_STAGES
from gui.battle_control.controllers.consumables.equipment_ctrl import EquipmentSound
_INVISIBILITY_MOD_A_START_VO = b'wt_vo_ability_invisibility_a_in'
_INVISIBILITY_MOD_A_STOP_VO = b'wt_vo_ability_invisibility_a_out'
_INVISIBILITY_MOD_B_START_VO = b'wt_vo_ability_invisibility_b_in'
_ABILITIES_VOICEOVERS = {b'wt_hyperion_mod_b': {(EQUIPMENT_STAGES.READY): b'wt_vo_ability_bells_ready'}, 
   b'wt_extractor_shot': {(EQUIPMENT_STAGES.ACTIVE): b'wt_vo_ability_energy_steal_work'}, 
   b'wt_stun_area': {(EQUIPMENT_STAGES.COOLDOWN): b'wt_vo_ability_emp_web_work'}, 
   b'wt_invisibility_mod_a': {(EQUIPMENT_STAGES.ACTIVE): _INVISIBILITY_MOD_A_START_VO, 
                              (EQUIPMENT_STAGES.COOLDOWN): _INVISIBILITY_MOD_A_STOP_VO}, 
   b'wt_invisibility_mod_b': {(EQUIPMENT_STAGES.ACTIVE): _INVISIBILITY_MOD_B_START_VO}}
_DECREASE_RELOAD_SOUND_BY_LEVEL = [
 17, 
 18, 
 19, 
 20, 
 21, 
 22]
_INCREASE_DAMAGE_SOUND_BY_LEVEL = [
 23, 
 24, 
 25, 
 26, 
 27, 
 28]
_INCREASE_DAMAGE_SOUND_3D_BY_LEVEL = {1: b'ev_wt_ability_increase_damage_shot_01', 
   2: b'ev_wt_ability_increase_damage_shot_02', 
   3: b'ev_wt_ability_increase_damage_shot_03', 
   4: b'ev_wt_ability_increase_damage_shot_04', 
   5: b'ev_wt_ability_increase_damage_shot_05'}
_EXPLOSIVE_SHIELD_SOUNDS = {b'Start': b'ev_wt_ability_explosive_shield_start', 
   b'Hit': b'ev_wt_ability_explosive_shield_hit', 
   b'End': b'ev_wt_ability_explosive_shield_stop', 
   b'Explode': b'ev_wt_ability_explosive_shield_explode'}
_WT_STUN_AREA_HIT_VO = b'wt_hunters_vo_ability_emp_web_debuff'
_WT_VAMPIRISM_REPAIR = b'ev_wt_gameplay_full_repair_impulse'
_WT_STUN_SHOT_PC = b'ev_white_tiger_gameplay_wt_stun_shot_pc'
_WT_STUN_SHOT_NPC = b'ev_white_tiger_gameplay_wt_stun_shot_npc'
_WT_ENHANCED_SHOT_ON_SHOT_PC = b'ev_wt_ability_enhanced_shot_PC'
_WT_ENHANCED_SHOT_ON_SHOT_NPC = b'ev_wt_ability_enhanced_shot_NPC'
_WT_DOME_ENTER = b'ev_wt_ability_dome_in'
_WT_DOME_EXIT = b'ev_wt_ability_dome_out'
_WT_HYPERION_CANCELED_VO = b'wt23_both_vo_hyperion_canceled'
_WT_HYPERION_MOD_B_CHARGING = b'ev_wt_gameplay_bells_charging'
_WT_HYPERION_MOD_B_SHOOTING = b'ev_wt_gameplay_bells_blast_main'
_WT_HYPERION_MOD_B_INTERRUPTION = b'ev_wt_gameplay_bells_start_up_interrupted'
_WT_INVISIBILITY_MOD_A_ENTRANCE = b'ev_wt_ability_invisibility_a_in_PC'
_WT_INVISIBILITY_MOD_A_ESCAPE = b'ev_wt_ability_invisibility_a_out_PC'
_WT_INVISIBILITY_MOD_B = b'ev_wt_ability_invisibility_b'

class WtEquipmentSound(EquipmentSound):

    @staticmethod
    def playPressed(item, result):
        equipment = vehicles.g_cache.equipments()[item.getEquipmentID()]
        if equipment is not None:
            sound = equipment.soundPressedReady if result else equipment.soundPressedNotReady
            if sound is not None:
                SoundGroups.g_instance.playSound2D(sound)
        return

    @staticmethod
    def playVoiceOver(voiceOver):
        sound_helpers.playNotification(voiceOver)
        return

    @staticmethod
    def playSound3D(soundEvent, position):
        SoundGroups.g_instance.playSoundPos(soundEvent, position)
        return

    @staticmethod
    def playSound2D(sound):
        SoundGroups.g_instance.playSound2D(sound)
        return


def playAbilityVoiceOver(item):
    ability = _ABILITIES_VOICEOVERS.get(item.getDescriptor().name, None)
    if ability:
        vo = ability.get(item.getStage(), None)
        WtEquipmentSound.playVoiceOver(vo)
    return


def playStunAreaHunterVO():
    WtEquipmentSound.playVoiceOver(_WT_STUN_AREA_HIT_VO)
    return


def playVampirismRepair(position):
    WtEquipmentSound.playSound3D(_WT_VAMPIRISM_REPAIR, position)
    return


def playExtractorShot(isPC, position):
    sound = _WT_STUN_SHOT_PC if isPC else _WT_STUN_SHOT_NPC
    WtEquipmentSound.playSound3D(sound, position)
    return


def playStunAreaShot(isPC, position):
    playExtractorShot(isPC, position)
    return


def playEnhancedShotOnShotSound(position, isPC):
    WtEquipmentSound.playSound3D(_WT_ENHANCED_SHOT_ON_SHOT_PC if isPC else _WT_ENHANCED_SHOT_ON_SHOT_NPC, position)
    return


def playDecreaseReloadByLevel(level):
    sound = _DECREASE_RELOAD_SOUND_BY_LEVEL[level]
    WtEquipmentSound.playSound2D(sound)
    return


def playIncreaseDamageByLevel(level, position):
    sound = _INCREASE_DAMAGE_SOUND_BY_LEVEL[level]
    WtEquipmentSound.playSound2D(sound)
    sound = _INCREASE_DAMAGE_SOUND_3D_BY_LEVEL.get(level)
    if sound:
        WtEquipmentSound.playSound3D(sound, position)
    return


def playExplosiveShieldSound(layerName, vehicle):
    event = _EXPLOSIVE_SHIELD_SOUNDS.get(layerName)
    if event:
        sound_helpers.playVehicleSound(event, vehicle)
    return


def playDomeSound(isEntered):
    sound = _WT_DOME_ENTER if isEntered else _WT_DOME_EXIT
    WtEquipmentSound.playSound2D(sound)
    return


def playHyperionModBCharging(position):
    WtEquipmentSound.playSound3D(_WT_HYPERION_MOD_B_CHARGING, position)
    return


def playHyperionModBShooting(position):
    WtEquipmentSound.playSound3D(_WT_HYPERION_MOD_B_SHOOTING, position)
    return


def playHyperionModBInterruption(position):
    WtEquipmentSound.playVoiceOver(_WT_HYPERION_CANCELED_VO)
    WtEquipmentSound.playSound3D(_WT_HYPERION_MOD_B_INTERRUPTION, position)
    return


def playInvisibilityModASound(isEntrance):
    sound = _WT_INVISIBILITY_MOD_A_ENTRANCE if isEntrance else _WT_INVISIBILITY_MOD_A_ESCAPE
    WtEquipmentSound.playSound2D(sound)
    return


def playInvisibilityModBSound():
    WtEquipmentSound.playSound2D(_WT_INVISIBILITY_MOD_B)
    return


def playVOInvisibilityModAStart():
    WtEquipmentSound.playVoiceOver(_INVISIBILITY_MOD_A_START_VO)
    return


def playVOInvisibilityModAStop():
    WtEquipmentSound.playVoiceOver(_INVISIBILITY_MOD_A_STOP_VO)
    return


def playVOInvisibilityModBStart():
    WtEquipmentSound.playVoiceOver(_INVISIBILITY_MOD_B_START_VO)
    return
