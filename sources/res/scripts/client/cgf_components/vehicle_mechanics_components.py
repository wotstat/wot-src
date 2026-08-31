from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent
_VEHICLE_MECHANICS_CATEGORY = b'Vehicle Mechanics'

@registerComponent
class VehicleMechanicSimpleActivationSounds(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Vehicle Mechanic Simple Activation Sounds'
    domain = CGF.Domain.Client
    soundTrigger = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Trigger sound', value=b'')
    soundNotReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Not ready sound', value=b'')


@registerComponent
class ConcentrationModeEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Concentration Mode Mechanic Effects'
    domain = CGF.Domain.Client
    soundTransitionReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition to ready state sound', value=b'gui_abl_concentration_ready')
    soundTransitionStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition to active state sound', value=b'gui_abl_concentration_start')
    soundTransitionBrake = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition to disabled state sound', value=b'gui_abl_concentration_brake')
    soundTransitionStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition from active state sound', value=b'gui_abl_concentration_stop')
    soundObservationActiveStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Observing active state start', value=b'gui_abl_concentration_start_loop')
    soundObservationActiveStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Observing active state stop', value=b'gui_abl_concentration_stop_utility')
    soundStateConcentration = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic WWISE state sync', value=b'STATE_ext_abl_concentration')
    soundStateConcentrationOn = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic WWISE state on value', value=b'STATE_ext_abl_concentration_on')
    soundStateConcentrationOff = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic WWISE state off value', value=b'STATE_ext_abl_concentration_off')


@registerComponent
class PowerModeEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Power Mode Mechanic Effects'
    domain = CGF.Domain.Client
    soundPowerModeActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode activation', value=b'abl_power_activation')
    soundPowerModeLoop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode loop', value=b'abl_power_loop')
    soundPowerModeStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode stop loop', value=b'abl_power_stop_utility')
    soundPowerModeDeactivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode deactivation', value=b'abl_power_disable')
    soundPowerModeActivationNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode activation', value=b'abl_power_activation_npc')
    soundPowerModeLoopNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode loop', value=b'abl_power_loop_npc')
    soundPowerModeStopNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode stop loop', value=b'abl_power_stop_npc_utility')
    soundPowerModeDeactivationNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Power mode deactivation', value=b'abl_power_disable_npc')
    startNodesList = ComponentProperty(type=CGF.PropertyType.LinkList, editorName=b'Start Nodes', value=())
    idleNodesList = ComponentProperty(type=CGF.PropertyType.LinkList, editorName=b'Idle Nodes', value=())
    endNodesList = ComponentProperty(type=CGF.PropertyType.LinkList, editorName=b'End Nodes', value=())


@registerComponent
class AccuracyStacksEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Accuracy Stacks Mechanic Effects'
    domain = CGF.Domain.Client
    soundGainStack = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Gain stack sound', value=b'gui_abl_stab_stack_gain')
    soundStacksLimitReached = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stacks limit reached sound', value=b'gui_abl_stab_stack_limit_reached')
    soundWarningNotification = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Warning notification sound', value=b'gui_abl_stab_stack_warning')
    soundGainStacksStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Start gaining stacks sound', value=b'gui_abl_stab_stack_progress')
    soundGainStacksStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stop gaining stacks sound', value=b'gui_abl_stab_stack_progress_stop')
    soundGainStacksPause = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Pause gaining stacks sound', value=b'gui_abl_stab_stack_pause')
    soundGainStacksResume = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Resume gaining stacks sound', value=b'gui_abl_stab_stack_resume')


@registerComponent
class AccuracyStacksRTPCComponent(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Accuracy stacks gaining RTPC'
    domain = CGF.Domain.Client
    RTPCName = ComponentProperty(type=CGF.PropertyType.String, value=b'RTPC_ext_abl_stab_stack_progress', editorName=b'RTPC name')

    def __init__(self):
        super(AccuracyStacksRTPCComponent, self).__init__()
        self.controllerGO = None
        self.progress = -1.0
        return


@registerComponent
class BattleFuryModeEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Battle Fury Mechanic Effects'
    domain = CGF.Domain.Client
    soundGainStack = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Gain stack sound', value=b'gui_abl_stack_gain')
    soundStacksLimitReached = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stacks limit reached sound', value=b'gui_abl_stack_limit_reached')
    soundDropStack = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Drop stack sound', value=b'gui_abl_stack_drop')
    soundRefreshStack = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Refresh stack sound', value=b'gui_abl_stack_refresh')


@registerComponent
class SupportWeaponEffects(object):
    category = b'Vehicle Mechanics'
    editorTitle = b'Support Weapon Mechanic Effects'
    domain = CGF.Domain.Client
    delayedReloadMinTime = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Min time for delayed reload', value=0.0)
    delayedReloadMaxTime = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Max time for delayed reload', value=3.0)
    soundDelayedReload = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Delayed sound for reload finishing', value=b'gui_abl_saw_reload')
    soundDelayedReloadCancel = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Finishing reload sound cancellation', value=b'gui_abl_saw_reload_stop')
    soundTransitionReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition to ready state sound', value=b'gui_abl_saw_ready')
    soundTransitionStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition to active state sound', value=b'gui_abl_saw_start')
    soundTransitionBreak = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition to disabled state sound', value=b'gui_abl_saw_break')
    soundTransitionStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Transition from active state sound', value=b'gui_abl_saw_stop')
    soundGeneralUtilityStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic sounds finalization', value=b'gui_abl_saw_stop_utility')


@registerComponent
class PillboxSiegeModeSoundEffects(object):
    category = b'Vehicle Mechanics'
    editorTitle = b'Pillbox Siege Mode Sound Effects'
    domain = CGF.Domain.Client
    longpressActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Long press activation 2D', value=b'gui_abl_pillbox_activation_longpress')
    longpressDeactivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Long press deactivation 2D', value=b'gui_abl_pillbox_deactivation_longpress')
    longpressError = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Long press unavailable 2D', value=b'gui_abl_button_not_ready')
    abilityActivationStart = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability activation start 2D', value=b'gui_abl_pillbox_activation_phase_start')
    abilityActivationStartEngine = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability activation start Engine', value=b'gp_abl_pillbox_engine_activation_phase_start')
    abilityActivationStop = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability activation stop 2D', value=b'gui_abl_pillbox_activation_phase_stop ')
    abilityActivationStopEngine = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability activation stop Engine', value=b'gp_abl_pillbox_engine_activation_phase_stop')
    abilityDeactivationStart = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability deactivation start 2D', value=b'gui_abl_pillbox_deactivation_phase_start')
    abilityDeactivationStartEngine = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability deactivation start Engine', value=b'gp_abl_pillbox_engine_deactivation_phase_start')
    abilityDeactivationStop = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability deactivation stop 2D', value=b'gui_abl_pillbox_deactivation_phase_stop')
    abilityDeactivationStopEngine = ComponentProperty(CGF.PropertyType.String, editorName=b'Ability deactivation stop Engine', value=b'gp_abl_pillbox_engine_deactivation_phase_stop')
    engineStateGroup = ComponentProperty(CGF.PropertyType.String, editorName=b'Engine state group', value=b'STATE_ext_abl_pillbox_engine_damage')
    engineDamageOn = ComponentProperty(CGF.PropertyType.String, editorName=b'Engine damage on', value=b'STATE_ext_abl_pillbox_engine_damage_on')
    engineDamageOff = ComponentProperty(CGF.PropertyType.String, editorName=b'Engine damage off', value=b'STATE_ext_abl_pillbox_engine_damage_off')


@registerComponent
class OverheatStacksEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Overheat Stacks mechanic effects'
    domain = CGF.Domain.Client
    soundDelayTimerUp = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Delay Timer boot up sound', value=b'gui_abl_charge_delay_up')
    soundDelayTimerDown = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Drop Delay shut down sound', value=b'gui_abl_charge_delay_down')
    eventChargingOn = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Start/continue charging event', value=b'gui_abl_charge_start')
    eventChargingOff = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stop/pause charging event', value=b'gui_abl_charge_stop')
    eventChargingSilentInterrupt = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stop/pause charging silently', value=b'gui_abl_charge_stop_utility')
    RTPCChargingProcess = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charging process rtpc', value=b'RTPC_ext_abl_charge_progress')
    soundChargeMax = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge Max sound', value=b'gui_abl_charge_max')


@registerComponent
class RechargeableNitroEffects(object):
    category = b'Vehicle Mechanics'
    editorTitle = b'Rechargeable Nitro Effects'
    domain = CGF.Domain.Client
    idle = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Idle Object', value=CGF.GameObject)
    start = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Start Object', value=CGF.GameObject)
    end = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Stop Object', value=CGF.GameObject)
    endSwitch = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Stop switch Object', value=CGF.GameObject)
    startFail = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Start fail Object', value=CGF.GameObject)
    nearEnd = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'Near end Object', value=CGF.GameObject)
    soundNodes = ComponentProperty(type=CGF.PropertyType.LinkList, editorName=b'Sound nodes', value=())
    rtpcHolder = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'RTPC component holder', value=CGF.GameObject)
    soundActivePC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Active PC sound', value=b'gp_abl_nitro_start_PC')
    soundStopPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stop PC sound', value=b'gp_abl_nitro_stop_PC')
    soundActiveNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Active NPC sound', value=b'gp_abl_nitro_start_NPC')
    soundStopNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stop NPC sound', value=b'gp_abl_nitro_stop_NPC')
    soundReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Ready sound', value=b'gui_abl_nitro_ready')
    soundDisable = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Disable sound', value=b'gui_abl_nitro_disable')
    soundDelayEnded = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Delay ended sound', value=b'gui_abl_nitro_delay_end')
    soundExhausted = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge exhausted sound', value=b'gui_abl_nitro_overheat')
    eventRTPCStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'RTPC start event', value=b'gui_abl_nitro_start_utility')
    eventRTPCStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'RTPC stop event', value=b'gui_abl_nitro_stop_utility')


