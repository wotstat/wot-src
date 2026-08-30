from gui.Scaleform.framework.entities.View import View

class RankedBattlesIntroMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onAcceptClick(self):
        self._printOverrideError(b'onAcceptClick')
        return

    def onDetailedClick(self):
        self._printOverrideError(b'onDetailedClick')
        return

    def onPlayVideoClick(self):
        self._printOverrideError(b'onPlayVideoClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setAlertMessageBlockDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlertMessageBlockData(data)
        return

    def as_setBeforeSeasonBlockDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBeforeSeasonBlockData(data)
        return
