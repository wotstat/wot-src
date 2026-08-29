from gui.Scaleform.framework.entities.View import View

class BCHighlightsMeta(View):

    def onComponentTriggered(self, highlightId):
        self._printOverrideError(b'onComponentTriggered')
        return

    def onHighlightAnimationComplete(self, highlightId):
        self._printOverrideError(b'onHighlightAnimationComplete')
        return

    def as_setDescriptorsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptors(data)
        return

    def as_addHighlightS(self, highlightId):
        if self._isDAAPIInited():
            return self.flashObject.as_addHighlight(highlightId)
        return

    def as_removeHighlightS(self, highlightId):
        if self._isDAAPIInited():
            return self.flashObject.as_removeHighlight(highlightId)
        return
