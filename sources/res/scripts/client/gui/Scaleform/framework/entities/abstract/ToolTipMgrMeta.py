from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ToolTipMgrMeta(BaseDAAPIComponent):

    def onCreateComplexTooltip(self, tooltipId, stateType):
        self._printOverrideError(b'onCreateComplexTooltip')
        return

    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        self._printOverrideError(b'onCreateTypedTooltip')
        return

    def onHideTooltip(self, tooltipId):
        self._printOverrideError(b'onHideTooltip')
        return

    def onCreateWulfTooltip(self, tooltipType, args, x, y):
        self._printOverrideError(b'onCreateWulfTooltip')
        return

    def as_showS(self, tooltipData, linkage, redraw=False):
        if self._isDAAPIInited():
            return self.flashObject.as_show(tooltipData, linkage, redraw)
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return
