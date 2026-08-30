from __future__ import absolute_import
import CGF
from functools import partial
from GenericComponents import DecalComponent, EntityGOSync
from cgf_script.registration import ComponentProperty, registerComponent
from vehicle_systems.model_assembler import loadAppearancePrefab
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import List

@registerComponent
class SerialNumberSwitcher(object):
    editorTitle = b'Serial Number Switcher'
    domain = CGF.Domain.Client
    lamp3digits = ComponentProperty(type=CGF.PropertyType.String, editorName=b'3 digits', annotations={b'path': b'*.prefab'})
    lamp4digits = ComponentProperty(type=CGF.PropertyType.String, editorName=b'4 digits', annotations={b'path': b'*.prefab'})
    lamp5digits = ComponentProperty(type=CGF.PropertyType.String, editorName=b'5 digits', annotations={b'path': b'*.prefab'})

    def getPrefabPath(self, counterValue):
        length = len(counterValue)
        if length > 4:
            return self.lamp5digits
        if length > 3:
            return self.lamp4digits
        return self.lamp3digits


@registerComponent
class SerialNumberComponent(object):
    editorTitle = b'Serial Number'
    domain = CGF.Domain.Client
    counterValue = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Counter Value', value=b'00000')
    splitNumber = ComponentProperty(type=CGF.PropertyType.Bool, editorName=b'Split number', value=False)
    decalComponent = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'DecalLink', value=DecalComponent)
    decalCount = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Decal count', value=1)


class SerialNumberComponentSystem(CGF.System):
    DEFAULT_NUMBER = b'00000'
    SwitcherActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(SerialNumberSwitcher))
    NumberActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(SerialNumberComponent))
    DecalAccess = CGF.AccessReaction(CGF.Rw(DecalComponent))
    EntityGOSyncAccess = CGF.AccessReaction(CGF.Rw(EntityGOSync))
    Reactions = CGF.Reactions(SwitcherActivated, NumberActivated, DecalAccess, EntityGOSyncAccess)

    def update(self):
        decalAccess = self.reaction(self.DecalAccess)
        for go, switcher in self.reaction(self.SwitcherActivated):
            vehicle = self.__getVehicle(go)
            if vehicle is not None:
                counterValue = self.__getSerialNumberValue(vehicle)
                prefabPath = switcher.getPrefabPath(counterValue)
                loadAppearancePrefab(prefabPath, vehicle.appearance, partial(self.__onLoaded, counterValue))

        for go, number in self.reaction(self.NumberActivated):
            vehicle = self.__getVehicle(go)
            counterValue = self.__getSerialNumberValue(vehicle)
            if number.decalComponent:
                if number.splitNumber:
                    for i, value in enumerate(counterValue):
                        decalAccess.find(number.decalComponent).setCounterStickerValue(i, value)

                else:
                    for i in range(number.decalCount):
                        decalAccess.find(number.decalComponent).setCounterStickerValue(i, counterValue)

        return

    def __onLoaded(self, counterValue, root, _, queue):
        if queue.hasComponent(root, SerialNumberComponent):
            serialNumber = queue.component(root, SerialNumberComponent)
            if serialNumber:
                serialNumber.counterValue = counterValue
        return

    def __getVehicle(self, gameObject):
        hierarchy = CGF.findHierarchySingleton(self.spaceID)
        access = self.reaction(self.EntityGOSyncAccess)
        rootGameObject = hierarchy.getTopMostParent(gameObject)
        goSyncComponent = access.find(rootGameObject)
        if goSyncComponent is None:
            return
        else:
            return goSyncComponent.entity

    def __getSerialNumberValue(self, vehicle):
        counterValue = str()
        if vehicle is not None:
            counterValue = vehicle.appearance.outfit.serialNumber
        if counterValue:
            return counterValue
        else:
            return self.DEFAULT_NUMBER
