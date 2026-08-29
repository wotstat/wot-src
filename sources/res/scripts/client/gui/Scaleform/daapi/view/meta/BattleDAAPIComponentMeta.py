from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleDAAPIComponentMeta(BaseDAAPIComponent):

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()
        return

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
        return