@registerComponent
class ChargeShotEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Charge Shot Mechanic Effects'
    domain = CGF.Domain.Client
    soundActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Activation sound', value=b'gui_abl_button_trigger')
    soundActivationDisabled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Disabled activation sound', value=b'gui_abl_button_not_ready')
    soundChargeStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge start sound', value=b'gui_abl_charged_shot_start')
    soundChargeLevel1 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge level 1 sound', value=b'gui_abl_charged_shot_reach_level_01')
    soundChargeLevel2 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge level 2 sound', value=b'gui_abl_charged_shot_reach_level_02')
    soundChargeLevelMax = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge level Max sound', value=b'gui_abl_charged_shot_reach_level_03')
    soundShootLevel0 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shoot level 0 sound', value=b'gui_abl_charged_shot_fire_level_00')
    soundShootLevel1 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shoot level 1 sound', value=b'gui_abl_charged_shot_fire_level_01')
    soundShootLevel2 = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shoot level 2 sound', value=b'gui_abl_charged_shot_fire_level_02')
    soundShootLevelMax = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shoot level Max sound', value=b'gui_abl_charged_shot_fire_level_03')
    soundOverheat = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overheat sound', value=b'gui_abl_charged_shot_overheat')
    soundMechanicStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic stop sound', value=b'gui_abl_charged_shot_stop_utility')


