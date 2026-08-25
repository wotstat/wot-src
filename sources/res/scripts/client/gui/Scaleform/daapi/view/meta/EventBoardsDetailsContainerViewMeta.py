from gui.Scaleform.framework.entities.View import View

class EventBoardsDetailsContainerViewMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return
