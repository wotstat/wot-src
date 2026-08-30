from gui.Scaleform.framework.entities.View import View

class PersonalMissionsOperationAwardsScreenMeta(View):

    def onCloseWindow(self):
        self._printOverrideError(b'onCloseWindow')
        return

    def onPlaySound(self, soundType):
        self._printOverrideError(b'onPlaySound')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setAwardDataS(self, awardData):
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardData(awardData)
        return

    def as_setCloseBtnEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseBtnEnabled(enabled)
        return

    def as_playAwardsAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playAwardsAnimation()
        return
