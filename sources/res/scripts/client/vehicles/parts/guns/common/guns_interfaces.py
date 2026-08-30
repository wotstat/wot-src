from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
from vehicles.components.component_interfaces import IVehicleGunSlotComponent

class IGunComponent(IVehicleGunSlotComponent):

    @property
    def shootingEvents(self):
        raise NotImplementedError
        return


class IGunShootingEventsLogic(object):
    onAppearanceReady = None
    onDiscreteShot = None
    onMultiShot = None

    def processAppearanceReady(self):
        raise NotImplementedError
        return

    def processAppearanceReset(self):
        raise NotImplementedError
        return

    def processDiscreteShot(self, gunIndex):
        raise NotImplementedError
        return

    def processMultiShot(self, gunIndexes):
        raise NotImplementedError
        return


class IGunShootingEvents(IClientEventsContainer, IGunShootingEventsLogic):
    pass


class IGunShootingListenerLogic(object):

    def onAppearanceReady(self):
        return

    def onDiscreteShot(self, gunIndex):
        return

    def onMultiShot(self, gunIndexes):
        return


class IGunShootingListener(IClientEventsContainerListener, IGunShootingListenerLogic):
    pass
