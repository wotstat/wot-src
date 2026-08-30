from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleHintProgressDefenceMeta(BaseDAAPIComponent):

    def as_updateProgressS(self, value, progressValue, pointsLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(value, progressValue, pointsLeft)
        return

    def as_updateHealthPointsS(self, nextWavePoints):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHealthPoints(nextWavePoints)
        return

    def as_updateVehiclesS(self, vehicles):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicles(vehicles)
        return

    def as_handleAsReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_handleAsReplay()
        return
