import logging, typing, BigWorld
from constants import AUTORELOADER_SURGE_RESTRICTION, BUSTLE_FEED_SWITCH_ACCESS, OVERHEAT_GAIN_STATE, SIGHT_POINTER_COMMON_CONSTANTS, TARGET_DESIGNATOR_STATE
from events_handler import eventHandler
from vehicles.mechanics.generic_mechanics.wheeled_dash import IWheeledDashListenerLogic
from vehicles.mechanics.mechanic_commands import IMechanicCommandsListenerLogic
from vehicles.mechanics.mechanic_constants import VEHICLE_MECHANIC_USED_COMMANDS, VehicleMechanic
from visual_script.block import Block
from visual_script.dependency import dependencyImporter
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE
from visual_script.vehicle_mechanics_blocks import AcceleratorStatusEnum, BustleFeedStateEnum, ConcentrationModeStateEnum, HeatingZonesGunEnum, LowChargeShotStateEnum, OverheatGainStateEnum, OverheatGunEnum, PhasedMechanicStateEnum, PowerModeStateEnum, PropellantGunEnum, RechargeableNitroStateEnum, SecondaryGunStateEnum, SightPointerStateEnum, StationaryReloadEnum, StationaryReloadLockEnum, TargetDesignatorStateEnum, TemperatureGunEnum, VehicleMechanicsMeta, VehicleSiegeStateEnum, WheeledDashDirectionEnum, ShellParamsSwitcherGunEnum, AutoreloaderSurgeStateEnum
from visual_script_client.vehicle_mechanics_common import VehicleMechanicEventsBlock, VehicleMechanicLifeCycleEventsBlock, VehicleMechanicStateEventsBlock, VehicleSelectableMechanicEventsBlock
cgf_helpers, = dependencyImporter(b'cgf_common.cgf_helpers')
if typing.TYPE_CHECKING:
    from typing import Any, List
    from AccuracyStacksController import AccuracyStacksState
    from BattleFuryController import BattleFuryState
    from ChargeShotComponent import ChargeShotState
    from ConcentrationModeComponent import ConcentrationModeState
    from vehicles.mechanics.generic_mechanics.bustle_feed import BustleFeedState
    from items.components.shared_components import ChargeShotParams
    from LowChargeShotController import LowChargeShotMechanicState
    from OverheatStacksController import OverheatStacksState
    from PillboxSiegeComponent import PillboxSiegeModeState
    from PowerModeController import PowerModeState
    from RechargeableNitroController import RechargeableNitroState
    from SightPointerComponent import SightPointerState
    from StagedJetBoostersController import StagedJetBoostersState
    from StanceDanceController import StanceDanceState
    from StationaryReloadController import StationaryReloadModeState
    from SupportWeaponComponent import SupportWeaponState
    from TargetDesignatorController import TargetDesignatorState
    from TemperatureGunController import TemperatureGunMechanicState
    from vehicles.mechanics.gun_mechanics.propellant_gun import IPropellantGunMechanicState
    from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun import IHeatingZonesGunMechanicState
    from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import IOverheatGunComponentParams, IOverheatGunMechanicState
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand
    from WheeledDashController import WheeledDashState
    from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher import AuxiliaryRocketLauncherState
    from ShellCalibrationController import ShellCalibrationModeState
    from AutoreloaderSurgeController import AutoreloaderSurgeState
_logger = logging.getLogger(__name__)

class ServerTime(Block):

    def __init__(self, *args, **kwargs):
        super(ServerTime, self).__init__(*args, **kwargs)
        self._currentTimestamp = self._makeDataOutputSlot(b'currentTimestamp', SLOT_TYPE.FLOAT, self._execValue)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/time'

    @classmethod
    def blockCategory(cls):
        return b'Time'

    def _execValue(self):
        self._currentTimestamp.setValue(BigWorld.serverTime())
        return


