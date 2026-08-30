from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class EventBoardsResultFilterPopoverViewMeta(SmartPopOverView):

    def changeFilter(self, id):
        self._printOverrideError(b'changeFilter')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return
