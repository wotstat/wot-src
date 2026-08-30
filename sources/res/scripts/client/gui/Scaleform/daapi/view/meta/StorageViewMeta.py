from gui.Scaleform.framework.entities.View import View

class StorageViewMeta(View):

    def navigateToHangar(self):
        self._printOverrideError(b'navigateToHangar')
        return

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_selectSectionS(self, sectionIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_selectSection(sectionIdx)
        return

    def as_setButtonCounterS(self, sectionIdx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonCounter(sectionIdx, value)
        return
