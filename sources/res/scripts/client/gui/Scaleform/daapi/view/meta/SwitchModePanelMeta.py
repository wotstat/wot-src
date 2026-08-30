from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SwitchModePanelMeta(BaseDAAPIComponent):

    def switchMode(self):
        self._printOverrideError(b'switchMode')
        return

    def onSelectCheckBoxAutoSquad(self, isSelected):
        self._printOverrideError(b'onSelectCheckBoxAutoSquad')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)
        return
