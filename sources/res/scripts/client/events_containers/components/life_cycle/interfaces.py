from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener

class ILifeCycleComponent(object):

    @property
    def lifeCycleEvents(self):
        raise NotImplementedError
        return

    def getComponentParams(self):
        return


class IComponentLifeCycleEventsLogic(object):
    onComponentParamsCollected = None
    onComponentAppearanceReady = None
    onComponentAppearanceReset = None
    onComponentDestroyed = None

    def processAppearanceReady(self):
        raise NotImplementedError
        return

    def processAppearanceReset(self):
        raise NotImplementedError
        return

    def processParamsCollected(self):
        raise NotImplementedError
        return


class IComponentLifeCycleEvents(IClientEventsContainer, IComponentLifeCycleEventsLogic):
    pass


class IComponentLifeCycleListenerLogic(object):

    def onComponentParamsCollected(self, params):
        return

    def onComponentAppearanceReady(self, component):
        return

    def onComponentAppearanceReset(self, component):
        return

    def onComponentDestroyed(self, component):
        return


class IComponentLifeCycleListener(IClientEventsContainerListener, IComponentLifeCycleListenerLogic):
    pass
