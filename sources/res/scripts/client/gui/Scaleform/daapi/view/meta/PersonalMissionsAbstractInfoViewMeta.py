from gui.Scaleform.framework.entities.View import View

class PersonalMissionsAbstractInfoViewMeta(View):

    def bigBtnClicked(self):
        self._printOverrideError(b'bigBtnClicked')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
        return
