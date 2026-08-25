from __future__ import absolute_import
import typing
from frameworks.state_machine import State
if typing.TYPE_CHECKING:
    from enum import IntEnum

class BaseState(State):
    __slots__ = (b'_view', b'_widgetType', b'_widgetId')

    def __init__(self, stateID, flags):
        super(BaseState, self).__init__(stateID.name, flags)
        self._view = None
        self._widgetType = None
        self._widgetId = None
        return

    def configure(self, view, widgetType, widgetId):
        super(BaseState, self).configure()
        self._view = view
        self._widgetType = widgetType
        self._widgetId = widgetId
        return

    def getSettings(self):
        return self._view.getSettings((self._widgetType, self._widgetId))

    def update(self):
        self._updateView()
        return

    def _onEntered(self, event):
        self._showView()
        return

    def _showView(self):
        return

    def _updateView(self):
        return


class BaseTimerState(BaseState):
    __slots__ = (b'_doShow', b'_doUpdate')

    def __init__(self, stateID, flags):
        super(BaseTimerState, self).__init__(stateID, flags)
        self._doUpdate = False
        self._doShow = False
        return

    def update(self):
        self._doUpdate = True
        return

    def _onEntered(self, event):
        self._doShow = True
        return

    def _onExited(self):
        super(BaseTimerState, self)._onExited()
        self._doUpdate = False
        self._doShow = False
        return

    def tick(self, currentTime):
        if self._doShow:
            self._showView()
            self._doShow = False
            self._doUpdate = False
        elif self._doUpdate:
            self._updateView()
            self._doUpdate = False
        return
