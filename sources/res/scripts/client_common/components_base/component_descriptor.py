from __future__ import absolute_import
from components_base.auto_properties import AutoProperty
from components_base.component_controller import ComponentController

class ComponentDescriptor(AutoProperty):

    def __init__(self, fieldName=None):
        AutoProperty.__init__(self, fieldName)
        return

    def __set__(self, instance, value):
        prevValue = getattr(instance, self.fieldName, None)
        if prevValue is not None:
            if self.__isIterable(prevValue):
                for element in prevValue:
                    instance.removeComponent(element)

            else:
                instance.removeComponent(prevValue)
        if value is not None:
            if self.__isIterable(value):
                for element in value:
                    self.__setValue(instance, element)

            else:
                self.__setValue(instance, value)
        instance.touchDescriptor(self.fieldName)
        setattr(instance, self.fieldName, value)
        return

    def __setValue(self, instance, value):
        if getattr(value, b'isOwning', True):
            instance.addComponent(value, self.fieldName)
        else:
            instance.registerComponent(value)
        return

    def __isIterable(self, value):
        return hasattr(value, b'__iter__')


class ComponentDescriptorTyped(ComponentDescriptor):

    def __init__(self, allowedType, fieldName=None):
        ComponentDescriptor.__init__(self, fieldName)
        self.allowedType = allowedType
        return

    def __set__(self, instance, value):
        ComponentDescriptor.__set__(self, instance, value)
        return
