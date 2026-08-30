import typing, random, weakref, BigWorld, GenericComponents
from constants import IS_VS_EDITOR, VEHICLE_CLASSES, OVERTURN_WARNING_LEVEL, DROWN_WARNING_LEVEL
from debug_utils import LOG_DEBUG_DEV
from visual_script.block import Block, InitParam, buildStrKeysValue
from visual_script.dependency import dependencyImporter
from visual_script.misc import ASPECT, EDITOR_TYPE, errorVScript
from visual_script.slot_types import SLOT_TYPE
from visual_script.tunable_event_block import TunableEventBlock
from visual_script.type import VScriptEnum
from visual_script.vehicle_blocks import VehicleMeta
from visual_script.vehicle_blocks_bases import NoCrewCriticalBase, OptionalDevicesBase, VehicleClassBase, GunTypeInfoBase, VehicleForwardSpeedBase, VehicleCooldownEquipmentBase, VehicleClipFullAndReadyBase, GetTankOptDevicesHPModBase, IsInHangarBase, VehicleRadioDistanceBase, NoInnerDeviceDamagedBase
if not IS_VS_EDITOR:
    from helpers import dependency, isPlayerAccount, isPlayerAvatar
    from skeletons.gui.shared import IItemsCache
    from VehicleRespawnComponent import VehicleRespawnComponent
if typing.TYPE_CHECKING:
    from typing import Optional
    from Vehicle import Vehicle
    from items.components.gun_installation_components import GunInstallationSlot
OwnVehicle, = dependencyImporter(b'OwnVehicle')

class OverturnWarningLevelEnum(VScriptEnum):

    @classmethod
    def slotType(cls):
        return b'EOverturnWarningLevel'

    @classmethod
    def vs_enum(cls):
        return OVERTURN_WARNING_LEVEL

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.CLIENT]


class DrownWarningLevelEnum(VScriptEnum):

    @classmethod
    def slotType(cls):
        return b'EDrownWarningLevel'

    @classmethod
    def vs_enum(cls):
        return DROWN_WARNING_LEVEL

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.CLIENT]


