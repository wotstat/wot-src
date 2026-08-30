from gui.Scaleform.framework.entities.View import View

class PersonalMissionsPageMeta(View):

    def onBarClick(self, chainID, operationIdx):
        self._printOverrideError(b'onBarClick')
        return

    def onSkipTaskClick(self, btnID):
        self._printOverrideError(b'onSkipTaskClick')
        return

    def onBackBtnClick(self):
        self._printOverrideError(b'onBackBtnClick')
        return

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onTutorialAcceptBtnClicked(self):
        self._printOverrideError(b'onTutorialAcceptBtnClicked')
        return

    def showAwards(self):
        self._printOverrideError(b'showAwards')
        return

    def as_setContentVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setContentVisible(value)
        return

    def as_initViewS(self, pmType, chainsLen):
        if self._isDAAPIInited():
            return self.flashObject.as_initView(pmType, chainsLen)
        return

    def as_reInitViewS(self, pmType, chainsLen):
        if self._isDAAPIInited():
            return self.flashObject.as_reInitView(pmType, chainsLen)
        return

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)
        return

    def as_updateSideBarDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSideBarData(data)
        return

    def as_setStatusDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusData(data)
        return

    def as_setSelectedBranchIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedBranchIndex(index)
        return

    def as_showFirstAwardSheetObtainedPopupS(self, useAnim, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFirstAwardSheetObtainedPopup(useAnim, data)
        return

    def as_showFourAwardSheetsObtainedPopupS(self, useAnim, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFourAwardSheetsObtainedPopup(useAnim, data)
        return

    def as_hideAwardSheetObtainedPopupS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAwardSheetObtainedPopup()
        return

    def as_showAwardsPopoverForTutorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showAwardsPopoverForTutor()
        return
