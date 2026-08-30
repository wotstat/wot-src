from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineScorePanelMeta(BaseDAAPIComponent):

    def as_updateBasesS(self, west, center, east):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBases(west, center, east)
        return

    def as_updateHeadquarterHealthS(self, id, healthInPercent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHeadquarterHealth(id, healthInPercent)
        return

    def as_headquarterDestroyedS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_headquarterDestroyed(idx)
        return

    def as_updatePointsForBaseS(self, idx, points):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePointsForBase(idx, points)
        return

    def as_setTargetS(self, targetType, targetId):
        if self._isDAAPIInited():
            return self.flashObject.as_setTarget(targetType, targetId)
        return

    def as_setPrebattleTimerS(self, remainingPrebattleTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrebattleTimer(remainingPrebattleTime)
        return
