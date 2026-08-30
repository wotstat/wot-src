from gui.Scaleform.framework.entities.DAAPIEntity import DAAPIEntity

class BaseDAAPIModuleMeta(DAAPIEntity):

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()
        return

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
        return
