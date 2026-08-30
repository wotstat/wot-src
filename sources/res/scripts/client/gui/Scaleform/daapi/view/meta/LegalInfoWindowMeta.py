from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LegalInfoWindowMeta(AbstractWindowView):

    def getLegalInfo(self):
        self._printOverrideError(b'getLegalInfo')
        return

    def onCancelClick(self):
        self._printOverrideError(b'onCancelClick')
        return

    def as_setLegalInfoS(self, legalInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setLegalInfo(legalInfo)
        return
