from __future__ import absolute_import
import typing
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.parts.guns.common.custom_integrations import GunShootingCustomIntegrations
from vehicles.parts.guns.common.guns_interfaces import IGunComponent, IGunShootingEvents, IGunShootingEventsLogic, IGunShootingListener, IGunShootingListenerLogic
from vehicles.parts.guns.common.shooting_events import GunShootingEvents, GunShootingCoreIntegration, GunShootingEventsDebugger
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle
__all__ = (b'IGunComponent', b'IGunShootingEvents', b'IGunShootingEventsLogic', b'IGunShootingListener', b'IGunShootingListenerLogic', b'GunShootingEvents', b'GunShootingCoreIntegration', b'GunShootingEventsDebugger', b'GunShootingCustomIntegrations', b'createGunShootingEvents')

@activateEventsContainer()
def createGunShootingEvents(vehicle, component, **_):
    shootingEvents = GunShootingEvents(component)
    GunShootingCustomIntegrations(vehicle, component).subscribeTo(shootingEvents)
    return shootingEvents