class OnVehicleMechanicCommand(VehicleSelectableMechanicEventsBlock, IMechanicCommandsListenerLogic):
    _EVENTS_NAME = b'commands'

    def __init__(self, *args, **kwargs):
        super(OnVehicleMechanicCommand, self).__init__(*args, **kwargs)
        self._commands = {command: self._makeEventOutputSlot(command.value) for command in VEHICLE_MECHANIC_USED_COMMANDS[self._vehicleMechanic]}
        return

    @eventHandler
    def onMechanicComponentCatching(self, component):
        self.subscribeTo(component.commandsEvents)
        return

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        self.unsubscribeFrom(component.commandsEvents)
        return

    @eventHandler
    def onMechanicCommand(self, command):
        self._commands[command].call()
        return

    @classmethod
    def _getInitParamMechanics(cls):
        return sorted(mechanic.value for mechanic in VEHICLE_MECHANIC_USED_COMMANDS)


class OnConcentrationModeState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnConcentrationModeState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', ConcentrationModeStateEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.CONCENTRATION_MODE

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        return

    def _onStateObservation(self, state):
        self._state.setValue(state.state)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.state)
        return


class OnPowerModeState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnPowerModeState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', PowerModeStateEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.POWER_MODE

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.state)
        return

    def _onStateObservation(self, state):
        self._state.setValue(state.state)
        return


class OnPillboxSiegeModeState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnPillboxSiegeModeState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', VehicleSiegeStateEnum.slotType(), None)
        self._nextState = self._makeDataOutputSlot(b'nextState', VehicleSiegeStateEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.PILLBOX_SIEGE_MODE

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        self._nextState.setValue(state.nextState)
        return

    def _onStateObservation(self, state):
        self._state.setValue(state.state)
        self._nextState.setValue(state.nextState)
        return

    def _onStateTransition(self, _, newState):
        self._state.setValue(newState.state)
        self._nextState.setValue(newState.nextState)
        return


class OnRechargeableNitroState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnRechargeableNitroState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', RechargeableNitroStateEnum.slotType(), None)
        self._isCharged = self._makeDataOutputSlot(b'isCharged', SLOT_TYPE.BOOL, None)
        self._isEmpty = self._makeDataOutputSlot(b'isEmpty', SLOT_TYPE.BOOL, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.RECHARGEABLE_NITRO

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._isCharged.setValue(state.isCharged)
        self._isEmpty.setValue(state.isEmpty)
        return

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, prevState, newState):
        self.__forwardStateToVSE(newState)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return


class OnBattleFuryState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnBattleFuryState, self).__init__(*args, **kwargs)
        self._prevLevelSlot = self._makeDataOutputSlot(b'prevLevel', SLOT_TYPE.INT, None)
        self._levelSlot = self._makeDataOutputSlot(b'level', SLOT_TYPE.INT, None)
        self._maxLevel = self._makeDataOutputSlot(b'maxLevel', SLOT_TYPE.INT, None)
        self._prevEndTimeSlot = self._makeDataOutputSlot(b'prevEndTime', SLOT_TYPE.FLOAT, None)
        self._endTimeSlot = self._makeDataOutputSlot(b'endTime', SLOT_TYPE.FLOAT, None)
        self._prevLevel = 0
        self._level = 0
        self._prevEndTime = 0.0
        self._endTime = 0.0
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.BATTLE_FURY

    def __recacheState(self, newState):
        self._prevLevel = self._level
        self._level = newState.level
        self._prevEndTime = self._endTime
        self._endTime = newState.endTime
        return

    def __setSlots(self):
        self._prevLevelSlot.setValue(self._prevLevel)
        self._levelSlot.setValue(self._level)
        self._prevEndTimeSlot.setValue(self._prevEndTime)
        self._endTimeSlot.setValue(self._endTime)
        return

    def _onStateObservation(self, state):
        self.__recacheState(state)
        self.__setSlots()
        return

    def _onStatePrepared(self, state):
        self.__recacheState(state)
        self.__setSlots()
        self._maxLevel.setValue(state.maxLevel)
        return

    def _onStateTransition(self, prevState, newState):
        self.__recacheState(newState)
        self.__setSlots()
        return


