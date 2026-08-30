from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StorageCategoryInHangarViewMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError(b'setActiveState')
        return

    def as_setTabsDataS(self, tabs):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsData(tabs)
        return
