from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GraphicsOptimizationManagerMeta(BaseDAAPIComponent):

    def registerOptimizationArea(self, x, y, width, height):
        self._printOverrideError(b'registerOptimizationArea')
        return

    def unregisterOptimizationArea(self, optimizationID):
        self._printOverrideError(b'unregisterOptimizationArea')
        return

    def updateOptimizationArea(self, optimizationID, x, y, width, height):
        self._printOverrideError(b'updateOptimizationArea')
        return

    def isOptimizationAvailable(self, alias):
        self._printOverrideError(b'isOptimizationAvailable')
        return

    def isOptimizationEnabled(self, alias):
        self._printOverrideError(b'isOptimizationEnabled')
        return

    def switchOptimizationEnabled(self, value):
        self._printOverrideError(b'switchOptimizationEnabled')
        return

    def as_invalidateRectanglesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_invalidateRectangles()
        return

    def as_switchOptimizationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchOptimizationEnabled(value)
        return
