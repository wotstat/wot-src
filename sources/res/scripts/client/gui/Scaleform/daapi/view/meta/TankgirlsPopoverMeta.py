from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class TankgirlsPopoverMeta(SmartPopOverView):

    def onRecruitClick(self, idx):
        self._printOverrideError(b'onRecruitClick')
        return

    def as_setListDataProviderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setListDataProvider(data)
        return
