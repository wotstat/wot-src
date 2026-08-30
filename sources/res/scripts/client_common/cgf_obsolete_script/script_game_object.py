import CGF
from cgf_obsolete_script.auto_properties import AutoProperty, AutoPropertyInitMetaclass

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


class ScriptGameObject(object):
    __metaclass__ = AutoPropertyInitMetaclass
    gameObject = property((lambda self: self._nativeSystem))

    def __init__(self, spaceID, name=b''):
        self._components = []
        self.__touchedDescriptors = set()
        self._nativeSystem = CGF.GameObject(spaceID, name)
        return

    def activate(self):
        self._nativeSystem.activate()
        return

    def deactivate(self):
        self._nativeSystem.deactivate()
        return

    def touchDescriptor(self, descriptorName):
        self.__touchedDescriptors.add(descriptorName)
        return

    def addComponent(self, component, name=b''):
        self._components.append(component)
        self._nativeSystem.addComponent(component, name)
        return

    def removeComponent(self, component):
        if self._nativeSystem.isValid():
            self._nativeSystem.removeComponent(component)
        try:
            self._components.remove(component)
        except ValueError:
            pass

        return

    def destroy(self):
        self.reset(False)
        return

    def reset(self, recreate=True):
        for descriptorName in self.__touchedDescriptors:
            setattr(self, descriptorName, None)

        spaceID = self._nativeSystem.spaceID
        self._components = []
        self._nativeSystem.destroy()
        if recreate:
            self._nativeSystem = CGF.GameObject(spaceID)
        else:
            self._nativeSystem = None
        return

    def __getattr__(self, item):
        if item == b'_nativeSystem':
            raise AttributeError(b'Missing nativeSystem.')
        return getattr(self._nativeSystem, item)

    def registerComponent(self, component):
        self._components.append(component)
        return
