from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicInGameRankMeta(BaseDAAPIComponent):

    def levelUpAnimationComplete(self):
        self._printOverrideError(b'levelUpAnimationComplete')
        return

    def as_triggerLevelUpS(self, previousProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_triggerLevelUp(previousProgress)
        return

    def as_updateProgressS(self, previousProgress, currentProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(previousProgress, currentProgress)
        return

    def as_setRankS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRank(data)
        return
