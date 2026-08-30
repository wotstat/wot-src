from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CarouselEnvironmentMeta(BaseDAAPIComponent):

    def selectVehicle(self, id):
        self._printOverrideError(b'selectVehicle')
        return

    def resetFilters(self):
        self._printOverrideError(b'resetFilters')
        return

    def updateHotFilters(self):
        self._printOverrideError(b'updateHotFilters')
        return

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(value)
        return

    def as_showCounterS(self, countText, isAttention):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)
        return

    def as_hideCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()
        return

    def as_blinkCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()
        return

    def as_setCarouselFilterS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilter(data)
        return

    def as_initCarouselFilterS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_initCarouselFilter(data)
        return
