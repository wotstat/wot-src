from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class BaseDAAPIComponentMeta(BaseDAAPIModule):

    def registerFlashComponent(self, component, alias):
        self._printOverrideError(b'registerFlashComponent')
        return

    def isFlashComponentRegistered(self, alias):
        self._printOverrideError(b'isFlashComponentRegistered')
        return

    def unregisterFlashComponent(self, alias):
        self._printOverrideError(b'unregisterFlashComponent')
        return

    def getAlias(self):
        self._printOverrideError(b'getAlias')
        return

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()
        return

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
        return
