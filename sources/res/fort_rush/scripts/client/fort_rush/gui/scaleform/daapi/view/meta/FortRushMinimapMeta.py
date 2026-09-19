from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent

class FortRushMinimapMeta(ClassicMinimapComponent):

    def onZoneClicked(self, zoneName):
        self._printOverrideError(b'onZoneClicked')
        return

    def as_showZonePingS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_showZonePing(zoneName)
        return

    def as_showZoneCommitS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_showZoneCommit(zoneName)
        return

    def as_clearZonePingS(self, zoneName):
        if self._isDAAPIInited():
            return self.flashObject.as_clearZonePing(zoneName)
        return

    def as_updateZoneCaptureStateS(self, zoneName, ownerTeam, progressTeam, captureActive, isContested, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateZoneCaptureState(zoneName, ownerTeam, progressTeam, captureActive, isContested, progress)
        return
