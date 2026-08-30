import BigWorld, settings
from account_helpers.settings_core.settings_constants import MARKERS
from comp7_core.gui.battle_control.arena_info.arena_vos import Comp7CoreKeys
from constants import ROLE_TYPE_TO_LABEL, ROLE_TYPE, INVALID_TIMESTAMP, ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.shared.markers2d.plugins import SettingsPlugin
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID
_COMP7_STATUS_EFFECTS_PRIORITY = (
 BATTLE_MARKER_STATES.STUN_STATE,
 BATTLE_MARKER_STATES.COMP7_AOE_HEAL_STATE,
 BATTLE_MARKER_STATES.COMP7_AOE_INSPIRE_STATE)

class Comp7SettingsPlugin(SettingsPlugin):
    __BEFORE_BATTLE_OVERRIDES = {(MARKERS.ALLY): (
                      (
                       b'markerAltIcon', False),
                      (
                       b'markerAltLevel', False),
                      (
                       b'markerAltHpIndicator', False),
                      (
                       b'markerAltDamage', False),
                      (b'markerAltHp', 3),
                      (
                       b'markerAltVehicleName', True),
                      (
                       b'markerAltPlayerName', True),
                      (
                       b'markerAltAimMarker2D', False),
                      (
                       b'markerBaseIcon', False),
                      (
                       b'markerBaseLevel', False),
                      (
                       b'markerBaseHpIndicator', False),
                      (
                       b'markerBaseDamage', False),
                      (b'markerBaseHp', 3),
                      (
                       b'markerBaseVehicleName', True),
                      (
                       b'markerBasePlayerName', True),
                      (
                       b'markerBaseAimMarker2D', False))}
    __ADDITIONAL_SETTINGS = {name: ((b'markerAltRoleName', True), (b'markerAltRoleSkillLevel', True), (b'markerBaseRoleName', False), (b'markerBaseRoleSkillLevel', False)) for name in MARKERS.ALL()}
    __ADDITIONAL_SETTINGS_BEFORE_BATTLE = {name: ((b'markerAltRoleName', True), (b'markerAltRoleSkillLevel', False), (b'markerBaseRoleName', True), (b'markerBaseRoleSkillLevel', False)) for name in MARKERS.ALL()}

    def __init__(self, parentObj):
        super(Comp7SettingsPlugin, self).__init__(parentObj)
        self._overrides = {}
        self._additionalSettings = self.__ADDITIONAL_SETTINGS
        return

    def start(self, *args):
        super(Comp7SettingsPlugin, self).start(*args)
        periodCtrl = self.sessionProvider.shared.arenaPeriod
        arenaPeriod = periodCtrl.getPeriod() if periodCtrl else None
        if arenaPeriod:
            self.__onArenaPeriodChange(arenaPeriod)
        arena = self.sessionProvider.arenaVisitor.getArenaSubscription()
        if arena is not None:
            arena.onPeriodChange += self.__onArenaPeriodChange
        return

    def stop(self):
        arena = self.sessionProvider.arenaVisitor.getArenaSubscription()
        if arena is not None:
            arena.onPeriodChange -= self.__onArenaPeriodChange
        super(Comp7SettingsPlugin, self).stop()
        return

    def __onArenaPeriodChange(self, period, *_, **__):
        isBeforeBattle = period < ARENA_PERIOD.BATTLE
        self._overrides = self.__BEFORE_BATTLE_OVERRIDES if isBeforeBattle else {}
        self._additionalSettings = self.__ADDITIONAL_SETTINGS_BEFORE_BATTLE if isBeforeBattle else self.__ADDITIONAL_SETTINGS
        self._setMarkerSettings(notify=True)
        return


