from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):

    def setVehicleModule(self, newId, oldId, isRemove):
        self._printOverrideError(b'setVehicleModule')
        return

    def upgradeVehicleModule(self, moduleId):
        self._printOverrideError(b'upgradeVehicleModule')
        return

    def showModuleInfo(self, moduleId):
        self._printOverrideError(b'showModuleInfo')
        return

    def setAutoRearm(self, autoRearm):
        self._printOverrideError(b'setAutoRearm')
        return

    def buyVehicleModule(self, moduleId):
        self._printOverrideError(b'buyVehicleModule')
        return

    def setCurrentTab(self, tabIndex):
        self._printOverrideError(b'setCurrentTab')
        return

    def listOverlayClosed(self):
        self._printOverrideError(b'listOverlayClosed')
        return

    def onManageBattleAbilitiesClicked(self):
        self._printOverrideError(b'onManageBattleAbilitiesClicked')
        return

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
        return
