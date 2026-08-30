from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesRewardsMeta(BaseDAAPIComponent):

    def onTabChanged(self, viewId):
        self._printOverrideError(b'onTabChanged')
        return

    def as_setTabsDataS(self, tabs):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsData(tabs)
        return

    def as_setCountersS(self, countersData):
        if self._isDAAPIInited():
            return self.flashObject.as_setCounters(countersData)
        return
