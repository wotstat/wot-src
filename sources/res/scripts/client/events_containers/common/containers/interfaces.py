from __future__ import absolute_import
import typing

class IClientEventsContainer(object):
    onEventsContainerDestroy = None

    @property
    def hasListeners(self):
        raise NotImplementedError
        return

    def destroy(self):
        return

    def attachCFGEvents(self):
        return

    def debugEvents(self):
        return

    def lateSubscribe(self, listener):
        listener.subscribeTo(self)
        return

    def unsubscribe(self, listener):
        listener.unsubscribeFrom(self)
        return


class IClientEventsContainerListener(object):

    def subscribeTo(self, events):
        raise NotImplementedError
        return

    def unsubscribeFrom(self, events):
        raise NotImplementedError
        return

    def lateSubscribeTo(self, events):
        raise NotImplementedError
        return
