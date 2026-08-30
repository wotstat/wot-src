from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelsManagementWindowMeta(AbstractWindowView):

    def getSearchLimitLabel(self):
        self._printOverrideError(b'getSearchLimitLabel')
        return

    def searchToken(self, token):
        self._printOverrideError(b'searchToken')
        return

    def joinToChannel(self, index):
        self._printOverrideError(b'joinToChannel')
        return

    def createChannel(self, name, usePassword, password, retype):
        self._printOverrideError(b'createChannel')
        return

    def as_hideChannelNameInputS(self, isHide):
        if self._isDAAPIInited():
            return self.flashObject.as_hideChannelNameInput(isHide)
        return

    def as_freezSearchButtonS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_freezSearchButton(isEnable)
        return

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
        return
