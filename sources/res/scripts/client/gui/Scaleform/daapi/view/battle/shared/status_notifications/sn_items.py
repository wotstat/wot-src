import typing, BigWorld
from AvatarInputHandler import AvatarInputHandler
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from constants import VEHICLE_MISC_STATUS
from constants import StunTypes
from gui.Scaleform.daapi.view.battle.shared.status_notifications.components import StatusNotificationItem
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE, TIMER_VIEW_STATE
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from items.utils import isclose
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from gui.battle_control.battle_constants import DestroyTimerViewState, DeathZoneTimerViewState

class LocalizationProvider(object):

    @property
    def _stringResource(self):
        raise NotImplementedError
        return


class TimeSnapshotHandler(object):

    def __init__(self, updateHandler):
        self._updateHandler = updateHandler
        self._startTime = 0
        return

    def setTimeParams(self, totalTime, finishTime):
        if finishTime:
            self._startTime = finishTime - totalTime
        else:
            self._startTime = BigWorld.serverTime()
        return

    def getCurrentTimeSnapshot(self):
        return BigWorld.serverTime() - self._startTime

    def destroy(self):
        self._updateHandler = None
        return


class SimpleSnapshotHandler(TimeSnapshotHandler):

    def setTimeParams(self, totalTime, finishTime):
        super(SimpleSnapshotHandler, self).setTimeParams(totalTime, finishTime)
        self._updateHandler(self.getCurrentTimeSnapshot(), totalTime)
        return


class VehicleStateSN(StatusNotificationItem):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)
    _HIDE_STATES_TRIGGERS = (
     VEHICLE_VIEW_STATE.DESTROYED, VEHICLE_VIEW_STATE.CREW_DEACTIVATED, VEHICLE_VIEW_STATE.SWITCHING)

    def start(self):
        super(VehicleStateSN, self).start()
        ctrl = self._sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleStateUpdated += self.__onVehicleStateUpdated
            contextID = self._getEquipmentName()
            if contextID:
                ctrl.onEquipmentComponentUpdated.subscribe(self.__onEquipmentComponentUpdated, contextID)
        handler = avatar_getter.getInputHandler()
        if handler is not None:
            if isinstance(handler, AvatarInputHandler):
                handler.onCameraChanged += self.__onCameraChanged
        return

    def _subscribeOnVehControlling(self):
        ctrl = self._sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleControlling += self._onVehicleControlling
            vehicle = ctrl.getControllingVehicle()
            if vehicle is not None:
                self._onVehicleControlling(vehicle)
        return

    def destroy(self):
        ctrl = self._sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onVehicleStateUpdated -= self.__onVehicleStateUpdated
            ctrl.onVehicleControlling -= self._onVehicleControlling
            ctrl.onEquipmentComponentUpdated.unsubscribe(self.__onEquipmentComponentUpdated)
        handler = avatar_getter.getInputHandler()
        if handler is not None:
            if isinstance(handler, AvatarInputHandler):
                handler.onCameraChanged -= self.__onCameraChanged
        super(VehicleStateSN, self).destroy()
        return

    def _getTitle(self, value):
        return b''

    def _getDescription(self, value):
        return b''

    def _getEquipmentName(self):
        return b''

    def _onVehicleControlling(self, vehicle):
        ctrl = self._sessionProvider.shared.vehicleState
        stateValue = ctrl.getStateValue(self.getItemID())
        if stateValue:
            self.__update(stateValue)
        return

    def _updateText(self, value):
        self._vo[b'title'] = self._getTitle(value)
        self._vo[b'description'] = self._getDescription(value)
        return

    def _update(self, value):
        return

    def __onCameraChanged(self, ctrlMode, vehicleID=None):
        if ctrlMode == b'video':
            self._hide()
        return

    def __onVehicleStateUpdated(self, state, value):
        if state in self._HIDE_STATES_TRIGGERS:
            self._hide()
        elif state == self.getItemID():
            self.__update(value)
        return

    def __onEquipmentComponentUpdated(self, _, vehicleID, equipmentInfo):
        if vehicleID == BigWorld.player().getObservedVehicleID():
            self._update(equipmentInfo)
        return

    def __update(self, value):
        self._updateText(value)
        self._update(value)
        return