class OnOverheatStacksState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnOverheatStacksState, self).__init__(*args, **kwargs)
        self._prevGainState = self._makeDataOutputSlot(b'prevGainState', OverheatGainStateEnum.slotType(), None)
        self._gainState = self._makeDataOutputSlot(b'gainState', OverheatGainStateEnum.slotType(), None)
        self._prevLevel = self._makeDataOutputSlot(b'prevLevel', SLOT_TYPE.INT, None)
        self._level = self._makeDataOutputSlot(b'level', SLOT_TYPE.INT, None)
        self._maxLevel = self._makeDataOutputSlot(b'maxLevel', SLOT_TYPE.INT, None)
        self._prevGainState.setValue(OVERHEAT_GAIN_STATE.NULL_STATE)
        self._gainState.setValue(OVERHEAT_GAIN_STATE.NULL_STATE)
        self._prevLevel.setValue(0)
        self._level.setValue(0)
        self._maxLevel.setValue(0)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.OVERHEAT_STACKS

    def _onStatePrepared(self, state):
        self._gainState.setValue(state.gainState)
        self._level.setValue(state.level)
        self._maxLevel.setValue(state.maxLevel)
        return

    def _onStateObservation(self, state):
        self._gainState.setValue(state.gainState)
        self._level.setValue(state.level)
        return

    def _onStateTransition(self, prevState, newState):
        self._prevGainState.setValue(prevState.gainState)
        self._gainState.setValue(newState.gainState)
        self._prevLevel.setValue(prevState.level)
        self._level.setValue(newState.level)
        return


