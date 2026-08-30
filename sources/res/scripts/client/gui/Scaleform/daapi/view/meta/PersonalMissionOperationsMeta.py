from gui.Scaleform.framework.entities.View import View

class PersonalMissionOperationsMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onOperationClick(self, pmType, operationID):
        self._printOverrideError(b'onOperationClick')
        return

    def showInfo(self):
        self._printOverrideError(b'showInfo')
        return

    def as_setOperationsS(self, operations):
        if self._isDAAPIInited():
            return self.flashObject.as_setOperations(operations)
        return

    def as_setTitleS(self, titleVO):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(titleVO)
        return
