from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesHangarWidgetMeta(BaseDAAPIComponent):

    def onWidgetClick(self):
        self._printOverrideError(b'onWidgetClick')
        return

    def onAnimationFinished(self):
        self._printOverrideError(b'onAnimationFinished')
        return

    def onSoundTrigger(self, triggerName):
        self._printOverrideError(b'onSoundTrigger')
        return

    def as_setDataS(self, states):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(states)
        return

    def as_setBonusBattlesLabelS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setBonusBattlesLabel(label)
        return
