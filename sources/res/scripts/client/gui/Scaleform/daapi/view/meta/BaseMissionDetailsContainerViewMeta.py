from gui.Scaleform.framework.entities.View import View

class BaseMissionDetailsContainerViewMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def requestMissionData(self, index):
        self._printOverrideError(b'requestMissionData')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setMissionDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setMissionData(data)
        return
