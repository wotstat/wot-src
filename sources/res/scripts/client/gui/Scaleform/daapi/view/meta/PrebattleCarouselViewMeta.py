from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class PrebattleCarouselViewMeta(InjectComponentAdaptor):

    def setFilter(self, id):
        self._printOverrideError(b'setFilter')
        return

    def onViewIsHidden(self):
        self._printOverrideError(b'onViewIsHidden')
        return

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()
        return

    def as_hideS(self, useAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)
        return