class OnAccuracyStacksState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnAccuracyStacksState, self).__init__(*args, **kwargs)
        self._prevIsGainingActive = self._makeDataOutputSlot(b'prevIsGainingActive', SLOT_TYPE.BOOL, None)
        self._isGainingActive = self._makeDataOutputSlot(b'isGainingActive', SLOT_TYPE.BOOL, None)
        self._prevLevel = self._makeDataOutputSlot(b'prevLevel', SLOT_TYPE.INT, None)
        self._level = self._makeDataOutputSlot(b'level', SLOT_TYPE.INT, None)
        self._maxLevel = self._makeDataOutputSlot(b'maxLevel', SLOT_TYPE.INT, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.ACCURACY_STACKS

    def _onStatePrepared(self, state):
        self._prevIsGainingActive.setValue(False)
        self._isGainingActive.setValue(state.isGainingActive)
        self._prevLevel.setValue(0)
        self._level.setValue(state.level)
        self._maxLevel.setValue(state.maxLevel)
        return

    def _onStateObservation(self, state):
        self._prevIsGainingActive.setValue(state.isGainingActive)
        self._isGainingActive.setValue(state.isGainingActive)
        self._prevLevel.setValue(state.level)
        self._level.setValue(state.level)
        self._maxLevel.setValue(state.maxLevel)
        return

    def _onStateTransition(self, prevState, newState):
        self._prevIsGainingActive.setValue(prevState.isGainingActive)
        self._isGainingActive.setValue(newState.isGainingActive)
        self._prevLevel.setValue(prevState.level)
        self._level.setValue(newState.level)
        self._maxLevel.setValue(newState.maxLevel)
        return


class OnSupportWeaponState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnSupportWeaponState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', SecondaryGunStateEnum.slotType(), None)
        self._timeLeft = self._makeDataOutputSlot(b'timeLeft', SLOT_TYPE.FLOAT, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.SUPPORT_WEAPON

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        self._timeLeft.setValue(state.timeLeft)
        return

    def _onStateObservation(self, state):
        self._state.setValue(state.state)
        self._timeLeft.setValue(state.timeLeft)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.state)
        self._timeLeft.setValue(newState.timeLeft)
        return


class OnStanceDanceState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnStanceDanceState, self).__init__(*args, **kwargs)
        self._isFightState = self._makeDataOutputSlot(b'isFightState', SLOT_TYPE.BOOL, None)
        self._isTurboState = self._makeDataOutputSlot(b'isTurboState', SLOT_TYPE.BOOL, None)
        self._isActiveFightState = self._makeDataOutputSlot(b'isActiveFightState', SLOT_TYPE.BOOL, None)
        self._isActiveTurboState = self._makeDataOutputSlot(b'isActiveTurboState', SLOT_TYPE.BOOL, None)
        self._isEngineDeadState = self._makeDataOutputSlot(b'isEngineDeadState', SLOT_TYPE.BOOL, None)
        self._isSwitchingState = self._makeDataOutputSlot(b'isSwitchingState', SLOT_TYPE.BOOL, None)
        self._fightEnergyRatio = self._makeDataOutputSlot(b'fightEnergyRatio', SLOT_TYPE.FLOAT, None)
        self._turboEnergyRatio = self._makeDataOutputSlot(b'turboEnergyRatio', SLOT_TYPE.FLOAT, None)
        self._isEnoughEnergyToActivate = self._makeDataOutputSlot(b'isEnoughEnergyToActivate', SLOT_TYPE.BOOL, None)
        self._prevIsFightState = self._makeDataOutputSlot(b'prevIsFightState', SLOT_TYPE.BOOL, None)
        self._prevIsTurboState = self._makeDataOutputSlot(b'prevIsTurboState', SLOT_TYPE.BOOL, None)
        self._prevIsActiveFightState = self._makeDataOutputSlot(b'prevIsActiveFightState', SLOT_TYPE.BOOL, None)
        self._prevIsActiveTurboState = self._makeDataOutputSlot(b'prevIsActiveTurboState', SLOT_TYPE.BOOL, None)
        self._prevIsEngineDeadState = self._makeDataOutputSlot(b'prevIsEngineDeadState', SLOT_TYPE.BOOL, None)
        self._prevIsSwitchingState = self._makeDataOutputSlot(b'prevIsSwitchingState', SLOT_TYPE.BOOL, None)
        self._isFightState.setValue(False)
        self._isTurboState.setValue(False)
        self._isActiveFightState.setValue(False)
        self._isActiveTurboState.setValue(False)
        self._isEngineDeadState.setValue(False)
        self._isSwitchingState.setValue(False)
        self._fightEnergyRatio.setValue(0.0)
        self._turboEnergyRatio.setValue(0.0)
        self._isEnoughEnergyToActivate.setValue(False)
        self._prevIsFightState.setValue(False)
        self._prevIsTurboState.setValue(False)
        self._prevIsActiveFightState.setValue(False)
        self._prevIsActiveTurboState.setValue(False)
        self._prevIsEngineDeadState.setValue(False)
        self._prevIsSwitchingState.setValue(False)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.STANCE_DANCE

    def _onStatePrepared(self, state):
        self.__updateCurrentState(state)
        self.__updatePrevState(state)
        return

    def _onStateObservation(self, state):
        self.__updateCurrentState(state)
        self.__updatePrevState(state)
        return

    def _onStateTransition(self, prevState, newState):
        self.__updateCurrentState(newState)
        self.__updatePrevState(prevState)
        return

    def __updateCurrentState(self, state):
        self._isFightState.setValue(state.isFightState)
        self._isTurboState.setValue(state.isTurboState)
        self._isActiveFightState.setValue(state.isActiveFightState)
        self._isActiveTurboState.setValue(state.isActiveTurboState)
        self._isEngineDeadState.setValue(state.isEngineDeadState)
        self._isSwitchingState.setValue(state.isSwitchingState)
        self._fightEnergyRatio.setValue(state.getFightEnergyRatio)
        self._turboEnergyRatio.setValue(state.getTurboEnergyRatio)
        self._isEnoughEnergyToActivate.setValue(state.isEnoughEnergyToActivate)
        return

    def __updatePrevState(self, state):
        self._prevIsFightState.setValue(state.isFightState)
        self._prevIsTurboState.setValue(state.isTurboState)
        self._prevIsActiveFightState.setValue(state.isActiveFightState)
        self._prevIsActiveTurboState.setValue(state.isActiveTurboState)
        self._prevIsEngineDeadState.setValue(state.isEngineDeadState)
        self._prevIsSwitchingState.setValue(state.isSwitchingState)
        return


