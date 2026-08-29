from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleTimerMeta(BaseDAAPIComponent):

    def as_setTotalTimeS(self, minutes, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalTime(minutes, seconds)
        return

    def as_setColorS(self, criticalColor):
        if self._isDAAPIInited():
            return self.flashObject.as_setColor(criticalColor)
        return

    def as_showBattleTimerS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showBattleTimer(show)
        return
