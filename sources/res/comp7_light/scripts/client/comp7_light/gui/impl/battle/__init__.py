def registerComp7LightBattle():
    from arena_component_system.assembler_helper import ARENA_BONUS_TYPE_CAP_COMPONENTS
    from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
    from comp7_core.gui.battle_control.controllers.consumables import comp7_equipment_ctrl
    from comp7_light.gui.battle_control.arena_info.arena_vos import Comp7LightKeys
    from comp7_light.gui.ingame_help.detailed_help_pages import Comp7LightPagesBuilder
    from comp7_light.helpers.tips import Comp7LightTipsCriteria
    from comp7_light.arena_components.comp7_light_equipment_component import Comp7LightEquipmentComponent
    from comp7_light_constants import ARENA_GUI_TYPE
    from constants import ARENA_BONUS_TYPE
    from gui.battle_control.controllers.consumables import extendEquipmentController
    from gui.shared.system_factory import registerBattleTipCriteria, registerIngameHelpPagesBuilder, registerGameModeArenaInfoKeys
    from gui.battle_control.controllers import callout_ctrl
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    registerBattleTipCriteria(ARENA_GUI_TYPE.COMP7_LIGHT, Comp7LightTipsCriteria)
    registerIngameHelpPagesBuilder(Comp7LightPagesBuilder)
    extendEquipmentController({(ARENA_BONUS_TYPE.COMP7_LIGHT): (comp7_equipment_ctrl.Comp7EquipmentController)}, {(ARENA_BONUS_TYPE.COMP7_LIGHT): (comp7_equipment_ctrl.Comp7ReplayEquipmentController)})
    registerGameModeArenaInfoKeys(ARENA_GUI_TYPE.COMP7_LIGHT, Comp7LightKeys)
    ARENA_BONUS_TYPE_CAP_COMPONENTS.update({b'comp7LightEquipmentComponent': (
                                       ARENA_BONUS_TYPE_CAPS.COMP7_LIGHT, Comp7LightEquipmentComponent)})
    callout_ctrl._CONSUMERS_LOCKS += (VIEW_ALIAS.COMP7_LIGHT_BATTLE_PAGE,)
    _extendEquipmentProperties()
    _extendEquipmentSounds()
    return


def _extendEquipmentProperties():
    from ApplicationPoint import _Comp7ReconApplicationPointEffect, _Comp7RedLineApplicationPointEffect, _EQUIPMENT_APPLICATION_POINTS
    from AvatarInputHandler.MapCaseMode import _STRIKE_SELECTORS
    from comp7_core.avatar_input_handler.map_case_mode import Comp7ArenaBoundArtilleryStrikeSelector, Comp7ArenaBoundPlaneStrikeSelector, Comp7PoiArtilleryStrikeSelector
    from comp7_core.gui.battle_control.controllers.consumables.comp7_equipment_items import _ROLE_SKILL_ITEM_CLASS_BY_NAME, _REPLAY_ROLE_SKILL_ITEM_CLASS_BY_NAME, _RoleSkillArtyVSItem, _RoleSkillReconVSItem, _ReplayRoleSkillArtyVSItem
    from comp7_light_common.items.comp7_light_artefacts import Comp7LightReconEquipment, Comp7LightRedlineEquipment
    from items.artefacts import PoiArtilleryEquipment
    _ROLE_SKILL_ITEM_CLASS_BY_NAME.update({b'comp7_light_recon': _RoleSkillReconVSItem, 
       b'comp7_light_redline': _RoleSkillArtyVSItem})
    _REPLAY_ROLE_SKILL_ITEM_CLASS_BY_NAME.update({b'comp7_light_redline': _ReplayRoleSkillArtyVSItem})
    _EQUIPMENT_APPLICATION_POINTS.update({b'comp7_light_recon': _Comp7ReconApplicationPointEffect, 
       b'comp7_light_redline': _Comp7RedLineApplicationPointEffect})
    _STRIKE_SELECTORS.update({Comp7LightReconEquipment: Comp7ArenaBoundPlaneStrikeSelector, 
       Comp7LightRedlineEquipment: Comp7ArenaBoundArtilleryStrikeSelector, 
       PoiArtilleryEquipment: Comp7PoiArtilleryStrikeSelector})
    return


def _extendEquipmentSounds():
    from comp7_core.gui.battle_control.controllers.sound_ctrls.comp7_battle_sounds import _EQUIPMENT_ACTIVATED_SOUNDS, _EQUIPMENT_DEACTIVATED_SOUNDS, _EQUIPMENT_PREPARING_START_SOUNDS, _EQUIPMENT_PREPARING_CANCEL_SOUNDS, _EQUIPMENT_PRE_DEACTIVATION_SOUNDS, _EQUIPMENT_ARTILLERY_NAMES, _PreDeactivationParams
    _EQUIPMENT_ACTIVATED_SOUNDS.update({b'comp7_light_hunter': b'comp_7_ability_buff_common', 
       b'comp7_light_aoe_heal': b'comp_7_ability_aoe_heal_apply', 
       b'comp7_light_ally_support': b'comp_7_ability_buff_common', 
       b'comp7_light_concentration': b'comp_7_ability_buff_common', 
       b'comp7_light_fast_recharge': b'comp_7_ability_buff_common', 
       b'comp7_light_juggernaut': b'comp_7_ability_buff_common', 
       b'comp7_light_risky_attack': b'comp_7_ability_buff_common', 
       b'comp7_light_recon': b'comp_7_ability_uav', 
       b'comp7_light_berserk': b'comp_7_ability_buff_common', 
       b'comp7_light_sure_shot': b'comp_7_ability_buff_common', 
       b'comp7_light_sniper': b'comp_7_ability_bullseye', 
       b'comp7_light_aggressive_detection': b'comp_7_ability_wheel', 
       b'comp7_light_march': b'comp_7_ability_buff_common', 
       b'comp7_light_redline': b'comp_7_ability_arty_apply'})
    _EQUIPMENT_DEACTIVATED_SOUNDS.update({b'comp7_light_aoe_heal': b'comp_7_ability_aoe_heal_stop', 
       b'comp7_light_hunter': b'comp_7_ability_buff_end', 
       b'comp7_light_ally_support': b'comp_7_ability_buff_end', 
       b'comp7_light_concentration': b'comp_7_ability_buff_end', 
       b'comp7_light_fast_recharge': b'comp_7_ability_buff_end', 
       b'comp7_light_juggernaut': b'comp_7_ability_buff_end', 
       b'comp7_light_risky_attack': b'comp_7_ability_buff_end', 
       b'comp7_light_berserk': b'comp_7_ability_buff_end', 
       b'comp7_light_sure_shot': b'comp_7_ability_buff_end', 
       b'comp7_light_sniper': b'comp_7_ability_buff_end', 
       b'comp7_light_aggressive_detection': b'comp_7_ability_buff_end', 
       b'comp7_light_march': b'comp_7_ability_buff_end'})
    _EQUIPMENT_PREPARING_START_SOUNDS.update({b'comp7_light_redline': b'comp_7_ability_arty_aim'})
    _EQUIPMENT_PREPARING_CANCEL_SOUNDS.update({b'comp7_light_redline': b'comp_7_ability_arty_cancel'})
    _EQUIPMENT_PRE_DEACTIVATION_SOUNDS.update({b'comp7_light_aoe_inspire': (_PreDeactivationParams(b'comp_7_ability_insp_stop', 3.0))})
    _EQUIPMENT_ARTILLERY_NAMES.append(b'comp7_light_redline')
    return
