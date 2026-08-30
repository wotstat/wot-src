from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationInscriptionControllerMeta(BaseDAAPIComponent):

    def sendChar(self, char):
        self._printOverrideError(b'sendChar')
        return

    def finish(self):
        self._printOverrideError(b'finish')
        return

    def removeChar(self):
        self._printOverrideError(b'removeChar')
        return

    def deleteAll(self):
        self._printOverrideError(b'deleteAll')
        return

    def as_showS(self, inscriptionLength):
        if self._isDAAPIInited():
            return self.flashObject.as_show(inscriptionLength)
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return

    def as_invalidInscriptionS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_invalidInscription(data)
        return

    def as_showHintS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(data)
        return
