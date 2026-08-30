from gui.Scaleform.framework.entities.View import View

class PersonalMissionsQuestAwardScreenMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onNextQuestLinkClick(self):
        self._printOverrideError(b'onNextQuestLinkClick')
        return

    def onNextQuestBtnClick(self):
        self._printOverrideError(b'onNextQuestBtnClick')
        return

    def onRecruitBtnClick(self):
        self._printOverrideError(b'onRecruitBtnClick')
        return

    def onContinueBtnClick(self):
        self._printOverrideError(b'onContinueBtnClick')
        return

    def onOkBtnClick(self):
        self._printOverrideError(b'onOkBtnClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
