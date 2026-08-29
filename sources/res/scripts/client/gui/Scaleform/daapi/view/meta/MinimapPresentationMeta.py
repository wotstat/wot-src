from gui.Scaleform.daapi.view.meta.MinimapEntityMeta import MinimapEntityMeta

class MinimapPresentationMeta(MinimapEntityMeta):

    def setMap(self, arenaID):
        self._printOverrideError(b'setMap')
        return

    def setMinimapData(self, arenaID, playerTeam, size):
        self._printOverrideError(b'setMinimapData')
        return

    def as_changeMapS(self, texture):
        if self._isDAAPIInited():
            return self.flashObject.as_changeMap(texture)
        return

    def as_addPointS(self, x, y, type, color, id):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoint(x, y, type, color, id)
        return

    def as_addPoiS(self, x, y, type, id):
        if self._isDAAPIInited():
            return self.flashObject.as_addPoi(x, y, type, id)
        return

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()
        return
