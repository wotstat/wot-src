from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class StrongholdBattlesListViewMeta(BaseRallyListView):

    def onFocusChange(self, hasFocus):
        self._printOverrideError(b'onFocusChange')
        return

    def updateBrowser(self):
        self._printOverrideError(b'updateBrowser')
        return
