from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PopoverManagerMeta(BaseDAAPIComponent):

    def requestShowPopover(self, alias, data):
        self._printOverrideError(b'requestShowPopover')
        return

    def requestHidePopover(self):
        self._printOverrideError(b'requestHidePopover')
        return

    def as_onPopoverDestroyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onPopoverDestroy()
        return