class OnChargeShotState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnChargeShotState, self).__init__(*args, **kwargs)
        self._level = self._makeDataOutputSlot(b'level', SLOT_TYPE.INT, None)
        self._isCharging = self._makeDataOutputSlot(b'isCharging', SLOT_TYPE.BOOL, None)
        self._isShotBlock = self._makeDataOutputSlot(b'isShotBlock', SLOT_TYPE.BOOL, None)
        self._canStart = self._makeDataOutputSlot(b'canStart', SLOT_TYPE.BOOL, None)
        self._isGunDestroyed = self._makeDataOutputSlot(b'isGunDestroyed', SLOT_TYPE.BOOL, None)
        self._prevLevel = self._makeDataOutputSlot(b'prevLevel', SLOT_TYPE.INT, None)
        self._prevIsCharging = self._makeDataOutputSlot(b'prevIsCharging', SLOT_TYPE.BOOL, None)
        self._prevIsShotBlock = self._makeDataOutputSlot(b'prevIsShotBlock', SLOT_TYPE.BOOL, None)
        self._prevIsGunDestroyed = self._makeDataOutputSlot(b'prevIsGunDestroyed', SLOT_TYPE.BOOL, None)
        self._level.setValue(0)
        self._isCharging.setValue(False)
        self._isShotBlock.setValue(False)
        self._canStart.setValue(False)
        self._prevLevel.setValue(0)
        self._prevIsCharging.setValue(False)
        self._prevIsShotBlock.setValue(False)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.CHARGE_SHOT

    def _onStatePrepared(self, state):
        self.__updateStateParams(state)
        return

    def _onStateObservation(self, state):
        self.__updateStateParams(state)
        return

    def _onStateTransition(self, prevState, newState):
        self._prevLevel.setValue(prevState.level)
        self._prevIsCharging.setValue(prevState.hasCharging)
        self._prevIsShotBlock.setValue(prevState.hasShotBlock)
        self._prevIsGunDestroyed.setValue(prevState.isGunDestroyed)
        self.__updateStateParams(newState)
        return

    def __updateStateParams(self, currentState):
        self._level.setValue(currentState.level)
        self._isCharging.setValue(currentState.hasCharging)
        self._isShotBlock.setValue(currentState.hasShotBlock)
        self._canStart.setValue(currentState.canStart)
        self._isGunDestroyed.setValue(currentState.isGunDestroyed)
        return


class OnChargeShotParams(VehicleMechanicLifeCycleEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnChargeShotParams, self).__init__(*args, **kwargs)
        self._maxLevel = self._makeDataOutputSlot(b'maxLevel', SLOT_TYPE.INT, None)
        self._maxLevel.setValue(0)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.CHARGE_SHOT

    @eventHandler
    def _onComponentParamsCollected(self, component):
        self._maxLevel.setValue(component.maxLevel)
        return


class OnTargetDesignatorState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnTargetDesignatorState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', TargetDesignatorStateEnum.slotType(), None)
        self._prevState = self._makeDataOutputSlot(b'prevState', TargetDesignatorStateEnum.slotType(), None)
        self._endTime = self._makeDataOutputSlot(b'endTime', SLOT_TYPE.FLOAT, None)
        self._state.setValue(TARGET_DESIGNATOR_STATE.COOLDOWN)
        self._prevState.setValue(TARGET_DESIGNATOR_STATE.COOLDOWN)
        self._endTime.setValue(0.0)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.TARGET_DESIGNATOR

    def _onStatePrepared(self, state):
        self.__updateState(state)
        return

    def _onStateObservation(self, state):
        self.__updateState(state)
        return

    def _onStateTransition(self, prevState, newState):
        self._prevState.setValue(prevState.state)
        self.__updateState(newState)
        return

    def __updateState(self, state):
        self._state.setValue(state.state)
        self._endTime.setValue(state.endTime)
        return


class OnStationaryReloadState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnStationaryReloadState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', StationaryReloadEnum.slotType(), None)
        self._lockState = self._makeDataOutputSlot(b'lockState', StationaryReloadLockEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.STATIONARY_RELOAD

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        self._lockState.setValue(state.gunLockMask)
        return

    def _onStateObservation(self, state):
        self._state.setValue(state.state)
        self._lockState.setValue(state.gunLockMask)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.state)
        self._lockState.setValue(newState.gunLockMask)
        return


