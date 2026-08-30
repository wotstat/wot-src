from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ServerStatsMeta(BaseDAAPIComponent):

    def relogin(self, id):
        self._printOverrideError(b'relogin')
        return

    def startListenCsisUpdate(self, startListenCsis):
        self._printOverrideError(b'startListenCsisUpdate')
        return

    def as_changePeripheryFailedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_changePeripheryFailed()
        return

    def as_disableRoamingDDS(self, disable):
        if self._isDAAPIInited():
            return self.flashObject.as_disableRoamingDD(disable)
        return

    def as_setServerStatsS(self, stats, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)
        return

    def as_setServerStatsInfoS(self, tooltipFullData):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStatsInfo(tooltipFullData)
        return

    def as_getServersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()
        return

    def as_setSelectedServerIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedServerIndex(index)
        return
