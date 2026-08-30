from __future__ import absolute_import
from events_containers.common.container_wrappers import activateEventsContainer
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_interfaces import IWheeledDashListenerLogic, IWheeledDashEvents
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_events import WheeledDashMiscEvents
__all__ = (b'IWheeledDashListenerLogic', b'IWheeledDashEvents', b'createWheeledDashMiscEvents')

@activateEventsContainer()
def createWheeledDashMiscEvents():
    return WheeledDashMiscEvents()
