from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesSeasonCompleteViewMeta(WrapperViewMeta):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def onSoundTrigger(self, soundName):
        self._printOverrideError(b'onSoundTrigger')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setPlaceS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlace(value)
        return

    def as_setAwardsDataS(self, awardsData):
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardsData(awardsData)
        return
