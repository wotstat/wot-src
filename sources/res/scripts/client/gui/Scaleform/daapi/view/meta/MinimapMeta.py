from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MinimapMeta(BaseDAAPIComponent):

    def onMinimapClicked(self, x, y, buttonIdx, mapScaleIndex):
        self._printOverrideError(b'onMinimapClicked')
        return

    def applyNewSize(self, sizeIndex):
        self._printOverrideError(b'applyNewSize')
        return

    def as_setSizeS(self, size):
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(size)
        return

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)
        return

    def as_setAlphaS(self, alpha):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlpha(alpha)
        return

    def as_showVehiclesNameS(self, visibility):
        if self._isDAAPIInited():
            return self.flashObject.as_showVehiclesName(visibility)
        return

    def as_setBackgroundS(self, path):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(path)
        return

    def as_enableHintPanelWithDataS(self, isStrategicArtyView, isSPG):
        if self._isDAAPIInited():
            return self.flashObject.as_enableHintPanelWithData(isStrategicArtyView, isSPG)
        return

    def as_disableHintPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_disableHintPanel()
        return

    def as_updateHintPanelDataS(self, isStrategicArtyView, isSPG):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHintPanelData(isStrategicArtyView, isSPG)
        return

    def as_initPrebattleSizeS(self, preferableSize):
        if self._isDAAPIInited():
            return self.flashObject.as_initPrebattleSize(preferableSize)
        return

    def as_setScenarioEventS(self, id, path, type):
        if self._isDAAPIInited():
            return self.flashObject.as_setScenarioEvent(id, path, type)
        return

    def as_setScenarioEventVisibleS(self, id, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setScenarioEventVisible(id, visible)
        return

    def as_clearScenarioEventS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_clearScenarioEvent(id)
        return
