from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CheckBoxDialogMeta(BaseDAAPIComponent):

    def onCheckBoxChange(self, isSelected):
        self._printOverrideError(b'onCheckBoxChange')
        return

    def as_setCheckBoxLabelS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxLabel(value)
        return

    def as_setCheckBoxSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxSelected(value)
        return

    def as_setCheckBoxEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckBoxEnabled(value)
        return
