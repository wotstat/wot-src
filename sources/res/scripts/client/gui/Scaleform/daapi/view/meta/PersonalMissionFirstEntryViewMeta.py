from gui.Scaleform.framework.entities.View import View

class PersonalMissionFirstEntryViewMeta(View):

    def playVideo(self):
        self._printOverrideError(b'playVideo')
        return

    def backBtnClicked(self):
        self._printOverrideError(b'backBtnClicked')
        return

    def onViewClose(self, isAcceptBtnClick):
        self._printOverrideError(b'onViewClose')
        return

    def onCardClick(self, cardID):
        self._printOverrideError(b'onCardClick')
        return

    def onNextCardClick(self, cardID):
        self._printOverrideError(b'onNextCardClick')
        return

    def onPrevCardClick(self, cardID):
        self._printOverrideError(b'onPrevCardClick')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setDetailedCardDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDetailedCardData(data)
        return
