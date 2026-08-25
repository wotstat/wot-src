from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsMarathonViewMeta(BaseDAAPIComponent):

    def viewSize(self, width, height):
        self._printOverrideError(b'viewSize')
        return

    def as_loadBrowserS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loadBrowser()
        return
