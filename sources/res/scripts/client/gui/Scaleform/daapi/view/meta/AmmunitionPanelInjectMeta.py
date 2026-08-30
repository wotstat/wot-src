from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class AmmunitionPanelInjectMeta(InjectComponentAdaptor):

    def onHangarSwitchAnimComplete(self, isComplete):
        self._printOverrideError(b'onHangarSwitchAnimComplete')
        return

    def as_setHelpLayoutS(self, helpLayoutData):
        if self._isDAAPIInited():
            return self.flashObject.as_setHelpLayout(helpLayoutData)
        return

    def as_clearHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearHelpLayout()
        return
