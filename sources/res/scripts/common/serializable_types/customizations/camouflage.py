from __future__ import absolute_import
from collections import OrderedDict
from items.components.c11n_constants import ApplyArea
from py2to3.patched_future import with_metaclass
from serialization.field import intField, applyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = (b'CamouflageComponent',)

class CamouflageComponent(with_metaclass(ReflectionMetaclass, SerializableComponent)):
    customType = C11nSerializationTypes.CAMOUFLAGE
    fields = OrderedDict((
     (
      b'id', intField()),
     (
      b'patternSize', intField(1)),
     (
      b'appliedTo', applyAreaEnumField(ApplyArea.CAMOUFLAGE_REGIONS_VALUE)),
     (
      b'palette', intField())))
    __slots__ = (b'id', b'patternSize', b'appliedTo', b'palette')

    def __init__(self, id=0, patternSize=1, appliedTo=ApplyArea.CAMOUFLAGE_REGIONS_VALUE, palette=0):
        self.id = id
        self.patternSize = patternSize
        self.appliedTo = appliedTo
        self.palette = palette
        super(CamouflageComponent, self).__init__()
        return
