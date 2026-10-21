from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PortalPlayersPanelMeta(BaseDAAPIComponent):

    def acceptSquad(self, sessionID):
        self._printOverrideError(b'acceptSquad')
        return

    def addToSquad(self, sessionID):
        self._printOverrideError(b'addToSquad')
        return

    def switchToOtherPlayer(self, vehicleID):
        self._printOverrideError(b'switchToOtherPlayer')
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_setPlayerHpS(self, vehID, hpMax, hpCurrent, isSkipAnimation=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerHp(vehID, hpMax, hpCurrent, isSkipAnimation)
        return

    def as_setChatCommandS(self, vehID, chatCommand, chatCommandFlags):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommand(vehID, chatCommand, chatCommandFlags)
        return

    def as_setChatCommandsVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommandsVisibility(value)
        return

    def as_setPlayersSwitchingAllowedS(self, isAllowed):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersSwitchingAllowed(isAllowed)
        return

    def as_setPlayerStateS(self, vehID, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerState(vehID, state)
        return