@registerComponent
class TargetDesignatorEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Target Designator Mechanic Effects'
    domain = CGF.Domain.Client
    soundReadyState = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Ready state sound', value=b'gui_abl_tda_ready')
    soundActiveState = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Active state sound', value=b'gui_abl_tda_start')
    soundCooldownState = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Cooldown state sound', value=b'gui_abl_tda_stop')
    soundActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Activation button sound', value=b'gui_abl_button_trigger')
    soundActivationDisabled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Disabled activation sound', value=b'gui_abl_button_not_ready')
    soundMechanicStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic stop sound', value=b'gui_abl_tda_stop_utility')


@registerComponent
class StanceDanceEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Stance Dance Mechanic Effects'
    domain = CGF.Domain.Client
    sound3DTurboActivatedPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turbo activate 3D sound (PC)', value=b'gp_abl_stance_turbo_active_on_pc')
    sound3DTurboDeactivatedPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turbo deactivate 3D sound (PC)', value=b'gp_abl_stance_turbo_active_off_pc')
    sound3DTurboActivatedNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turbo activate 3D sound (NPC)', value=b'gp_abl_stance_turbo_active_on_npc')
    sound3DTurboDeactivatedNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turbo deactivate 3D sound (NPC)', value=b'gp_abl_stance_turbo_active_off_npc')
    soundTurboFullEnergy = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turbo full energy sound', value=b'gui_abl_stance_turbo_full')
    soundFightFullEnergy = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Fight full energy sound', value=b'gui_abl_stance_shooting_full')
    soundTurboModeOn = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turbo mode on sound', value=b'gui_abl_stance_turbo_on_pc')
    soundFightModeOn = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Fight mode on sound', value=b'gui_abl_stance_shooting_on_pc')
    soundFightActivated = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Fight activate sound', value=b'gui_abl_stance_shooting_active_on_pc')
    soundFightDeactivated = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Fight deactivate sound', value=b'gui_abl_stance_shooting_active_off_pc')
    soundMechanicStopPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic stop sound (PC)', value=b'abl_stance_stop_utility')
    soundMechanicStopNPC = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic stop sound (NPC)', value=b'abl_stance_stop_npc_utility')
    soundActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Activation sound', value=b'gui_abl_button_trigger')
    soundActivationDisabled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Disabled activation sound', value=b'gui_abl_button_not_ready')
    soundSwitch = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Switch sound', value=b'gui_abl_stance_mode_switch')


