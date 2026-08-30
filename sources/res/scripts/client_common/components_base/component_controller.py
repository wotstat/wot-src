from __future__ import absolute_import
import typing
from future.utils import with_metaclass
from components_base.auto_properties import AutoPropertyInitMetaclass
if typing.TYPE_CHECKING:
    from components_base.component import Component

class ComponentController(with_metaclass(AutoPropertyInitMetaclass, object)):

    def __init__(self, name=b''):
        self._components = []
        self.__touchedDescriptors = set()
        self.__name = name
        return

    def activate(self):
        for component in self._components:
            component.activate()

        return

    def deactivate(self):
        for component in self._components:
            component.deactivate()

        return

    def touchDescriptor(self, descriptorName):
        self.__touchedDescriptors.add(descriptorName)
        return

    def addComponent(self, component, name=b''):
        self._components.append(component)
        return

    def removeComponent(self, component):
        self._components.remove(component)
        return

    def destroy(self):
        for component in self._components:
            component.destroy()

        self.reset()
        return

    def reset(self):
        for descriptorName in self.__touchedDescriptors:
            setattr(self, descriptorName, None)

        self._components = []
        return

    def registerComponent(self, component):
        self._components.append(component)
        return
