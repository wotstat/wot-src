from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class BattleTypeSelectPopoverMeta(SmartPopOverView):

    def selectFight(self, actionName):
        self._printOverrideError(b'selectFight')
        return

    def demoClick(self):
        self._printOverrideError(b'demoClick')
        return

    def getTooltipData(self, itemData, itemIsDisabled):
        self._printOverrideError(b'getTooltipData')
        return

    def as_updateS(self, items, extraItems, isShowDemonstrator, demonstratorEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_update(items, extraItems, isShowDemonstrator, demonstratorEnabled)
        return

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)
        return
