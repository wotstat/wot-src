from gui.Scaleform.framework.entities.View import View

class VehiclePreviewMeta(View):

    def onBackClick(self):
        self._printOverrideError(b'onBackClick')
        return

    def onOpenInfoTab(self, index):
        self._printOverrideError(b'onOpenInfoTab')
        return

    def onCompareClick(self):
        self._printOverrideError(b'onCompareClick')
        return

    def onGoToPostProgressionClick(self):
        self._printOverrideError(b'onGoToPostProgressionClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setTabsDataS(self, tabs):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsData(tabs)
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

    def as_setBulletVisibilityS(self, bulletTabIdx, isBulletVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setBulletVisibility(bulletTabIdx, isBulletVisible)
        return
