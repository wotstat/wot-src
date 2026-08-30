from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class AcousticPopoverMeta(SmartPopOverView):

    def onActionStart(self, actionID):
        self._printOverrideError(b'onActionStart')
        return

    def onSpeakerClick(self, speakerID):
        self._printOverrideError(b'onSpeakerClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_onItemPlayS(self, itemsID):
        if self._isDAAPIInited():
            return self.flashObject.as_onItemPlay(itemsID)
        return

    def as_onItemSelectS(self, itemsID):
        if self._isDAAPIInited():
            return self.flashObject.as_onItemSelect(itemsID)
        return

    def as_setEnableS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnable(isEnable)
        return

    def as_updateBtnEnabledS(self, btnId, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBtnEnabled(btnId, isEnabled)
        return
