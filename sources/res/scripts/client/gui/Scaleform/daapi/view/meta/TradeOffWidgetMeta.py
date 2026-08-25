from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TradeOffWidgetMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError(b'onClick')
        return

    def onResetClick(self):
        self._printOverrideError(b'onResetClick')
        return

    def getTooltip(self):
        self._printOverrideError(b'getTooltip')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
