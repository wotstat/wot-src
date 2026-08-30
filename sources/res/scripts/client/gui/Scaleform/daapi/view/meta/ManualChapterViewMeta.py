from gui.Scaleform.framework.entities.View import View

class ManualChapterViewMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def pageButtonClicked(self, pageType):
        self._printOverrideError(b'pageButtonClicked')
        return

    def buttonHighlighted(self):
        self._printOverrideError(b'buttonHighlighted')
        return

    def onPreviewClicked(self, videoUrl):
        self._printOverrideError(b'onPreviewClicked')
        return

    def onPageChanged(self, id):
        self._printOverrideError(b'onPageChanged')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setPagesS(self, pages):
        if self._isDAAPIInited():
            return self.flashObject.as_setPages(pages)
        return

    def as_showPageS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_showPage(index)
        return
