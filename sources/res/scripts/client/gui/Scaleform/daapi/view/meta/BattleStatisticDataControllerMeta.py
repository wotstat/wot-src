from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleStatisticDataControllerMeta(BaseDAAPIComponent):

    def onRefreshComplete(self):
        self._printOverrideError(b'onRefreshComplete')
        return

    def as_refreshS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refresh()
        return

    def as_resetFragsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetFrags()
        return

    def as_setVehiclesDataS(self, vehData):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesData(vehData)
        return

    def as_addVehiclesInfoS(self, vehInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_addVehiclesInfo(vehInfo)
        return

    def as_updateVehiclesInfoS(self, upVehInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehiclesInfo(upVehInfo)
        return

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)
        return

    def as_setFragsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setFrags(data)
        return

    def as_updateVehiclesStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehiclesStats(data)
        return

    def as_updatePlayerStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePlayerStatus(data)
        return

    def as_setArenaInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setArenaInfo(data)
        return

    def as_setQuestStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setQuestStatus(data)
        return

    def as_setUserTagsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setUserTags(data)
        return

    def as_updateUserTagsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateUserTags(data)
        return

    def as_updateInvitationsStatusesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateInvitationsStatuses(data)
        return

    def as_setPersonalStatusS(self, bitmask):
        if self._isDAAPIInited():
            return self.flashObject.as_setPersonalStatus(bitmask)
        return

    def as_updatePersonalStatusS(self, added=0, removed=0):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePersonalStatus(added, removed)
        return

    def as_setQuestsInfoS(self, data, setForce):
        if self._isDAAPIInited():
            return self.flashObject.as_setQuestsInfo(data, setForce)
        return

    def as_updateQuestProgressS(self, condID, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestProgress(condID, data)
        return

    def as_updateQuestHeaderProgressS(self, headerProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestHeaderProgress(headerProgress)
        return

    def as_updateTriggeredChatCommandsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTriggeredChatCommands(data)
        return
