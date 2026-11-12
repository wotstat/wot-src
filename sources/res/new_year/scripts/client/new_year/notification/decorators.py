from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from new_year.skeletons.new_year import INewYearController
from notification.decorators import MessageDecorator
from notification.settings import NOTIFICATION_BUTTON_STATE

class NyMessageButtonDecorator(MessageDecorator, IGlobalListener):
    _nyController = dependency.descriptor(INewYearController)

    def __init__(self, entityID, entity=None, settings=None, model=None):
        super(NyMessageButtonDecorator, self).__init__(entityID, entity, settings, model)
        self.startGlobalListening()
        self._nyController.onStateChanged += self.__doUpdateButtons
        return

    def clear(self):
        self.stopGlobalListening()
        self._nyController.onStateChanged -= self.__doUpdateButtons
        super(NyMessageButtonDecorator, self).clear()
        return

    def onEnqueued(self, queueType, *args):
        self.__doUpdateButtons()
        return

    def onDequeued(self, queueType, *args):
        self.__doUpdateButtons()
        return

    def onUnitFlagsChanged(self, flags, timeLeft):
        self.__doUpdateButtons()
        return

    def _make(self, formatted=None, settings=None):
        self._updateEntityButtons()
        super(NyMessageButtonDecorator, self)._make(formatted, settings)
        return

    def _updateEntityButtons(self):
        if self._entity is None:
            return
        else:
            buttonsLayout = self._entity.get(b'buttonsLayout')
            if not buttonsLayout:
                return
            buttonsStates = self._entity.get(b'buttonsStates')
            state, tooltip = self._getButtonState()
            buttonsStates[b'submit'] = state
            buttonsLayout[0][b'tooltip'] = tooltip
            return

    def _getButtonState(self):
        state, tooltip = NOTIFICATION_BUTTON_STATE.DEFAULT, b''
        bodyId = None
        if self.prbEntity is not None and self.prbEntity.isInQueue():
            state = NOTIFICATION_BUTTON_STATE.VISIBLE
            bodyId = R.strings.system_messages.queue.isInQueue()
        elif not self._isButtonEnabled():
            state = NOTIFICATION_BUTTON_STATE.VISIBLE
            if self._nyController.isSuspended():
                bodyId = R.strings.ny.notification.suspend()
            elif self._nyController.isPostEvent():
                bodyId = R.strings.ny.notification.postEvent()
            elif self._nyController.isFinished():
                bodyId = R.strings.ny.notification.finish()
        if bodyId:
            tooltip = makeTooltip(body=backport.text(bodyId))
        return (state, tooltip)

    def _updateButtons(self):
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return

    def _isButtonEnabled(self):
        return self._nyController.isEnabled()

    def __doUpdateButtons(self):
        self._updateEntityButtons()
        self._updateButtons()
        return
