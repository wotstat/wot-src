from gui.Scaleform.framework.entities.View import View

class BattleVehicleConfiguratorMeta(View):

    def onModuleMouseOver(self, intCD):
        self._printOverrideError(b'onModuleMouseOver')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)
        return

    def as_updateModuleInfoPanelS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateModuleInfoPanel(data)
        return

    def as_updateChoiceInfoPanelS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateChoiceInfoPanel(data)
        return
