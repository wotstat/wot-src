from gui.Scaleform.daapi.view.lobby.award_window_base import AwardWindowBase

class AwardWindowMeta(AwardWindowBase):

    def onOKClick(self):
        self._printOverrideError(b'onOKClick')
        return

    def onTakeNextClick(self):
        self._printOverrideError(b'onTakeNextClick')
        return

    def onCloseClick(self):
        self._printOverrideError(b'onCloseClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
