from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleRoyalePlayersPanelMeta(BaseDAAPIComponent):

    def switchToPlayer(self, vehicleID):
        self._printOverrideError(b'switchToPlayer')
        return

    def as_setPlayersDataS(self, data, lostIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersData(data, lostIndex)
        return

    def as_setSeparatorVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setSeparatorVisibility(isVisible)
        return