class Comp7VehicleMarkerPlugin(VehicleMarkerPlugin):
    __slots__ = ()

    def start(self):
        super(Comp7VehicleMarkerPlugin, self).start()
        prebattleCtrl = self.sessionProvider.dynamic.prebattleSetup
        if prebattleCtrl is not None:
            prebattleCtrl.onTeammateSelectionStatuses += self.__onTeammateSelectionStatuses
            prebattleCtrl.onBattleStarted += self.__onBattleStarted
        return

    def stop(self):
        prebattleCtrl = self.sessionProvider.dynamic.prebattleSetup
        if prebattleCtrl is not None:
            prebattleCtrl.onTeammateSelectionStatuses -= self.__onTeammateSelectionStatuses
            prebattleCtrl.onBattleStarted -= self.__onBattleStarted
        super(Comp7VehicleMarkerPlugin, self).stop()
        return

    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        marker = self._markers.get(vInfoVO.vehicleID)
        if marker is not None:
            self.__setIsPlayerLoaded(marker, vInfoVO)
        return

    def updateVehiclesInfo(self, updated, arenaDP):
        super(Comp7VehicleMarkerPlugin, self).updateVehiclesInfo(updated, arenaDP)
        for _, vInfo in updated:
            vehicleID = vInfo.vehicleID
            if vehicleID not in self._markers:
                continue
            marker = self._markers[vehicleID]
            self.__setModeSpecificData(marker, vInfo)

        return

    def _getMarkerSymbol(self, _):
        return settings.Comp7markersSymbolsNames.COMP7_VEHICLE_MARKER

    def _setMarkerInitialState(self, marker, vInfo):
        super(Comp7VehicleMarkerPlugin, self)._setMarkerInitialState(marker, vInfo)
        self.__setModeSpecificData(marker, vInfo)
        return

    def _onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        super(Comp7VehicleMarkerPlugin, self)._onVehicleFeedbackReceived(eventID, vehicleID, value)
        arenaDP = self.sessionProvider.getArenaDP()
        if arenaDP is None or vehicleID not in self._markers:
            return
        marker = self._markers[vehicleID]
        vInfo = arenaDP.getVehicleInfo(vehicleID)
        handle = marker.getMarkerID()
        if eventID == FEEDBACK_EVENT_ID.VEHICLE_AOE_HEAL:
            self.__updateAoeHealMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_AOE_INSPIRE:
            self.__updateAoeInspireMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_RISKY_ATTACK_BUFF:
            self.__updateRiskyAttackBuffMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_RISKY_ATTACK_HEAL:
            self.__updateRiskyAttackHealMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_BERSERK:
            self.__updateBerserkMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_ALLY_SUPPORT:
            self.__updateAllySupportMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_HUNTER:
            self.__updateHunterMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_FAST_RECHARGE:
            self.__updateFastRechargeMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_JUGGERNAUT:
            self.__updateJuggernautMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_SURE_SHOT:
            self.__updateSureShotMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_CONCENTRATION:
            self.__updateConcentrationMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_SNIPER:
            self.__updateSniperMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_MARCH:
            self.__updateMarchMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_AGGRESSIVE_DETECTION:
            self.__updateAggressiveDetectionMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_POINT_RECON:
            self.__updatePointReconMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_RED_LINE:
            self.__updateRedLineMarker(vehicleID, handle, value)
        elif eventID == FEEDBACK_EVENT_ID.VEHICLE_DEAD:
            self.__setRoleSkillLevel(marker, vInfo)
        return

    def _getMarkerStatusPriority(self, markerState):
        aoeMarker = markerState.statusID in (
         BATTLE_MARKER_STATES.COMP7_AOE_INSPIRE_STATE, BATTLE_MARKER_STATES.COMP7_AOE_HEAL_STATE)
        if aoeMarker and markerState.isSourceVehicle:
            return -2
        try:
            return _COMP7_STATUS_EFFECTS_PRIORITY.index(markerState.statusID)
        except ValueError:
            return -1

        return

    def __setModeSpecificData(self, marker, vInfo):
        self.__setRole(marker, vInfo)
        self.__setRoleSkillLevel(marker, vInfo)
        self.__setIsPlayerLoaded(marker, vInfo)
        periodCtrl = self.sessionProvider.shared.arenaPeriod
        if periodCtrl is not None and periodCtrl.getPeriod() < ARENA_PERIOD.BATTLE:
            teamInfo = avatar_getter.getArena().teamInfo
            if teamInfo is not None:
                vehSwitchComponent = teamInfo.TeamInfoInBattleVehicleSwitch
                if vehSwitchComponent is not None:
                    vehStatus = vehSwitchComponent.statuses.get(vInfo.vehicleID, False)
                    self.__onTeammateSelectionStatuses({(vInfo.vehicleID): vehStatus})
        return

    def __setRole(self, marker, vInfo):
        role = vInfo.vehicleType.role
        roleName = ROLE_TYPE_TO_LABEL[role] if role != ROLE_TYPE.NOT_DEFINED else None
        self._invokeMarker(marker.getMarkerID(), b'setRoleName', roleName)
        return

    def __setRoleSkillLevel(self, marker, vInfo):
        if not marker.getIsPlayerTeam():
            return
        if marker.isAlive():
            roleSkillLevel = vInfo.gameModeSpecific.getValue(Comp7CoreKeys.ROLE_SKILL_LEVEL, default=0)
        else:
            roleSkillLevel = 0
        self._invokeMarker(marker.getMarkerID(), b'setRoleSkillLevel', roleSkillLevel)
        return

    def __setIsPlayerLoaded(self, marker, vInfo):
        self._invokeMarker(marker.getMarkerID(), b'setIsPlayerLoaded', vInfo.isReady())
        return

    def __updateAoeHealMarker(self, vehicleID, handle, state):
        showCountdown = state.get(b'isSourceVehicle', False)
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_AOE_HEAL_STATE, showCountdown=showCountdown)
        return

    def __updateAoeInspireMarker(self, vehicleID, handle, state):
        showCountdown = state.get(b'isSourceVehicle', False)
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_AOE_INSPIRE_STATE, showCountdown=showCountdown)
        return

    def __updateBerserkMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_BERSERK_STATE)
        return

    def __updateAllySupportMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_ALLY_SUPPORT_STATE)
        return

    def __updateHunterMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_HUNTER_STATE)
        return

    def __updateRiskyAttackBuffMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_RISKY_ATTACK_STATE)
        return

    def __updateRiskyAttackHealMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_RISKY_ATTACK_HEAL_STATE)
        return

    def __updateFastRechargeMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_FAST_RECHARGE_STATE)
        return

    def __updateJuggernautMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_JUGGERNAUT_STATE)
        return

    def __updateSureShotMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_SURE_SHOT_STATE)
        return

    def __updateConcentrationMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_CONCENTRATION_STATE)
        return

    def __updateSniperMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_SNIPER_STATE)
        return

    def __updateMarchMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_MARCH_STATE)
        return

    def __updateAggressiveDetectionMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_AGGRESSIVE_DETECTION_STATE)
        return

    def __updatePointReconMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_POINT_RECON_STATE)
        return

    def __updateRedLineMarker(self, vehicleID, handle, state):
        self.__updateAbilityMarker(vehicleID, state, handle, BATTLE_MARKER_STATES.COMP7_ARTYLLERY_SUPPORT_STATE)
        return

    def __updateConfirmedMarker(self, vehicleID, handle, isShown):
        self._updateStatusMarkerState(vehicleID=vehicleID, isShown=isShown, handle=handle, statusID=BATTLE_MARKER_STATES.CONFIRMED_STATE, duration=0, animated=True, isSourceVehicle=False, blinkAnim=False)
        return

    def __updateAbilityMarker(self, vehicleID, state, handle, stateID, showCountdown=False):
        vehicle = BigWorld.entities.get(vehicleID)
        if vehicle is None or not vehicle.isAlive():
            return
        show = not state.get(b'finishing', False)
        isSourceVehicle = state.get(b'isSourceVehicle', False)
        endTime = state.get(b'endTime', INVALID_TIMESTAMP)
        duration = max(endTime - BigWorld.serverTime(), 0) if show and endTime != INVALID_TIMESTAMP else 0
        self._updateMarkerTimer(vehicleID, handle=handle, duration=duration, statusID=stateID, showCountdown=showCountdown, isSourceVehicle=isSourceVehicle)
        return

    def __onTeammateSelectionStatuses(self, statuses):
        for vehicleID, status in statuses.iteritems():
            marker = self._markers.get(vehicleID)
            if marker is not None:
                self.__updateConfirmedMarker(vehicleID, marker.getMarkerID(), status)

        return

    def __onBattleStarted(self):
        statuses = {vehicleID: False for vehicleID in self._markers.iterkeys()}
        self.__onTeammateSelectionStatuses(statuses)
        return
