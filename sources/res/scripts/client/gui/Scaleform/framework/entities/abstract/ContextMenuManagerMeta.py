from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContextMenuManagerMeta(BaseDAAPIComponent):

    def requestOptions(self, type, ctx):
        self._printOverrideError(b'requestOptions')
        return

    def onOptionSelect(self, optionId):
        self._printOverrideError(b'onOptionSelect')
        return

    def onHide(self):
        self._printOverrideError(b'onHide')
        return

    def as_setOptionsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setOptions(data)
        return

    def as_showS(self, type, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show(type, args)
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return
