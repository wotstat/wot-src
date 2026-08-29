from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.meta.BaseRallyViewMeta import BaseRallyViewMeta
from gui.prb_control.entities.base.cooldown import getPrbRequestCoolDown
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared import events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.utils.MethodsRules import MethodsRules

class BaseRallyView(BaseRallyViewMeta, IGlobalListener, MethodsRules):

    def setData(self, initialData):
        LOG_DEBUG(b'BaseRallyView.setItemId stub implementation. Passed id is:', initialData)
        return

    def getCoolDownRequests(self):
        return []

    @MethodsRules.delayable()
    def _populate(self):
        super(BaseRallyView, self)._populate()
        self._startListening()
        self._checkCoolDowns()
        return

    def _dispose(self):
        self._stopListening()
        self.clear()
        super(BaseRallyView, self)._dispose()
        return

    def _handleSetPrebattleCoolDown(self, event):
        if event.requestID in self.getCoolDownRequests():
            self.as_setCoolDownS(event.coolDown, event.requestID)
        return

    def _checkCoolDowns(self):
        for requestID in self.getCoolDownRequests():
            coolDown = getPrbRequestCoolDown(requestID)
            if coolDown > 0:
                self.as_setCoolDownS(coolDown, requestID)

        return

    def _doLeave(self, isExit=True):
        action = LeavePrbAction(isExit=isExit)
        event = events.PrbActionEvent(action, events.PrbActionEvent.LEAVE)
        g_eventBus.handleEvent(event, EVENT_BUS_SCOPE.LOBBY)
        return

    @MethodsRules.delayable(b'_populate')
    def _startListening(self):
        self.startPrbListening()
        self.startGlobalListening()
        self.addListener(events.CoolDownEvent.PREBATTLE, self._handleSetPrebattleCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _stopListening(self):
        self.stopGlobalListening()
        self.stopPrbListening()
        self.removeListener(events.CoolDownEvent.PREBATTLE, self._handleSetPrebattleCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        return
