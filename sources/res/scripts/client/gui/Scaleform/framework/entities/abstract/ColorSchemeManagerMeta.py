from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ColorSchemeManagerMeta(BaseDAAPIComponent):

    def getColorScheme(self, schemeName):
        self._printOverrideError(b'getColorScheme')
        return

    def getIsColorBlind(self):
        self._printOverrideError(b'getIsColorBlind')
        return

    def as_updateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_update()
        return
