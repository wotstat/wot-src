from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesUnreachableViewMeta(WrapperViewMeta):

    def onCloseBtnClick(self):
        self._printOverrideError(b'onCloseBtnClick')
        return

    def onEscapePress(self):
        self._printOverrideError(b'onEscapePress')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