class GetTemperatureTimeLeft(Block, VehicleMechanicsMeta):

    def __init__(self, *args, **kwargs):
        super(GetTemperatureTimeLeft, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        self._object = self._makeDataInputSlot(b'gameObjectLink', SLOT_TYPE.GAME_OBJECT)
        self._targetTemp = self._makeDataInputSlot(b'targetTemperature', SLOT_TYPE.FLOAT)
        self._cooldownTime = self._makeDataOutputSlot(b'cooldownTime', SLOT_TYPE.FLOAT, None)
        return

    def _execute(self):
        vehicleGameObject = self._object.getValue()
        if vehicleGameObject is not None:
            vehicle = cgf_helpers.getVehicleEntityByVehicleGameObject(vehicleGameObject)
            controller = vehicle.getVehicleMechanicComponent(VehicleMechanic.TEMPERATURE_GUN)
            if controller is not None:
                targetTemp = self._targetTemp.getValue()
                cdTime = controller.getMechanicState().getCoolingTime(targetTemp)
                self._cooldownTime.setValue(cdTime)
            else:
                _logger.debug(b'Could not find temperature gun controller')
                self._cooldownTime.setValue(-1.0)
        else:
            _logger.debug(b'Vehicle game object is None')
            self._cooldownTime.setValue(-1.0)
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnTemperatureGunState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnTemperatureGunState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', TemperatureGunEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.TEMPERATURE_GUN

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.state)
        return


class OnOverheatGunState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnOverheatGunState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', OverheatGunEnum.slotType(), None)
        self._prevState = self._makeDataOutputSlot(b'prevState', OverheatGunEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.OVERHEAT_GUN

    def _onStatePrepared(self, state):
        self._state.setValue(state.overheatState)
        self._prevState.setValue(state.overheatState)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.overheatState)
        self._prevState.setValue(prevState.overheatState)
        return


class OnOverheatGunParams(VehicleMechanicLifeCycleEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnOverheatGunParams, self).__init__(*args, **kwargs)
        self._overheatOffThreshold = self._makeDataOutputSlot(b'overheatOffThreshold', SLOT_TYPE.FLOAT, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.OVERHEAT_GUN

    @eventHandler
    def _onComponentParamsCollected(self, component):
        self._overheatOffThreshold.setValue(component.overheatOffThreshold)
        return


class OnHeatingZonesGunState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnHeatingZonesGunState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', HeatingZonesGunEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.HEATING_ZONES_GUN

    def _onStatePrepared(self, state):
        self._state.setValue(state.heatingZoneState)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.heatingZoneState)
        return


class OnStagedJetBoostersState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnStagedJetBoostersState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', PhasedMechanicStateEnum.slotType(), None)
        self._acceleratorStatus = self._makeDataOutputSlot(b'acceleratorStatus', AcceleratorStatusEnum.slotType(), None)
        self._duration = self._makeDataOutputSlot(b'duration', SLOT_TYPE.FLOAT, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.STAGED_JET_BOOSTERS

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, prevState, newState):
        self.__forwardStateToVSE(newState)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._duration.setValue(state.timeLeft)
        self._acceleratorStatus.setValue(state.acceleratorStatus)
        return


class OnLowChargeShotState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnLowChargeShotState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', LowChargeShotStateEnum.slotType(), None)
        self._duration = self._makeDataOutputSlot(b'duration', SLOT_TYPE.FLOAT, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.LOW_CHARGE_SHOT

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, prevState, newState):
        self.__forwardStateToVSE(newState)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.reloadingState)
        self._duration.setValue(state.duration)
        return


class OnPropellantGunState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnPropellantGunState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', PropellantGunEnum.slotType(), None)
        self._isOvercharge = self._makeDataOutputSlot(b'isOvercharge', SLOT_TYPE.BOOL, None)
        self._isAvailable = self._makeDataOutputSlot(b'isAvailable', SLOT_TYPE.BOOL, None)
        self._isLastStage = self._makeDataOutputSlot(b'isLastStage', SLOT_TYPE.BOOL, None)
        self._isLastChargeStage = self._makeDataOutputSlot(b'isLastChargeStage', SLOT_TYPE.BOOL, None)
        self._isMaxOverCharged = self._makeDataOutputSlot(b'isMaxOverCharged', SLOT_TYPE.BOOL, None)
        self._isMaxCharged = self._makeDataOutputSlot(b'isMaxCharged', SLOT_TYPE.BOOL, None)
        self._timeLeft = self._makeDataOutputSlot(b'timeLeft', SLOT_TYPE.FLOAT, None)
        self._isUsableShell = self._makeDataOutputSlot(b'isUsableShell', SLOT_TYPE.BOOL, None)
        self.__prevState = None
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.PROPELLANT_GUN

    def _onStatePrepared(self, state):
        self._state.setValue(state.state)
        self._onStateObservation(state)
        return

    def _onStateTransition(self, prevState, newState):
        self._state.setValue(newState.state)
        return

    @eventHandler
    def onStateObservation(self, state):
        if self.__prevState is None or self.__prevState != state:
            self._onStateObservation(state)
            self._onStateObservationSlot.call()
        return

    def _onStateObservation(self, state):
        self._isOvercharge.setValue(state.isOvercharge)
        self._isAvailable.setValue(state.isAvailable)
        self._timeLeft.setValue(state.timeLeft)
        self._isLastStage.setValue(state.isLastStage)
        self._isLastChargeStage.setValue(state.isLastChargeStage)
        self._isMaxOverCharged.setValue(state.isMaxOverCharged)
        self._isMaxCharged.setValue(state.isMaxCharged)
        self._isUsableShell.setValue(state.isUsableShell)
        self.__prevState = state
        return


