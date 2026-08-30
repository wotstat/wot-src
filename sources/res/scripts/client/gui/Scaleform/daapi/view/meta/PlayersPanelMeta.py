from gui.Scaleform.daapi.view.battle.shared.base_stats import StatsBase

class PlayersPanelMeta(StatsBase):

    def tryToSetPanelModeByMouse(self, panelMode):
        self._printOverrideError(b'tryToSetPanelModeByMouse')
        return

    def switchToOtherPlayer(self, vehicleID):
        self._printOverrideError(b'switchToOtherPlayer')
        return

    def as_setPanelModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelMode(value)
        return

    def as_setChatCommandsVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommandsVisibility(value)
        return

    def as_setPlayerHPS(self, isAlly, index, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerHP(isAlly, index, percent)
        return

    def as_setOverrideExInfoS(self, exOverrideInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setOverrideExInfo(exOverrideInfo)
        return

    def as_setPanelHPBarVisibilityStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPanelHPBarVisibilityState(value)
        return
