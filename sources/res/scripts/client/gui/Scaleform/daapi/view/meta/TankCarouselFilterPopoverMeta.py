from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class TankCarouselFilterPopoverMeta(SmartPopOverView):

    def changeFilter(self, groupId, itemId):
        self._printOverrideError(b'changeFilter')
        return

    def changeSearchNameVehicle(self, inputText):
        self._printOverrideError(b'changeSearchNameVehicle')
        return

    def switchCarouselType(self, selected):
        self._printOverrideError(b'switchCarouselType')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)
        return

    def as_showCounterS(self, countText):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText)
        return
