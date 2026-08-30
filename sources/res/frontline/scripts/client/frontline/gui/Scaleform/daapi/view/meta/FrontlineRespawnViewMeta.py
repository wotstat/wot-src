from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineRespawnViewMeta(BaseDAAPIComponent):

    def onLocationSelected(self, pointIdx):
        self._printOverrideError(b'onLocationSelected')
        return

    def onRespawnBtnClick(self):
        self._printOverrideError(b'onRespawnBtnClick')
        return

    def onDeploymentReady(self):
        self._printOverrideError(b'onDeploymentReady')
        return

    def as_updateTimerS(self, timeIsOver, mainTimer):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(timeIsOver, mainTimer)
        return

    def as_updateAutoTimerS(self, timeIsOver, mainTimer):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAutoTimer(timeIsOver, mainTimer)
        return

    def as_resetRespawnStateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetRespawnState()
        return

    def as_setSelectedLocationS(self, pointIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedLocation(pointIdx)
        return

    def as_setLaneStateS(self, laneId, value, blockReasonText):
        if self._isDAAPIInited():
            return self.flashObject.as_setLaneState(laneId, value, blockReasonText)
        return

    def as_setMapDimensionsS(self, mapWidth, mapHeight):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapDimensions(mapWidth, mapHeight)
        return

    def as_setRespawnLocationsS(self, locations):
        if self._isDAAPIInited():
            return self.flashObject.as_setRespawnLocations(locations)
        return

    def as_handleAsReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsReplay()
        return
