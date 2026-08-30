from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProgressiveRewardWidgetMeta(BaseDAAPIComponent):

    def onWidgetClick(self):
        self._printOverrideError(b'onWidgetClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
