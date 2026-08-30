from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicBattlesWidgetMeta(BaseDAAPIComponent):

    def onWidgetClick(self):
        self._printOverrideError(b'onWidgetClick')
        return

    def onAnimationFinished(self):
        self._printOverrideError(b'onAnimationFinished')
        return

    def onSoundTrigger(self, trigerName):
        self._printOverrideError(b'onSoundTrigger')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
