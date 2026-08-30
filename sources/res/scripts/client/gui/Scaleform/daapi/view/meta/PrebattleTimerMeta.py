from gui.Scaleform.daapi.view.battle.shared.prebattle_timers.timer_base import PreBattleTimerBase

class PrebattleTimerMeta(PreBattleTimerBase):

    def onShowInfo(self):
        self._printOverrideError(b'onShowInfo')
        return

    def onHideInfo(self):
        self._printOverrideError(b'onHideInfo')
        return

    def as_addInfoS(self, linkage, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addInfo(linkage, data)
        return

    def as_setInfoHintS(self, hint):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfoHint(hint)
        return

    def as_showInfoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showInfo()
        return
