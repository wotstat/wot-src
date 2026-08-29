from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadialMenuMeta(BaseDAAPIComponent):

    def onSelect(self):
        self._printOverrideError(b'onSelect')
        return

    def onAction(self, action):
        self._printOverrideError(b'onAction')
        return

    def onHideCompleted(self):
        self._printOverrideError(b'onHideCompleted')
        return

    def onRefresh(self):
        self._printOverrideError(b'onRefresh')
        return

    def as_buildDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_buildData(data)
        return

    def as_showS(self, cursorX, cursorY, radialState, replyStateDiff, offset):
        if self._isDAAPIInited():
            return self.flashObject.as_show(cursorX, cursorY, radialState, replyStateDiff, offset)
        return

    def as_hideS(self, allowAction):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(allowAction)
        return
