from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CrewOperationsPopOverMeta(SmartPopOverView):

    def invokeOperation(self, operationName):
        self._printOverrideError(b'invokeOperation')
        return

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
        return
