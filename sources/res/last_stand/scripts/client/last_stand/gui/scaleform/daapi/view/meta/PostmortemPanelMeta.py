from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel

class PostmortemPanelMeta(PostmortemPanel):

    def as_setHintTitleS(self, value, isShadow=True):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintTitle(value, isShadow)
        return

    def as_setHintDescrS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHintDescr(value)
        return

    def as_showRespawnIconS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showRespawnIcon(value)
        return

    def as_setCanExitS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCanExit(value)
        return

    def as_showSpectatorPanelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showSpectatorPanel(value)
        return
