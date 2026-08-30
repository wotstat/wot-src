from gui.Scaleform.framework.entities.View import View

class CustomizationMainViewMeta(View):

    def showQuestProgressionInfoWindow(self):
        self._printOverrideError(b'showQuestProgressionInfoWindow')
        return

    def showBuyWindow(self):
        self._printOverrideError(b'showBuyWindow')
        return

    def onCloseWindow(self):
        self._printOverrideError(b'onCloseWindow')
        return

    def fadeOutAnchors(self, value):
        self._printOverrideError(b'fadeOutAnchors')
        return

    def changeSeason(self, season, keepSelect):
        self._printOverrideError(b'changeSeason')
        return

    def onLobbyClick(self):
        self._printOverrideError(b'onLobbyClick')
        return

    def onSelectAnchor(self, areaID, slotID, regionID):
        self._printOverrideError(b'onSelectAnchor')
        return

    def onHoverAnchor(self, areaID, slotID, regionID, hover):
        self._printOverrideError(b'onHoverAnchor')
        return

    def onDragAnchor(self, areaID, slotID, regionID):
        self._printOverrideError(b'onDragAnchor')
        return

    def onReleaseItem(self):
        self._printOverrideError(b'onReleaseItem')
        return

    def onAnchorsShown(self, anchors):
        self._printOverrideError(b'onAnchorsShown')
        return

    def propertiesSheetSet(self, sheet, width, height, crnterX, centerY):
        self._printOverrideError(b'propertiesSheetSet')
        return

    def onButtonPressed(self, name):
        self._printOverrideError(b'onButtonPressed')
        return

    def onPressEscBtn(self):
        self._printOverrideError(b'onPressEscBtn')
        return

    def onPressSelectNextItem(self, reverse):
        self._printOverrideError(b'onPressSelectNextItem')
        return

    def playCustomSound(self, sound):
        self._printOverrideError(b'playCustomSound')
        return

    def onRemoveSelectedItem(self):
        self._printOverrideError(b'onRemoveSelectedItem')
        return

    def resetC11nItemsNovelty(self, itemsList):
        self._printOverrideError(b'resetC11nItemsNovelty')
        return

    def onShopEntryPointClick(self):
        self._printOverrideError(b'onShopEntryPointClick')
        return

    def onEntryPointClick(self, itemId):
        self._printOverrideError(b'onEntryPointClick')
        return

    def as_hideS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(value)
        return

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)
        return

    def as_setAnchorInitS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnchorInit(data)
        return

    def as_updateAnchorDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAnchorData(data)
        return

    def as_onRegionHighlightedS(self, slotId, highlightingType, highlightingResult, areaMouseBehavior):
        if self._isDAAPIInited():
            return self.flashObject.as_onRegionHighlighted(slotId, highlightingType, highlightingResult, areaMouseBehavior)
        return

    def as_updateSelectedRegionsS(self, slotId):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSelectedRegions(slotId)
        return

    def as_setAnchorsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnchorsData(data)
        return

    def as_setSeasonsBarDataS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_setSeasonsBarData(dataProvider)
        return

    def as_enableDNDS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDND(value)
        return

    def as_selectSeasonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_selectSeason(value)
        return

    def as_releaseItemS(self, deselectAnchor=True):
        if self._isDAAPIInited():
            return self.flashObject.as_releaseItem(deselectAnchor)
        return

    def as_showCarouselsArrowsNotificationS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showCarouselsArrowsNotification(text)
        return

    def as_reselectS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_reselect(data)
        return

    def as_setNotificationCountersS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotificationCounters(counters)
        return

    def as_setAnchorsStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnchorsState(data)
        return

    def as_attachToCursorS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_attachToCursor(data)
        return

    def as_updateInnerEntriesS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInnerEntries(items)
        return
