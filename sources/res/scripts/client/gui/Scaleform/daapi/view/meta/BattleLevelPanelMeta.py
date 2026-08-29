from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleLevelPanelMeta(BaseDAAPIComponent):

    def onPlaySound(self, soundType):
        self._printOverrideError(b'onPlaySound')
        return

    def as_setLevelS(self, currentLevel, nextLevel, experience):
        if self._isDAAPIInited():
            return self.flashObject.as_setLevel(currentLevel, nextLevel, experience)
        return

    def as_setExperienceS(self, currentExperience, targetExperience, expDiff, percent, playSound):
        if self._isDAAPIInited():
            return self.flashObject.as_setExperience(currentExperience, targetExperience, expDiff, percent, playSound)
        return

    def as_setMaxLevelReachedS(self, levelReached):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxLevelReached(levelReached)
        return

    def as_resetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_reset()
        return

    def as_setIsPausedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsPaused(value)
        return

    def as_setAnimationS(self, enable):
        if self._isDAAPIInited():
            return self.flashObject.as_setAnimation(enable)
        return
