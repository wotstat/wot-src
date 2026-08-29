from gui.Scaleform.daapi.view.lobby.rally.BaseRallyListView import BaseRallyListView

class CyberSportUnitsListMeta(BaseRallyListView):

    def getTeamData(self, index):
        self._printOverrideError(b'getTeamData')
        return

    def refreshTeams(self):
        self._printOverrideError(b'refreshTeams')
        return

    def filterVehicles(self):
        self._printOverrideError(b'filterVehicles')
        return

    def loadPrevious(self):
        self._printOverrideError(b'loadPrevious')
        return

    def loadNext(self):
        self._printOverrideError(b'loadNext')
        return

    def as_setDummyS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummy(data)
        return

    def as_setDummyVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setDummyVisible(visible)
        return

    def as_setHeaderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)
        return

    def as_updateNavigationBlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateNavigationBlock(data)
        return

    def as_updateRallyIconS(self, iconPath):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRallyIcon(iconPath)
        return
