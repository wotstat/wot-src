from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class DAAPISimpleContainerMeta(BaseDAAPIModule):

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()
        return

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
        return
