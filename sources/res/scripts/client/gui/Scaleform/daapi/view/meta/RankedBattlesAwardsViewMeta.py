from gui.Scaleform.framework.entities.View import View

class RankedBattlesAwardsViewMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onSoundTrigger(self, triggerName):
        self._printOverrideError(b'onSoundTrigger')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
