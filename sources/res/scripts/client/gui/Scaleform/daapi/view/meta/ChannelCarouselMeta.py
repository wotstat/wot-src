from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ChannelCarouselMeta(BaseDAAPIComponent):

    def channelOpenClick(self, itemID):
        self._printOverrideError(b'channelOpenClick')
        return

    def closeAll(self):
        self._printOverrideError(b'closeAll')
        return

    def channelCloseClick(self, itemID):
        self._printOverrideError(b'channelCloseClick')
        return

    def updateItemDataFocus(self, itemID, wndType, isFocusIn):
        self._printOverrideError(b'updateItemDataFocus')
        return

    def updateItemDataOpened(self, itemID, wndType, isWindowOpened):
        self._printOverrideError(b'updateItemDataOpened')
        return

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
        return

    def as_getBattlesDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getBattlesDataProvider()
        return
