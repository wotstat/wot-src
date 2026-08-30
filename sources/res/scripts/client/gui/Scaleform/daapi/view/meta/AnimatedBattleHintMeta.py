from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AnimatedBattleHintMeta(BaseDAAPIComponent):

    def animFinish(self):
        self._printOverrideError(b'animFinish')
        return

    def as_showHintS(self, frame, msgStr, isCompleted):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(frame, msgStr, isCompleted)
        return

    def as_hideHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint()
        return

    def as_closeHintS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHint()
        return

    def as_setPenetrationS(self, penetrationType, isPurple):
        if self._isDAAPIInited():
            return self.flashObject.as_setPenetration(penetrationType, isPurple)
        return
