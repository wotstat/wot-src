from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand

class IMechanicCommandsComponent(object):

    @property
    def commandsEvents(self):
        raise NotImplementedError
        return


class IMechanicCommandsEventsLogic(object):
    onMechanicCommand = None

    def processMechanicCommand(self, command):
        raise NotImplementedError
        return


class IMechanicCommandsEvents(IClientEventsContainer, IMechanicCommandsEventsLogic):
    pass


class IMechanicCommandsListenerLogic(object):

    def onMechanicCommand(self, command):
        return


class IMechanicCommandsListener(IClientEventsContainerListener, IMechanicCommandsListenerLogic):
    pass
