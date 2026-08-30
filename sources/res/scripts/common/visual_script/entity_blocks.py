from __future__ import absolute_import
import weakref, BigWorld, Math, items
from constants import IS_CLIENT
from visual_script.block import Meta, Block, InitParam, buildStrKeysValue
from visual_script.misc import ASPECT, errorVScript, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE

class EntityMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 65280

    @classmethod
    def blockCategory(cls):
        return b'Entity'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/object'


class CreateEntity(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(CreateEntity, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._arena = self._makeDataInputSlot(b'arena', SLOT_TYPE.ARENA)
        self._type = self._makeDataInputSlot(b'type', SLOT_TYPE.STR)
        self._position = self._makeDataInputSlot(b'position', SLOT_TYPE.VECTOR3)
        self._direction = self._makeDataInputSlot(b'direction', SLOT_TYPE.VECTOR3)
        self._out = self._makeEventOutputSlot(b'out')
        self._entity = self._makeDataOutputSlot(b'entity', SLOT_TYPE.ENTITY, None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]

    def validate(self):
        if not self._arena.hasValue():
            return b'Arena value is required'
        if not self._type.hasValue():
            return b'Type value is required'
        if not self._position.hasValue():
            return b'Position value is required'
        return b''

    def _execute(self):
        mat = Math.Matrix()
        direction = self._direction.getValue() if self._direction.hasValue() else Math.Vector3(1.0, 0.0, 0.0)
        mat.lookAt(Math.Vector3(0.0, 0.0, 0.0), direction, Math.Vector3(0.0, 1.0, 0.0))
        entity = BigWorld.createEntity(self._type.getValue(), self._arena.getValue().spaceID, self._position.getValue(), (
         mat.roll, mat.pitch, mat.yaw), {})
        self._entity.setValue(weakref.proxy(entity))
        self._out.call()
        return


class CreateApplicationPoint(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(CreateApplicationPoint, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._arena = self._makeDataInputSlot(b'arena', SLOT_TYPE.ARENA)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._equipmentName = self._makeDataInputSlot(b'equipmentName', SLOT_TYPE.STR)
        self._position = self._makeDataInputSlot(b'position', SLOT_TYPE.VECTOR3)
        self._direction = self._makeDataInputSlot(b'direction', SLOT_TYPE.VECTOR3)
        self._level = self._makeDataInputSlot(b'level', SLOT_TYPE.INT)
        self._out = self._makeEventOutputSlot(b'out')
        self._entity = self._makeDataOutputSlot(b'entity', SLOT_TYPE.ENTITY, None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]

    def validate(self):
        if not self._arena.hasValue():
            return b'Arena value is required'
        if not self._vehicle.hasValue():
            return b'Vehicle value is required'
        if not self._equipmentName.hasValue():
            return b'EquipmentName value is required'
        if not self._position.hasValue():
            return b'Position value is required'
        return b''

    def _execute(self):
        mat = Math.Matrix()
        direction = self._direction.getValue() if self._direction.hasValue() else Math.Vector3(1.0, 0.0, 0.0)
        mat.lookAt(Math.Vector3(0.0, 0.0, 0.0), direction, Math.Vector3(0.0, 1.0, 0.0))
        vehicle = self._vehicle.getValue()
        equipmentName = self._equipmentName.getValue()
        equipmentID = items.vehicles.g_cache.equipmentIDs().get(equipmentName)
        if equipmentID is None:
            errorVScript(self, (b'Unknown equipment [{}]').format(equipmentName))
            return
        else:
            level = self._level.getValue() if self._level.hasValue() else 0
            entity = BigWorld.createEntity(b'ApplicationPoint', self._arena.getValue().spaceID, self._position.getValue(), (
             mat.roll, mat.pitch, mat.yaw), {b'vehicleID': (vehicle.id), 
               b'equipmentID': equipmentID, 
               b'launchTime': (BigWorld.time()), 
               b'level': level})
            self._entity.setValue(weakref.proxy(entity))
            self._out.call()
            return


class DestroyEntity(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(DestroyEntity, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._ignoreIfMissing = self._makeDataInputSlot(b'ignoreIfMissing', SLOT_TYPE.BOOL)
        self._ignoreIfMissing.setDefaultValue(False)
        self._out = self._makeEventOutputSlot(b'out')
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]

    def _execute(self):
        entity = self._entity.getValue()
        try:
            entity.destroy()
        except (AttributeError, ReferenceError, TypeError):
            if not self._ignoreIfMissing.getValue():
                errorVScript(self, b'Cannot destroy entity: entity is None')

        self._out.call()
        return


class IsEntityOfType(Block, EntityMeta):
    _types = (b'EmptyEntity', b'Vehicle')

    def __init__(self, *args, **kwargs):
        super(IsEntityOfType, self).__init__(*args, **kwargs)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._type, = self._getInitParams()
        self._res = self._makeDataOutputSlot(b'res', SLOT_TYPE.BOOL, self._execute)
        return

    @classmethod
    def initParams(cls):
        return super(IsEntityOfType, cls).initParams() + [
         InitParam(b'Type', SLOT_TYPE.STR, buildStrKeysValue(*cls._types), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def captionText(self):
        return b'Is Entity ' + self._type

    def _execute(self):
        entity = self._entity.getValue()
        if IS_CLIENT:
            className = entity.__class__.__name__
        else:
            className = entity.className
        self._res.setValue(className == self._type)
        return


class BoardEntity(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(BoardEntity, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._exec)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.ENTITY)
        self._out = self._makeEventOutputSlot(b'out')
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]

    def _exec(self):
        entity = self._entity.getValue()
        vehicle = self._vehicle.getValue()
        entity.boardVehicle(vehicle.id)
        self._out.call()
        return


class Teleport(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(Teleport, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._exec)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._position = self._makeDataInputSlot(b'position', SLOT_TYPE.VECTOR3)
        self._direction = self._makeDataInputSlot(b'direction', SLOT_TYPE.VECTOR3)
        self._out = self._makeEventOutputSlot(b'out')
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]

    def validate(self):
        if not self._entity.hasValue():
            return b'Entity value is required'
        if not self._position.hasValue():
            return b'Position value is required'
        return b''

    def _exec(self):
        entity = self._entity.getValue()
        position = self._position.getValue()
        if self._direction.hasValue():
            direction = self._direction.getValue()
        else:
            direction = (
             entity.yaw, entity.pitch, entity.roll)
        entity.teleport(None, position, direction)
        self._out.call()
        return


class GetEntityId(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(GetEntityId, self).__init__(*args, **kwargs)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._res = self._makeDataOutputSlot(b'id', SLOT_TYPE.INT, self._exec)
        return

    def _exec(self):
        entity = self._entity.getValue()
        if entity:
            self._res.setValue(entity.id)
        return


class GetEntityTransform(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(GetEntityTransform, self).__init__(*args, **kwargs)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._position = self._makeDataOutputSlot(b'position', SLOT_TYPE.VECTOR3, self._exec)
        self._direction = self._makeDataOutputSlot(b'direction', SLOT_TYPE.VECTOR3, self._exec)
        self._yaw = self._makeDataOutputSlot(b'yaw', SLOT_TYPE.FLOAT, self._exec)
        self._pitch = self._makeDataOutputSlot(b'pitch', SLOT_TYPE.FLOAT, self._exec)
        self._roll = self._makeDataOutputSlot(b'roll', SLOT_TYPE.FLOAT, self._exec)
        return

    def _exec(self):
        entity = self._entity.getValue()
        if entity:
            self._position.setValue(entity.position)
            self._direction.setValue(entity.direction)
            self._yaw.setValue(entity.yaw)
            self._pitch.setValue(entity.pitch)
            self._roll.setValue(entity.roll)
        return


class IsEntityDestroyed(Block, EntityMeta):

    def __init__(self, *args, **kwargs):
        super(IsEntityDestroyed, self).__init__(*args, **kwargs)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._isDestroyed = self._makeDataOutputSlot(b'isDestroyed', SLOT_TYPE.BOOL, self._exec)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER]

    def _exec(self):
        try:
            entity = self._entity.getValue()
            if entity:
                self._isDestroyed.setValue(entity.isDestroyed)
            else:
                self._isDestroyed.setValue(True)
        except (AttributeError, ReferenceError):
            errorVScript(self, b'Dead weakref')
            self._isDestroyed.setValue(True)

        return
