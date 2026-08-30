from gui.Scaleform.framework.entities.View import View

class TrainingFormMeta(View):

    def joinTrainingRequest(self, id):
        self._printOverrideError(b'joinTrainingRequest')
        return

    def createTrainingRequest(self):
        self._printOverrideError(b'createTrainingRequest')
        return

    def onEscape(self):
        self._printOverrideError(b'onEscape')
        return

    def onLeave(self):
        self._printOverrideError(b'onLeave')
        return

    def as_setInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(data)
        return

    def as_setListS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setList(data)
        return