class OnWheeledDashState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnWheeledDashState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', PhasedMechanicStateEnum.slotType(), None)
        self._duration = self._makeDataOutputSlot(b'duration', SLOT_TYPE.FLOAT, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, _):
        return VehicleMechanic.WHEELED_DASH

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, _, newState):
        self.__forwardStateToVSE(newState)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._duration.setValue(state.timeLeft)
        return


class OnWheeledDashImpulse(VehicleMechanicEventsBlock, IWheeledDashListenerLogic):

    def __init__(self, *args, **kwargs):
        super(OnWheeledDashImpulse, self).__init__(*args, **kwargs)
        self._onImpulseStarted = self._makeEventOutputSlot(b'onImpulseStarted')
        self._direction = self._makeDataOutputSlot(b'direction', WheeledDashDirectionEnum.slotType(), None)
        return

    @classmethod
    def _getVehicleMechanic(cls, _):
        return VehicleMechanic.WHEELED_DASH

    @eventHandler
    def onMechanicComponentCatching(self, component):
        component.impulseEvents.lateSubscribe(self)
        return

    @eventHandler
    def onMechanicComponentReleasing(self, component):
        self.unsubscribeFrom(component.impulseEvents)
        return

    @eventHandler
    def onImpulseStarted(self, direction):
        self._direction.setValue(direction)
        self._onImpulseStarted.call()
        return


class OnAuxiliaryRocketLauncherState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnAuxiliaryRocketLauncherState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', SecondaryGunStateEnum.slotType(), None)
        self._duration = self._makeDataOutputSlot(b'duration', SLOT_TYPE.FLOAT, None)
        self._isInAimingMode = self._makeDataOutputSlot(b'isInAimingMode', SLOT_TYPE.BOOL, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, _):
        return VehicleMechanic.AUXILIARY_ROCKET_LAUNCHER

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, _, newState):
        self.__forwardStateToVSE(newState)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._duration.setValue(state.timeLeft)
        self._isInAimingMode.setValue(state.isInAimingMode)
        return