@registerComponent
class StationaryReloadEffects(object):
    category = b'Vehicle Mechanics'
    editorTitle = b'Stationary Reload Mechanic Effects'
    domain = CGF.Domain.Client
    soundTurretMoveStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turret starts moving sound', value=b'gui_abl_podrld_turret_start')
    soundTurretMoveEnd = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turret at load point sound', value=b'gui_abl_podrld_turret_loadpoint')
    soundTurretLoadStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turret load stop sound', value=b'gui_abl_podrld_turret_loadstop')
    soundTurretStopUtility = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turret stop utility sound', value=b'gui_abl_podrld_turret_stop_utility')
    soundTurretBrake = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Turret break brake sound', value=b'gp_abl_podrld_pods_brake')
    soundDelayStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Delay start sound', value=b'gui_abl_podrld_turret_delay_start')
    soundDelayStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Delay stop sound', value=b'gui_abl_podrld_turret_delay_stop')


@registerComponent
class OverheatGunEffects(object):
    category = b'OverheatGun'
    editorTitle = b'Overheat Gun Effects'
    domain = CGF.Domain.Client
    soundHeating = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Gun heating start sound', value=b'gui_abl_overheat_gun_heating')
    soundCooling = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Gun colling start sound', value=b'gui_abl_overheat_gun_cooling')
    soundIdle = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Gun colling stop sound', value=b'gui_abl_overheat_gun_cooling_stop')
    soundUtilityStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Utility stop', value=b'gui_abl_overheat_gun_utility_stop')
    soundOverheatWarning = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overheat warning sound', value=b'gui_abl_overheat_gun_block_on_pre')
    soundOverheated = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overheat occurs sound', value=b'gui_abl_overheat_gun_block_on')
    soundPreCooled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overheat near end sound', value=b'gui_abl_overheat_gun_block_off_pre')
    soundCooled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overheat ended sound', value=b'gui_abl_overheat_gun_block_off')


@registerComponent
class HeatingZonesGunEffects(object):
    category = b'HeatingZonesGun'
    editorTitle = b'Heating Zones Gun State Effects'
    domain = CGF.Domain.Client
    soundHeatingOn = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Heating start sound', value=b'gui_abl_gun_heating_on')
    soundHeatingOff = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Heating stop sound', value=b'gui_abl_gun_heating_off')
    soundHeatingDropMarker = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Heating marker drop sound', value=b'gui_abl_gun_heating_marker')
    soundHeatingIdleMarker = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Heating marker idle sound', value=b'gui_abl_gun_heating_marker_last_aim')
    soundUtilityStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Heating utility stop', value=b'gui_abl_gun_heating_stop_utility')


@registerComponent
class PropellantGunEffects(object):
    category = b'PropellantGun'
    editorTitle = b'Propellant Gun Effects'
    domain = CGF.Domain.Client
    soundActivationDisabled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Disabled activation sound', value=b'gui_abl_button_not_ready')
    soundChargeMin = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Normal charge mode was set', value=b'gui_abl_afterburner_set_min')
    soundChargeMax = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overcharge mode was set', value=b'gui_abl_afterburner_set_max')
    soundPreCharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Precharging sound', value=b'gui_abl_afterburner_pre_min')
    soundPreOvercharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Preovercharging sound', value=b'gui_abl_afterburner_pre_max')
    soundReachCharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Charge reach sound', value=b'gui_abl_afterburner_reach_min')
    soundReachOvercharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Overcharge reach sound', value=b'gui_abl_afterburner_reach_max')
    soundStartOvercharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Start overcharging  sound', value=b'gui_abl_afterburner_exceed_min')
    soundShotFromMinCharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shot from normal charge limit', value=b'gui_abl_afterburner_min_shot')
    soundShotExitOvercharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shot in overcharge range', value=b'gui_abl_afterburner_max_shot')
    soundShotNocharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shot under charge limit', value=b'gui_abl_afterburner_nocharge_shot')
    soundDropOvercharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Drop overcharge', value=b'gui_abl_afterburner_drop_max_switch')
    soundUtilityStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Propellant utility stop', value=b'gui_abl_afterburner_stop_utility')


