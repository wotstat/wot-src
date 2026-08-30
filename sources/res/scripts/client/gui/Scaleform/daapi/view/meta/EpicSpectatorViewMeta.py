from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel

class EpicSpectatorViewMeta(PostmortemPanel):

    def as_setFollowInfoTextS(self, folowText):
        if self._isDAAPIInited():
            return self.flashObject.as_setFollowInfoText(folowText)
        return

    def as_changeModeS(self, mode):
        if self._isDAAPIInited():
            return self.flashObject.as_changeMode(mode)
        return

    def as_focusOnVehicleS(self, focused):
        if self._isDAAPIInited():
            return self.flashObject.as_focusOnVehicle(focused)
        return

    def as_setTimerS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(time)
        return
