from gui.Scaleform.daapi.view.lobby.award_window_base import AwardWindowBase

class MissionAwardWindowMeta(AwardWindowBase):

    def onCurrentQuestClick(self):
        self._printOverrideError(b'onCurrentQuestClick')
        return

    def onNextQuestClick(self):
        self._printOverrideError(b'onNextQuestClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
