import typing, logging
from collections import namedtuple
from functools import partial
import BigWorld, WWISE
from shared_utils import nextTick
import SoundGroups
from Vehicle import StunInfo
from constants import EQUIPMENT_STAGES
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from points_of_interest_shared import PoiStatus, ENEMY_VEHICLE_ID
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicle_systems.tankStructure import TankSoundObjectsIndexes
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController, VehicleStateSoundPlayer, SoundPlayer
_logger = logging.getLogger(__name__)

class Comp7BattleSoundController(SoundPlayersBattleController):

    def startControl(self, *args):
        WWISE.activateRemapping(b'comp7')
        super(Comp7BattleSoundController, self).startControl()
        return

    def stopControl(self):
        super(Comp7BattleSoundController, self).stopControl()
        nextTick(partial(WWISE.deactivateRemapping, b'comp7'))()
        return

    def _initializeSoundPlayers(self):
        return (
         _EquipmentStateSoundPlayer(),
         _EquipmentZoneSoundPlayer(),
         _ArtillerySoundPlayer(),
         _RoleSkillSoundPlayer(),
         _PrebattleSoundPlayer(),
         _PoiSNSoundPlayer(),
         _BuffSNSoundPlayer())


_PreDeactivationParams = namedtuple(b'_PreDeactivationParams', (b'soundName', b'timeDelta'))

