from messenger.gui.Scaleform.view.lobby.BaseContactView import BaseContactView

class BaseManageContactViewMeta(BaseContactView):

    def checkText(self, txt):
        self._printOverrideError(b'checkText')
        return

    def as_setLabelS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setLabel(msg)
        return

    def as_setInputTextS(self, msg):
        if self._isDAAPIInited():
            return self.flashObject.as_setInputText(msg)
        return
