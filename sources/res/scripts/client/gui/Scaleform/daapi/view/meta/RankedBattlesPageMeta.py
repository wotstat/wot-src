from gui.Scaleform.framework.entities.View import View

class RankedBattlesPageMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def onPageChanged(self, viewId):
        self._printOverrideError(b'onPageChanged')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)
        return

    def as_setCountersS(self, countersData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounters(countersData)
        return
