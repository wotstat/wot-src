from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent
from gui.shared.events import NavigationEvent

class _BackNavigationEvent(SharedEvent):
    EVENT_ID = b'backNavigationEvent'

    def __init__(self, requestingState=None):
        super(_BackNavigationEvent, self).__init__(eventType=self.EVENT_ID)
        self.requestingState = requestingState
        return


class _BackNavigationGeneratedNavigationEvent(NavigationEvent):

    def __init__(self, targetStateID, params, shouldKillView):
        super(_BackNavigationGeneratedNavigationEvent, self).__init__(targetStateID, params)
        self.shouldKillView = shouldKillView
        return


class _NonViewClosingBackNavigationEvent(_BackNavigationEvent):
    EVENT_ID = b'nonViewClosingBackNavigationEvent'


class _StopEvent(NavigationEvent):
    pass
