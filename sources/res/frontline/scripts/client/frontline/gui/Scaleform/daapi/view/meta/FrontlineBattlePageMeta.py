from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class FrontlineBattlePageMeta(ClassicPage):

    def onDeactivateRadialMenu(self):
        self._printOverrideError(b'onDeactivateRadialMenu')
        return

    def as_setSelectReservesAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectReservesAvailable(value)
        return

    def as_setVehPostProgressionEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehPostProgressionEnabled(value)
        return