class TimerSN(VehicleStateSN):

    def __init__(self, updateCallback):
        super(TimerSN, self).__init__(updateCallback)
        self.__timeHandler = SimpleSnapshotHandler(self.__applySnapshot)
        return

    def setTimeHandler(self, clazz):
        self.__destroyHandler()
        self.__timeHandler = clazz(self.__applySnapshot)
        return

    def destroy(self):
        self.__destroyHandler()
        super(TimerSN, self).destroy()
        return

    def getVO(self):
        vo = super(TimerSN, self).getVO()
        self._vo[b'currentTime'] = self.__timeHandler.getCurrentTimeSnapshot()
        return vo

    def _updateTimeParams(self, totalTime, finishTime):
        self.__timeHandler.setTimeParams(totalTime, finishTime)
        return

    def __applySnapshot(self, currTime, totalTime, isUpdateRequired=False):
        self._vo[b'currentTime'] = currTime
        self._vo[b'totalTime'] = totalTime
        if isUpdateRequired:
            self._sendUpdate()
        return

    def __destroyHandler(self):
        if self.__timeHandler:
            self.__timeHandler.destroy()
        self.__timeHandler = None
        return


class _DestroyTimerSN(TimerSN):
    _ANY_SUPPORTED_LEVEL = b'anySupportedLevel'

    def start(self):
        super(_DestroyTimerSN, self).start()
        self._subscribeOnVehControlling()
        return

    def _getSupportedLevel(self):
        raise NotImplementedError
        return


class _DeathZoneSN(LocalizationProvider, _DestroyTimerSN):

    def getItemID(self):
        return VEHICLE_VIEW_STATE.DEATHZONE_TIMER

    def _getDescription(self, value):
        return backport.text(self._stringResource.deathZone())

    def _canBeShown(self, value):
        return self._getSupportedLevel() == value.level

    def _update(self, value):
        if self._canBeShown(value):
            self._isVisible = True
            self._updateTimeParams(value.totalTime, value.finishTime)
            self._sendUpdate()
            return
        self._setVisible(False)
        return


class StaticDeathZoneSN(_DestroyTimerSN):

    def getItemID(self):
        return VEHICLE_VIEW_STATE.DEATHZONE

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.SECTOR_AIRSTRIKE

    def _getDescription(self, value):
        return backport.text(R.strings.ingame_gui.statusNotificationTimers.staticDeathZone())

    def _update(self, value):
        visible, playerEntering, strikeTime, waveDuration = value
        self._isVisible = visible
        if playerEntering:
            self._updateTimeParams(waveDuration, strikeTime)
        else:
            self._updateTimeParams(0, 0)
        self._sendUpdate()
        return

    def _getSupportedLevel(self):
        return


