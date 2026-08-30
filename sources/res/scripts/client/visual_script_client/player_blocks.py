import weakref, typing, BigWorld
from aih_constants import CTRL_MODES
from constants import DEFAULT_GUN_INSTALLATION_INDEX
from visual_script import ASPECT
from visual_script.ability_common import Stage
from visual_script.block import Meta, Block, InitParam, buildStrKeysValue
from visual_script.dependency import dependencyImporter
from visual_script.misc import errorVScript, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.type import VScriptEnum
from visual_script.tunable_event_block import TunableEventBlock
from visual_script_client.vehicle_common import TunablePlayerVehicleEventBlock, getPartState, getPartNames, getPartName, TriggerListener
import items.vehicles as vehicles
if typing.TYPE_CHECKING:
    from Vehicle import StunInfo
helpers, TriggersManager, gun_marker_ctrl, equipment_ctrl, Avatar = dependencyImporter(b'helpers', b'TriggersManager', b'AvatarInputHandler.gun_marker_ctrl', b'gui.battle_control.controllers.consumables.equipment_ctrl', b'Avatar')

def isMainGunInstallation(gunInstallationIndex):
    return gunInstallationIndex == DEFAULT_GUN_INSTALLATION_INDEX


class PlayerMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16777215

    @classmethod
    def blockCategory(cls):
        return b'Player'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/player'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]

    @property
    def _avatar(self):
        if helpers.isPlayerAvatar():
            return BigWorld.player()
        errorVScript(self, b'BigWorld.player is not player avatar.')
        return


class PlayerEventMeta(PlayerMeta):

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena_event'


class GetPlayerVehicleGun(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerVehicleGun, self).__init__(*args, **kwargs)
        self._gunPosition = self._makeDataOutputSlot(b'gunPosition', SLOT_TYPE.VECTOR3, self._getGunPosition)
        self._gunDirection = self._makeDataOutputSlot(b'gunDirection', SLOT_TYPE.VECTOR3, self._getGunDirection)
        return

    def _getGunPosition(self):
        avatar = self._avatar
        if avatar:
            position, _ = avatar.gunRotator.getCurShotPosition()
            self._gunPosition.setValue(position)
        return

    def _getGunDirection(self):
        avatar = self._avatar
        if avatar:
            _, direction = avatar.gunRotator.getCurShotPosition()
            direction.normalise()
            self._gunDirection.setValue(direction)
        return


class GetPlayerGunMarkerInfo(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerGunMarkerInfo, self).__init__(*args, **kwargs)
        self._pos = self._makeDataOutputSlot(b'position', SLOT_TYPE.VECTOR3, self._getPosition)
        self._dir = self._makeDataOutputSlot(b'direction', SLOT_TYPE.VECTOR3, self._getDirection)
        self._size = self._makeDataOutputSlot(b'size', SLOT_TYPE.FLOAT, self._getSize)
        return

    @property
    def _markerInfo(self):
        avatar = self._avatar
        if avatar:
            return avatar.gunRotator.markerInfo
        return

    def _getPosition(self):
        markerInfo = self._markerInfo
        if markerInfo:
            self._pos.setValue(markerInfo[0])
        return

    def _getDirection(self):
        markerInfo = self._markerInfo
        if markerInfo:
            self._dir.setValue(markerInfo[1])
        return

    def _getSize(self):
        markerInfo = self._markerInfo
        if markerInfo:
            self._size.setValue(markerInfo[2])
        return


