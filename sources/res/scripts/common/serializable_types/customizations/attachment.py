from __future__ import absolute_import
from collections import OrderedDict
from py2to3.patched_future import with_metaclass
from serialization.field import intField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = (b'AttachmentComponent',)

class AttachmentComponent(with_metaclass(ReflectionMetaclass, SerializableComponent)):
    customType = C11nSerializationTypes.ATTACHMENT
    fields = OrderedDict((
     (
      b'id', intField()),
     (
      b'slotId', intField()),
     (
      b'scaleFactorId', intField()),
     (
      b'rotated', intField())))
    __slots__ = (b'id', b'slotId', b'scaleFactorId', b'rotated')

    def __init__(self, id=0, slotId=0, scaleFactorId=0, rotated=0):
        self.id = id
        self.slotId = slotId
        self.scaleFactorId = scaleFactorId
        self.rotated = rotated
        super(AttachmentComponent, self).__init__()
        return

    @property
    def isRotated(self):
        return bool(self.rotated)

    def setScaleFactorId(self, itemScaleFactorId, slotScaleFactorId):
        self.scaleFactorId = min(itemScaleFactorId, slotScaleFactorId)
        return