@registerComponent
class ShellParamsSwitcherGunEffects(object):
    category = b'ShellParamsSwitcherGun'
    editorTitle = b'Shell Params Switcher Gun Effects'
    domain = CGF.Domain.Client
    soundActivationDisabled = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Disabled activation sound', value=b'gui_abl_button_not_ready')
    soundTriggered = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Control activation', value=b'gui_abl_button_trigger')
    soundCharge2Noncharge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Switch the chargeable state to the non-chargeable state', value=b'gui_abl_scs_chrgble_to_nonchrgble')
    soundNoncharge2Charge = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Switch the non-chargeable state to the chargeable state', value=b'gui_abl_scs_nonchrgble_to_chrgble')
    soundFinish = ComponentProperty(type=CGF.PropertyType.String, editorName=b'The transition to any state is completed', value=b'gui_abl_scs_finish')
    soundBroken = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Weapon breakdown', value=b'gui_abl_scs_broken')
    soundUtilityStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shell Switcher utility stop', value=b'gui_abl_scs_stop_utility')


@registerComponent
class ShellCalibrationEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    domain = CGF.Domain.Client
    editorTitle = b'Shell Calibration Mechanic Effects'
    soundShellCalibrationPenetrationActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shell Calibration Penetration activation', value=b'gui_abl_afs_pen_buff')
    soundShellCalibrationDamageActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Shell Calibration Damage activation', value=b'gui_abl_afs_dam_buff')


@registerComponent
class AutoreloaderSurgeEffects(object):
    editorTitle = b'Autoreloader Surge Effects'
    category = b'AutoreloaderSurge'
    domain = CGF.Domain.Client
    soundActivationStart = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sound of applied ability', value=b'gui_abl_flm_start')
    soundChargeAlmostReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sound of almost ready charge', value=b'gui_abl_flm_charge_complete')


@registerComponent
class BustleFeedEffects(object):
    editorTitle = b'Bustle Feed Effects'
    category = _VEHICLE_MECHANICS_CATEGORY
    domain = CGF.Domain.Client
    soundActivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Activation (from Versatile to BAF)', value=b'gui_abl_swmt_change_from_versatile')
    soundActive = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Active (BAF enabled)', value=b'gui_abl_swmt_set_bustle')
    soundDeactivation = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Deactivation (from BAF to Versatile)', value=b'gui_abl_swmt_change_from_bustle')
    soundInactive = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Inactive (BAF disabled)', value=b'gui_abl_swmt_set_versatile')
    soundNotReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Switch attempt while locked', value=b'gui_abl_swmt_not_ready')
    soundStopUtility = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Mechanic stop utility', value=b'gui_abl_swmt_stop_utility')


@registerComponent
class SightPointerEffects(object):
    category = _VEHICLE_MECHANICS_CATEGORY
    editorTitle = b'Sight Pointer Effects'
    domain = CGF.Domain.Client
    soundReady = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Ready sound event', value=b'gui_abl_sp_ready')
    soundActivateButton = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Successful button press sound event', value=b'gui_abl_button_trigger')
    soundActivationFail = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Unsuccessful button press sound event', value=b'gui_abl_button_not_ready')
    soundActivate = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Activation sound event', value=b'gui_abl_sp_start')
    soundConeOn = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Cone stages on sound event', value=b'gui_abl_sp_cone_on')
    soundRTPCStage = ComponentProperty(type=CGF.PropertyType.String, editorName=b'RTPC for cone stages', value=b'RTPC_ext_abl_sp_stage')
    soundConeOff = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Cone stages off sound event', value=b'gui_abl_sp_cone_off')
    soundEnemyEnterSector = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Enemy enter sector sound event', value=b'gui_abl_sp_enemy_indication_on')
    soundEnemyLeftSector = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Enemy left sector sound event', value=b'gui_abl_sp_enemy_indication_off')
    soundStop = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Stop ability utility sound event', value=b'gui_abl_sp_utility_stop')
