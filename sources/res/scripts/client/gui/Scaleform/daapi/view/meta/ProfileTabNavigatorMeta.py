from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProfileTabNavigatorMeta(BaseDAAPIComponent):

    def onTabChange(self, tabId):
        self._printOverrideError(b'onTabChange')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setBtnTabCountersS(self, counters):
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnTabCounters(counters)
        return
