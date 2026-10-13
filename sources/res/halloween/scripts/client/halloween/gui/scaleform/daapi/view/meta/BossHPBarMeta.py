from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BossHPBarMeta(BaseDAAPIComponent):

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)
        return

    def as_setLockedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setLocked(value)
        return

    def as_setMaxLivesS(self, value, difficulty, info):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxLives(value, difficulty, info)
        return

    def as_setLivesS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setLives(value)
        return

    def as_setBossHPS(self, label, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setBossHP(label, progress)
        return

    def as_setShieldsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShields(value)
        return
