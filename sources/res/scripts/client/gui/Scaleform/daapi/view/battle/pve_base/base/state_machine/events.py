from __future__ import absolute_import
import typing
from frameworks_common.state_machine import StateEvent, StringEvent

class ToStateEvent(StringEvent):

    def __init__(self, widgetStateName, **kwargs):
        super(ToStateEvent, self).__init__(token=widgetStateName, **kwargs)
        return


class OneSecondEvent(StateEvent):

    @property
    def lastTime(self):
        return self.getArgument(b'lastTime', 0.0)

    @property
    def currentTime(self):
        return self.getArgument(b'currentTime', 0.0)
