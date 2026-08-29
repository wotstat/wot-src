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

    def as_showDeadReasonS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showDeadReason()
        return

    def as_setPlayerInfoS(self, playerInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerInfo(playerInfo)
        return

    def as_showKillerDogTagS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showKillerDogTag(data)
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
