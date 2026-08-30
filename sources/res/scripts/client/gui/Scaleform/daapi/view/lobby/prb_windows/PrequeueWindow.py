from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from adisp import adisp_process
from gui.Scaleform.daapi.view.meta.PrequeueWindowMeta import PrequeueWindowMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.managers.windows_stored_data import DATA_TYPE, TARGET_ID
from gui.Scaleform.managers.windows_stored_data import stored_window
from gui.prb_control.entities.base.ctx import LeavePrbAction
from gui.prb_control.entities.base.pre_queue.listener import IPreQueueListener
from gui.shared import events, EVENT_BUS_SCOPE
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

@stored_window(DATA_TYPE.CAROUSEL_WINDOW, TARGET_ID.CHANNEL_CAROUSEL)
class PrequeueWindow(PrequeueWindowMeta, IPreQueueListener):

    def __init__(self, queueName=b'prequeue'):
        super(PrequeueWindow, self).__init__()
        self.__queueName = queueName
        return

    def onWindowClose(self):
        self.destroy()
        return

    def onWindowMinimize(self):
        self.destroy()
        return

    def requestToEnqueue(self):
        self.prbEntity.doAction()
        return

    def requestToLeave(self):
        self._doLeave()
        return

    def showFAQWindow(self):
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(MESSENGER_VIEW_ALIAS.FAQ_WINDOW)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def isEnqueueBtnEnabled(self):
        return g_currentVehicle.isReadyToPrebattle() and not self.prbEntity.isInQueue()

    def isLeaveBtnEnabled(self):
        return not self.prbEntity.isInQueue()

    def startListening(self):
        self.startPrbListening()
        g_currentVehicle.onChanged += self._handleCurrentVehicleChanged
        return

    def stopListening(self):
        self.stopPrbListening()
        g_currentVehicle.onChanged -= self._handleCurrentVehicleChanged
        return

    def _populate(self):
        super(PrequeueWindow, self)._populate()
        self.startListening()
        self.as_enableEnqueueBtnS(self.isEnqueueBtnEnabled())
        return

    def _dispose(self):
        self.stopListening()
        super(PrequeueWindow, self)._dispose()
        return

    def _handleCurrentVehicleChanged(self):
        self.as_enableEnqueueBtnS(self.isEnqueueBtnEnabled())
        return

    @adisp_process
    def _doLeave(self, isExit=True):
        yield self.prbDispatcher.doLeaveAction(LeavePrbAction(isExit))
        return