class DeathZoneDamagingSN(_DeathZoneSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.DAMAGING_ZONE

    def _canBeShown(self, value):
        if super(DeathZoneDamagingSN, self)._canBeShown(value):
            vehicle = self._sessionProvider.shared.vehicleState.getControllingVehicle()
            isAlive = vehicle is not None and vehicle.isAlive()
            return value.isCausingDamage and isAlive
        else:
            return False

    def _getSupportedLevel(self):
        return


class DeathZoneDangerSN(_DeathZoneSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.DEATH_ZONE

    def _canBeShown(self, value):
        if super(DeathZoneDangerSN, self)._canBeShown(value):
            return value.needToShow()
        return False

    def _getSupportedLevel(self):
        return TIMER_VIEW_STATE.CRITICAL


class DeathZoneWarningSN(_DeathZoneSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.ORANGE_ZONE

    def _canBeShown(self, value):
        if super(DeathZoneWarningSN, self)._canBeShown(value):
            return value.needToShow()
        return False

    def _getSupportedLevel(self):
        return TIMER_VIEW_STATE.WARNING


class DestroyMiscTimerSN(_DestroyTimerSN):

    def getItemID(self):
        return VEHICLE_VIEW_STATE.DESTROY_TIMER

    def _getSupportedMiscStatus(self):
        raise NotImplementedError
        return

    def _update(self, value):
        if value.needToCloseAll():
            self._setVisible(False)
            return
        level = value.level
        supportedLevel = self._getSupportedLevel()
        if self._getSupportedMiscStatus() == value.code:
            if value.needToCloseTimer():
                self._setVisible(False)
            elif supportedLevel == self._ANY_SUPPORTED_LEVEL or supportedLevel == level:
                if not value.needToCloseTimer():
                    self._isVisible = True
                    self._updateTimeParams(value.totalTime, 0)
                    self._sendUpdate()
                    return
                self._setVisible(False)
        return


class _OverturnedBaseSN(LocalizationProvider, DestroyMiscTimerSN):

    def __init__(self, updateCallback):
        super(_OverturnedBaseSN, self).__init__(updateCallback)
        self._vo[b'description'] = self._getDescription()
        return

    def _getSupportedMiscStatus(self):
        return VEHICLE_MISC_STATUS.VEHICLE_IS_OVERTURNED

    def _getDescription(self, value=None):
        liftOverEnabled = ARENA_BONUS_TYPE_CAPS.checkAny(BigWorld.player().arenaBonusType, ARENA_BONUS_TYPE_CAPS.LIFT_OVER)
        if liftOverEnabled:
            return backport.text(R.strings.ingame_gui.destroyTimer.liftOver())
        return b''


class OverturnedSN(_OverturnedBaseSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.OVERTURNED

    def _getSupportedLevel(self):
        return TIMER_VIEW_STATE.CRITICAL


class HalfOverturnedSN(_OverturnedBaseSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.HALF_OVERTURNED

    def _getSupportedLevel(self):
        return TIMER_VIEW_STATE.WARNING


class DrownSN(DestroyMiscTimerSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.DROWN

    def _getSupportedLevel(self):
        return self._ANY_SUPPORTED_LEVEL

    def _getSupportedMiscStatus(self):
        return VEHICLE_MISC_STATUS.VEHICLE_DROWN_WARNING


class UnderFireSN(VehicleStateSN):

    def start(self):
        super(UnderFireSN, self).start()
        self._subscribeOnVehControlling()
        return

    def getItemID(self):
        return VEHICLE_VIEW_STATE.UNDER_FIRE

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.UNDER_FIRE

    def _update(self, isUnderFire):
        self._setVisible(isUnderFire)
        return


class FireSN(VehicleStateSN):

    def start(self):
        super(FireSN, self).start()
        self._subscribeOnVehControlling()
        return

    def getItemID(self):
        return VEHICLE_VIEW_STATE.FIRE

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.FIRE

    def _update(self, isInFire):
        self._setVisible(isInFire)
        return


class StunSN(TimerSN):

    def __init__(self, updateCallback):
        super(StunSN, self).__init__(updateCallback)
        self._vo[b'title'] = backport.text(R.strings.ingame_gui.stun.indicator())
        return

    def start(self):
        super(StunSN, self).start()
        self._subscribeOnVehControlling()
        return

    def getItemID(self):
        return VEHICLE_VIEW_STATE.STUN

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.STUN

    def _update(self, value):
        if value.duration > 0.0 and value.stunType == self._getStunType():
            self._updateTimeParams(value.totalTime, value.endTime)
            self._isVisible = True
            self._sendUpdate()
        else:
            self._setVisible(False)
        return

    def _getTitle(self, value):
        return backport.text(R.strings.ingame_gui.stun.indicator())

    def _getStunType(self):
        return StunTypes.DEFAULT.value


class StunFlameSN(StunSN):

    def __init__(self, updateCallback):
        super(StunFlameSN, self).__init__(updateCallback)
        self._vo[b'title'] = backport.text(R.strings.ingame_gui.stunFlame.indicator())
        return

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.STUN_FLAME

    def _getTitle(self, value):
        return backport.text(R.strings.ingame_gui.stunFlame.indicator())

    def _getStunType(self):
        return StunTypes.FLAME.value


class ThermalWarningSN(TimerSN):

    def getItemID(self):
        return VEHICLE_VIEW_STATE.THERMAL_VISION_WARNING

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.THERMAL_VISION_WARNING

    def _update(self, value):
        startTime, duration = value
        isVisible = not (isclose(startTime, duration) and isclose(startTime, 0))
        self._updateTimeParams(duration, startTime + duration)
        self._setVisible(isVisible)
        return


class _SmokeBase(LocalizationProvider, TimerSN):

    def start(self):
        super(_SmokeBase, self).start()
        self._subscribeOnVehControlling()
        return

    def getItemID(self):
        return VEHICLE_VIEW_STATE.SMOKE

    def _update(self, smokesInfo):
        endTime, equipment = self._getSmokeData(smokesInfo)
        if endTime is None:
            if self._isVisible:
                self._setVisible(False)
            return
        self._updateTimeParams(equipment.expireDelay if smokesInfo[b'expiring'] else equipment.totalDuration, endTime)
        self._isVisible = True
        self._sendUpdate()
        return

    def _getSmokeData(self, smokesInfo):
        raise NotImplementedError
        return


class SmokeSN(_SmokeBase):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.SMOKE

    def _getTitle(self, value):
        return backport.text(self._stringResource.smoke.ally())


class EnemySmokeSN(_SmokeBase):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.DAMAGING_SMOKE

    def _getTitle(self, value):
        return backport.text(self._stringResource.smoke.enemy())


class DamagingSmokeSN(_SmokeBase):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.DAMAGING_SMOKE

    def _getTitle(self, value):
        return backport.text(self._stringResource.smoke.damaging())


class BuffSN(LocalizationProvider, TimerSN):

    def _getInActivationState(self):
        raise NotImplementedError
        return

    def _updateTimeValues(self, value):
        self._updateTimeParams(value.get(b'duration'), value.get(b'endTime'))
        return

    def _isValidForUpdateVisibility(self, value):
        isInactivation = value.get(b'isInactivation')
        return isInactivation is not None and self._getInActivationState() == isInactivation

    def _update(self, value):
        if self._isValidForUpdateVisibility(value):
            self._isVisible = True
            self._updateTimeValues(value)
            self._sendUpdate()
            return
        self._setVisible(False)
        return


class _BaseHealingSN(BuffSN):

    def getItemID(self):
        return VEHICLE_VIEW_STATE.HEALING


class HealingSN(_BaseHealingSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.HEALING

    def _getInActivationState(self):
        return False

    def _getTitle(self, value):
        healingString = self._stringResource.healPoint.healing
        beingHealedString = self._stringResource.healPoint.healed
        isSourceVehicle = value.get(b'isSourceVehicle', False)
        if isSourceVehicle:
            return backport.text(healingString())
        return backport.text(beingHealedString())


class HealingCooldownSN(_BaseHealingSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.HEALING_CD

    def _getInActivationState(self):
        return True

    def _getTitle(self, value):
        return backport.text(self._stringResource.healPoint.healed())


class _BaseRepairingSN(BuffSN):

    def getItemID(self):
        return VEHICLE_VIEW_STATE.REPAIR_POINT

    def _getTitle(self, value):
        return backport.text(self._stringResource.repairPoint())


class RepairingSN(_BaseRepairingSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.REPAIRING

    def _getInActivationState(self):
        return False


class RepairingCooldownSN(_BaseRepairingSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.REPAIRING_CD

    def _getInActivationState(self):
        return True


class _InspireBaseSN(BuffSN):

    def start(self):
        super(_InspireBaseSN, self).start()
        self._subscribeOnVehControlling()
        return

    def getItemID(self):
        return VEHICLE_VIEW_STATE.INSPIRE

    def _shouldProcessInspireSource(self):
        return False

    def _isValidForUpdateVisibility(self, value):
        isValidForUpdateVisibility = super(_InspireBaseSN, self)._isValidForUpdateVisibility(value)
        primary = bool(value.get(b'primary', 1))
        isSourceVehicle = bool(value.get(b'isSourceVehicle', 0))
        isValidSource = isSourceVehicle is self._shouldProcessInspireSource()
        return isValidForUpdateVisibility and primary and isValidSource

    def _getTitle(self, value):
        return backport.text(self._stringResource.inspire.inspired())


class InspireSN(_InspireBaseSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.INSPIRE

    def _getInActivationState(self):
        return False


class InspireCooldownSN(_InspireBaseSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.INSPIRE_CD

    def _getInActivationState(self):
        return True


class InspireSourceSN(_InspireBaseSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.INSPIRE_SOURCE

    def _getTitle(self, value):
        return backport.text(self._stringResource.inspire.inspiring())

    def _shouldProcessInspireSource(self):
        return True

    def _getInActivationState(self):
        return False


class InspireInactivationSourceSN(InspireSourceSN):

    def getViewTypeID(self):
        return BATTLE_NOTIFICATIONS_TIMER_TYPES.INSPIRE_INACTIVATION_SOURCE

    def _getInActivationState(self):
        return True
