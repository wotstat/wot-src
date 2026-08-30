import BigWorld
from visual_script.block import Block, Meta
from visual_script.slot_types import SLOT_TYPE
from visual_script.misc import ASPECT
from constants import IS_VS_EDITOR

class TriggerMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16738047

    @classmethod
    def blockCategory(cls):
        return b'Arena'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/input'

    @classmethod
    def blockAspects(cls):
        return [
         ASPECT.CLIENT]


class TriggerExternal(Block, TriggerMeta):

    def __init__(self, *args, **kwargs):
        super(TriggerExternal, self).__init__(*args, **kwargs)
        self._subscribeSlot = self._makeEventInputSlot(b'subscribe', self._onSubscribe)
        self._unsubscribeSlot = self._makeEventInputSlot(b'unsubscribe', self._onUnsubscribe)
        self._eventIDSlot = self._makeDataInputSlot(b'eventID', SLOT_TYPE.STR)
        self._isActiveInputSlot = self._makeDataInputSlot(b'isActive', SLOT_TYPE.BOOL)
        self._outSlot = self._makeEventOutputSlot(b'out')
        self._active = False
        return

    def validate(self):
        if not self._eventIDSlot.hasValue():
            return b'EventID value is required'
        return super(TriggerExternal, self).validate()

    def onStartScript(self):
        isActive = self._isActiveInputSlot.getValue() if self._isActiveInputSlot.hasValue() else True
        if isActive:
            self.setActive(True)
        return

    def onFinishScript(self):
        if self.isActive():
            self.setActive(False)
        return

    def isActive(self):
        return self._active

    def setActive(self, value):
        if self.isActive() == value:
            return
        self._active = value
        if not IS_VS_EDITOR and hasattr(BigWorld.player(), b'onTrigger'):
            if self._active:
                BigWorld.player().onTrigger += self._onTrigger
            else:
                BigWorld.player().onTrigger -= self._onTrigger
        return

    def _onTrigger(self, eventId, *args, **kwargs):
        if self._eventIDSlot.getValue() == eventId:
            self._outSlot.call()
        return

    def _onSubscribe(self):
        self.setActive(True)
        return

    def _onUnsubscribe(self):
        self.setActive(False)
        return
