import weakref, BigWorld, Math
from skeletons.gui.battle_session import IBattleSessionProvider
from PlayerEvents import g_playerEvents
from visual_script import ASPECT
from visual_script.block import Meta, Block
from visual_script.dependency import dependencyImporter
from visual_script.misc import errorVScript
from visual_script.slot_types import SLOT_TYPE
from visual_script.tunable_event_block import TunableEventBlock
from visual_script.type import VScriptEnum
from visual_script_client.vehicle_common import TunablePlayerVehicleEventBlock, getPartState, getPartNames, getPartName, TriggerListener
import items.vehicles as vehicles
from constants import EQUIPMENT_STAGES
helpers, dependency, TriggersManager, gun_marker_ctrl, Avatar = dependencyImporter(b'helpers', b'helpers.dependency', b'TriggersManager', b'AvatarInputHandler.gun_marker_ctrl', b'Avatar')

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
        self._isLocked = self._makeDataOutputSlot(b'isLocked', SLOT_TYPE.BOOL, self._isGunLocked)
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
            self._gunDirection.setValue(direction)
        return

    def _isGunLocked(self):
        avatar = self._avatar
        if avatar:
            self._isLocked.setValue(avatar.gunRotator.isGunLocked())
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

    def _onGunMarkerStateChanged(self, _, position, direction, collision):
        avatar = self._avatar
        if avatar:
            shotResultResolver = gun_marker_ctrl.createShotResultResolver()
            result = shotResultResolver.getShotResult(position, collision, direction, excludeTeam=avatar.team)
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


class OnPlayerVehicleShoot(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onShoot']

    @TunableEventBlock.eventProcessor
    def onPlayerShoot(self, aimInfo):
        return


class OnPlayerShotMissed(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onMissed']

    @TunableEventBlock.eventProcessor
    def onPlayerShotMissed(self):
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


class OnBootcampPlayerVehicleDetected(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES = [
     b'onDetected', b'onLost']

    def onPlayerDetected(self, isDetected):
        if isDetected:
            self._index = 0
        else:
            self._index = 1
        self._callOutput()
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self):
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


class OnProjectileExplosion(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(OnProjectileExplosion, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._position = self._makeDataOutputSlot(b'position', SLOT_TYPE.VECTOR3, None)
        self._hitDirection = self._makeDataOutputSlot(b'hitDirection', SLOT_TYPE.VECTOR3, None)
        self._shellVelocity = self._makeDataOutputSlot(b'shellVelocity', SLOT_TYPE.FLOAT, None)
        self._shellMass = self._makeDataOutputSlot(b'shellMass', SLOT_TYPE.FLOAT, None)
        self._splashRadius = self._makeDataOutputSlot(b'splashRadius', SLOT_TYPE.FLOAT, None)
        self._splashStrength = self._makeDataOutputSlot(b'splashStrength', SLOT_TYPE.FLOAT, None)
        return

    def onStartScript(self):
        g_playerEvents.onProjectileExplosion += self.__onProjectileExplosion
        return

    def onFinishScript(self):
        g_playerEvents.onProjectileExplosion -= self.__onProjectileExplosion
        return

    def __onProjectileExplosion(self, position, hitDirection, shellVelocity, shellMass, splashRadius, splashStrength):
        self._position.setValue(position)
        self._hitDirection.setValue(hitDirection)
        self._shellVelocity.setValue(shellVelocity)
        self._shellMass.setValue(shellMass)
        self._splashRadius.setValue(splashRadius)
        self._splashStrength.setValue(splashStrength)
        self._out.call()
        return


class OnEquipmentUpdated(Block, PlayerMeta):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, *args, **kwargs):
        super(OnEquipmentUpdated, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._equipmentName = self._makeDataOutputSlot(b'equipmentName', SLOT_TYPE.STR, None)
        self._equipmentStage = self._makeDataOutputSlot(b'equipmentStage', SLOT_TYPE.INT, None)
        self._equipmentStageName = self._makeDataOutputSlot(b'equipmentStageName', SLOT_TYPE.STR, None)
        return

    def onStartScript(self):
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated += self.__onEquipmentUpdated
        return

    def onFinishScript(self):
        ctrl = self.__sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        return

    def __onEquipmentUpdated(self, intCD, item):
        descriptor = item.getDescriptor()
        self._equipmentName.setValue(descriptor.name)
        self._equipmentStage.setValue(item.getStage())
        self._equipmentStageName.setValue(EQUIPMENT_STAGES.toString(item.getStage()))
        self._out.call()
        return


class EVehCollisionSide(VScriptEnum):
    UNDEFINED = 0
    LEFT = 1
    RIGHT = 2


class OnCollidedWithAliveEnemy(Block, PlayerMeta):

    def __init__(self, *args, **kwargs):
        super(OnCollidedWithAliveEnemy, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._collisionSide = self._makeDataOutputSlot(b'collisionSide', SLOT_TYPE.E_VEH_COLLISION_SIDE, None)
        self._position = self._makeDataOutputSlot(b'position', SLOT_TYPE.VECTOR3, None)
        return

    def onStartScript(self):
        g_playerEvents.onCollisionWithOtherAliveVehicle += self.__onCollisionWithOtherAliveVehicle
        self._collisionSide.setValue(EVehCollisionSide.UNDEFINED)
        return

    def onFinishScript(self):
        g_playerEvents.onCollisionWithOtherAliveVehicle -= self.__onCollisionWithOtherAliveVehicle
        return

    def __onCollisionWithOtherAliveVehicle(self, position, isOtherAlly):
        if isOtherAlly:
            return
        self.__calcCollisionSide(position)
        self._position.setValue(position)
        self._out.call()
        return

    def __calcCollisionSide(self, collisionPos):
        avatar = self._avatar
        if avatar is None:
            return
        else:
            vehicleMatrix = avatar.inputHandler.steadyVehicleMatrixCalculator.outputMProv
            rightVector = Math.Matrix(vehicleMatrix).applyToAxis(0)
            vehiclePos = avatar.getOwnVehiclePosition()
            collisionDirection = collisionPos - vehiclePos
            collisionDirection.normalise()
            dotProduct = collisionDirection.dot(rightVector)
            self._collisionSide.setValue(EVehCollisionSide.LEFT if dotProduct < 0 else EVehCollisionSide.RIGHT)
            return
