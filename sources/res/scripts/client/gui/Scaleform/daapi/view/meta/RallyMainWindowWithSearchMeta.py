from gui.Scaleform.daapi.view.lobby.rally.BaseRallyMainWindow import BaseRallyMainWindow

class RallyMainWindowWithSearchMeta(BaseRallyMainWindow):

    def onAutoMatch(self, value, values):
        self._printOverrideError(b'onAutoMatch')
        return

    def autoSearchApply(self, value):
        self._printOverrideError(b'autoSearchApply')
        return

    def autoSearchCancel(self, value):
        self._printOverrideError(b'autoSearchCancel')
        return

    def as_autoSearchEnableBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_autoSearchEnableBtn(value)
        return

    def as_changeAutoSearchStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchState(value)
        return

    def as_changeAutoSearchBtnsStateS(self, waitingPlayers, searchEnemy):
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchBtnsState(waitingPlayers, searchEnemy)
        return

    def as_hideAutoSearchS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAutoSearch()
        return

    def as_changeAutoSearchMainLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchMainLabel(value)
        return

    def as_changeAutoSearchTimeDirectionS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchTimeDirection(value)
        return

    def as_changeAutoSearchCountDownSecondsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchCountDownSeconds(value)
        return
