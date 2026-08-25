from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanSearchInfoMeta(BaseDAAPIComponent):

    def sendRequest(self):
        self._printOverrideError(b'sendRequest')
        return

    def openClanProfile(self):
        self._printOverrideError(b'openClanProfile')
        return

    def requestData(self, clanId):
        self._printOverrideError(b'requestData')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setStateDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStateData(data)
        return

    def as_setEmblemS(self, emblem):
        if self._isDAAPIInited():
            return self.flashObject.as_setEmblem(emblem)
        return

    def as_setWaitingVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingVisible(visible)
        return

    def as_setDummyS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)
        return

    def as_setDummyVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)
        return