class _EquipmentStateSoundPlayer(VehicleStateSoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __EQUIPMENT_ACTIVATED = {b'comp7_hunter': b'comp_7_ability_buff_common', 
       b'comp7_aoe_heal': b'comp_7_ability_aoe_heal_apply', 
       b'comp7_ally_support': b'comp_7_ability_buff_common', 
       b'comp7_concentration': b'comp_7_ability_buff_common', 
       b'comp7_aoe_inspire': b'comp_7_ability_insp_start', 
       b'comp7_fast_recharge': b'comp_7_ability_buff_common', 
       b'comp7_juggernaut': b'comp_7_ability_buff_common', 
       b'comp7_risky_attack': b'comp_7_ability_buff_common', 
       b'comp7_recon': b'comp_7_ability_uav', 
       b'comp7_berserk': b'comp_7_ability_buff_common', 
       b'comp7_sure_shot': b'comp_7_ability_buff_common', 
       b'comp7_sniper': b'comp_7_ability_bullseye', 
       b'comp7_aggressive_detection': b'comp_7_ability_wheel', 
       b'comp7_march': b'comp_7_ability_buff_common', 
       b'comp7_redline': b'comp_7_ability_arty_apply'}
    __EQUIPMENT_DEACTIVATED = {b'comp7_aoe_heal': b'comp_7_ability_aoe_heal_stop', 
       b'comp7_hunter': b'comp_7_ability_buff_end', 
       b'comp7_ally_support': b'comp_7_ability_buff_end', 
       b'comp7_concentration': b'comp_7_ability_buff_end', 
       b'comp7_fast_recharge': b'comp_7_ability_buff_end', 
       b'comp7_juggernaut': b'comp_7_ability_buff_end', 
       b'comp7_risky_attack': b'comp_7_ability_buff_end', 
       b'comp7_berserk': b'comp_7_ability_buff_end', 
       b'comp7_sure_shot': b'comp_7_ability_buff_end', 
       b'comp7_sniper': b'comp_7_ability_buff_end', 
       b'comp7_aggressive_detection': b'comp_7_ability_buff_end', 
       b'comp7_march': b'comp_7_ability_buff_end'}
    __EQUIPMENT_PREPARING_START = {b'comp7_redline': b'comp_7_ability_arty_aim', 
       b'poi_artillery_aoe': b'comp_7_ability_arty_aim', 
       b'poi_smoke': b'comp_7_ability_arty_aim', 
       b'poi_minefield': b'comp_7_ability_arty_aim'}
    __EQUIPMENT_PREPARING_CANCEL = {b'comp7_redline': b'comp_7_ability_arty_cancel', 
       b'poi_artillery_aoe': b'comp_7_ability_arty_cancel', 
       b'poi_smoke': b'comp_7_ability_arty_cancel', 
       b'poi_minefield': b'comp_7_ability_arty_cancel'}
    __PRE_DEACTIVATION_SOUNDS = {b'comp7_aoe_inspire': (_PreDeactivationParams(b'comp_7_ability_insp_stop', 3.0))}
    __POI_EQUIPMENT_ACTIVATED = {b'poi_radar': b'comp_7_ability_poi_radar', 
       b'poi_radar_ally': b'comp_7_ability_poi_radar_ally', 
       b'poi_radar_enemy': b'comp_7_ability_poi_radar_enemy', 
       b'poi_artillery_aoe': b'comp_7_ability_arty_apply', 
       b'poi_artillery_aoe_ally': b'comp_7_ability_arty_ally', 
       b'poi_artillery_aoe_enemy': b'comp_7_ability_arty_enemy', 
       b'poi_smoke': b'comp_7_ability_arty_apply', 
       b'poi_smoke_ally': b'comp_7_ability_arty_ally', 
       b'poi_smoke_enemy': b'comp_7_ability_arty_enemy', 
       b'poi_minefield': b'comp_7_ability_arty_apply', 
       b'poi_minefield_ally': b'comp_7_ability_arty_ally', 
       b'poi_minefield_enemy': b'comp_7_ability_arty_enemy'}

    def __init__(self):
        super(_EquipmentStateSoundPlayer, self).__init__()
        self.__callbackDelayer = None
        self.__activeEquipment = set()
        return

    def init(self):
        super(_EquipmentStateSoundPlayer, self).init()
        self.__callbackDelayer = CallbackDelayer()
        self.__activeEquipment.clear()
        return

    def destroy(self):
        super(_EquipmentStateSoundPlayer, self).destroy()
        if self.__callbackDelayer is not None:
            self.__callbackDelayer.destroy()
            self.__callbackDelayer = None
        self.__activeEquipment.clear()
        return

    def _subscribe(self):
        super(_EquipmentStateSoundPlayer, self)._subscribe()
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated += self.__onEquipmentUpdated
        poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
        if poiCtrl is not None:
            poiCtrl.onPoiEquipmentUsed += self.__onPoiEquipmentUsed
        return

    def _unsubscribe(self):
        super(_EquipmentStateSoundPlayer, self)._unsubscribe()
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        poiCtrl = self.__sessionProvider.dynamic.pointsOfInterest
        if poiCtrl is not None:
            poiCtrl.onPoiEquipmentUsed -= self.__onPoiEquipmentUsed
        return

    def _onVehicleStateUpdated(self, state, value):
        if state == VEHICLE_VIEW_STATE.DESTROYED:
            self.__clearActiveEquipment()
        return

    def _onSwitchViewPoint(self):
        self.__clearActiveEquipment()
        return

    def __onEquipmentUpdated(self, _, item):
        if item.getPrevStage() == item.getStage():
            return
        prevStageIsReady = item.getPrevStage() in (EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.PREPARING)
        prevStageIsActive = item.getPrevStage() in (EQUIPMENT_STAGES.ACTIVE,)
        stageIsCooldown = item.getStage() in (
         EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.READY, EQUIPMENT_STAGES.UNAVAILABLE)
        stageIsActive = item.getStage() in (
         EQUIPMENT_STAGES.ACTIVE, EQUIPMENT_STAGES.COOLDOWN, EQUIPMENT_STAGES.EXHAUSTED)
        if item.getPrevStage() == EQUIPMENT_STAGES.READY and item.getStage() == EQUIPMENT_STAGES.PREPARING:
            self.__play2dFromMapping(self.__EQUIPMENT_PREPARING_START, item)
        elif item.getPrevStage() == EQUIPMENT_STAGES.PREPARING and item.getStage() == EQUIPMENT_STAGES.READY:
            self.__play2dFromMapping(self.__EQUIPMENT_PREPARING_CANCEL, item)
        elif prevStageIsReady and stageIsActive:
            self.__play2dFromMapping(self.__EQUIPMENT_ACTIVATED, item)
            self.__play2dFromMappingDelayed(self.__PRE_DEACTIVATION_SOUNDS, item)
            self.__activeEquipment.add(item.getDescriptor().name)
        elif stageIsCooldown and prevStageIsActive:
            self.__play2dFromMapping(self.__EQUIPMENT_DEACTIVATED, item)
            self.__activeEquipment.discard(item.getDescriptor().name)
        return

    def __onPoiEquipmentUsed(self, equipment, vehicleID):
        equipmentName = equipment.name
        ownVehicleID = self.__sessionProvider.shared.vehicleState.getControllingVehicleID()
        if vehicleID == ENEMY_VEHICLE_ID:
            equipmentName = (b'{}_enemy').format(equipmentName)
        elif vehicleID != ownVehicleID:
            equipmentName = (b'{}_ally').format(equipmentName)
        self.__play2dFromMapping(self.__POI_EQUIPMENT_ACTIVATED, itemName=equipmentName)
        return

    def __play2dFromMapping(self, soundsMapping, item=None, itemName=None):
        soundName = soundsMapping.get(itemName if itemName else item.getDescriptor().name)
        _play2d(soundName)
        return

    def __play2dFromMappingDelayed(self, soundsMapping, item):
        delayedSoundParams = soundsMapping.get(item.getDescriptor().name)
        if delayedSoundParams is not None:
            self.__callbackDelayer.delayCallback(item.getTimeRemaining() - delayedSoundParams.timeDelta, _play2d, delayedSoundParams.soundName)
        return

    def __clearActiveEquipment(self):
        for equipment in self.__activeEquipment:
            soundName = self.__EQUIPMENT_DEACTIVATED.get(equipment)
            if soundName is not None:
                _play2d(soundName)

        self.__activeEquipment.clear()
        self.__callbackDelayer.clearCallbacks()
        return


class _EquipmentZoneSoundPlayer(VehicleStateSoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __EQUIPMENT_ZONE_ENTER = {(VEHICLE_VIEW_STATE.AOE_HEAL): b'comp_7_ability_aoe_heal_enter', 
       (VEHICLE_VIEW_STATE.STUN): b'artillery_stun_effect_start'}
    __EQUIPMENT_ZONE_EXIT = {(VEHICLE_VIEW_STATE.AOE_HEAL): b'comp_7_ability_aoe_heal_exit', 
       (VEHICLE_VIEW_STATE.STUN): b'artillery_stun_effect_end'}

    def __init__(self):
        super(_EquipmentZoneSoundPlayer, self).__init__()
        self.__vehicleStates = set()
        return

    def destroy(self):
        super(_EquipmentZoneSoundPlayer, self).destroy()
        self.__vehicleStates = None
        return

    def _onVehicleStateUpdated(self, state, value):
        if state in self.__EQUIPMENT_ZONE_ENTER and self.__stateIsActive(value) and self.__checkSource(value):
            _play2d(self.__EQUIPMENT_ZONE_ENTER[state])
            self.__vehicleStates.add(state)
        elif state in self.__EQUIPMENT_ZONE_EXIT and not self.__stateIsActive(value) and state in self.__vehicleStates:
            _play2d(self.__EQUIPMENT_ZONE_EXIT[state])
            self.__vehicleStates.discard(state)
        return

    def __stateIsActive(self, value):
        if isinstance(value, StunInfo):
            return value.duration > 0.0
        return not value.get(b'finishing')

    def __checkSource(self, value):
        if isinstance(value, StunInfo):
            return True
        return not value.get(b'isSourceVehicle')


class _RoleSkillSoundPlayer(SoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __EQUIPMENT_LEVEL_UP = b'comp_7_ability_levelup'

    def _subscribe(self):
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onRoleEquipmentStateChanged += self.__onRoleEquipmentStateChanged
        return

    def _unsubscribe(self):
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onRoleEquipmentStateChanged -= self.__onRoleEquipmentStateChanged
        return

    def __onRoleEquipmentStateChanged(self, state, previousState):
        if state is not None and previousState is not None:
            if state.level > previousState.level:
                _play2d(self.__EQUIPMENT_LEVEL_UP)
        return


_ArtilleryAreaParams = namedtuple(b'_ArtilleryAreaParams', (b'position', b'radius', b'endTime'))

class _ArtillerySoundPlayer(SoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __COMP7_ARTILLERY_NAMES = (b'comp7_redline', b'poi_artillery_aoe', b'poi_smoke', b'poi_minefield')
    __ARTILLERY_START = b'comp_7_ability_arty_enter'
    __ARTILLERY_STOP = b'comp_7_ability_arty_exit'
    __ARTILLERY_DAMAGE_PC = b'imp_artillery_expl_huge_NPC_PC'

    def __init__(self):
        super(_ArtillerySoundPlayer, self).__init__()
        self.__callbackDelayer = None
        self.__attacked = False
        self.__artilleryAreas = []
        return

    def init(self):
        super(_ArtillerySoundPlayer, self).init()
        self.__callbackDelayer = CallbackDelayer()
        return

    def destroy(self):
        super(_ArtillerySoundPlayer, self).destroy()
        if self.__callbackDelayer is not None:
            self.__callbackDelayer.destroy()
            self.__callbackDelayer = None
        self.__artilleryAreas = None
        return

    def _subscribe(self):
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentAreaCreated += self.__onEquipmentAreaCreated
        return

    def _unsubscribe(self):
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentAreaCreated -= self.__onEquipmentAreaCreated
        return

    def __onEquipmentAreaCreated(self, equipment, position, endTime, level=None, team=None):
        if equipment.name in self.__COMP7_ARTILLERY_NAMES:
            radius = equipment.getRadiusBasedOnSkillLevel(level) if level is not None else equipment.areaRadius
            self.__artilleryAreas.append(_ArtilleryAreaParams(position, radius, endTime))
            self.__updateAttack()
        return

    def __updateAttack(self):
        self.__artilleryAreas = [area for area in self.__artilleryAreas if BigWorld.serverTime() < area.endTime]
        vehicle = _getPlayerVehicle()
        if vehicle is not None:
            affectAreas = [area for area in self.__artilleryAreas if vehicle.position.flatDistTo(area.position) < area.radius]
            attacked = bool(affectAreas)
        else:
            attacked = False
        if attacked and not self.__attacked:
            _play2d(self.__ARTILLERY_START)
        elif not attacked and self.__attacked:
            _play2d(self.__ARTILLERY_STOP)
            _playVehiclePC(self.__ARTILLERY_DAMAGE_PC, TankSoundObjectsIndexes.ENGINE)
        self.__attacked = attacked
        if self.__artilleryAreas:
            self.__callbackDelayer.delayCallback(0.2, self.__updateAttack)
        return


class _PrebattleSoundPlayer(SoundPlayer):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __CONFIRM_VEHICLE_SELECTION = b'comp_7_tank_confirm'

    def _subscribe(self):
        prebattleCtrl = self.__sessionProvider.dynamic.comp7PrebattleSetup
        if prebattleCtrl is not None:
            prebattleCtrl.onSelectionConfirmed += self.__onSelectionConfirmed
        return

    def _unsubscribe(self):
        prebattleCtrl = self.__sessionProvider.dynamic.comp7PrebattleSetup
        if prebattleCtrl is not None:
            prebattleCtrl.onSelectionConfirmed -= self.__onSelectionConfirmed
        return

    def __onSelectionConfirmed(self):
        _play2d(self.__CONFIRM_VEHICLE_SELECTION)
        return


class _PoiSNSoundPlayer(VehicleStateSoundPlayer):
    __POI_CAPTURE_TIMER_SHOWN = b'comp_7_poi_timer_capture'
    __POI_COOLDOWN_TIMER_SHOWN = b'comp_7_poi_timer_cooldown'

    def _onVehicleStateUpdated(self, state, value):
        if state == VEHICLE_VIEW_STATE.POINT_OF_INTEREST_STATE and value is not None:
            if value.status.statusID is PoiStatus.CAPTURING:
                _play2d(self.__POI_CAPTURE_TIMER_SHOWN)
            elif value.status.statusID is PoiStatus.COOLDOWN:
                _play2d(self.__POI_COOLDOWN_TIMER_SHOWN)
        return


class _BuffSNSoundPlayer(VehicleStateSoundPlayer):
    __RESET_ABILITY = b'comp_7_ability_timer_reset'
    __EQUIPMENT_STATE_ACTIVATED = {(VEHICLE_VIEW_STATE.AOE_INSPIRE): b'comp_7_ability_insp_start'}

    def __init__(self):
        super(_BuffSNSoundPlayer, self).__init__()
        self.__vehicleStates = {}
        return

    def _onVehicleStateUpdated(self, state, value):
        if VEHICLE_VIEW_STATE.AOE_INSPIRE <= state <= VEHICLE_VIEW_STATE.AGGRESSIVE_DETECTION and value is not None:
            if value.get(b'finishing'):
                self.__vehicleStates.pop(state, None)
            else:
                currentValue = self.__vehicleStates.get(state)
                if currentValue is not None and value.get(b'endTime') > currentValue:
                    _play2d(self.__RESET_ABILITY)
                else:
                    _play2d(self.__EQUIPMENT_STATE_ACTIVATED.get(state))
                self.__vehicleStates[state] = value.get(b'endTime')
        return


def _getPlayerVehicle():
    vehicle = avatar_getter.getPlayerVehicle()
    if vehicle is not None and vehicle.isAlive():
        return vehicle
    else:
        return


def _play2d(soundName):
    if soundName is None:
        return
    else:
        SoundGroups.g_instance.playSound2D(soundName)
        return


def _playVehiclePC(soundName, soundObjectIndex):
    vehicle = _getPlayerVehicle()
    if vehicle is not None:
        soundObject = vehicle.appearance.engineAudition.getSoundObject(soundObjectIndex)
        if soundObject is not None:
            soundObject.play(soundName)
        else:
            _logger.debug(b'Could not find audition sound object for %s', soundName)
    else:
        _logger.debug(b'Vehicle for %s is destroyed or not loaded', soundName)
    return
