from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StorageCarouselEnvironmentMeta(BaseDAAPIComponent):

    def resetFilter(self):
        self._printOverrideError(b'resetFilter')
        return

    def showItemInfo(self, itemId):
        self._printOverrideError(b'showItemInfo')
        return

    def changeSearchNameVehicle(self, inputText):
        self._printOverrideError(b'changeSearchNameVehicle')
        return

    def as_updateSearchS(self, searchInputLabel, searchInputName, searchInputTooltip, searchInputMaxChars):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSearch(searchInputLabel, searchInputName, searchInputTooltip, searchInputMaxChars)
        return

    def as_updateCounterS(self, shouldShow, displayString, isZeroCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounter(shouldShow, displayString, isZeroCount)
        return
