from __future__ import absolute_import
import typing
from events_containers.common.container_wrappers import activateEventsContainer
from events_containers.components.life_cycle.events import ComponentLifeCycleEvents
from events_containers.components.life_cycle.interfaces import ILifeCycleComponent, IComponentLifeCycleEvents, IComponentLifeCycleListener, IComponentLifeCycleListenerLogic
__all__ = (b'ILifeCycleComponent', b'IComponentLifeCycleEvents', b'IComponentLifeCycleListener', b'IComponentLifeCycleListenerLogic', b'ComponentLifeCycleEvents', b'isLifeCycleComponent', b'createComponentLifeCycleEvents')

def isLifeCycleComponent(component):
    return isinstance(component, ILifeCycleComponent)


@activateEventsContainer()
def createComponentLifeCycleEvents(component, **_):
    return ComponentLifeCycleEvents(component)
