from gui.Scaleform.framework.entities.View import View

class VehicleBasePreviewMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onBackClick(self):
        self._printOverrideError(b'onBackClick')
        return

    def onOpenInfoTab(self, index):
        self._printOverrideError(b'onOpenInfoTab')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setAdditionalInfoS(self, info):
        if self._isDAAPIInited():
            return self.flashObject.as_setAdditionalInfo(info)
        return

    def as_show3DSceneTooltipS(self, id, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)
        return

    def as_hide3DSceneTooltipS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()
        return

    def as_setTopPanelS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setTopPanel(linkage)
        return

    def as_setBottomPanelS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setBottomPanel(linkage)
        return
