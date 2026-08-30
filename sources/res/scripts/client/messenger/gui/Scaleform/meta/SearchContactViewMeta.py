from messenger.gui.Scaleform.view.lobby.BaseContactView import BaseContactView

class SearchContactViewMeta(BaseContactView):

    def search(self, data):
        self._printOverrideError(b'search')
        return

    def as_getSearchDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getSearchDP()
        return

    def as_setSearchResultTextS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchResultText(message)
        return

    def as_setSearchDisabledS(self, coolDown):
        if self._isDAAPIInited():
            return self.flashObject.as_setSearchDisabled(coolDown)
        return
