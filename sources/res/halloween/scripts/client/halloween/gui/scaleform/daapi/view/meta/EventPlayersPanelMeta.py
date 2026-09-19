from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventPlayersPanelMeta(BaseDAAPIComponent):

    def acceptSquad(self, sessionID):
        self._printOverrideError(b'acceptSquad')
        return

    def addToSquad(self, sessionID):
        self._printOverrideError(b'addToSquad')
        return

    def as_setPlayerPanelInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelInfo(data)
        return

    def as_clearPlayerPanelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearPlayerPanel()
        return

    def as_setPlayerPanelHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelHp(vehID, hpMax, hpCurrent)
        return

    def as_setPlayerDeadS(self, vehID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerDead(vehID)
        return

    def as_setPlayerPanelCountSoulsS(self, vehID, countSouls):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelCountSouls(vehID, countSouls)
        return

    def as_setCollectorGoalS(self, goal):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectorGoal(goal)
        return

    def as_setCollectorNeedValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectorNeedValue(value)
        return

    def as_setChatCommandS(self, vehicleID, chatCommand, chatCommandFlags):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommand(vehicleID, chatCommand, chatCommandFlags)
        return