class OnShellParamsSwitcherGunState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnShellParamsSwitcherGunState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', ShellParamsSwitcherGunEnum.slotType(), None)
        self._isBroken = self._makeDataOutputSlot(b'isBroken', SLOT_TYPE.BOOL, None)
        self._isNoAmmo = self._makeDataOutputSlot(b'isNoAmmo', SLOT_TYPE.BOOL, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.SHELL_PARAMS_SWITCHER

    def _onStatePrepared(self, state):
        self.__setState(state)
        return

    def _onStateTransition(self, prevState, newState):
        self.__setState(newState)
        return

    def __setState(self, state):
        self._state.setValue(state.baseState)
        self._isBroken.setValue(state.isCritState())
        self._isNoAmmo.setValue(state.isNoAmmo())
        return


class OnShellCalibrationState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnShellCalibrationState, self).__init__(*args, **kwargs)
        self._isPenBonusActive = self._makeDataOutputSlot(b'isPenBonusActive', SLOT_TYPE.BOOL, None)
        self._isNonPenBonusActive = self._makeDataOutputSlot(b'isNonPenBonusActive', SLOT_TYPE.BOOL, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.SHELL_CALIBRATION

    def _onStateTransition(self, prevState, newState):
        self._isPenBonusActive.setValue(bool(newState.isPenBonusActive))
        self._isNonPenBonusActive.setValue(bool(newState.isNonPenBonusActive))
        return


_AUTORELOADER_SURGE_RESTRICTION_TO_ERROR_KEY = {(AUTORELOADER_SURGE_RESTRICTION.NO_CHARGES): b'autoreloaderSurgeNoCharges', 
   (AUTORELOADER_SURGE_RESTRICTION.CLIP_FULL): b'autoreloaderSurgeClipFull', 
   (AUTORELOADER_SURGE_RESTRICTION.SHORT_RELOAD_TIME): b'autoreloaderSurgeReloadingSmall', 
   (AUTORELOADER_SURGE_RESTRICTION.NO_AMMO): b'autoreloaderSurgeNoAmmo'}

class OnAutoreloaderSurgeState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnAutoreloaderSurgeState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', AutoreloaderSurgeStateEnum.slotType(), None)
        self._hasRestrictions = self._makeDataOutputSlot(b'hasRestrictions', SLOT_TYPE.BOOL, None)
        self._chargeIntervalEnd = self._makeDataOutputSlot(b'chargeIntervalEnd', SLOT_TYPE.FLOAT, None)
        self._restrictionErrorKey = self._makeDataOutputSlot(b'restrictionErrorKey', SLOT_TYPE.STR, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.AUTORELOADER_SURGE

    @eventHandler
    def onMechanicComponentCatching(self, component):
        super(OnAutoreloaderSurgeState, self).onMechanicComponentCatching(component)
        return

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, prevState, newState):
        self.__forwardStateToVSE(newState)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._hasRestrictions.setValue(state.restrictions != 0)
        self._chargeIntervalEnd.setValue(state.chargeIntervalEnd)
        topRestriction = AUTORELOADER_SURGE_RESTRICTION.getTopPriorityRestriction(state.restrictions)
        self._restrictionErrorKey.setValue(_AUTORELOADER_SURGE_RESTRICTION_TO_ERROR_KEY.get(topRestriction, b''))
        return


class OnBustleFeedState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnBustleFeedState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', BustleFeedStateEnum.slotType(), None)
        self._prevState = self._makeDataOutputSlot(b'prevState', BustleFeedStateEnum.slotType(), None)
        self._canSwitch = self._makeDataOutputSlot(b'canSwitch', SLOT_TYPE.BOOL, None)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.BUSTLE_FEED

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, prevState, newState):
        self._prevState.setValue(prevState.state)
        self.__forwardStateToVSE(newState)
        return

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._canSwitch.setValue(state.switchAccessState == BUSTLE_FEED_SWITCH_ACCESS.ENABLED)
        return


class OnSightPointerState(VehicleMechanicStateEventsBlock):

    def __init__(self, *args, **kwargs):
        super(OnSightPointerState, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', SightPointerStateEnum.slotType(), None)
        self._hasVehicles = self._makeDataOutputSlot(b'hasVehicles', SLOT_TYPE.BOOL, None)
        self._stage = self._makeDataOutputSlot(b'stage', SLOT_TYPE.INT, None)
        self._startTime = self._makeDataOutputSlot(b'startTime', SLOT_TYPE.FLOAT, None)
        self._minActiveTime = self._makeDataOutputSlot(b'minActiveTime', SLOT_TYPE.FLOAT, None)
        self._minActiveTime.setValue(SIGHT_POINTER_COMMON_CONSTANTS.MIN_ACTIVE_DURATION)
        return

    @classmethod
    def _getVehicleMechanic(cls, initParams):
        return VehicleMechanic.SIGHT_POINTER

    def __forwardStateToVSE(self, state):
        self._state.setValue(state.state)
        self._hasVehicles.setValue(state.vehiclesUnderScan)
        self._stage.setValue(state.stage)
        self._startTime.setValue(state.baseTime)
        return

    def _onStatePrepared(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateObservation(self, state):
        self.__forwardStateToVSE(state)
        return

    def _onStateTransition(self, _, newState):
        self.__forwardStateToVSE(newState)
        return
