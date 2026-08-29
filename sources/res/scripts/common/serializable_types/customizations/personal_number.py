from collections import OrderedDict
from items.components.c11n_constants import ApplyArea
from serialization.field import intField, strField, applyAreaEnumField
from serialization.serializable_component import SerializableComponent
from wrapped_reflection_framework import ReflectionMetaclass
from ..types import C11nSerializationTypes
__all__ = (b'PersonalNumberComponent',)

class PersonalNumberComponent(SerializableComponent):
    __metaclass__ = ReflectionMetaclass
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
