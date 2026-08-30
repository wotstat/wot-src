from gui.Scaleform.daapi.view.meta.BasePostmortemPanelMeta import BasePostmortemPanelMeta

class PostmortemPanelMeta(BasePostmortemPanelMeta):

    def onDogTagKillerInPlaySound(self):
        self._printOverrideError(b'onDogTagKillerInPlaySound')
        return

    def onDogTagKillerOutPlaySound(self):
        self._printOverrideError(b'onDogTagKillerOutPlaySound')
        return

    def onVictimDogTagInPlaySound(self):
        self._printOverrideError(b'onVictimDogTagInPlaySound')
        return

    def as_setPlayerInfoS(self, playerInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerInfo)
        return

    def as_showKillerDogTagS(self, data, fadeOut):
        if self._isDAAPIInited():
            return self.flashObject.as_showKillerDogTag(data, fadeOut)
        return

    def as_showVictimDogTagS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showVictimDogTag(data)
        return

    def as_preloadComponentsS(self, components):
        if self._isDAAPIInited():
            return self.flashObject.as_preloadComponents(components)
        return

    def as_hideComponentsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideComponents()
        return

    def as_handleAsReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsReplay()
        return

    def as_togglePostmortemInfoPanelS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_togglePostmortemInfoPanel(isVisible)
        return

    def as_movePostmortemPanelUpS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_movePostmortemPanelUp()
        return

    def as_resetPostmortemPositionS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetPostmortemPosition()
        return

    def as_fadePostmortemPanelOutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_fadePostmortemPanelOut()
        return

    def as_setInDeathCamS(self, isInDeathCam):
        if self._isDAAPIInited():
            return self.flashObject.as_setInDeathCam(isInDeathCam)
        return
