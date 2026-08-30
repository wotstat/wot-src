from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleParametersMeta(BaseDAAPIComponent):

    def onParamClick(self, paramID):
        self._printOverrideError(b'onParamClick')
        return

    def onListScroll(self):
        self._printOverrideError(b'onListScroll')
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_setIsParamsAnimatedS(self, isParamsAnimated):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsParamsAnimated(isParamsAnimated)
        return
