from gui.Scaleform.framework.entities.View import View

class ManualMainViewMeta(View):

    def onChapterOpenedS(self, id):
        self._printOverrideError(b'onChapterOpenedS')
        return

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onBackButton(self):
        self._printOverrideError(b'onBackButton')
        return

    def as_setChaptersS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setChapters(data)
        return

    def as_setPageBackgroundS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPageBackground(value)
        return

    def as_showCloseBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showCloseBtn(value)
        return

    def as_showBackBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackBtn(value)
        return

    def as_setDescrLabelBackBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescrLabelBackBtn(value)
        return
