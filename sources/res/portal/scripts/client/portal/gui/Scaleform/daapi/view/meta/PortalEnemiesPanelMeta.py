from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PortalEnemiesPanelMeta(BaseDAAPIComponent):

    def as_setCurrentPhaseS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurrentPhase(value)
        return

    def as_setPhasesCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPhasesCount(value)
        return

    def as_setLaneVehicleInfoS(self, laneIndex, heavyCount, mediumCount, lightCount, spgCount, atSpgCount):
        if self._isDAAPIInited():
            return self.flashObject.as_setLaneVehicleInfo(laneIndex, heavyCount, mediumCount, lightCount, spgCount, atSpgCount)
        return

    def as_setBuffStatusVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuffStatusVisible(value)
        return

    def as_resetStateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetState()
        return
