from __future__ import absolute_import
from collections import OrderedDict
from typing import Dict
from items.components.c11n_constants import ApplyArea
from py2to3.patched_future import with_metaclass
from serialization.field import intField, strField, applyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = (b'PersonalNumberComponent',)

class PersonalNumberComponent(with_metaclass(ReflectionMetaclass, SerializableComponent)):
    customType = C11nSerializationTypes.PERSONAL_NUMBER
    fields = OrderedDict((
     (
      b'id', intField()),
     (
      b'number', strField()),
     (
      b'appliedTo', applyAreaEnumField(ApplyArea.NONE))))
    __slots__ = (b'id', b'number', b'appliedTo')

    def __init__(self, id=0, number=None, appliedTo=ApplyArea.NONE):
        self.id = id
        self.number = number or b''
        self.appliedTo = appliedTo
        super(PersonalNumberComponent, self).__init__()
        return

    def isFilled(self):
        return bool(self.number)

    def toDict(self):
        at = self.appliedTo
        p = self.id
        return {i: p for i in ApplyArea.RANGE if i & at}