class OnPlayerSnipeMode(TunableEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES = [
     b'onEnter', b'onExit']

    def onStartScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.addListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onFinishScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.delListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onTriggerActivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.SNIPER_MODE:
            self._index = 0
            self._callOnEnter()
        return

    def onTriggerDeactivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.SNIPER_MODE:
            self._index = 1
            self._callOnExit()
        return

    @TunableEventBlock.eventProcessor
    def _callOnEnter(self):
        return

    @TunableEventBlock.eventProcessor
    def _callOnExit(self):
        return


class OnPlayerSPGMode(TunableEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES = [
     b'onEnterTopDown', b'onEnterTrajectory', b'onExit']

    def onStartScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.addListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onFinishScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.delListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onTriggerActivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_ENTER_SPG_STRATEGIC_MODE:
            self._index = 0
            self._callOnEnterTopDown()
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_ENTER_SPG_SNIPER_MODE:
            self._index = 1
            self._callOnEnterTrajectory()
        elif triggerType == TriggersManager.TRIGGER_TYPE.PLAYER_LEAVE_SPG_MODE:
            self._index = 2
            self._callOnExit()
        return

    @TunableEventBlock.eventProcessor
    def _callOnEnterTopDown(self):
        return

    @TunableEventBlock.eventProcessor
    def _callOnEnterTrajectory(self):
        return

    @TunableEventBlock.eventProcessor
    def _callOnExit(self):
        return


class OnPlayerControlModeChange(TunableEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES = [
     b'OnEnter', b'OnExit']
    __CTRL_MODE_ANY = b'Any mode'

    def __init__(self, *args, **kwargs):
        super(OnPlayerControlModeChange, self).__init__(*args, **kwargs)
        self._controlMode, = self._getInitParams()
        self._previousMode = self._makeDataOutputSlot(b'previous mode', PlayerControlMode.slotType(), None)
        self._currentMode = self._makeDataOutputSlot(b'current mode', PlayerControlMode.slotType(), None)
        return

    @classmethod
    def initParams(cls):
        allModes = [OnPlayerControlModeChange.__CTRL_MODE_ANY] + list(CTRL_MODES)
        return [
         InitParam(b'ControlMode', SLOT_TYPE.STR, buildStrKeysValue(*allModes), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def captionText(self):
        return b'On Change Control Mode (' + self._controlMode.upper() + b')'

    def onStartScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.addListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onFinishScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.delListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onTriggerActivated(self, params):
        triggerType = params.get(b'type')
        if triggerType is not TriggersManager.TRIGGER_TYPE.CTRL_MODE_CHANGE:
            return
        isAnyMode = self._controlMode == OnPlayerControlModeChange.__CTRL_MODE_ANY
        previousMode = params.get(b'previousMode')
        currentMode = params.get(b'currentMode')
        if isAnyMode or previousMode == self._controlMode:
            self._index = 1
            self._callOnExit(previousMode, currentMode)
        if isAnyMode or currentMode == self._controlMode:
            self._index = 0
            self._callOnEnter(previousMode, currentMode)
        return

    @TunableEventBlock.eventProcessor
    def _callOnExit(self, previousMode, currentMode):
        self.__setOutputValues(previousMode, currentMode)
        return

    @TunableEventBlock.eventProcessor
    def _callOnEnter(self, previousMode, currentMode):
        self.__setOutputValues(previousMode, currentMode)
        return

    def __setOutputValues(self, previousMode, currentMode):
        previousModeIndex = PlayerControlMode.nameToIndex(previousMode)
        self._previousMode.setValue(previousModeIndex)
        currentModeIndex = PlayerControlMode.nameToIndex(currentMode)
        self._currentMode.setValue(currentModeIndex)
        return


class IsControlModeActive(Block, PlayerEventMeta):

    def __init__(self, *args, **kwargs):
        super(IsControlModeActive, self).__init__(*args, **kwargs)
        self._controlMode = self._makeDataInputSlot(b'control mode', PlayerControlMode.slotType())
        self._active = self._makeDataOutputSlot(b'active', SLOT_TYPE.BOOL, self.__execute)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]

    def __execute(self):
        player = BigWorld.player()
        aih = player.inputHandler if player else None
        if not aih:
            errorVScript(self, b'Cannot get players input handler')
            return
        else:
            controlMode = self._controlMode.getValue()
            self._active.setValue(controlMode == PlayerControlMode.nameToIndex(aih.ctrlModeName))
            return


class PlayerControlMode(VScriptEnum):

    @classmethod
    def slotType(cls):
        return b'EControlModes'

    @classmethod
    def vs_enum(cls):
        return CTRL_MODES

    @classmethod
    def nameToIndex(cls, ctrlModeName):
        return cls.vs_enum().index(ctrlModeName)

    @classmethod
    def _vs_collectEnumEntries(cls):
        entriesData = {}
        for name in cls.vs_enum():
            entriesData[name] = cls.vs_enum().index(name)

        return entriesData

    @classmethod
    def vs_aspects(cls):
        return [
         ASPECT.CLIENT]


class OnGunMarkerPenetrationStateChanged(TunableEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onChanged']

    def __init__(self, *args, **kwargs):
        super(OnGunMarkerPenetrationStateChanged, self).__init__(*args, **kwargs)
        self._state = self._makeDataOutputSlot(b'state', SLOT_TYPE.INT, None)
        self._oldResult = None
        return

    def onStartScript(self):
        avatar = self._avatar
        if avatar:
            avatar.guiSessionProvider.shared.crosshair.onGunMarkerStateChanged += self._onGunMarkerStateChanged
        return

    def onFinishScript(self):
        avatar = self._avatar
        if avatar:
            crosshair = avatar.guiSessionProvider.shared.crosshair
            if crosshair:
                crosshair.onGunMarkerStateChanged -= self._onGunMarkerStateChanged
        return

    def _onGunMarkerStateChanged(self, _, gunMarkerState, __):
        avatar = self._avatar
        if avatar:
            shotResultResolver = gun_marker_ctrl.createShotResultResolver()
            result = shotResultResolver.getShotResult(gunMarkerState, excludeTeam=avatar.team)
            if result != self._oldResult:
                self._oldResult = result
                self._callOutput(result)
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, result):
        self._state.setValue(result)
        return


class GetPlayerVehicleDeviceState(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerVehicleDeviceState, self).__init__(*args, **kwargs)
        self._device = self._makeDataInputSlot(b'device', SLOT_TYPE.E_VEHICLE_DEVICE)
        self._state = self._makeDataOutputSlot(b'state', SLOT_TYPE.E_MODULE_STATE, self._execState)
        self._hasDevice = self._makeDataOutputSlot(b'hasDevice', SLOT_TYPE.BOOL, self._execHasDevice)
        return

    def _execState(self):
        if helpers.isPlayerAvatar():
            deviceIdx = self._device.getValue()
            if deviceIdx >= len(vehicles.VEHICLE_DEVICE_TYPE_NAMES):
                errorVScript(self, b'unknown device identifier.')
                return
            state = getPartState(vehicles.VEHICLE_DEVICE_TYPE_NAMES[deviceIdx])
            self._state.setValue(state)
        else:
            errorVScript(self, b'BigWorld.player is not player avatar.')
        return

    def _execHasDevice(self):
        if helpers.isPlayerAvatar():
            deviceIdx = self._device.getValue()
            if deviceIdx >= len(vehicles.VEHICLE_DEVICE_TYPE_NAMES):
                errorVScript(self, b'unknown device identifier.')
                return
            deviceNames = [pn + b'Health' for pn in getPartNames(vehicles.VEHICLE_DEVICE_TYPE_NAMES[deviceIdx])]
            isHas = any(te.name in deviceNames for te in BigWorld.player().vehicleTypeDescriptor.type.devices)
            self._hasDevice.setValue(isHas)
        else:
            errorVScript(self, b'BigWorld.player is not player avatar.')
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetPlayerVehicleTankmanState(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerVehicleTankmanState, self).__init__(*args, **kwargs)
        self._tankman = self._makeDataInputSlot(b'tankman', SLOT_TYPE.E_VEHICLE_TANKMAN)
        self._state = self._makeDataOutputSlot(b'state', SLOT_TYPE.E_MODULE_STATE, self._execState)
        self._hasTankman = self._makeDataOutputSlot(b'hasTankman', SLOT_TYPE.BOOL, self._execHasTankman)
        return

    def _execState(self):
        if helpers.isPlayerAvatar():
            tankmanIdx = self._tankman.getValue()
            if tankmanIdx >= len(vehicles.VEHICLE_TANKMAN_TYPE_NAMES):
                errorVScript(self, b'unknown tankman identifier.')
                return
            state = getPartState(vehicles.VEHICLE_TANKMAN_TYPE_NAMES[tankmanIdx])
            self._state.setValue(state)
        else:
            errorVScript(self, b'BigWorld.player is not player avatar.')
        return

    def _execHasTankman(self):
        if helpers.isPlayerAvatar():
            tankmanIdx = self._tankman.getValue()
            if tankmanIdx >= len(vehicles.VEHICLE_TANKMAN_TYPE_NAMES):
                errorVScript(self, b'unknown tankman identifier.')
                return
            tankmanName = [pn + b'Health' for pn in getPartNames(vehicles.VEHICLE_TANKMAN_TYPE_NAMES[tankmanIdx])]
            isHas = any(te.name in tankmanName for te in BigWorld.player().vehicleTypeDescriptor.type.tankmen)
            self._hasTankman.setValue(isHas)
        else:
            errorVScript(self, b'BigWorld.player is not player avatar.')
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnPlayerVehicleDiscreteShoot(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onDiscreteShoot']

    def onPlayerDiscreteShoot(self, gunInstallationIndex):
        if isMainGunInstallation(gunInstallationIndex):
            self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return


class OnPlayerShotMissed(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onMissed']

    def onPlayerShotMissed(self, gunInstallationIndex):
        if isMainGunInstallation(gunInstallationIndex):
            self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return


class OnPlayerShotHit(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onHit']

    def __init__(self, *args, **kwargs):
        super(OnPlayerShotHit, self).__init__(*args, **kwargs)
        self._target = self._makeDataOutputSlot(b'target', SLOT_TYPE.VEHICLE, None)
        self._flags = self._makeDataOutputSlot(b'hitFlags', SLOT_TYPE.INT, None)
        return

    def onPlayerShotHit(self, target, flags, gunInstallationIndex):
        if isMainGunInstallation(gunInstallationIndex):
            self._callOutput(target, flags)
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, target, flags):
        if target is not None:
            self._target.setValue(weakref.proxy(target))
        else:
            self._target.setValue(None)
        self._flags.setValue(flags)
        return


class OnPlayerAutoAim(TunablePlayerVehicleEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES = [
     b'onEnabled', b'onDisabled']

    def onStartScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.addListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onFinishScript(self):
        manager = TriggersManager.g_manager
        if manager:
            manager.delListener(self)
        else:
            errorVScript(self, b'TriggersManager.g_manager is None')
        return

    def onTriggerActivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.AUTO_AIM_AT_VEHICLE:
            self._index = 0
            self._callOnEnter()
        return

    def onTriggerDeactivated(self, params):
        triggerType = params.get(b'type')
        if triggerType == TriggersManager.TRIGGER_TYPE.AUTO_AIM_AT_VEHICLE:
            self._index = 1
            self._callOnExit()
        return

    @TunableEventBlock.eventProcessor
    def _callOnEnter(self):
        return

    @TunableEventBlock.eventProcessor
    def _callOnExit(self):
        return


class OnPlayerMoveVehicle(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onMove']

    def __init__(self, *args, **kwargs):
        super(OnPlayerMoveVehicle, self).__init__(*args, **kwargs)
        self._forward = self._makeDataOutputSlot(b'forward', SLOT_TYPE.BOOL, None)
        self._backward = self._makeDataOutputSlot(b'backward', SLOT_TYPE.BOOL, None)
        self._left = self._makeDataOutputSlot(b'left', SLOT_TYPE.BOOL, None)
        self._right = self._makeDataOutputSlot(b'right', SLOT_TYPE.BOOL, None)
        self._cc25 = self._makeDataOutputSlot(b'cruise25pc', SLOT_TYPE.BOOL, None)
        self._cc50 = self._makeDataOutputSlot(b'cruise50pc', SLOT_TYPE.BOOL, None)
        self._break = self._makeDataOutputSlot(b'break', SLOT_TYPE.BOOL, None)
        return

    @TunableEventBlock.eventProcessor
    def onPlayerMove(self, moveCommands):
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.FORWARD, self._forward)
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.BACKWARD, self._backward)
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.ROTATE_LEFT, self._left)
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.ROTATE_RIGHT, self._right)
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.CRUISE_CONTROL25, self._cc25)
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.CRUISE_CONTROL50, self._cc50)
        self._processMoveCommand(moveCommands, Avatar.MOVEMENT_FLAGS.BLOCK_TRACKS, self._break)
        return

    @staticmethod
    def _processMoveCommand(moveCommands, commandToCheck, slotToSet):
        if moveCommands & commandToCheck:
            slotToSet.setValue(True)
        else:
            slotToSet.setValue(False)
        return


class OnPlayerVehicleDetectEnemy(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onDetect', b'onLost']

    def __init__(self, *args, **kwargs):
        super(OnPlayerVehicleDetectEnemy, self).__init__(*args, **kwargs)
        self._target = self._makeDataOutputSlot(b'target', SLOT_TYPE.VEHICLE, None)
        return

    def onPlayerDetectEnemy(self, new, lost):
        if new:
            self._index = 0
            self._callOutput(new[0])
        elif lost:
            self._index = 1
            self._callOutput(lost[0])
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, vehicle):
        self._target.setValue(weakref.proxy(vehicle))
        return


class OnPlayerVehicleFireEvent(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onFire', b'onFireEnds']

    def onPlayerVehicleFireEvent(self, isStart):
        if isStart:
            self._index = 0
            self._callOutput()
        else:
            self._index = 1
            self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return


class OnPlayerVehicleContinuousBurstStart(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onContinuousBurstStart']

    def onPlayerContinuousBurstStart(self, gunInstallationIndex):
        if isMainGunInstallation(gunInstallationIndex):
            self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return


class OnPlayerVehicleContinuousBurstStop(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onContinuousBurstStop']

    def onPlayerContinuousBurstStop(self, gunInstallationIndex):
        if isMainGunInstallation(gunInstallationIndex):
            self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return


class OnPlayerVehicleTankmanEvent(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onShocked', b'onHealed']

    def __init__(self, *args, **kwargs):
        super(OnPlayerVehicleTankmanEvent, self).__init__(*args, **kwargs)
        self._tankman = self._makeDataOutputSlot(b'tankman', SLOT_TYPE.E_VEHICLE_TANKMAN, None)
        return

    def onPlayerVehicleTankmanEvent(self, tankmanName, isHit):
        tankmanName = getPartName(tankmanName)
        if tankmanName in vehicles.VEHICLE_TANKMAN_TYPE_NAMES:
            tankman = vehicles.VEHICLE_TANKMAN_TYPE_NAMES.index(tankmanName)
            if isHit:
                self._index = 0
            else:
                self._index = 1
            self._callOutput(tankman)
        else:
            errorVScript(self, b'OnVehiclePlayerDeviceCrit unknown tankmanName')
            return
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, tankman):
        self._tankman.setValue(tankman)
        return


class OnPlayerVehicleDeviceCrit(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onDamaged', b'onDestroyed', b'onHealed', b'onAutoHealToDamaged']

    def __init__(self, *args, **kwargs):
        super(OnPlayerVehicleDeviceCrit, self).__init__(*args, **kwargs)
        self._device = self._makeDataOutputSlot(b'device', SLOT_TYPE.E_VEHICLE_DEVICE, None)
        return

    def onPlayerVehicleDeviceEvent(self, deviceName, isCritical, isHit):
        deviceName = getPartName(deviceName)
        if deviceName in vehicles.VEHICLE_DEVICE_TYPE_NAMES:
            device = vehicles.VEHICLE_DEVICE_TYPE_NAMES.index(deviceName)
            if isHit:
                self._index = 0 if isCritical else 1
            else:
                self._index = 3 if isCritical else 2
            self._callOutput(device)
        else:
            errorVScript(self, b'OnVehiclePlayerDeviceCrit unknown deviceName')
            return
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, device):
        self._device.setValue(device)
        return


class OnPlayerVehicleAreaTrigger(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onEnter', b'onExit']

    def __init__(self, *args, **kwargs):
        super(OnPlayerVehicleAreaTrigger, self).__init__(*args, **kwargs)
        self._trigger = self._makeDataInputSlot(b'trigger', SLOT_TYPE.AREA_TRIGGER)
        return

    def onPlayerEnterTrigger(self, trigger, enter):
        if trigger == self._trigger.getValue().name:
            if enter:
                self._index = 0
            else:
                self._index = 1
            self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return

    def validate(self):
        if not self._trigger.hasValue():
            return b'Trigger value is required'
        return super(OnPlayerVehicleAreaTrigger, self).validate()


class OnShowTracer(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onShow']

    def __init__(self, *args, **kwargs):
        super(OnShowTracer, self).__init__(*args, **kwargs)
        self._attacker = self._makeDataOutputSlot(b'attacker', SLOT_TYPE.VEHICLE, None)
        self._isRicochet = self._makeDataOutputSlot(b'isRicochet', SLOT_TYPE.BOOL, None)
        self._startPoint = self._makeDataOutputSlot(b'startPoint', SLOT_TYPE.VECTOR3, None)
        self._direction = self._makeDataOutputSlot(b'direction', SLOT_TYPE.VECTOR3, None)
        self._velocity = self._makeDataOutputSlot(b'velocity', SLOT_TYPE.FLOAT, None)
        self._gravity = self._makeDataOutputSlot(b'gravity', SLOT_TYPE.FLOAT, None)
        self._maxDist = self._makeDataOutputSlot(b'maxDist', SLOT_TYPE.FLOAT, None)
        return

    def onShowTracer(self, attacker, isRicochet, startPoint, velocity, gravity, maxShotDist, gunInstallationIndex):
        if isMainGunInstallation(gunInstallationIndex):
            self._callOutput(attacker, isRicochet, startPoint, velocity, gravity, maxShotDist)
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, attacker, isRicochet, startPoint, velocity, gravity, maxShotDist):
        if attacker is not None:
            self._attacker.setValue(weakref.proxy(attacker))
        else:
            self._attacker.setValue(None)
        self._isRicochet.setValue(bool(isRicochet))
        self._startPoint.setValue(startPoint)
        self._velocity.setValue(velocity.length)
        velocity.normalise()
        self._direction.setValue(velocity)
        self._gravity.setValue(gravity)
        self._maxDist.setValue(maxShotDist)
        return


class GetPlayerGunDispersionAngles(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerGunDispersionAngles, self).__init__(*args, **kwargs)
        self._current = self._makeDataOutputSlot(b'current', SLOT_TYPE.ANGLE, self._getCurrentDispersions)
        self._target = self._makeDataOutputSlot(b'target', SLOT_TYPE.ANGLE, self._getCurrentDispersions)
        self._ideal = self._makeDataOutputSlot(b'ideal', SLOT_TYPE.ANGLE, self._getIdealDispersion)
        return

    def _getCurrentDispersions(self):
        avatar = self._avatar
        if avatar:
            angles = avatar.gunRotator.getCurShotDispersionAngles()
            self._current.setValue(angles[0])
            self._target.setValue(angles[1])
        return

    def _getIdealDispersion(self):
        avatar = self._avatar
        if avatar:
            td = avatar.getVehicleDescriptor()
            self._ideal.setValue(td.gun.shotDispersionAngle)
        return


class GetPlayerEquipments(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerEquipments, self).__init__(*args, **kwargs)
        self._equipments = self._makeDataOutputSlot(b'equipments', arrayOf(SLOT_TYPE.STR), self._getEquipments)
        return

    def _getEquipments(self):
        avatar = self._avatar
        res = []
        if avatar:
            eqs = avatar.guiSessionProvider.shared.equipments.getOrderedEquipmentsLayout()
            for _, item in eqs:
                res.append(item.getDescriptor().name)

        self._equipments.setValue(res)
        return


class GetPlayerEquipmentState(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerEquipmentState, self).__init__(*args, **kwargs)
        self._equipmentName = self._makeDataInputSlot(b'equipment', SLOT_TYPE.STR)
        self._equipped = self._makeDataOutputSlot(b'isEquipped', SLOT_TYPE.BOOL, self._isEquipped)
        self._availableToUse = self._makeDataOutputSlot(b'isAvailableToUse', SLOT_TYPE.BOOL, self._isAvailableToUse)
        self._canActivate = self._makeDataOutputSlot(b'canBeActivated', SLOT_TYPE.BOOL, self._canBeActivated)
        self._stage = self._makeDataOutputSlot(b'stage', Stage.slotType(), self._getStage)
        return

    @property
    def _equipment(self):
        avatar = self._avatar
        if avatar:
            equipName = self._equipmentName.getValue()
            eqs = avatar.guiSessionProvider.shared.equipments.getOrderedEquipmentsLayout()
            for _, item in eqs:
                if item.getDescriptor().name == equipName:
                    return item

        return

    def _isEquipped(self):
        self._equipped.setValue(self._equipment is not None)
        return

    def _canBeActivated(self):
        item = self._equipment
        if item is not None:
            result, info = item.canActivate()
            if isinstance(info, equipment_ctrl.NeedEntitySelection):
                result = True
            self._canActivate.setValue(result)
        return

    def _isAvailableToUse(self):
        item = self._equipment
        if item is not None:
            self._availableToUse.setValue(item.isAvailableToUse)
        return

    def _getStage(self):
        item = self._equipment
        if item is not None:
            self._stage.setValue(item.getStage())
        return


class OnPlayerVehicleStun(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onStun', b'onStunHealed', b'onStunAutoHeal']

    def __init__(self, *args, **kwargs):
        super(OnPlayerVehicleStun, self).__init__(*args, **kwargs)
        self._reset()
        self._stunDuration = self._makeDataOutputSlot(b'stunDuration', SLOT_TYPE.FLOAT, None)
        return

    def _reset(self):
        self._lastStartTime = 0.0
        self._lastDuration = 0.0
        return

    def onStunInfoUpdated(self, stunInfo):
        if stunInfo.duration > 0:
            self._stunDuration.setValue(stunInfo.duration)
            self._lastDuration = stunInfo.duration
            self._lastStartTime = stunInfo.startTime
            self._index = 0
            self._callOutput()
        elif stunInfo.duration == 0.0 and self._lastStartTime != 0.0:
            self._index = 1 if self._lastStartTime + self._lastDuration > BigWorld.serverTime() else 2
            self._reset()
            self._callOutput()
        elif stunInfo.duration == 0.0 and self._lastStartTime == 0.0:
            self._reset()
        else:
            self._reset()
            errorVScript(self, b'OnPlayerVehicleStun has got inconsistent stun data.')
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
        return


class OnVehicleSixthSenseActivated(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onDetected']

    @TunableEventBlock.eventProcessor
    def onSixthSenceActivated(self):
        return


class OnPlayerUsedAOEEquipment(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onEquipmentUsed']

    def __init__(self, *args, **kwargs):
        super(OnPlayerUsedAOEEquipment, self).__init__(*args, **kwargs)
        self._name = self._makeDataOutputSlot(b'name', SLOT_TYPE.STR, None)
        self._position = self._makeDataOutputSlot(b'position', SLOT_TYPE.VECTOR3, None)
        return

    @TunableEventBlock.eventProcessor
    def onPlayerUsedAoEEquipment(self, name, position):
        self._name.setValue(name)
        self._position.setValue(position)
        return


class GetPlayerShellsState(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(GetPlayerShellsState, self).__init__(*args, **kwargs)
        shells = self._shells
        self._shellsLeft = self._makeDataOutputSlot(b'currentLeft', SLOT_TYPE.INT, shells)
        self._shellsLoaded = self._makeDataOutputSlot(b'currentLoaded', SLOT_TYPE.INT, shells)
        self._loadPercent = self._makeDataOutputSlot(b'clipLoadPercentLeft', SLOT_TYPE.FLOAT, self._curLoadPercentLeft)
        return

    def _shells(self):
        avatar = self._avatar
        if avatar:
            shells = avatar.guiSessionProvider.shared.ammo.getCurrentShells()
            self._shellsLeft.setValue(shells[0])
            self._shellsLoaded.setValue(shells[1])
        return

    def _curLoadPercentLeft(self):
        avatar = self._avatar
        if avatar:
            self._loadPercent.setValue(avatar.guiSessionProvider.shared.ammo.getClipPercentLeft())
        return
