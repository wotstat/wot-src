from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LoaderManagerMeta(BaseDAAPIComponent):

    def viewLoaded(self, alias, viewName, view):
        self._printOverrideError(b'viewLoaded')
        return

    def viewLoadError(self, alias, viewName, text):
        self._printOverrideError(b'viewLoadError')
        return

    def viewInitializationError(self, alias, viewName):
        self._printOverrideError(b'viewInitializationError')
        return

    def viewLoadCanceled(self, alias, viewName):
        self._printOverrideError(b'viewLoadCanceled')
        return

    def as_loadViewS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(data)
        return

    def as_cancelLoadViewS(self, viewName):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelLoadView(viewName)
        return