class GetVehicleLabel(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleLabel, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._label = self._makeDataOutputSlot(b'label', SLOT_TYPE.STR, self._getLabel)
        return

    def _getLabel(self):
        vehicle = self._vehicle.getValue()
        label = vehicle.label if hasattr(vehicle, b'label') else None
        if label is None:
            label = b''
        self._label.setValue(label)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnAnyVehicleDestroyed(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES = [
     b'onDestroyed']

    def __init__(self, *args, **kwargs):
        super(OnAnyVehicleDestroyed, self).__init__(*args, **kwargs)
        self._target = self._makeDataOutputSlot(b'target', SLOT_TYPE.VEHICLE, None)
        self._attacker = self._makeDataOutputSlot(b'attacker', SLOT_TYPE.VEHICLE, None)
        return

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena_event'

    def onStartScript(self):
        if hasattr(BigWorld.player(), b'arena'):
            BigWorld.player().arena.onVehicleKilled += self.__onVehicleKilled
        else:
            errorVScript(self, b'can not subscribe on event')
        return

    def onFinishScript(self):
        if hasattr(BigWorld.player(), b'arena'):
            BigWorld.player().arena.onVehicleKilled -= self.__onVehicleKilled
        return

    @TunableEventBlock.eventProcessor
    def __onVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        target = BigWorld.entities.get(targetID)
        if target:
            self._target.setValue(weakref.proxy(BigWorld.entities.get(targetID)))
        else:
            self._target.setValue(None)
        if attackerID > 0:
            attacker = BigWorld.entities.get(attackerID)
            if attacker:
                attacker = weakref.proxy(BigWorld.entities.get(attackerID))
                self._attacker.setValue(attacker)
            else:
                self._attacker.setValue(None)
        else:
            self._attacker.setValue(None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnAnyVehicleDamaged(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES = [
     b'onDamaged']

    def __init__(self, *args, **kwargs):
        super(OnAnyVehicleDamaged, self).__init__(*args, **kwargs)
        self._target = self._makeDataOutputSlot(b'target', SLOT_TYPE.VEHICLE, None)
        self._attacker = self._makeDataOutputSlot(b'attacker', SLOT_TYPE.VEHICLE, None)
        self._damage = self._makeDataOutputSlot(b'damage', SLOT_TYPE.INT, None)
        return

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena_event'

    def onStartScript(self):
        if hasattr(BigWorld.player(), b'arena'):
            BigWorld.player().arena.onVehicleHealthChanged += self.__onDamageReceived
        else:
            errorVScript(self, b'can not subscribe on event')
        return

    def onFinishScript(self):
        if hasattr(BigWorld.player(), b'arena'):
            BigWorld.player().arena.onVehicleHealthChanged -= self.__onDamageReceived
        return

    @TunableEventBlock.eventProcessor
    def __onDamageReceived(self, vehicleId, attackerId, damage):
        self._damage.setValue(damage)
        vehicle = BigWorld.entities.get(vehicleId)
        if vehicle:
            self._target.setValue(weakref.proxy(vehicle))
        else:
            self._damage.setValue(None)
            self._target.setValue(None)
        if attackerId > 0:
            attacker = BigWorld.entities.get(attackerId)
            if attacker:
                attacker = weakref.proxy(BigWorld.entities.get(attackerId))
                self._attacker.setValue(attacker)
            else:
                self._attacker.setValue(None)
        else:
            self._attacker.setValue(None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class IsVehicleBurning(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(IsVehicleBurning, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._exec)
        return

    def _exec(self):
        v = self._vehicle.getValue()
        self._res.setValue(v.isOnFire())
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class NoCrewCritical(NoCrewCriticalBase):

    def _execute(self):
        self._outSlot.setValue(True)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class NoInnerDeviceDamaged(NoInnerDeviceDamagedBase):

    def _execute(self):
        self._outSlot.setValue(True)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OptionalDevices(OptionalDevicesBase):

    def _execute(self):
        self._outSlot.setValue([])
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetTankOptDevicesHPMod(GetTankOptDevicesHPModBase):

    def _execute(self):
        self._outSlot.setValue(1.0)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class VehicleClass(VehicleClassBase):

    def _execute(self):
        if isPlayerAccount():
            from CurrentVehicle import g_currentVehicle
            itemsCache = dependency.instance(IItemsCache)
            vehicle = self._vehicle.getValue()
            vehId = vehicle.vehicleID
            if g_currentVehicle.item and g_currentVehicle.item.descriptor.type.compactDescr == vehId:
                vehicle = g_currentVehicle.item
            else:
                vehicle = itemsCache.items.getItemByCD(vehId)
            self._outSlot.setValue(next(iter(vehicle.type)))
        else:
            avatar = BigWorld.player()
            if avatar:
                tags = avatar.vehicleTypeDescriptor.type.tags
                self._outSlot.setValue(next((classTag for classTag in VEHICLE_CLASSES if classTag in tags), b''))
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]


class GunTypeInfo(GunTypeInfoBase):

    def _execute(self):
        self._outSlot.setValue([])
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class VehicleForwardSpeed(VehicleForwardSpeedBase):

    def _execute(self):
        vehicle = self._vehicle.getValue()
        self._outSlot.setValue(vehicle.getSpeed())
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class VehicleCooldownEquipment(VehicleCooldownEquipmentBase):

    def _execute(self):
        if isPlayerAccount():
            from CurrentVehicle import g_currentVehicle
            itemsCache = dependency.instance(IItemsCache)
            vehicle = self._vehicle.getValue()
            vehIntId = vehicle.vehicleID
            if g_currentVehicle.item and g_currentVehicle.item.descriptor.type.compactDescr == vehIntId:
                vehicle = g_currentVehicle.item
            else:
                vehicle = itemsCache.items.getItemByCD(vehIntId)
            eqs = vehicle.getCooldownEquipment()
            self._outSlot.setValue(eqs)
        else:
            self._outSlot.setValue([])
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class VehicleClipFullAndReady(VehicleClipFullAndReadyBase):

    def _execute(self):
        self._outSlot.setValue(True)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetNearestAliveVehicle(Block, VehicleMeta):
    _settingTypes = [
     b'Ally', b'Enemy', b'Any']

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Vehicle Team', SLOT_TYPE.STR, buildStrKeysValue(*cls._settingTypes), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def __init__(self, *args, **kwargs):
        super(GetNearestAliveVehicle, self).__init__(*args, **kwargs)
        self._settingType, = self._getInitParams()
        self._position = self._makeDataInputSlot(b'position', SLOT_TYPE.VECTOR3)
        self._vehicle = self._makeDataOutputSlot(b'vehicle', SLOT_TYPE.VEHICLE, self._execute)
        return

    def __checkVehicle(self, vehicle):
        player = BigWorld.player()
        if not hasattr(vehicle, b'isStarted') or not vehicle.isStarted or not vehicle.isAlive():
            return False
        if player.vehicle and vehicle.id == player.vehicle.id:
            return False
        if self._settingType == b'Ally':
            return vehicle.publicInfo.team == player.team
        if self._settingType == b'Enemy':
            return vehicle.publicInfo.team != player.team
        return True

    def _execute(self):
        player = BigWorld.player()
        vehicles = (v for v in player.vehicles if self.__checkVehicle(v))
        vehicle = None
        minDist = 99999
        for v in vehicles:
            dist = player.vehicle.position.distTo(v.position)
            if dist < minDist:
                vehicle = v
                minDist = dist

        self._vehicle.setValue(weakref.proxy(vehicle) if vehicle else None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetAnyVehicle(Block, VehicleMeta):
    _settingTypes = [
     b'Ally', b'Enemy', b'Any']

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Vehicle Team', SLOT_TYPE.STR, buildStrKeysValue(*cls._settingTypes), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def __init__(self, *args, **kwargs):
        super(GetAnyVehicle, self).__init__(*args, **kwargs)
        self._settingType, = self._getInitParams()
        self._vehicle = self._makeDataOutputSlot(b'vehicle', SLOT_TYPE.VEHICLE, self._execute)
        return

    def __checkVehicle(self, vehicle):
        player = BigWorld.player()
        if not hasattr(vehicle, b'isStarted') or not vehicle.isStarted or not vehicle.isAlive():
            return False
        if player.vehicle and vehicle.id == player.vehicle.id:
            return False
        if self._settingType == b'Ally':
            return vehicle.publicInfo.team == player.team
        if self._settingType == b'Enemy':
            return vehicle.publicInfo.team != player.team
        return True

    def _execute(self):
        player = BigWorld.player()
        vehicles = [v for v in player.vehicles if self.__checkVehicle(v)]
        vehicle = random.choice(vehicles) if vehicles else None
        self._vehicle.setValue(weakref.proxy(vehicle) if vehicle else None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GameObjectToVehicle(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GameObjectToVehicle, self).__init__(*args, **kwargs)
        self._go = self._makeDataInputSlot(b'gameObject', SLOT_TYPE.GAME_OBJECT)
        self._vehicle = self._makeDataOutputSlot(b'vehicle', SLOT_TYPE.VEHICLE, self._exec)
        return

    def _exec(self):
        go = self._go.getValue()
        if go is None:
            errorVScript(self, b'Please check input game object.')
            return
        else:
            goSyncComponent = go.findRead(GenericComponents.EntityGOSync)
            if goSyncComponent is None:
                LOG_DEBUG_DEV(b"Can't find associated entity. Please check input game object")
                self._vehicle.setValue(None)
                return
            try:
                entity = weakref.proxy(goSyncComponent.entity)
            except TypeError:
                LOG_DEBUG_DEV(b'Cannot find associated entity. Input GO might be partially destroyed.')
                entity = None

            self._vehicle.setValue(entity)
            return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class IsInHangar(IsInHangarBase):

    def _execute(self):
        self._outSlot.setValue(isPlayerAccount())
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class VehicleRadioDistance(VehicleRadioDistanceBase):

    def _execute(self):
        self._outSlot.setValue(256.0)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetVehicleTier(Block):

    def __init__(self, *args, **kwargs):
        super(GetVehicleTier, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._outSlot = self._makeDataOutputSlot(b'tier', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        v = self._vehicle.getValue()
        self._outSlot.setValue(v.typeDescriptor.level)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnAnyVehicleRespawned(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES = [
     b'onRespawn']

    def __init__(self, *args, **kwargs):
        super(OnAnyVehicleRespawned, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataOutputSlot(b'vehicle', SLOT_TYPE.VEHICLE, None)
        return

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena_event'

    def onStartScript(self):
        VehicleRespawnComponent.onVehicleRespawned += self._vehicleRespawnHandler
        return

    def onFinishScript(self):
        VehicleRespawnComponent.onVehicleRespawned -= self._vehicleRespawnHandler
        return

    @TunableEventBlock.eventProcessor
    def _vehicleRespawnHandler(self, vehicle):
        self._vehicle.setValue(weakref.proxy(vehicle))
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class VehicleMaxSpeed(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(VehicleMaxSpeed, self).__init__(*args, **kwargs)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._speed = self._makeDataOutputSlot(b'speed', SLOT_TYPE.FLOAT, self._execute)
        return

    def _execute(self):
        vehicle = self._vehicle.getValue()
        self._speed.setValue(vehicle.typeDescriptor.physics[b'speedLimits'][0])
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnVehicleCollided(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(OnVehicleCollided, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._vehicle = self._makeDataOutputSlot(b'vehicle', SLOT_TYPE.VEHICLE, None)
        self._velocity = self._makeDataOutputSlot(b'velocity', SLOT_TYPE.FLOAT, None)
        return

    def onStartScript(self):
        if isPlayerAvatar():
            BigWorld.player().inputHandler.OnVehicleCollided += self._onVehicleCollided
        else:
            errorVScript(self, b'can not subscribe on event')
        return

    def onFinishScript(self):
        if isPlayerAvatar():
            BigWorld.player().inputHandler.OnVehicleCollided -= self._onVehicleCollided
        return

    def _onVehicleCollided(self, vehicleId, velocity):
        vehicle = BigWorld.entity(vehicleId)
        if vehicle:
            self._vehicle.setValue(weakref.proxy(vehicle))
            self._velocity.setValue(velocity)
            self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnVehicleShaked(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(OnVehicleShaked, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._vehicle = self._makeDataOutputSlot(b'vehicle', SLOT_TYPE.VEHICLE, None)
        self._shakeReason = self._makeDataOutputSlot(b'shakeReason', SLOT_TYPE.INT, None)
        return

    def onStartScript(self):
        if isPlayerAvatar():
            BigWorld.player().inputHandler.OnVehicleShaked += self._onVehicleShaked
        else:
            errorVScript(self, b'can not subscribe on event')
        return

    def onFinishScript(self):
        if isPlayerAvatar():
            BigWorld.player().inputHandler.OnVehicleShaked -= self._onVehicleShaked
        return

    def _onVehicleShaked(self, vehicleId, shakeReason):
        vehicle = BigWorld.entity(vehicleId)
        if vehicle:
            self._vehicle.setValue(weakref.proxy(vehicle))
            self._shakeReason.setValue(shakeReason)
            self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetVehicleOverturnLevel(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleOverturnLevel, self).__init__(*args, **kwargs)
        self._vehicleGO = self._makeDataInputSlot(b'vehicleGameObject', SLOT_TYPE.GAME_OBJECT)
        self._overturnLevel = self._makeDataOutputSlot(b'overturnLevel', OverturnWarningLevelEnum.slotType(), self._getData)
        return

    def _getData(self):
        vehicleGO = self._vehicleGO.getValue()
        if vehicleGO.valid:
            ownVehicle = vehicleGO.findRead(OwnVehicle.OwnVehicle)
            if ownVehicle is not None:
                overturnLevel = ownVehicle.overturnLevel
                if overturnLevel is not None:
                    self._overturnLevel.setValue(overturnLevel.level)
                    return
        self._overturnLevel.setValue(OVERTURN_WARNING_LEVEL.SAFE)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class GetVehicleDrownLevel(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleDrownLevel, self).__init__(*args, **kwargs)
        self._vehicleGO = self._makeDataInputSlot(b'vehicleGameObject', SLOT_TYPE.GAME_OBJECT)
        self._drownLevel = self._makeDataOutputSlot(b'drownLevel', DrownWarningLevelEnum.slotType(), self._getData)
        return

    def _getData(self):
        vehicleGO = self._vehicleGO.getValue()
        if vehicleGO.valid:
            ownVehicle = vehicleGO.findRead(OwnVehicle.OwnVehicle)
            if ownVehicle is not None:
                drownLevel = ownVehicle.drownLevel
                if drownLevel is not None:
                    self._drownLevel.setValue(drownLevel.level)
                    return
        self._drownLevel.setValue(DROWN_WARNING_LEVEL.SAFE)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class OnDiscreteShotDone(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(OnDiscreteShotDone, self).__init__(*args, **kwargs)
        self._subscribe = self._makeEventInputSlot(b'subscribe', self.__subscribe)
        self._unsubscribe = self._makeEventInputSlot(b'unsubscribe', self.__unsubscribe)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._onDiscreteShotDoneSlot = self._makeEventOutputSlot(b'onDiscreteShotDone')
        return

    def __subscribe(self):
        vehicle = self._vehicle.getValue()
        if vehicle is None:
            errorVScript(self, b'vehicle not found')
            return
        else:
            vehicle.events.onDiscreteShotDone += self.__onDiscreteShotDone
            return

    def __unsubscribe(self):
        vehicle = self._vehicle.getValue()
        if vehicle is None:
            return
        else:
            vehicle.events.onDiscreteShotDone -= self.__onDiscreteShotDone
            return

    def __onDiscreteShotDone(self, gunInstallationSlot):
        if gunInstallationSlot.isMainInstallation():
            self._onDiscreteShotDoneSlot.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]
