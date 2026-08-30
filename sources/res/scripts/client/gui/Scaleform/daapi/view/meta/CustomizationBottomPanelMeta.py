from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationBottomPanelMeta(BaseDAAPIComponent):

    def resetFilter(self):
        self._printOverrideError(b'resetFilter')
        return

    def showBuyWindow(self):
        self._printOverrideError(b'showBuyWindow')
        return

    def refreshFilterData(self):
        self._printOverrideError(b'refreshFilterData')
        return

    def onSelectItem(self, index, intCD, progressionLevel):
        self._printOverrideError(b'onSelectItem')
        return

    def onEditItem(self, intCD):
        self._printOverrideError(b'onEditItem')
        return

    def showGroupFromTab(self, groupId):
        self._printOverrideError(b'showGroupFromTab')
        return

    def onSelectHotFilter(self, index, value):
        self._printOverrideError(b'onSelectHotFilter')
        return

    def switchMode(self, index):
        self._printOverrideError(b'switchMode')
        return

    def returnToStyledMode(self):
        self._printOverrideError(b'returnToStyledMode')
        return

    def onItemIsNewAnimationShown(self, intCD):
        self._printOverrideError(b'onItemIsNewAnimationShown')
        return

    def showVideo(self):
        self._printOverrideError(b'showVideo')
        return

    def showVehiclesSideBar(self):
        self._printOverrideError(b'showVehiclesSideBar')
        return

    def as_showBillS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showBill()
        return

    def as_hideBillS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBill()
        return

    def as_setBottomPanelInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelInitData(data)
        return

    def as_setBottomPanelTabsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelTabsData(data)
        return

    def as_setCarouselDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselData(data)
        return

    def as_setCarouselInfoLabelDataS(self, text, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselInfoLabelData(text, tooltip)
        return

    def as_setFilterDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterData(data)
        return

    def as_setBottomPanelPriceStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanelPriceState(data)
        return

    def as_setCarouselFiltersDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFiltersData(data)
        return

    def as_setProjectionDecalHintVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProjectionDecalHintVisibility(value)
        return

    def as_showPopoverBtnS(self, alias, src, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_showPopoverBtn(alias, src, tooltip)
        return

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
        return

    def as_setItemsPopoverBtnEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setItemsPopoverBtnEnabled(value)
        return

    def as_setNotificationCountersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotificationCounters(data)
        return

    def as_scrollToSlotS(self, intCD, immediately=False):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToSlot(intCD, immediately)
        return

    def as_playFilterBlinkS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playFilterBlink()
        return

    def as_updateEscHelpMessageS(self, visibility):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEscHelpMessage(visibility)
        return

    def as_setFilterFallbackDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilterFallbackData(data)
        return

    def as_setStageSwitcherVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStageSwitcherVisibility(value)
        return

    def as_setVehiclesSidebarBtnVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesSidebarBtnVisibility(value)
        return
