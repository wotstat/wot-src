from gui.Scaleform.framework.entities.View import View

class RankedBattlesBattleResultsMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onWidgetUpdate(self):
        self._printOverrideError(b'onWidgetUpdate')
        return

    def animationCheckBoxSelected(self, value):
        self._printOverrideError(b'animationCheckBoxSelected')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
