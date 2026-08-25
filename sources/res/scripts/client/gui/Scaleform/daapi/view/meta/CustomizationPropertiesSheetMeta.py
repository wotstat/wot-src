from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CustomizationPropertiesSheetMeta(BaseDAAPIComponent):

    def onActionBtnClick(self, actionType, actionData):
        self._printOverrideError(b'onActionBtnClick')
        return

    def elementControlsHide(self):
        self._printOverrideError(b'elementControlsHide')
        return

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def registerInscriptionController(self, inscriptionController, inputLines):
        self._printOverrideError(b'registerInscriptionController')
        return

    def as_setDataAndShowS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataAndShow(data)
        return

    def as_setArrowsStatesS(self, left, right):
        if self._isDAAPIInited():
            return self.flashObject.as_setArrowsStates(left, right)
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return
