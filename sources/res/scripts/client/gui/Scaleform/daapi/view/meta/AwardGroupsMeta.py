from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AwardGroupsMeta(BaseDAAPIComponent):

    def showGroup(self, groupId):
        self._printOverrideError(b'showGroup')
        return

    def as_setDataS(self, groups):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(groups)
        return

    def as_setTooltipsS(self, tooltips):
        if self._isDAAPIInited():
            return self.flashObject.as_setTooltips(tooltips)
        return

    def as_setSelectedS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelected(id, value)
        return

    def as_setEnabledS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(id, value)
        return
